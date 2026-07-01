from kmk.handlers.sequences import simple_key_sequence, send_string
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.macros import Press, Release, Tap, Delay, Macro

modtap = HoldTap()
macros = Macro()

keyboard = KMKKeyboard()

# Configuración genérica de pines (Ajústalos a los pines reales de tu placa)
# En este ejemplo usamos una matriz de 2x2 para las 4 teclas
keyboard.col_pins = (board.GP0)
keyboard.row_pins = (board.GP1, board.GP2, board.GP3)
keyboard.diode_orientation = col2row
keyboard.modules.append(modtap)
keyboard.modules.append(macros)


ENFOCAR_OBJ  = KC.PDOT      # Hace zoom/focus al objeto seleccionado
DUPLICAR_OBJ  = KC.H         # Oculta el objeto seleccionado
MOSTRAR_TODO = KC.LALT(KC.H) # Revela todo lo oculto (Alt + H)


OPEN_BLENDER = [
     KC.LWIN(no_release=True),
        KC.R,
        KC.LWIN(no_press=True),
        KC.MACRO_SLEEP_MS(250), # Wait for the Run window to pop up
        send_string("Blender.exe"),
        KC.ENTER,
]
VISTA_Z = KC.Z,        

TECLA_DOBLE = KC.HT(VISTA_Z, OPEN_BLENDER, prefer_hold=True, tap_time=250)

keyboard.keymap = [
    [
        # Fila 1: Botón Izquierdo, Botón Derecho
        TECLA_DOBLE,           ENFOCAR_OBJ,
        
        # Fila 2: Botón Izquierdo, Botón Derecho
        DUPLICAR_OBJ,       MOSTRAR_TODO
    ]
]

if __name__ == '__main__':
    keyboard.go()
