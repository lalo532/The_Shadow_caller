# ==========================================
# MADRE NOCHE - script.rpy (Versión FINAL mejorada)
# Inicio, configuración, backstory orgánico y HUB
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
            $ mc_rol = "hermano"
            narrador "Vives con tu [madre_rol] y tus hermanas."

        "Prima (Viven con su tía)":
            $ madre_rol = "tía"
            $ roxy_rol = "prima"
            $ roxane_rol = "prima mayor"
            $ kiry_rol = "prima menor"
            $ mc_rol = "primo"
            narrador "Vives con tu [madre_rol] y tus primas."

        "Tía joven (Vives con tu abuela)":
            $ madre_rol = "abuela"
            $ roxy_rol = "tía"
            $ roxane_rol = "tía mayor"
            $ kiry_rol = "tía menor"
            $ mc_rol = "sobrino"
            narrador "Vives con tu [madre_rol] y tus tías jóvenes."

    jump finalizar_configuracion

label establecer_inquilinos:
    narrador "Entendido. No son familia directa."

    $ madre_rol = "casera"
    $ roxy_rol = "compañera"
    $ roxane_rol = "compañera de piso"
    $ kiry_rol = "compañera de cuarto"
    $ mc_rol = "inquilino"
    
    narrador "Vives alquilado con tu [madre_rol] y tus [kiry_rol]s."

    jump finalizar_configuracion
    
label finalizar_configuracion:

    menu:
        "Este juego contiene temas para adultos. ¿Aceptarías contenido GAY con [roxy_name] (siendo tu [roxy_rol])?"

        "Sí, lo acepto.":
            $ contenido_gay_activado = True
            show Roxy_muestra1 at fullscreen with flash
            roxy "Muchas gracias por aceptar este contenido."
            pause 1.5
            hide Roxy_muestra1 with dissolve

        "No, omitir.":
            $ contenido_gay_activado = False
            show Roxy_muestra2 at fullscreen with flash
            roxy "Una pena... nos lo perdemos, [mc_name]."
            pause 1.5
            hide Roxy_muestra2 with dissolve

    scene fondo_casa with dissolve

    # ==========================================
    # INTRODUCCIÓN + BACKSTORY ORGÁNICO (usando sprites)
    # ==========================================
    narrador "La nieve lleva semanas cayendo sin parar. La casa está completamente aislada del mundo exterior."
    narrador "Llevan más de un mes encerrados aquí. La calefacción funciona, pero la tensión crece día a día."

    show Madre at right, zoom_sprite with easeinright
    madre "Tranquilo, [mc_name]. Todo va a estar bien mientras nos mantengamos unidos."
    madre "Aunque... a veces siento que este encierro está sacando cosas que llevábamos años guardando."

    hide Madre with dissolve
    show Roxane at left, zoom_sprite with easeinleft
    roxane "No seas dramática, [madre_rol]. Solo es nieve. Sobreviviremos."
    roxane "Aunque admito que estar tanto tiempo encerrada con la misma gente... termina por cambiar la forma en que los ves."

    hide Roxane with dissolve
    show Roxy at right, zoom_sprite with easeinright
    roxy "Yo solo quiero que alguien me mire como a una chica de verdad... no como 'la rarita de la casa'."
    roxy "Especialmente tú, [mc_name]. Siempre fuiste el único que no me trató con lástima."

    hide Roxy with dissolve
    show Kiri at left, zoom_sprite with easeinleft
    kiry "¡Yo solo quiero que alguien me preste atención! Me aburro muchísimo aquí..."
    kiry "Y tú siempre me has cuidado, [mc_name]. Eres como mi héroe desde que era niña."

    hide Kiri with dissolve

    mc "(Pensando) Llevo años siendo el único hombre fuerte en esta casa. Papá nunca estuvo cuando lo necesitábamos..."
    mc "(Pensando) Madre se ha marchitado al lado de un hombre débil. Roxane reprime todo. Roxy busca validación desesperadamente. Kiry aún me ve como su protector..."
    mc "(Pensando) Este encierro va a terminar por explotar. Y temo que cuando lo haga... ya no habrá vuelta atrás."

    show screen hud_tiempo
    jump hub_principal

# ==========================================
# HUB PRINCIPAL
# ==========================================
label hub_principal:
    scene fondo_casa with dissolve
    narrador "Estás en el pasillo principal de la planta baja. La tensión en el aire es cada vez más palpable."

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
    $ tension_casa += 12   # Aumenta la tensión general para desbloquear eventos

    if momento_dia == "Mañana":
        $ momento_dia = "Tarde"
    elif momento_dia == "Tarde":
        $ momento_dia = "Noche"
    else:
        $ momento_dia = "Mañana"
        $ dia += 1

        # Reset de eventos diarios
        $ evento_madre_cocina_visto = False
        $ evento_roxy_bano_visto = False
        $ evento_playcartas_visto = False
        $ evento_roxane_yoga_visto = False
        $ evento_kiry_platica_visto = False

    scene black with dissolve
    narrador "Unas horas más tarde..."

    if dia == 2 and momento_dia == "Mañana":
        jump evento_kiry_cama   # Evento especial día 2

    jump hub_principal