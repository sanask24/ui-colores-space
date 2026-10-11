# SPDX-License-Identifier: GPL-3.0-or-later
"""The host-0.x compatibility boundary; no host methods are replaced."""
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow


def belongs_to(action, window):
    obj = action.parent()
    while obj is not None:
        if obj is window:
            return True
        if isinstance(obj, QMainWindow):
            return False
        obj = obj.parent()
    return False


def actions(window):
    return [a for a in window.findChildren(QAction) if belongs_to(a, window)]


def search_action(window):
    return next((a for a in actions(window)
                 if a.objectName() == "command_search"), None)


def select_action(window):
    return getattr(window, "_tool_actions", {}).get("select")


def icon_actions(window):
    # API 2 does not expose icon keys. IngeTrazo 0.5.7+ keeps this registry.
    return [(action, key) for action, key in getattr(window, "_icon_actions", [])
            if belongs_to(action, window)]


def validate(window):
    if search_action(window) is None or select_action(window) is None:
        raise RuntimeError("No se encuentra el buscador nativo o la herramienta Seleccionar. "
                           "Esta extensión necesita IngeTrazo 0.5.7 o posterior.")
    if not icon_actions(window):
        raise RuntimeError("Esta versión no expone el registro de iconos compatible.")
