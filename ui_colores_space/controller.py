# SPDX-License-Identifier: GPL-3.0-or-later
from PySide6.QtCore import QEvent, QObject, QSettings, QTimer
from PySide6.QtGui import QIcon, QKeySequence

from . import host, icons

PREFIX = "ui_colores_space/"
SPACE = QKeySequence("Space")


class Controller(QObject):
    def __init__(self, app):
        super().__init__(app.window)
        self.app = app
        self.window = app.window
        self.original_icons = {}
        self.shortcut_changes = {}
        self.colors_enabled = QSettings().value(PREFIX + "colors", True, type=bool)
        self.search_enabled = QSettings().value(PREFIX + "space", True, type=bool)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.refresh_icons)

    def install(self):
        host.validate(self.window)
        menu = self.app.add_menu("UI Colores + Space")
        self.color_action = menu.addAction("Iconos con colores por categoría")
        self.color_action.setCheckable(True)
        self.color_action.setChecked(self.colors_enabled)
        self.color_action.toggled.connect(self.set_colors)
        self.space_action = menu.addAction("Espacio abre el buscador de comandos")
        self.space_action.setCheckable(True)
        self.space_action.setChecked(self.search_enabled)
        self.space_action.toggled.connect(self.set_search)
        menu.addSeparator()
        open_action = menu.addAction("Buscar comandos…")
        open_action.triggered.connect(host.search_action(self.window).trigger)
        self.window.installEventFilter(self)
        # MainWindow applies saved user shortcuts AFTER setup(app).
        QTimer.singleShot(0, self, self.start)

    def start(self):
        self.refresh_icons()
        if self.search_enabled:
            self.configure_space()

    def eventFilter(self, watched, event):
        if event.type() in (QEvent.PaletteChange, QEvent.ApplicationPaletteChange,
                            QEvent.ThemeChange, QEvent.ChildAdded):
            if event.type() != QEvent.ChildAdded:
                self.original_icons.clear()
            # Run after the host refreshes its own icons for the new palette.
            self.timer.start(0)
        return False

    def refresh_icons(self):
        if not self.colors_enabled:
            return
        cache = {}
        for action, key in host.icon_actions(self.window):
            if action not in self.original_icons:
                self.original_icons[action] = QIcon(action.icon())
            if key not in cache:
                cache[key] = icons.tool_icon(key)
            if not cache[key].isNull():
                action.setIcon(cache[key])

    def set_colors(self, enabled):
        self.colors_enabled = bool(enabled)
        QSettings().setValue(PREFIX + "colors", self.colors_enabled)
        if enabled:
            self.refresh_icons()
        else:
            for action, icon in self.original_icons.items():
                action.setIcon(icon)
            self.original_icons.clear()

    def _change_shortcuts(self, action, keys):
        old = action.shortcuts()
        if old != keys:
            self.shortcut_changes[action] = (old, list(keys))
            action.setShortcuts(keys)

    def configure_space(self):
        search = host.search_action(self.window)
        select = host.select_action(self.window)
        all_actions = host.actions(self.window)
        v = QKeySequence("V")
        v_free = not any(v in action.shortcuts() for action in all_actions
                         if action is not select)
        for action in all_actions:
            if action is search:
                continue
            keys = action.shortcuts()
            if SPACE in keys:
                updated = [key for key in keys if key != SPACE]
                if action is select and v_free and v not in updated:
                    updated.append(v)
                self._change_shortcuts(action, updated)
        keys = search.shortcuts()
        self._change_shortcuts(search, [SPACE] + [key for key in keys if key != SPACE])

    def set_search(self, enabled):
        self.search_enabled = bool(enabled)
        QSettings().setValue(PREFIX + "space", self.search_enabled)
        if enabled:
            self.configure_space()
        else:
            for action, (before, applied) in self.shortcut_changes.items():
                # Respect a shortcut edited by the user after activation.
                if action.shortcuts() == applied:
                    action.setShortcuts(before)
            self.shortcut_changes.clear()
