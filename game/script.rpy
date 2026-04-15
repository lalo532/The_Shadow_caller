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
default evento_madre_noche_visto = False

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
            show Roxy_muestra1 at fullscreen with flash
            roxy "Muchas gracias por aceptar este contenido."
            pause 2.0
            hide Roxy_muestra1 with dissolve

        "No, omitir.":
            $ contenido_gay_activado = False
            show Roxy_muestra2 at fullscreen with flash
            roxy "Una pena... nos lo perdemos, [mc_name]."
            pause 2.0
            hide Roxy_muestra2 with dissolve

    scene fondo_casa with dissolve

    narrador "La nieve cubre todo. Llevamos días sin poder salir. Tienen suerte de tener calefacción y luz gubernamental."
    narrador "La radio dijo que esto podría durar meses. Por suerte, hay mucha comida enlatada abajo."

    mc "Tres meses encerrados... esto se va a volver una locura."

    show Madre at right, zoom_sprite with easeinright
    madre "Tranquilo, [mc_name]. Todo va a estar bien mientras no nos matemos entre nosotros."
    madre "Voy a organizar la comida. Busca algo que hacer."

    hide Madre with dissolve
    show screen hud_tiempo
    jump hub_principal

# ==========================================
# 9. El "Hub" o Pasillos
# ==========================================
label hub_principal:
    scene fondo_casa with dissolve
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
    scene pasillo_arriba with dissolve
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
    # Recuerda usar fondo_casa si no has agregado la imagen de cuarto_madre al .bat
    scene cuarto_madre 
    
    # Primero verificamos si tienen alto nivel de amor (Evento especial)
    if momento_dia == "Noche" and amor_roxy >= 10:
        jump evento_madrexroxy

    # Si es de noche pero el amor es 5 o menos (Evento normal)
    elif momento_dia == "Noche" and amor_roxy <= 5:
        narrador "La puerta está entreabierta. [madre_name] está sentada en su cama aplicándose crema en las piernas."
        show Madre at right, zoom_sprite
        madre "¿Necesitas algo antes de dormir, [mc_name]?"
        mc "Solo pasaba a ver si todo estaba en orden."
        madre "Todo bien. Aunque esta cama se siente demasiado grande para una sola persona con este frío..."
        jump menu_planta_alta

    # Para cualquier otro momento del día o si el amor está entre 6 y 9
    else:
        narrador "El cuarto de tu [madre_rol] está impecable y huele a su perfume."
        jump menu_planta_alta


# Separamos la escena especial en su propio label para mantener el orden
label evento_madrexroxy:
    
    narrador "Te acercas a la habitación. La puerta no está cerrada del todo. Escuchas jadeos ahogados y el sonido húmedo de piel contra piel."
    
    scene mom_roxy at fullscreen with flash 
    
    narrador "Te asomas con cuidado. Lo que ves te deja helado. [roxy_name] está sobre la cama, dominando a tu [madre_rol]."
    
    madre "Mghh... Ay, [roxy_name]... con todo el esfuerzo que haces por verte tan femenina, y resulta que esto sigue siendo lo más rico que tienes."
    
    scene mom_roxy1 at fullscreen with dissolve
    
    roxy "Cállate y traga. Sabes que soy bisexual... y si te estoy dejando usarme así, es porque el encierro me tiene loca."
    roxy "Además... me sirve para calentar motores. Sabes perfectamente a quién tengo en la cabeza mientras te follo."
    
    scene mom_roxy2 at fullscreen with dissolve
    
    madre "Ah... ¿[mc_name]? Ja... no seas ingenua, zorrita. Él me mira a mí."
    madre "Desde que nos quedamos atrapados aquí, veo cómo se le van los ojos a mis tetas. Tiene una mirada de hambre pura... de un hombre de verdad que está a punto de perder el control. Eso me empapa."
    
    scene mom_roxy3 at fullscreen with dissolve
    
    roxy "Te equivocas. Él tiene esa misma mirada ruda conmigo. Y me encanta."
    roxy "Me gusta que no tiene filtros, me trata como quiere... necesito sentir cómo me agarra duro contra la pared y me revienta. Me pone a mil pensar en lo bruto que puede llegar a ser."
    
    scene mom_roxy4 at fullscreen with flash
    
    madre "Mmmhhh... dios... entonces méntelo más profundo, perra. Imagina que es él quien te está usando así."
    roxy "Ahhh... joder, sí. Las dos estamos igual de enfermas por él."
    
    narrador "El sonido de los gemidos se vuelve más intenso. Sientes una erección a punto de rasgarte el pantalón."
    
    mc "(Mierda... están completamente locas. Será mejor que me vaya antes de que me descubran y esto se salga de control.)"
    
    narrador "Te alejas lentamente por el pasillo, intentando calmar tu respiración."

    jump menu_planta_alta
    
label loc_cuarto_roxane:
    scene cuarto_roxane
    if momento_dia == "Tarde":
        show Roxane at right, zoom_sprite
        roxane "Si vas a entrar, cierra la puerta. Hay corrientes de aire."
        mc "Siempre tan hospitalaria, [h_mayor_name]."
        roxane "No me molestes, estoy intentando leer. Aunque si quieres ser útil, podrías masajearme los hombros."
    else:
        narrador "El cuarto de [h_mayor_name] es ordenado y algo frío."
    jump menu_planta_alta

label loc_cuarto_roxy:
    scene cuarto_roxy
    if momento_dia == "Mañana":
        show Roxy at right, zoom_sprite
        roxy "¡Cuidado donde pisas! Todavía no termino de arreglar mis cosas."
        mc "Parece que explotó una maleta aquí dentro."
        roxy "Es el precio de la belleza. ¿Te gusta mi outfit o vas a seguir criticando, [mc_name]?"
    else:
        narrador "El cuarto de [roxy_name] tiene un espejo enorme y mucha ropa por todas partes."
    jump menu_planta_alta

label loc_cuarto_kiry:
    scene cuarto_kiry
    if momento_dia == "Tarde":
        show Kiri at right, zoom_sprite
        kiry "¡[mc_name]! Ven a jugar conmigo, me aburro muchísimo."
        mc "Tengo cosas que hacer, [h_menor_name]."
        kiry "No seas amargado. Si te quedas, te dejo que me ayudes a elegir qué pijama ponerme."
    else:
        narrador "El cuarto de [h_menor_name] es un caos de peluches y cargadores de celular."
    jump menu_planta_alta
    
label loc_cuarto_mc:
    scene fondo_casa
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
    scene fondo_casa
    
    if momento_dia == "Mañana" and not evento_roxane_yoga_visto:
        jump evento_yoga_roxane
        
    elif momento_dia == "Tarde" and not evento_kiry_platica_visto:
        jump evento_platica_kiry
        
    elif momento_dia == "Noche":
        # Verificamos primero el evento de la madre
        if amor_madre >= 1 and not evento_madre_noche_visto:
            jump evento_noche_madre
            
        # Si no se cumple o ya se vio, carga la escena normal de Roxane
        else:
            narrador "La sala está oscura. [h_mayor_name] está sentada en el sofá con una copa de vino."
            show Roxane at right, zoom_sprite
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
            hide Roxane
            
    else:
        narrador "La sala está vacía. Solo se escucha el viento golpeando la ventana."
        
    jump hub_principal

# --- COCINA ---
label loc_cocina:
    scene fondo_casa
    if momento_dia == "Mañana" and not evento_madre_cocina_visto:
        $ evento_madre_cocina_visto = True
        narrador "[madre_name] está sacando unas latas de los estantes inferiores."
        show madre_cocina1 at fullscreen with flash
        narrador "Tu [madre_rol] lleva un vestido de tirantes rojos. Sin darse cuenta, la tela se ha subido, exponiendo sus muslos y su trasero."
        mc "Mierda... menuda vista."
        show madre_cocina2 at fullscreen with flash

        menu:
            "Quedarte mirando descaradamente.":
                $ tension_madre += 3
                narrador "No intentas disimular. Ella se da cuenta al voltear."
                show madre_cocina3 at fullscreen with flash
                madre "¿Te gusta la vista, [mc_name]?"
                mc "Si te pones así, es imposible mirar a otro lado."
                if tipo_relacion == "familia":
                    madre "Eres un descarado... y soy tu [madre_rol]. Ten un poco de respeto, aunque me guste que prestes atención."
                else:
                    madre "Eres un descarado... pero me gusta que prestes atención, [mc_name]."
                show madre_cocina4 at fullscreen with flash
                madre "Mejor ven y ayúdame con esto."

            "Ofrecerle ayuda.":
                $ amor_madre += 2
                mc "Déjame ayudarte con eso antes de que te caigas."
                show madre_cocina5 at fullscreen with flash
                madre "Gracias, [mc_name]. Qué considerado eres."

            "Ignorarla y servirte café.":
                $ odio_madre += 1
                narrador "Pasas de largo buscando tu taza. Ella se acomoda el vestido rápidamente, algo ofendida por tu frialdad."
    else:
        narrador "No hay nadie en la cocina. El fregadero está limpio."
    jump hub_principal

# --- BAÑO ---
label loc_bano:
    scene fondo_casa
    if momento_dia == "Tarde" and contenido_gay_activado and not evento_roxy_bano_visto:
        $ evento_roxy_bano_visto = True
        narrador "La puerta está entreabierta. Escuchas agua correr. Es [roxy_name]."
        menu:
            "Entrar sin tocar.":
                $ tension_madre += 2
                $ amor_roxy += 3
                show roxy_baño1 at fullscreen with flash
                roxy "¡Oye! ¿No sabes tocar?"
                show roxy_baño2 at fullscreen with flash
                mc "La puerta estaba abierta. Culpa tuya."
                roxy "Cierra la boca y pásame la toalla. Ya que estás aquí de mirón..."
                show roxy_baño3 at fullscreen with flash
                narrador "Roxy te mira con una sonrisa muy provocativa mientras el agua resbala por sus curvas."
                show roxy_baño4 at fullscreen with flash
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
        roxy "Estoy lista para recibirte [roxy_rol], siempre he querido que juegues conmigo por ahí. Hazme tu puta, la puta de tu [roxy_rol] soy yo, [roxy_name]."
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
# NUEVO EVENTO: Madre en la Sala (Noche, Amor >= 25)
# ==========================================


label evento_noche_madre:
    $ evento_madre_noche_visto = True
    # --- FASE 1: CONFESIÓN ---
    scene sala night with dissolve
    narrador "Bajas a la sala a oscuras. Las sombras apenas dejan ver la silueta de tu [madre_rol] en el sofá. Lleva un camisón que no oculta casi nada de sus curvas."
    
    show madre_noche_1 at fullscreen with dissolve
    narrador "Se pone de pie lentamente cuando te ve. Su mirada es pesada, cargada de una decisión que lleva años guardando."
    
    show madre_noche_2 at fullscreen with dissolve
    madre "Pensé que estabas dormido, [mc_name]..."
    
    show madre_noche_3 at fullscreen with dissolve
    madre "No podía dormir. El frío, el encierro... todo esto me está volviendo loca. Me hace pensar en cosas que no debería."
    
    show madre_noche_4 at fullscreen with dissolve
    madre "He pasado años cuidándote, viéndote crecer... y viéndome a mí misma marchitarme con un hombre débil. Un esposo que nunca me miró de la forma en que tú lo haces."
    
    show madre_noche_5 at fullscreen with dissolve
    mc "Estás borracha o delirando."
    
    show madre_noche_6 at fullscreen with dissolve
    madre "Ni una ni la otra. Estoy harta de verte mirar a Roxy. Me hierve la sangre ver cómo buscas su atención, cómo la deseas..."
    
    show madre_noche_7 at fullscreen with dissolve
    madre "Soy mucho más mujer que ella. Tengo más experiencia, más hambre... Tengo más años deseándote en silencio de los que ella lleva viva. Y esta noche, te lo voy a demostrar."

    # --- FASE 2: PROPUESTA Y DESNUDO ESPECTACULAR ---
    show madre_noche_propuesta1 at fullscreen with flash
    narrador "Sin dudarlo un segundo, [madre_name] comienza a quitarse el camisón. Su cuerpo se revela en la penumbra de la sala."
    
    show madre_noche_propuesta2 at fullscreen
    madre "Llevo tanto tiempo esperando este momento..."
    
    show madre_noche_propuesta3 at fullscreen
    mc "Dios... sabes que esto es una locura absoluta."
    
    show madre_noche_propuesta4 at fullscreen
    madre "La única locura es haber esperado tanto. Mírame, [mc_name]. ¿Acaso no soy lo que siempre has querido?"
    
    show madre_noche_propuesta5 at fullscreen
    madre "¿Crees que Roxy te miraría con este hambre? ¿Crees que ella sabría cómo usarte de verdad?"
    
    show madre_noche_propuesta6 at fullscreen
    mc "Cállate... no lo hagas más difícil."
    
    show madre_noche_propuesta7 at fullscreen
    madre "Házmelo difícil tú. Tómame. Hazme tuya como solo tú sabes hacerlo."
    
    show madre_noche_propuesta8 at fullscreen
    narrador "[madre_name] se desliza el resto de su ropa. Su cuerpo está totalmente expuesto ante ti, temblando de anticipación."
    
    show madre_noche_propuesta9 at fullscreen
    madre "He imaginado tus manos en mí... tus labios en los míos. Cada vez que pasabas a mi lado, cada vez que te veía dormir..."
    
    show madre_noche_propuesta10 at fullscreen
    mc "He querido esto... pero no así."
    
    show madre_noche_propuesta11 at fullscreen
    madre "Mientes. Quieres que te use. Quieres sentir mi cuerpo contra el tuyo."
    
    show madre_noche_propuesta12 at fullscreen
    madre "He visto cómo me miras cuando cocinas, cuando me agacho. He sentido cómo tu deseo me quemaba la piel."
    
    show madre_noche_propuesta13 at fullscreen
    madre "Eres rudo, posesivo... exactamente lo que necesito. Él nunca tuvo esa oscuridad, ese fuego que tienes tú."
    
    show madre_noche_propuesta14 at fullscreen
    mc "Estás enferma."
    
    show madre_noche_propuesta15 at fullscreen
    madre "Enferma de ti, sí. Me pone a mil pensar en lo bruto que puedes llegar a ser. Necesito sentir cómo me agarras duro contra la pared y me revientas."
    
    show madre_noche_propuesta16 at fullscreen
    madre "Sé que quieres romperme, [mc_name]. Sé que quieres poseer a tu [madre_rol]."
    
    show madre_noche_propuesta17 at fullscreen
    madre "No me importa lo que piensen los demás. No me importa el pecado. Solo me importas tú, tu deseo, tu cuerpo sobre el mío."
    
    show madre_noche_propuesta18 at fullscreen
    madre "Él nunca fue suficiente. Tú... tú eres más hombre que él jamás fue."
    
    show madre_noche_propuesta19 at fullscreen
    mc "Mierda... cállate..."
    
    show madre_noche_propuesta20 at fullscreen
    madre "¿Vas a seguir hablando o vas a coger lo que te ofrezco?"
    
    show madre_noche_propuesta21 at fullscreen
    madre "Mírame... Mírame bien. Soy tuya. Todo mi ser está a tu disposición."
    
    show madre_noche_propuesta22 at fullscreen
    madre "Solo tienes que decir que sí..."

    # --- FASE 3: ORAL ESPECTACULAR ---
    show madre_noche_oral at fullscreen with flash
    narrador "Sin esperar respuesta, [madre_name] se arrodilla ante ti. La tensión se rompe con el primer contacto húmedo de su lengua."
    
    show madre_noche_oral2 at fullscreen
    mc "Dios... no... para..."
    
    show madre_noche_oral3 at fullscreen
    madre "Mmmhhh... te gusta, ¿verdad, [mc_name]? No puedes negarlo ahora."
    
    show madre_noche_oral4 at fullscreen
    mc "Eres increíble... esto es una locura..."
    
    show madre_noche_oral5 at fullscreen
    madre "Solo es el principio, cariño... Mírame. Soy tu [madre_rol] y te estoy sirviendo. ¿Acaso no es lo más rudo que has hecho?"

    # --- FASE 4: EL ACTO (PENETRACIÓN) ESPECTACULAR ---
    show madre_noche_sexo1 at fullscreen with flash
    narrador "La sala se llena de jadeos rítmicos y el sonido húmedo de la piel contra la piel. La tensión acumulada estalla en un acto primal."
    
    show madre_noche_sexo2 at fullscreen
    madre "¡Ahhh! ¡Por fin... Dios, [mc_name], por fin estás dentro!"
    
    show madre_noche_sexo3 at fullscreen
    mc "Eres una zorra... siempre supe que querías esto."
    
    show madre_noche_sexo4 at fullscreen
    madre "¡Sí, soy tu zorra, cariño! ¡Trátame como la ruda que soy! ¡Rompe a tu [madre_rol]!"
    
    show madre_noche_sexo5 at fullscreen
    mc "¡Eres ruda, enfermiza... y me encanta!"
    
    show madre_noche_sexo6 at fullscreen
    madre "¡Mmmhhh... dios... sí! ¡Fóllame como él nunca pudo! ¡Olvida a Roxy! ¡Yo soy tuya, cariño, solo tuya!"

    # --- FASE 5: ARREPENTIMIENTO DRAMÁTICO ---
    show madre_noche_sexo_arrepentimiento at fullscreen with dissolve
    narrador "El silencio cae pesado en la sala. Las respiraciones agitadas se calman lentamente. La adrenalina baja y la realidad golpea con dureza."
    
    show madre_noche_sexo_arrepentimiento2 at fullscreen
    narrador "[madre_name] se queda inmóvil bajo tu cuerpo, con la mirada perdida en el techo de la sala."
    
    show madre_noche_sexo_arrepentimiento3 at fullscreen
    madre "Mierda... ¿qué... qué hemos hecho?"
    
    show madre_noche_sexo_arrepentimiento4 at fullscreen
    madre "Soy una monstruosidad... Soy tu [madre_rol] y..."
    
    show madre_noche_sexo_arrepentimiento5 at fullscreen
    mc "Tranquila. Pasó. Los dos lo quisimos."
    
    show madre_noche_sexo_arrepentimiento6 at fullscreen
    madre "¡Cállate! No lo entiendes. Esto... esto es imperdonable."
    
    show madre_noche_sexo_arrepentimiento7 at fullscreen
    madre "Fue el encierro... la tensión me volvió loca. Tienes que olvidar que esto pasó. Fue un error. Un asqueroso error."
    
    show madre_noche_sexo_arrepentimiento8 at fullscreen
    narrador "[Agrega aquí diálogo explícito sobre el arrepentimiento asqueroso]"
    
    show madre_noche_sexo_arrepentimiento9 at fullscreen
    mc "No finjas ahora. Lo quisiste. Lo pediste."
    
    show madre_noche_sexo_arrepentimiento10 at fullscreen
    madre "¡He dicho que te calles! ¡No me vuelvas a mirar así! Olvídalo todo, ¿me oyes? ¡Olvida que soy tuya!"
    
    narrador "Se viste a trompicones, evitando mirarte a la cara a toda costa, y sale corriendo hacia el pasillo de arriba. Te quedas solo en el sofá."
    
    $ tension_madre += 10
    $ amor_madre += 2 
    
    jump hub_principal




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
        scene fondo_casa
        show Kiri at right, zoom_sprite
        kiry "¡Despierta, [mc_name]! Me aburro."
        mc "¿Qué quieres, enana?"
        kiry "No me digas enana. Tengo frío, hazme un espacio."
        narrador "Se mete bajo tus sábanas antes de que puedas protestar, pegando sus piernas a las tuyas."
        $ amor_kiry += 2

    jump hub_principal