# ==========================================
# 1. Variables de nombres y RELACIONES
# ==========================================
default mc_name = "MC"

# Nombres propios
default madre_name = "Madre"
default roxy_name = "Roxy"
default h_mayor_name = "Roxane"
default h_menor_name = "Kiry"

# VARIABLES DE ROL
default madre_rol = "madre"
default roxy_rol = "hermana"
default roxane_rol = "hermana mayor"
default kiry_rol = "hermana menor"

# Variable de control interna
default tipo_relacion = "familia" 

# ==========================================
# 2. Declaración de personajes
# ==========================================
define mc = Character("[mc_name]", color="#3366FF")
define madre = Character("[madre_name]", color="#33CC33")
define roxy = Character("[roxy_name]", color="#FF66B2")
define roxane = Character("[h_mayor_name]", color="#8A2BE2")
define kiry = Character("[h_menor_name]", color="#FFFF33")
define narrador = Character(None)

# ==========================================
# 3. Efectos y transformaciones
# ==========================================
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

transform fullscreen:
    size (1920, 1080)
    align (0.5, 0.5)

transform zoom_sprite:
    zoom 1.5
    yalign 1.0

# ==========================================
# 4. Variables de Sandbox y Tiempo
# ==========================================
default dia = 1
default momento_dia = "Mañana"
default contenido_gay_activado = False

# ==========================================
# 5. Sistema de Estadísticas
# ==========================================
default amor_madre = 0
default tension_madre = 0

default amor_roxy = 0
default odio_roxy = 0

default amor_roxane = 0
default tension_roxane = 0

default amor_kiry = 0
default odio_kiry = 0

# ==========================================
# 6. Variables de control de eventos
# ==========================================
default evento_madre_cocina_visto = False
default evento_roxy_bano_visto = False
default evento_playcartas_visto = False
default evento_roxane_yoga_visto = False
default evento_kiry_platica_visto = False

# ==========================================
# 7. Imágenes (Fondos y Sprites Base)
# ==========================================
image bg sala = "fondo_casa.png"
image bg pasillo = "fondo_casa.png"
image bg cocina = "fondo_casa.png"
image bg bano = "fondo_casa.png"
image bg cuarto_mc = "fondo_casa.png"
image bg tormenta = "fondo_casa.png"
image bg pasillo_arriba = "pasillo_arriba.png"
image bg cuarto_madre = "cuarto_madre.png"
image bg cuarto_roxane = "cuarto_roxane.png"
image bg cuarto_roxy = "cuarto_roxy.png"
image bg cuarto_kiry = "cuarto_kiry.png"

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

# Imágenes de Escenas: Kiry Plática
image kiri_platica1 = "kiri_platica1.png"
image kiri_platica2 = "kiri_platica2.png"
image kiri_platica3 = "kiri_platica3.png"
image kiri_platica4 = "kiri_platica4.png"
image kiri_platica5 = "kiri_platica5.png"
image kiri_platica6 = "kiri_platica6.png"

# Imágenes de Escenas: Roxane Yoga
image roxane_yoga1 = "roxane_yoga1.png"
image roxane_yoga2 = "roxane_yoga2.png"
image roxane_yoga3 = "roxane_yoga3.png"
image roxane_yoga4 = "roxane_yoga4.png"
image roxane_yoga5 = "roxane_yoga5.png"
image roxane_yoga6 = "roxane_yoga6.png"
image roxane_yoga7 = "roxane_yoga7.png"
image roxane_yoga8 = "roxane_yoga8.png"

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

# ==========================================
# 8. Inicio del juego (Configuración)
# ==========================================
label start:

    $ mc_name = renpy.input("¿Cuál es tu nombre?").strip() or "MC"
    $ madre_name = renpy.input("¿Cómo se llama la dueña de casa/madre?").strip() or "Madre"
    $ roxy_name = renpy.input("¿Cómo se llama la chica trans (23 años)?").strip() or "Roxy"
    $ h_mayor_name = renpy.input("¿Cómo se llama la mujer mayor (29 años)?").strip() or "Roxane"
    $ h_menor_name = renpy.input("¿Cómo se llama la chica joven (20 años)?").strip() or "Kiry"

    narrador "Antes de empezar, define tu relación con las personas que viven en la casa."

    menu:
        "¿Qué relación tienes con ellas?"

        "Somos Familia (Relaciones de sangre/políticas)":
            $ tipo_relacion = "familia"
            jump establecer_familia

        "Somos Compañeros de piso / inquilinos":
            $ tipo_relacion = "inquilinos"
            jump establecer_inquilinos

label establecer_familia:
    narrador "Entendido. Son familia. Ahora define el parentesco específico usando a [h_menor_name] de ejemplo."

    menu:
        "En este script, [h_menor_name] es tu...?"

        "Hermana (Viven con su madre)":
            $ madre_rol = "madre"
            $ roxy_rol = "hermana"
            $ roxane_rol = "hermana mayor"
            $ kiry_rol = "hermana menor"
            narrador "Vives con tu [madre_rol] y tus hermanas."

        "Prima (Viven con su tía)":
            $ madre_rol = "tía"
            $ roxy_rol = "prima"
            $ roxane_rol = "prima mayor"
            $ kiry_rol = "prima menor"
            narrador "Vives con tu [madre_rol] y tus primas."

        "Tía joven (Vives con tu abuela)":
            $ madre_rol = "abuela"
            $ roxy_rol = "tía"
            $ roxane_rol = "tía mayor"
            $ kiry_rol = "tía menor"
            narrador "Vives con tu [madre_rol] y tus tías jóvenes."

    jump finalizar_configuracion

label establecer_inquilinos:
    narrador "Entendido. No son familia directa."

    $ madre_rol = "casera"
    $ roxy_rol = "compañera"
    $ roxane_rol = "compañera de piso"
    $ kiry_rol = "compañera de cuarto"
    
    narrador "Vives alquilado con tu [madre_rol] y tus [kiry_rol]s."

    jump finalizar_configuracion
    
label finalizar_configuracion:

    menu:
        "Este juego contiene temas para adultos. ¿Aceptarías contenido GAY con [roxy_name] (siendo tu [roxy_rol])?"

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

# ==========================================
# 9. El "Hub" o Pasillos
# ==========================================
label hub_principal:
    scene bg pasillo with dissolve
    narrador "Estás en el pasillo principal de la planta baja."

    menu:
        "¿A dónde quieres ir?"

        "Planta Baja (Sala, Cocina, Baño)":
            jump menu_planta_baja
            
        "Planta Alta (Habitaciones)":
            jump menu_planta_alta
            
        "Avanzar el tiempo":
            jump avanzar_tiempo

label menu_planta_baja:
    menu:
        "Ir a la Sala":
            jump loc_sala
        "Ir a la Cocina":
            jump loc_cocina
        "Ir al Baño":
            jump loc_bano
        "Volver":
            jump hub_principal

label menu_planta_alta:
    scene bg pasillo_arriba with dissolve
    narrador "El pasillo de arriba es más estrecho. Aquí están todas las habitaciones."
    
    menu:
        "Tu Cuarto ([mc_name])":
            jump loc_cuarto_mc
        "Cuarto de [madre_name] ([madre_rol])":
            jump loc_cuarto_madre
        "Cuarto de [h_mayor_name] ([roxane_rol])":
            jump loc_cuarto_roxane
        "Cuarto de [roxy_name] ([roxy_rol])":
            jump loc_cuarto_roxy
        "Cuarto de [h_menor_name] ([kiry_rol])":
            jump loc_cuarto_kiry
        "Bajar las escaleras":
            jump hub_principal

# ==========================================
# 10. Locaciones y Eventos 
# ==========================================
# --- CUARTOS ---
label loc_cuarto_madre:
    scene bg cuarto_madre
    if momento_dia == "Noche":
        narrador "La puerta está entreabierta. [madre_name] está sentada en su cama aplicándose crema en las piernas."
        show sprite mom at right, zoom_sprite
        madre "¿Necesitas algo antes de dormir, [mc_name]?"
        mc "Solo pasaba a ver si todo estaba en orden."
        madre "Todo bien. Aunque esta cama se siente demasiado grande para una sola persona con este frío..."
    else:
        narrador "El cuarto de tu [madre_rol] está impecable y huele a su perfume."
    jump menu_planta_alta

label loc_cuarto_roxane:
    scene bg cuarto_roxane
    if momento_dia == "Tarde":
        show sprite roxane at right, zoom_sprite
        roxane "Si vas a entrar, cierra la puerta. Hay corrientes de aire."
        mc "Siempre tan hospitalaria, [h_mayor_name]."
        roxane "No me molestes, estoy intentando leer. Aunque si quieres ser útil, podrías masajearme los hombros."
    else:
        narrador "El cuarto de [h_mayor_name] es ordenado y algo frío."
    jump menu_planta_alta

label loc_cuarto_roxy:
    scene bg cuarto_roxy
    if momento_dia == "Mañana":
        show sprite roxy at right, zoom_sprite
        roxy "¡Cuidado donde pisas! Todavía no termino de arreglar mis cosas."
        mc "Parece que explotó una maleta aquí dentro."
        roxy "Es el precio de la belleza. ¿Te gusta mi outfit o vas a seguir criticando, [mc_name]?"
    else:
        narrador "El cuarto de [roxy_name] tiene un espejo enorme y mucha ropa por todas partes."
    jump menu_planta_alta

label loc_cuarto_kiry:
    scene bg cuarto_kiry
    if momento_dia == "Tarde":
        show sprite kiry at right, zoom_sprite
        kiry "¡[mc_name]! Ven a jugar conmigo, me aburro muchísimo."
        mc "Tengo cosas que hacer, [h_menor_name]."
        kiry "No seas amargado. Si te quedas, te dejo que me ayudes a elegir qué pijama ponerme."
    else:
        narrador "El cuarto de [h_menor_name] es un caos de peluches y cargadores de celular."
    jump menu_planta_alta
    
label loc_cuarto_mc:
    scene bg cuarto_mc
    narrador "Este es tu cuarto. Es pequeño y frío."

    menu:
        "Dormir una siesta (Avanzar tiempo)":
            mc "Un rato en la cama no me hará daño."
            jump avanzar_tiempo

        "{color=#f00}Jugar a las Cartas con [roxy_name]{/color}" if momento_dia == "Noche" and evento_roxy_bano_visto and amor_roxy >= 5 and not evento_playcartas_visto:
            jump evento_cartas_roxy

        "Volver al pasillo":
            jump menu_planta_alta

# --- SALA ---
label loc_sala:
    scene bg sala
    
    if momento_dia == "Mañana" and not evento_roxane_yoga_visto:
        jump evento_yoga_roxane
        
    elif momento_dia == "Tarde" and not evento_kiry_platica_visto:
        jump evento_platica_kiry
        
    elif momento_dia == "Noche":
        narrador "La sala está oscura. [h_mayor_name] está sentada en el sofá con una copa de vino."
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

# --- COCINA ---
label loc_cocina:
    scene bg cocina
    if momento_dia == "Mañana" and not evento_madre_cocina_visto:
        $ evento_madre_cocina_visto = True
        narrador "[madre_name] está sacando unas latas de los estantes inferiores."
        show Vista_cocina at fullscreen with flash
        narrador "Tu [madre_rol] lleva un vestido de tirantes rojos. Sin darse cuenta, la tela se ha subido, exponiendo sus muslos y su trasero."
        mc "Mierda... menuda vista."
        show Vista_cocina2 at fullscreen with flash

        menu:
            "Quedarte mirando descaradamente.":
                $ tension_madre += 3
                narrador "No intentas disimular. Ella se da cuenta al voltear."
                show Vista_cocina3 at fullscreen with flash
                madre "¿Te gusta la vista, [mc_name]?"
                mc "Si te pones así, es imposible mirar a otro lado."
                if tipo_relacion == "familia":
                    madre "Eres un descarado... y soy tu [madre_rol]. Ten un poco de respeto, aunque me guste que prestes atención."
                else:
                    madre "Eres un descarado... pero me gusta que prestes atención, [mc_name]."
                show Vista_cocina4 at fullscreen with flash
                madre "Mejor ven y ayúdame con esto."

            "Ofrecerle ayuda.":
                $ amor_madre += 2
                mc "Déjame ayudarte con eso antes de que te caigas."
                show Vista_cocina5 at fullscreen with flash
                madre "Gracias, [mc_name]. Qué considerado eres."

            "Ignorarla y servirte café.":
                $ odio_madre += 1
                narrador "Pasas de largo buscando tu taza. Ella se acomoda el vestido rápidamente, algo ofendida por tu frialdad."
    else:
        narrador "No hay nadie en la cocina. El fregadero está limpio."
    jump hub_principal

# --- BAÑO ---
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
                roxy "Deja de verme el culo... soy tu [roxy_rol], parece que quieres comértelo."

                menu:
                    "Ese cuerpo está para eso y más, [roxy_name].":
                        $ amor_roxy += 3
                        if tipo_relacion == "familia":
                            roxy "Mmm... que cosas dices de tu [roxy_rol]. Pásame esa toalla antes de que te quedes babeando."
                        else:
                            roxy "Mmm... atrevido para ser un [roxy_rol]. Pásame esa toalla antes de que te quedes babeando."

                    "Bájate de tu nube. Ni que fueras para tanto.":
                        $ amor_roxy -= 2
                        roxy "Idiota. Lárgate de aquí y cierra la puerta."

            "Cerrar la puerta e irte.":
                $ odio_roxy += 1
                narrador "Decides no buscar problemas hoy y te vas en silencio."

    elif momento_dia == "Tarde" and not contenido_gay_activado:
        narrador "El baño está ocupado. [roxy_name] está cantando desafinada bajo la ducha."
    else:
        narrador "El baño está libre y huele a humedad."
    jump hub_principal

# --- EVENTOS ESPECÍFICOS ---

label evento_yoga_roxane:
    $ evento_roxane_yoga_visto = True
    
    show roxane_yoga1 at fullscreen with dissolve
    narrador "Entras a la sala y encuentras a [h_mayor_name] en el suelo. Lleva ropa deportiva muy ajustada y está estirando."
    
    show roxane_yoga2 at fullscreen
    mc "¿Yoga a estas horas y con este frío?"
    
    show roxane_yoga3 at fullscreen
    roxane "Algunos tenemos disciplina, [mc_name]. No todos podemos pasarnos el encierro pudriéndonos en la cama."
    
    show roxane_yoga4 at fullscreen
    roxane "Además, hazte un favor y aléjate. Apestas a pereza y tu ropa huele mal. Me desconcentras."
    
    show roxane_yoga5 at fullscreen
    narrador "Su tono es despectivo y cortante, pero la postura en la que está expone cada curva de su cuerpo de forma agresiva."
    
    menu:
        "No te pases de lista, sea tu [roxane_rol] o no.":
            $ tension_roxane += 3
            show roxane_yoga6 at fullscreen
            mc "Bájale a tu tono. El agua caliente está racionada, no es mi culpa. Si no te gusta mi presencia, vete a tu cuarto."
            
            show roxane_yoga7 at fullscreen
            roxane "Tsk... qué carácter. Al menos demuestras tener algo de sangre en las venas en lugar de solo agachar la cabeza."
            
            show roxane_yoga8 at fullscreen
            narrador "Te lanza una mirada afilada, pero notas una leve sonrisa de satisfacción en su rostro antes de ignorarte y seguir con lo suyo."
        
        "Admirar la vista en silencio y coquetear.":
            $ amor_roxane += 2
            show roxane_yoga6 at fullscreen
            mc "Como digas. Aunque con esas posturas que me estás regalando, el olor es lo de menos."
            
            show roxane_yoga7 at fullscreen
            roxane "¿Eres idiota? Cierra la boca y deja de mirarme así."
            
            show roxane_yoga8 at fullscreen
            narrador "Se queja y te da la espalda, pero notas cómo se ruboriza un poco. No hace ningún esfuerzo por cubrirse ni cambiar a una posición más recatada."
            
    jump hub_principal

label evento_platica_kiry:
    $ evento_kiry_platica_visto = True
    
    show kiri_platica1 at fullscreen with dissolve
    narrador "[h_menor_name] está sentada en el sofá, moviendo los pies de forma impaciente y jugando con su cabello."
    
    show kiri_platica2 at fullscreen
    kiry "¡Al fin sales de tu cueva, [mc_name]! Ven, siéntate aquí un rato."
    
    show kiri_platica3 at fullscreen
    mc "¿Qué mosca te picó ahora?"
    
    show kiri_platica4 at fullscreen
    kiry "Estoy aburrida. Ya me cansé de ver las paredes y el techo. Dame algo de atención."
    
    show kiri_platica5 at fullscreen
    kiry "Dime la verdad... ¿Crees que me estoy viendo fea con tanto encierro? Siento que parezco un oso desaliñado."
    
    menu:
        "Te ves bien, como siempre.":
            $ amor_kiry += 3
            show kiri_platica6 at fullscreen
            mc "Tranquila, te ves linda. El encierro no te ha quitado lo atractiva."
            kiry "Aww... sabía que en el fondo no eras tan insensible de roca. Gracias, [mc_name]."
            narrador "Te regala una sonrisa genuina y se acurruca un poco más cerca de ti en el sofá, buscando tu calor."
        
        "Te ves como una niña caprichosa.":
            $ odio_kiry += 2
            show kiri_platica6 at fullscreen
            mc "Te ves igual de mandona y desordenada que siempre. Deja de quejarte."
            kiry "¡Oye! Eres un amargado de lo peor. Ojalá te congeles en el pasillo."
            narrador "Cruza los brazos, hace un puchero ofendida y se voltea hacia el otro lado indignada."
            
    jump hub_principal

label evento_cartas_roxy:
    $ evento_playcartas_visto = True

    show playcartas1 at fullscreen with dissolve
    roxy "¿Aburrido, [mc_name]? Juguemos unas manos. A ver si tienes agallas."

    show playcartas2 at fullscreen
    mc "¿Apostando qué? No hay un peso en esta casa."

    show playcartas3 at fullscreen
    roxy "Prendas. Strip poker de toda la vida. Pierdes y te quitas algo. Sin llorar."

    show playcartas4 at fullscreen with flash
    narrador "Aceptas el reto. Ganas la primera ronda con facilidad."
    roxy "Mierda... bien, un trato es un trato."

    show playcartas5 at fullscreen
    narrador "[roxy_name] se quita su collar negro con una sonrisa desafiante y lo tira a la cama."

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
    narrador "Te quitas la camisa sin protestar. Notas cómo los ojos de [roxy_name] bajan rápidamente por tu torso."

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
    narrador "Se quita su tanga rosa sin un gramo de vergüenza."

    show playcartas19 at fullscreen
    narrador "[roxy_name] está desnuda. La habitación de pronto se siente mucho más caliente."

    show playcartas20 at fullscreen
    roxy "¿Te gusta lo que ves? Tienes la boca medio abierta."

    show playcartas21 at fullscreen
    mc "No pienses que la tienes fácil."
    roxy "Mírate, pareces un animal."

    show playcartas22 at fullscreen
    roxy "Tan duro por fuera... me pregunto qué más estará duro ahora mismo."

    show playcartas23 at fullscreen
    narrador "Ella se inclina sobre la cama, mostrándose descaradamente para antojarte."

    show playcartas24 at fullscreen
    roxy "¿Qué vas a hacer [mc_name]?"

    show playcartas25 at fullscreen
    roxy "Vamos, dime."

    show playcartas26 at fullscreen
    narrador "Los dedos de [mc_name] se introducen en el ano de [roxy_name]."

    show playcartas27 at fullscreen
    if tipo_relacion == "familia":
        roxy "Estoy lista para recibirte [roxy_rol]ito, siempre he querido que juegues conmigo por ahí. Hazme tu puta, la puta de tu [roxy_rol] soy yo, [roxy_name]."
    else:
        roxy "Estoy lista para recibirte [mc_name], siempre he querido que juegues conmigo por ahí. Hazme tu puta, la puta de la casa soy yo, [roxy_name]."

    show playcartas28 at fullscreen
    narrador "La tensión está a punto de reventar. Su cavidad anal está lista para recibirte cuando..."

    madre "¡Chicos! ¡La cena ya está caliente! ¡Bajen al comedor ahora mismo!"

    narrador "Ambos saltan del susto, separándose de golpe como si los hubieran quemado."

    mc "Mierda... [madre_name]."

    roxy "Jaja... salvado por la campana, Romeo. Vístete rápido. Te espero abajo."

    $ amor_roxy += 5
    $ tension_roxane += 2 

    jump avanzar_tiempo


# ==========================================
# 11. Motor de paso de tiempo
# ==========================================
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
        $ evento_roxane_yoga_visto = False
        $ evento_kiry_platica_visto = False

    scene black with dissolve
    narrador "Unas horas más tarde..."

    if dia == 2 and momento_dia == "Mañana":
        scene bg cuarto_mc
        show sprite kiry at right, zoom_sprite
        kiry "¡Despierta, [mc_name]! Me aburro."
        mc "¿Qué quieres, enana?"
        kiry "No me digas enana. Tengo frío, hazme un espacio."
        narrador "Se mete bajo tus sábanas antes de que puedas protestar, pegando sus piernas a las tuyas."
        $ amor_kiry += 2

    jump hub_principal