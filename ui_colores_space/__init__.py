# SPDX-License-Identifier: GPL-3.0-or-later
"""Category-coloured toolbar icons and Space command search for IngeTrazo."""
__version__ = "0.1.0"


def setup(app):
    if getattr(app, "api_version", 0) < 2:
        raise RuntimeError("UI Colores + Space requiere la API de extensiones 2.")
    if getattr(app.window, "_ui_colores_space_controller", None) is not None:
        return
    from .controller import Controller
    controller = Controller(app)
    controller.install()
    app.window._ui_colores_space_controller = controller
