# 1. Declaración de personajes
define roxy = Character("Roxy")

# 2. Declaración de variables para el sandbox (Días y momentos)
default dia = 1
default momento_dia = "Mañana" # Opciones: "Mañana", "Tarde", "Noche"

# 3. Variable para el contenido GAY
default contenido_gay_activado = False

# 4. Alta de imágenes
# Nota: Asegúrate de que los archivos "fondo_casa.png" y "Roxy_blender.png" 
# estén dentro de la carpeta "images" de tu proyecto en Ren'Py.
image bg fondo_casa = "fondo_casa.png"
image sprite roxy = "Roxy_blender.png"


# 5. Inicio del juego
label start:

    # Pregunta inicial para definir la variable de contenido
    menu:
        "Este juego contiene temas para adultos. ¿Aceptarías contenido GAY con tu hermana trans (Roxy) ?"
        
        "Sí, acepto el contenido.":
            $ contenido_gay_activado = True
            
        "No, prefiero omitirlo.":
            $ contenido_gay_activado = False

    # 6. Primera escena de prueba
    # 'scene' limpia la pantalla y pone la imagen en la capa de fondo (capa 1)
    scene bg fondo_casa
    
    # 'show' sobrepone al personaje. 'at right' lo coloca en la esquina derecha.
    show sprite roxy at right

    # Diálogo de prueba
    roxy "Hola soy roxy y soy el hermano de mc bienvenido"

    # A partir de aquí puedes conectar con tu sistema de sandbox
    jump sandbox_loop

# Estructura básica para tu bucle de días
label sandbox_loop:
    "Día [dia] - [momento_dia]"
    
    # Aquí iría el menú de acciones de tu sandbox (ir a la cocina, hablar con la madre, etc.)
    
    return