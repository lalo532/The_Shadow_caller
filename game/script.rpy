# ==========================================
# MADRE NOCHE - script.rpy (Versión FINAL limpia)
# Solo contiene inicio, configuración y HUB.
# Los eventos están en game/events/
# ==========================================

# ==========================================
# INICIO DEL JUEGO
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
# HUB PRINCIPAL
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
# AVANZAR TIEMPO (Slow-burn)
# ==========================================
label avanzar_tiempo:
    $ tension_casa += 12

    if momento_dia == "Mañana":
        $ momento_dia = "Tarde"
    elif momento_dia == "Tarde":
        $ momento_dia = "Noche"
    else:
        $ momento_dia = "Mañana"
        $ dia += 1

        $ evento_madre_cocina_visto = False
        $ evento_roxy_bano_visto = False
        $ evento_playcartas_visto = False
        $ evento_roxane_yoga_visto = False
        $ evento_kiry_platica_visto = False

    scene black with dissolve
    narrador "Unas horas más tarde..."

    if dia == 2 and momento_dia == "Mañana":
        jump evento_kiry_cama

    jump hub_principal