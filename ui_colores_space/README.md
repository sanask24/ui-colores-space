# UI Colores + Space — 0.1.0

Extensión para IngeTrazo 0.5.7+ con API de extensiones 2.

[Español](#instalación) · [English](#english)

## Instalación

1. En IngeTrazo abre **Extensiones → Abrir carpeta de plugins**.
2. Cierra el programa guardando el trabajo.
3. Copia la carpeta `ui_colores_space` completa a esa carpeta.
4. Abre IngeTrazo. No debe quedar una carpeta duplicada dentro de otra.

No requiere instalar dependencias adicionales ni modificar los archivos de
IngeTrazo. El ZIP contiene una sola carpeta instalable.

## Uso

- **Espacio** abre el buscador nativo. Escribe el nombre del comando,
  usa las flechas y pulsa **Enter**. **Esc** cancela.
- F3 se conserva si estaba asignado. El buscador incluye los comandos que
  IngeTrazo y sus otras extensiones exponen como acciones.
- Si Seleccionar ocupaba Espacio, pasa a **V** cuando esa tecla está libre.
- Los espacios siguen funcionando en los campos de texto y en las medidas.
- En **Extensiones → UI Colores + Space** puedes desactivar por separado
  los colores y el atajo. La preferencia queda guardada para siguientes sesiones.
- Al desactivar el atajo se restauran las asignaciones anteriores, excepto
  las que hayas modificado posteriormente en el editor de atajos.

## Colores

| Familia | Tema claro | Tema oscuro |
| --- | --- | --- |
| Dibujo | Azul | Azul claro |
| Modelado / BIM | Naranja | Naranja claro |
| Secciones | Violeta | Violeta claro |
| Operaciones de sólidos | Rojo | Rosa claro |
| Anotaciones | Verde | Verde claro |
| Navegación | Turquesa | Turquesa claro |
| Materiales | Magenta | Rosa |
| Composición | Ocre | Amarillo suave |
| Utilidades | Gris azulado | Gris claro |

Se conservan las formas de los iconos de IngeTrazo y se adaptan sus colores
cuando cambia el tema. Solo se colorean las acciones con una clave de icono
reconocida en el registro de la ventana. Los iconos propios de terceros no
registrados conservan su apariencia.

La extensión usa `setup(app)` y menús de la API documentada. La adaptación
de iconos y Seleccionar necesita los registros internos de IngeTrazo 0.5.7+;
esas dependencias están aisladas en `host.py`. Una versión futura puede
necesitar adaptar ese archivo. El buscador es el nativo; no se duplica.
No modifica geometría, materiales del modelo, historial ni datos BIM.

## Licencia y créditos

GPL-3.0-or-later. El archivo `icons.py` deriva del renderer de iconos de
IngeTrazo: Copyright (C) 2026 Marco Sumari Tellez y colaboradores de IngeTrazo.
Se conserva el aviso de copyright original y se incluye la licencia.

Documentación de la API: https://github.com/ingelibre/ingetrazo/blob/main/docs/plugins.md

## English

Category-coloured toolbar icons for light and dark themes, plus **Space**
to open IngeTrazo's native command search. Requires IngeTrazo 0.5.7+ and
extension API 2. Tested on Windows with IngeTrazo 0.5.7; other platforms
have not been verified.

### Installation

Open **Extensions → Open plugins folder**, save your work and close
IngeTrazo. Extract the release ZIP and copy its single `ui_colores_space`
folder into the plugins folder. Restart IngeTrazo. No additional dependencies
or changes to the application's source files are required.

### Usage

Press **Space**, type a command, choose it with the arrows and press **Enter**.
Press **Esc** to cancel. Text fields still accept spaces. F3 remains assigned
if it was previously available. If Select used Space, it moves to **V** only
when V is free. Each feature can be disabled independently under
**Extensions → UI Colores + Space**. Previous shortcut assignments are
restored when disabling Space, unless subsequently edited by the user.

Drawing uses blue; modelling orange; sections purple; solids red;
annotations green; navigation turquoise; materials magenta. The dark theme
uses lighter variants. Third-party icons without a recognized icon key keep
their original appearance.

This package uses the documented `setup(app)` entry point and menu API.
Icon keys and the Select action depend on internal host registries isolated
in `host.py`; later IngeTrazo versions may need an adapter update. It reuses
native command search. It makes no network requests, starts no processes,
deletes no files and does not modify model geometry or BIM data. Preferences
are stored locally with Qt QSettings.

GPL-3.0-or-later. Icon renderer derived from IngeTrazo; original copyright
notices are retained. See `LICENSE`.
