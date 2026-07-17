import time

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.macros import Macro

try:
    import digitalio
except ImportError:  # pragma: no cover - handles host-side syntax checks
    digitalio = None

try:
    import adafruit_ssd1306
except ImportError:  # pragma: no cover - handles host-side syntax checks
    adafruit_ssd1306 = None

from kmk.scanners.diode import DiodeOrientation

modtap = HoldTap()
macros = Macro()
keyboard = KMKKeyboard()

keyboard.modules.append(modtap)
keyboard.modules.append(macros)

# --- Key layout: 2x2 matrix mapped to D7-D10 ---
keyboard.col_pins = ()
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

ENFOCAR_OBJ = KC.F
DUPLICAR_OBJ = KC.H
MOSTRAR_TODO = KC.LALT(KC.H)
ABRIR_PROP = KC.N

MODES = ["Blender Shortcuts", "Friday Night Funkin", "Mini Game"]
MODE_HINTS = [
    "F=focus | H=hide | Alt+H=show all",
    "Arrows for notes | A/S/W/D as extras",
    "OLED mini game + button actions",
]
MODE_ACTIONS = [
    [ENFOCAR_OBJ, DUPLICAR_OBJ, MOSTRAR_TODO, ABRIR_PROP],
    [KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT],
    [KC.A, KC.S, KC.W, KC.D],
]

current_mode = 0


def get_pin(*names):
    for name in names:
        pin = getattr(board, name, None)
        if pin is not None:
            return pin
    raise RuntimeError("Could not find a matching pin for the requested hardware")


# --- Hardware pins ---
SDA_PIN = get_pin("GP4", "D4")
SCL_PIN = get_pin("GP5", "D5")
ENCODER_PIN = get_pin("GP1", "D1")
BUTTON_PINS = [get_pin("GP7", "D7"), get_pin("GP8", "D8"), get_pin("GP9", "D9"), get_pin("GP10", "D10")]


# --- OLED setup ---
if digitalio is not None and adafruit_ssd1306 is not None:
    import busio

    i2c = busio.I2C(SCL_PIN, SDA_PIN)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)
else:
    oled = None


# --- Button inputs ---
if digitalio is not None:
    buttons = []
    for pin in BUTTON_PINS:
        io = digitalio.DigitalInOut(pin)
        io.direction = digitalio.Direction.INPUT
        io.pull = digitalio.Pull.UP
        buttons.append(io)

    encoder_button = digitalio.DigitalInOut(ENCODER_PIN)
    encoder_button.direction = digitalio.Direction.INPUT
    encoder_button.pull = digitalio.Pull.UP
else:
    buttons = []
    encoder_button = None

button_last_states = [False] * len(buttons)
encoder_last_state = False


def draw_status():
    if oled is None:
        return

    oled.fill(0)
    oled.text("Mode:", 0, 0, 1)
    oled.text(MODES[current_mode][:12], 0, 10, 1)
    oled.text(MODE_HINTS[current_mode][:16], 0, 20, 1)
    oled.show()


# --- Simple OLED mini game ---
ball_x = 10
ball_y = 10
ball_dx = 2
ball_dy = 1


def draw_game_frame():
    global ball_x, ball_y, ball_dx, ball_dy

    if oled is None:
        return

    oled.fill(0)
    oled.text("Mini Game", 0, 0, 1)
    oled.pixel(ball_x, ball_y, 1)
    oled.pixel(ball_x + 1, ball_y, 1)
    oled.pixel(ball_x, ball_y + 1, 1)
    oled.pixel(ball_x + 1, ball_y + 1, 1)

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= 0 or ball_x >= 126:
        ball_dx *= -1
    if ball_y <= 8 or ball_y >= 30:
        ball_dy *= -1

    oled.show()


# --- Helper to send key presses ---
def send_key(action):
    try:
        keyboard.tap_key(action)
    except AttributeError:
        pass


# --- Background task for encoder/button handling and OLED output ---
def control_loop():
    global current_mode, button_last_states, encoder_last_state

    while True:
        if buttons:
            for idx, button in enumerate(buttons):
                pressed = not button.value
                if pressed and not button_last_states[idx]:
                    action = MODE_ACTIONS[current_mode][idx]
                    send_key(action)
                button_last_states[idx] = pressed

        if encoder_button is not None:
            pressed = not encoder_button.value
            if pressed and not encoder_last_state:
                current_mode = (current_mode + 1) % len(MODES)
                draw_status()
            encoder_last_state = pressed

        if current_mode == 2:
            draw_game_frame()
        else:
            draw_status()

        time.sleep(0.05)


keyboard.keymap = [[KC.NO, KC.NO], [KC.NO, KC.NO]]

if __name__ == '__main__':
    draw_status()
    try:
        import _thread
    except ImportError:  # pragma: no cover - handles host-side syntax checks
        _thread = None

    if _thread is not None:
        _thread.start_new_thread(control_loop, ())

    keyboard.go()
