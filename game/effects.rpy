# ==========================================
# EFECTOS Y TRANSFORMACIONES
# ==========================================

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define slow_dissolve = Dissolve(1.0)

transform fullscreen:
    size (1920, 1080)
    align (0.5, 0.5)

transform zoom_sprite:
    zoom 1.5
    yalign 1.0