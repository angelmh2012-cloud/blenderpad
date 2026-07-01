import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# Configuración genérica de pines (Ajústalos a los pines reales de tu placa)
# En este ejemplo usamos una matriz de 2x2 para las 4 teclas
keyboard.col_pins = (board.GP0)
keyboard.row_pins = (board.GP1, board.GP2, board.GP3)
keyboard.diode_orientation = col2row

# --- DEFINICIÓN DE ATRAJOS DE BLENDER ---
VISTA_Z      = KC.Z         # Menú de sombreado (Wireframe/Solid)
ENFOCAR_OBJ  = KC.PDOT      # Hace zoom/focus al objeto seleccionado
DUPLICAR_OBJ  = KC.LSFT(KC.D)         # Oculta el objeto seleccionado
MOSTRAR_TODO = KC.LALT(KC.H) # Revela todo lo oculto (Alt + H)

# --- MAPA DE LAS 4 TECLAS ---
# El orden aquí abajo define qué botón físico hace qué cosa:
keyboard.keymap = [
    [
        # Fila 1: Botón Izquierdo, Botón Derecho
        VISTA_Z,           ENFOCAR_OBJ,
        
        # Fila 2: Botón Izquierdo, Botón Derecho
        DUPLICAR_OBJ,       MOSTRAR_TODO
    ]
]

if __name__ == '__main__':
    keyboard.go()
