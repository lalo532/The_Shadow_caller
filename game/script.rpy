# 1. Variables de nombres
default mc_name = "MC"
default madre_name = "Madre"
default roxy_name = "Roxy"
default h_mayor_name = "Roxane"
default h_menor_name = "Kiry"

# 2. Declaración de personajes
define mc = Character("[mc_name]", color="#3366FF")      
define madre = Character("[madre_name]", color="#33CC33") 
define roxy = Character("[roxy_name]", color="#FF66B2")   
define roxane = Character("[h_mayor_name]", color="#8A2BE2") 
define kiry = Character("[h_menor_name]", color="#FFFF33") 
define narrador = Character(None) # Narrador sin nombre, más inmersivo 

# 3. Efectos y transformaciones
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

transform fullscreen:
    size (1920, 1080)
    align (0.5, 0.5)

transform zoom_sprite:
    zoom 1.5  
    yalign 1.0 

# 4. Variables de Sandbox y Tiempo
default dia = 1
default momento_dia = "Mañana"
default contenido_gay_activado = False

# 5. Sistema de Estadísticas
# Variables para medir la relación con cada personaje
default amor_madre = 0
default tension_madre = 0

default amor_roxy = 0
default odio_roxy = 0

default amor_roxane = 0
default tension_roxane = 0

default amor_kiry = 0
default odio_kiry = 0

# 6. Variables de control de eventos
# Para que una escena no se repita dos veces
default evento_madre_cocina_visto = False
default evento_roxy_bano_visto = False

# 7. Imágenes
# Por ahora uso "fondo_casa.png" para todo, cámbialo cuando tengas tus fondos
image bg sala = "fondo_casa.png"
image bg pasillo = "fondo_casa.png"
image bg cocina = "fondo_casa.png"
image bg bano = "fondo_casa.png"
image bg cuarto_mc = "fondo_casa.png"
image bg tormenta = "fondo_casa.png" 

# Sprites
image sprite roxy = "Roxy.png"
image sprite mom = "Madre.png"
image sprite roxane = "Roxane.png"
image sprite kiry = "Kiry.png"

# Imágenes del menú inicial
image Roxy_primer_imagen = "Roxy_muestra1.png"
image Roxy_rechazo = "Roxy_muestra2.png"

# Imágenes escenas
image Vista_cocina = "madre_cocina1.png"
image Vista_cocina2 = "madre_cocina2.png"
image Vista_cocina3 = "madre_cocina3.png"
image Vista_cocina4 = "madre_cocina4.png"
image Vista_cocina5 = "madre_cocina5.png"

image roxy_baño0 = "roxy_baño1.png"
image roxy_baño1 = "roxy_baño2.png"
image roxy_baño2 = "roxy_baño3.png"
image roxy_baño3 = "roxy_baño4.png"

# 8. Inicio del juego
label start:

    $ mc_name = renpy.input("¿Cuál es tu nombre?").strip() or "MC"
    $ madre_name = renpy.input("¿Cuál es el nombre de tu madre?").strip() or "Madre"
    $ roxy_name = renpy.input("¿Cuál es el nombre de tu hermana trans (23 años)?").strip() or "Roxy"
    $ h_mayor_name = renpy.input("¿Cuál es el nombre de tu hermana mayor (29 años)?").strip() or "Roxane"
    $ h_menor_name = renpy.input("¿Cuál es el nombre de tu hermana menor (20 años)?").strip() or "Kiry"

    menu:
        "Este juego contiene temas para adultos. ¿Aceptarías contenido GAY con tu hermana trans ([roxy_name])?"
        
        "Sí, lo acepto.":
            $ contenido_gay_activado = True
            show Roxy_primer_imagen at fullscreen with flash
            roxy "Muchas gracias por aceptar este contenido."
            pause 2.0
            hide Roxy_primer_imagen with dissolve

        "No, omitir.":
            $ contenido_gay_activado = False
            show Roxy_rechazo at fullscreen with flash
            roxy "Una pena... nos lo perdemos, [mc_name]."
            pause 2.0
            hide Roxy_rechazo with dissolve

    scene bg tormenta with dissolve
    
    narrador "La nieve cubre todo. Llevamos días sin poder salir. Tienen suerte de tener calefacción y luz gubernamental."
    narrador "La radio dijo que esto podría durar meses. Por suerte, hay mucha comida enlatada abajo."
    
    mc "Tres meses encerrados... esto se va a volver una locura."
    
    show sprite mom at right, zoom_sprite with easeinright
    madre "Tranquilo, [mc_name]. Todo va a estar bien mientras no nos matemos entre nosotros."
    madre "Voy a organizar la comida. Busca algo que hacer."
    
    hide sprite mom with dissolve
    
    # Muestra el recuadro del tiempo en pantalla
    show screen hud_tiempo
    jump hub_principal


# 9. El "Hub" o Pasillo Central
label hub_principal:
    scene bg pasillo with dissolve
    narrador "Estás en el pasillo de la cabaña."

    menu:
        "¿A dónde quieres ir?"
        
        "Ir a la Sala":
            jump loc_sala
            
        "Ir a la Cocina":
            jump loc_cocina
            
        "Ir al Baño":
            jump loc_bano
            
        "Ir a tu Cuarto":
            jump loc_cuarto_mc
            
        "Avanzar el tiempo":
            jump avanzar_tiempo


# 10. Locaciones y Eventos

label loc_sala:
    scene bg sala
    
    if momento_dia == "Noche":
        narrador "La sala está oscura. Roxane está sentada en el sofá con una copa de vino."
        show sprite roxane at right, zoom_sprite
        roxane "¿No puedes dormir, [mc_name]?"
        
        menu:
            "Hacerle compañía":
                mc "No. El frío no me deja."
                roxane "Si tienes frío, acércate. No muerdo. Al menos, no siempre."
                $ amor_roxane += 1
                $ tension_roxane += 2
                narrador "Te sientas a su lado. Su pierna roza la tuya bajo la manta."
                
            "Dejarla sola":
                mc "Solo iba por agua. Ya me voy."
                roxane "Qué aburrido eres."
                $ amor_roxane -= 1
                
        hide sprite roxane
    else:
        narrador "La sala está vacía. Solo se escucha el viento golpeando la ventana."
        
    jump hub_principal


label loc_cocina:
    scene bg cocina
    
    if momento_dia == "Mañana" and not evento_madre_cocina_visto:
        $ evento_madre_cocina_visto = True
        narrador "[madre_name] está sacando unas latas de los estantes inferiores."
        show Vista_cocina at fullscreen with flash
        
        narrador "Tu madre lleva un vestido de tirantes rojos. Sin darse cuenta, la tela se ha subido, exponiendo sus muslos y su trasero."
        mc "Mierda... menuda vista."
        show Vista_cocina2 at fullscreen with flash
        
        menu:
            "Quedarte mirando descaradamente.":
                $ tension_madre += 3
                narrador "No intentas disimular. La recorres con la mirada hasta que ella se da cuenta al voltear."
                show Vista_cocina3 at fullscreen with flash
                madre "¿Te gusta la vista, [mc_name]?"
                mc "Si te pones así, es imposible mirar a otro lado."
                madre "Eres un descarado... pero me gusta que prestes atención."
                show Vista_cocina4 at fullscreen with flash
                madre "Cuidado con acercarte mucho, podrías quemarte. Mejor ven y ayúdame con esto."
                
            "Ofrecerle ayuda.":
                $ amor_madre += 2
                mc "Déjame ayudarte con eso antes de que te caigas."
                show Vista_cocina5 at fullscreen with flash
                madre "Gracias, hijo. Qué considerado eres."
                
            "Ignorarla y servirte café.":
                $ odio_madre += 1
                narrador "Pasas de largo buscando tu taza. Ella se acomoda el vestido rápidamente, algo ofendida por tu frialdad."
                
    else:
        narrador "No hay nadie en la cocina. El fregadero está limpio."
        
    jump hub_principal


label loc_bano:
    scene bg bano
    
    if momento_dia == "Tarde" and contenido_gay_activado and not evento_roxy_bano_visto:
        $ evento_roxy_bano_visto = True
        narrador "La puerta está entreabierta. Escuchas agua correr. Es [roxy_name]."
        
        menu:
            "Entrar sin tocar.":
                $ tension_madre += 2
                $ amor_roxy += 3
                show roxy_baño0 at fullscreen with flash
                roxy "¡Oye! ¿No sabes tocar?"
                show roxy_baño1 at fullscreen with flash
                mc "La puerta estaba abierta. Culpa tuya."
                roxy "Cierra la boca y pásame la toalla. Ya que estás aquí de mirón..."
                show roxy_baño2 at fullscreen with flash
                narrador "Roxy te mira con una sonrisa muy provocativa mientras el agua resbala por sus curvas."
                show roxy_baño3 at fullscreen with flash
                roxy "Deja de verme el culo... parece que quieres comértelo."
                
                # CORRECCIÓN DE ERROR: Faltaban los dos puntos (:) al final de las opciones
                menu:
                    "Ese cuerpo está para eso y más, [roxy_name].":
                        $ amor_roxy += 3
                        roxy "Mmm... al menos eres honesto. Pásame esa toalla antes de que te quedes babeando."
                        
                    "Bájate de tu nube. Ni que fueras para tanto.":
                        $ amor_roxy -= 2
                        roxy "Idiota. Lárgate de aquí y cierra la puerta."

            "Cerrar la puerta e irte.":
                $ odio_roxy += 1
                narrador "Decides no buscar problemas hoy y te vas en silencio."
                
    elif momento_dia == "Tarde" and not contenido_gay_activado:
        narrador "El baño está ocupado. Roxy está cantando desafinada bajo la ducha."
    else:
        narrador "El baño está libre y huele a humedad."
        
    jump hub_principal


label loc_cuarto_mc:
    scene bg cuarto_mc
    narrador "Este es tu cuarto. Es pequeño y frío."
    
    menu:
        "Dormir una siesta (Avanzar tiempo)":
            mc "Un rato en la cama no me hará daño."
            jump avanzar_tiempo
            
        "Volver al pasillo":
            jump hub_principal


# 11. Motor de paso de tiempo
label avanzar_tiempo:
    if momento_dia == "Mañana":
        $ momento_dia = "Tarde"
    elif momento_dia == "Tarde":
        $ momento_dia = "Noche"
    else:
        $ momento_dia = "Mañana"
        $ dia += 1
        
        # Reseteamos los eventos al cambiar de día
        $ evento_madre_cocina_visto = False
        $ evento_roxy_bano_visto = False
        
    scene black with dissolve
    narrador "Unas horas más tarde..."
    
    # Evento automático al cambiar el día
    if dia == 2 and momento_dia == "Mañana":
        scene bg cuarto_mc
        show sprite kiry at right, zoom_sprite
        kiry "¡Despierta, [mc_name]! Me aburro."
        mc "¿Qué quieres, enana?"
        kiry "No me digas enana. Tengo frío, hazme un espacio."
        narrador "Se mete bajo tus sábanas antes de que puedas protestar, pegando sus piernas a las tuyas."
        $ amor_kiry += 2
        
    jump hub_principal