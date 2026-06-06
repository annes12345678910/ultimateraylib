from ._classes import *
# gui

# int GuiButton(Rectangle bounds, const char *text)
lib.GuiButton.argtypes = [Rectangle, c_char_p]
lib.GuiButton.restype = ctypes.c_int
def gui_button(bounds: Rectangle, text:str):
    return bool(lib.GuiButton(bounds, text.encode()))

# int GuiMessageBox(Rectangle bounds, const char *title, const char *message, const char *buttons)
makeconnect("GuiMessageBox", [Rectangle, c_char_p, c_char_p, c_char_p], c_int)
def gui_message_box(bounds, title, message, buttons):
    return lib.GuiMessageBox(bounds, title, message, buttons)

makeconnect("GuiDropdownBox", [Rectangle, c_char_p, POINTER(c_int), c_bool], c_int)
def gui_dropdown_box(bounds: Rectangle, text: str, active: int, edit_mode: bool):
    dad = c_int(active)
    lib.GuiDropdownBox(bounds, text, byref(dad), edit_mode)
    return dad.value

makeconnect("GuiSpinner", [Rectangle, c_char_p, POINTER(c_int), c_int, c_int, c_bool], c_int)
def gui_spinner(bounds, text, value: int, min_value, max_value, edit_mode):
    dad = c_int(value)
    lib.GuiSpinner(bounds, text, byref(dad), min_value, max_value, edit_mode)
    return dad.value

makeconnect("GuiValueBox", [Rectangle, c_char_p, POINTER(c_int), c_int, c_int, c_bool], c_int)
def gui_value_box(bounds: Rectangle, text: str, value: int, min_value: int, max_value: int, edit_mode: bool):
    dad = c_int(value)
    lib.GuiValueBox(bounds, text, byref(dad), min_value, max_value, edit_mode)
    return dad.value

makeconnect("GuiValueBoxFloat", [Rectangle, c_char_p, c_char_p, POINTER(c_float), c_bool], c_int)
def gui_value_box_float(bounds: Rectangle, text: str, text_value: str, value: float, edit_mode: bool):
    dad = c_float(value)
    lib.GuiValueBoxFloat(bounds, text, text_value, byref(dad), edit_mode)
    return dad.value

makeconnect("GuiTextBox", [Rectangle, c_char_p, c_int, c_bool], c_int)
def gui_text_box(bounds: Rectangle, text: str, text_size: int, edit_mode: bool) -> tuple[bool, str]:
    # Create a buffer of the right size
    buf = create_string_buffer(text.encode(), text_size)
    caret = lib.GuiTextBox(bounds, buf, text_size, edit_mode)
    return bool(caret), buf.value.decode()  # Return caret and updated string

makeconnect("GuiSlider", [Rectangle, c_char_p, c_char_p, POINTER(c_float), c_float, c_float], c_int)
def gui_slider(bounds: Rectangle, text_left: str, text_right: str, value: float, min_value: float, max_value: float) -> tuple[float, int]:
    skibiidi = c_float(value)
    da = lib.GuiSlider(bounds, text_left.encode(), text_right.encode(), byref(skibiidi), min_value, max_value)
    return skibiidi.value, da

makeconnect("GuiSliderBar", [Rectangle, c_char_p, c_char_p, POINTER(c_float), c_float, c_float], c_int)
def gui_slider_bar(bounds: Rectangle, text_left: str, text_right: str, value: float, min_value: float, max_value: float) -> tuple[float, int]:
    skibiidi = c_float(value)
    da = lib.GuiSliderBar(bounds, text_left.encode(), text_right.encode(), byref(skibiidi), min_value, max_value)
    return skibiidi.value, da

makeconnect("GuiProgressBar", [Rectangle, c_char_p, c_char_p, POINTER(c_float), c_float, c_float], c_int)
def gui_progress_bar(bounds: Rectangle, text_left: str, text_right: str, value: float, min_value: float, max_value: float) -> tuple[float, int]:
    skibiidi = c_float(value)
    da = lib.GuiProgressBar(bounds, text_left.encode(), text_right.encode(), byref(skibiidi), min_value, max_value)
    return skibiidi.value, da

makeconnect("GuiStatusBar", [Rectangle, c_char_p], c_int)
def gui_status_bar(bounds: Rectangle, text: str) -> int:
    return lib.GuiStatusBar(bounds, text.encode())

makeconnect("GuiDummyRec", [Rectangle, c_char_p], c_int)
def gui_dummy_rec(bounds: Rectangle, text: str) -> int:
    return lib.GuiDummyRec(bounds, text.encode())

makeconnect("GuiGrid", [Rectangle, c_char_p, c_float, c_int, POINTER(Vector2)], c_int)
def gui_grid(bounds:Rectangle, text:str, spacing:float, subdivs:int, mouse_cell:Vector2) -> int:
    return lib.GuiGrid(bounds, text.encode(), spacing, subdivs, byref(mouse_cell))

"""
RAYGUIAPI int GuiListView(Rectangle bounds, const char *text, int *scrollIndex, int *active);          // List View control, returns selected list item index
RAYGUIAPI int GuiListViewEx(Rectangle bounds, const char **text, int count, int *scrollIndex, int *active, int *focus); // List View with extended parameters
RAYGUIAPI int GuiMessageBox(Rectangle bounds, const char *title, const char *message, const char *buttons); // Message Box control, displays a message
RAYGUIAPI int GuiTextInputBox(Rectangle bounds, const char *title, const char *message, const char *buttons, char *text, int textMaxSize, bool *secretViewActive); // Text Input Box control, ask for text, supports secret


RAYGUIAPI int GuiColorPicker(Rectangle bounds, const char *text, Color *color);                        // Color Picker control (multiple color controls)
RAYGUIAPI int GuiColorPanel(Rectangle bounds, const char *text, Color *color);                         // Color Panel control
RAYGUIAPI int GuiColorBarAlpha(Rectangle bounds, const char *text, float *alpha);                      // Color Bar Alpha control
RAYGUIAPI int GuiColorBarHue(Rectangle bounds, const char *text, float *value);                        // Color Bar Hue control
RAYGUIAPI int GuiColorPickerHSV(Rectangle bounds, const char *text, Vector3 *colorHsv);                // Color Picker control that avoids conversion to RGB on each call (multiple color controls)
RAYGUIAPI int GuiColorPanelHSV(Rectangle bounds, const char *text, Vector3 *colorHsv);                 // Color Panel control that returns HSV color value, used by GuiColorPickerHSV()
"""
makeconnect("GuiColorPicker", [Rectangle, c_char_p, POINTER(Color)], c_int)
def gui_color_picker(bounds:Rectangle, text:str, color:Color)-> int:
    return lib.GuiColorPicker(bounds, text.encode(), byref(color))

makeconnect("GuiColorPanel", [Rectangle, c_char_p, POINTER(Color)], c_int)
def gui_color_panel(bounds:Rectangle, text:str, color:Color)-> int:
    return lib.GuiColorPanel(bounds, text.encode(), byref(color))

gui_enable = lib.GuiEnable
gui_disable = lib.GuiDisable
gui_lock = lib.GuiLock
gui_unlock = lib.GuiUnlock

makeconnect("GuiIsLocked", [], c_bool)
def gui_is_locked() -> bool:
    return lib.GuiIsLocked()

makeconnect("GuiSetAlpha", [c_float])
def gui_set_alpha(alpha: float):
    lib.GuiSetAlpha(alpha)

makeconnect("GuiSetState", [c_int])
def gui_set_state(state: int):
    lib.GuiSetState(state)

makeconnect("GuiGetState", [], c_int)
def gui_get_state() -> int:
    return lib.GuiGetState()

makeconnect("GuiSetFont", [Font])
def gui_set_font(font: Font):
    lib.GuiSetFont(font)

makeconnect("GuiGetFont", [], Font)
def gui_get_font() -> Font:
    return lib.GuiGetFont()

makeconnect("GuiSetStyle", [c_int, c_int, c_int])
def gui_set_style(control: int, property: int, value: int):
    lib.GuiSetStyle(control, property, value)

makeconnect("GuiGetStyle", [c_int, c_int], c_int)
def gui_get_style(control: int, property: int) -> int:
    return lib.GuiGetStyle(control, property)

makeconnect("GuiLoadStyle", [c_char_p])
def gui_load_style(file_name: str):
    lib.GuiLoadStyle(file_name.encode())

gui_load_style_default = lib.GuiLoadStyleDefault

gui_enable_tooltip = lib.GuiEnableTooltip
gui_disable_tooltip = lib.GuiDisableTooltip

makeconnect("GuiSetTooltip", [c_char_p])
def gui_set_tooltip(tooltip:str):
    lib.GuiSetTooltip(tooltip.encode())

makeconnect("GuiIconText", [c_int, c_char_p], c_char_p)
def gui_icon_text(icon_id:int, text:str) -> str:
    return lib.GuiIconText(icon_id, text).decode()

makeconnect("GuiSetIconScale", [c_int])
def gui_set_icon_scale(scale:int):
    lib.GuiSetIconScale(scale)

makeconnect("GuiGetIcons", [], POINTER(c_uint))
def gui_get_icons() -> list[int]:
    ptr = lib.GuiGetIcons()

    if not ptr:
        return []

    return [ptr[i] for i in range(len(ptr))]

makeconnect("GuiLoadIcons", [c_char_p, c_bool], POINTER(c_char_p))
def gui_load_icons(file_name:str, load_icons_name:bool) -> list[str]:
    ptr = lib.GuiLoadIcons(file_name.encode(), load_icons_name)

    if not ptr:
        return []

    return [ptr[i].decode() for i in range(len(ptr))]

makeconnect("GuiDrawIcon", [c_int, c_int, c_int, c_int, Color])
def gui_draw_icon(icon_id:int, pos_x:int, pos_y:int, pixel_size:int, color:Color):
    lib.GuiDrawIcon(icon_id, pos_x, pos_y, pixel_size, color)

makeconnect("GuiGetTextWidth", [c_char_p], c_int)
def gui_get_text_width(text:str) -> int:
    return lib.GuiGetTextWidth(text.encode())
