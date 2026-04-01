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
define narrador = Character(None)

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
default amor_madre = 0
default tension_madre = 0

default amor_roxy = 0
default odio_roxy = 0

default amor_roxane = 0
default tension_roxane = 0

default amor_kiry = 0
default odio_kiry = 0

# 6. Variables de control de eventos
default evento_madre_cocina_visto = False
default evento_roxy_bano_visto = False
default evento_playcartas_visto = False

# 7. Imágenes (Fondos y Sprites Base)
image bg sala = "fondo_casa.png"
image bg pasillo = "fondo_casa.png"
image bg cocina = "fondo_casa.png"
image bg bano = "fondo_casa.png"
image bg cuarto_mc = "fondo_casa.png"
image bg tormenta = "fondo_casa.png" 

image sprite roxy = "Roxy.png"
image sprite mom = "Madre.png"
image sprite roxane = "Roxane.png"
image sprite kiry = "Kiry.png"

image Roxy_primer_imagen = "Roxy_muestra1.png"
image Roxy_rechazo = "Roxy_muestra2.png"

# Imágenes de Escenas: Cocina y Baño
image Vista_cocina = "madre_cocina1.png"
image Vista_cocina2 = "madre_cocina2.png"
image Vista_cocina3 = "madre_cocina3.png"
image Vista_cocina4 = "madre_cocina4.png"
image Vista_cocina5 = "madre_cocina5.png"

image roxy_baño0 = "roxy_baño1.png"
image roxy_baño1 = "roxy_baño2.png"
image roxy_baño2 = "roxy_baño3.png"
image roxy_baño3 = "roxy_baño4.png"

# Imágenes de Escenas: Cartas con Roxy
image playcartas1 = "playcartas1.png"
image playcartas2 = "playcartas2.png"
image playcartas3 = "playcartas3.png"
image playcartas4 = "playcartas4.png"
image playcartas5 = "playcartas5.png"
image playcartas6 = "playcartas6.png"
image playcartas7 = "playcartas7.png"
image playcartas8 = "playcartas8.png"
image playcartas9 = "playcartas9.png"
image playcartas10 = "playcartas10.png"
image playcartas11 = "playcartas11.png"
image playcartas12 = "playcartas12.png"
image playcartas13 = "playcartas13.png"
image playcartas14 = "playcartas14.png"
image playcartas15 = "playcartas15.png"
image playcartas16 = "playcartas16.png"
image playcartas17 = "playcartas17.png"
image playcartas18 = "playcartas18.png"
image playcartas19 = "playcartas19.png"
image playcartas20 = "playcartas20.png"
image playcartas21 = "playcartas21.png"
image playcartas22 = "playcartas22.png"
image playcartas23 = "playcartas23.png"
image playcartas24 = "playcartas24.png"
image playcartas25 = "playcartas25.png"
image playcartas26 = "playcartas26.png"
image playcartas27 = "playcartas27.png"
image playcartas28 = "playcartas28.png"

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
    
    # Menú corregido. Usamos {color=#f00} dentro del texto para pintarlo de rojo.
    menu:
        "Dormir una siesta (Avanzar tiempo)":
            mc "Un rato en la cama no me hará daño."
            jump avanzar_tiempo
            
        "{color=#f00}Jugar a las Cartas con Roxy{/color}" if momento_dia == "Noche" and evento_roxy_bano_visto and amor_roxy >= 5 and not evento_playcartas_visto:
            jump evento_cartas_roxy

        "Volver al pasillo":
            jump hub_principal

# --- Escena del Juego de Cartas con Roxy ---
label evento_cartas_roxy:
    $ evento_playcartas_visto = True
    
    show playcartas1 at fullscreen with dissolve
    roxy "¿Aburrido, [mc_name]?"
    
    mc "Un poco. Las paredes se me están cerrando."
    
    narrador "Roxy se sienta en la orilla de tu cama y te mira un momento en silencio, con una expresión más suave de lo normal."
    
    roxy "Estaba pensando en antes... cuando empecé con todo el rollo de las cirugías y el tratamiento."
    
    mc "¿A qué viene eso ahora?"
    
    roxy "A que fuiste el único en esta casa que no me miró como a un bicho raro. Estuviste ahí apoyándome cuando ni yo me aguantaba."
    
    mc "Era lo que tocaba. Para eso estamos."
    
    narrador "Roxy sonríe de lado. Se estira un poco, arqueando la espalda para resaltar su figura a propósito."
    
    roxy "Lo sé. Pero me encanta ver cómo me miras ahora. Quedé bastante bien, ¿no?"
    
    mc "Siempre has sido terca. Conseguiste lo que querías."
    
    roxy "Y a mí me gusta provocarte. Ver cómo te pones tenso cuando me acerco y no sabes a dónde mirar."
    roxy "A veces pienso que todo ese apoyo tuyo venía con otras intenciones escondidas..."
    
    mc "Estás loca, Roxy."
    
    roxy "Pruébalo. Juguemos unas manos. A ver si tienes agallas de mirarme a la cara."
    
    show playcartas2 at fullscreen
    mc "¿Apostando qué? No hay un peso en esta casa."
    
    show playcartas3 at fullscreen
    roxy "Prendas. Strip poker de toda la vida. Pierdes y te quitas algo. Sin llorar."
    
    show playcartas4 at fullscreen with flash
    narrador "Aceptas el reto. Ganas la primera ronda con facilidad."
    roxy "Mierda... bien, un trato es un trato."
    
    show playcartas5 at fullscreen
    narrador "Roxy se quita su collar negro con una sonrisa desafiante y lo tira a la cama."
    
    show playcartas6 at fullscreen with flash
    narrador "Ganas la segunda ronda. Ella te mira cruzando los brazos."
    
    show playcartas7 at fullscreen
    roxy "Hoy vienes con suerte. Disfruta la vista, no durará."
    narrador "Se quita la playera blanca por la cabeza, dejando su sostén a la vista."
    
    show playcartas8 at fullscreen with flash
    narrador "Roxy gana la tercera ronda con una jugada perfecta."
    
    show playcartas9 at fullscreen
    roxy "Mi turno. Fuera esa camisa, [mc_name]."
    
    show playcartas10 at fullscreen
    narrador "Te quitas la camisa sin protestar. Notas cómo los ojos de Roxy bajan rápidamente por tu torso."
    
    show playcartas11 at fullscreen with flash
    narrador "La suerte vuelve a ti. Ganas la cuarta ronda."
    
    show playcartas12 at fullscreen
    roxy "Vaya... me estás dejando sin defensas muy rápido."
    narrador "Roxy se desliza el short por las piernas lentamente, sin dejar de mirarte."
    
    show playcartas14 at fullscreen with flash
    narrador "Roxy gana la quinta ronda."
    
    show playcartas15 at fullscreen
    roxy "Tus pantalones, [mc_name]. Quítatelos."
    
    show playcartas16 at fullscreen with flash
    narrador "Juegan una ronda rápida y muy agresiva. Las miradas están fijas. Ganas tú."
    
    show playcartas17 at fullscreen
    roxy "Bueno... creo que me quedé sin opciones, ¿no?"
    
    show playcartas18 at fullscreen
    narrador "se quita su tanga rosa sin un gramo de vergüenza."
    
    show playcartas19 at fullscreen
    narrador "Roxy está desnuda. La habitación de pronto se siente mucho más caliente."
    
    show playcartas20 at fullscreen
    roxy "¿Te gusta lo que ves? Tienes la boca medio abierta."
    
    show playcartas21 at fullscreen
    mc "no pienses que la tienes facil."
    roxy "mirate pareces un animal"
    
    show playcartas22 at fullscreen
    roxy "Tan duro por fuera... me pregunto qué más estará duro ahora mismo."
    
    show playcartas23 at fullscreen
    narrador "Ella se inclina sobre la cama, mostrándose descaradamente para antojarte."
    
    show playcartas24 at fullscreen
    roxy "¿Qué vas a hacer [mc_name]?"
    
    show playcartas25 at fullscreen
    roxy "vamos dime"
    
    show playcartas26 at fullscreen
    narrador "los dedos de [mc_name] se intruden en el ano de [roxy_name]"
    
    show playcartas27 at fullscreen
    roxy "estoy lista para recibirte hermanito siempre eh querido que juegues conmigo por ahi , hazme tu puta , la puta de tu hermana soy yo [roxy_name]"
    
    show playcartas28 at fullscreen
    narrador "La tensión está a punto de reventar. Su cavidad anal esta lista para recibirte  cuando..."
    
    madre "¡Hijos! ¡La cena ya está caliente! ¡Bajen al comedor ahora mismo!"
    
    narrador "Ambos saltan del susto, separándose de golpe como si los hubieran quemado."
    
    mc "Mierda... mamá."
    
    roxy "Jaja... salvado por la campana, Romeo. Vístete rápido. Te espero abajo."
    
    $ amor_roxy += 5
    $ tension_roxane += 2 # La tensión general en la casa sube
    
    jump avanzar_tiempo


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
        $ evento_playcartas_visto = False
        
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