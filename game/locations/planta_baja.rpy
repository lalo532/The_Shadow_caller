# ==========================================
# LOCACIÓN: SALA (planta baja)
# ==========================================
label loc_sala:
    scene fondo_casa with dissolve

    # === PRIORIDAD DE EVENTOS (de mayor a menor importancia) ===
    
    # Evento especial de la madre (prioridad alta)
    if momento_dia == "Noche" and amor_madre >= 1 and not evento_madre_noche_visto:
        jump evento_noche_madre

    # Nuevo evento: Conversación en la Sala con Roxane (Tarde)
    elif momento_dia == "Tarde" and not evento_roxane_sala_visto:
        jump evento_sala_roxane

  
    # Evento viejo de Yoga (Mañana) - se mantiene
    elif momento_dia == "Mañana" and not evento_roxane_yoga_visto:
        jump evento_yoga_roxane

    # Evento viejo de Kiry (Tarde)
    elif momento_dia == "Tarde" and not evento_kiry_platica_visto:
        jump evento_platica_kiry

    # Escena normal de noche en la sala (cuando no hay eventos especiales)
    elif momento_dia == "Noche":
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

    # Si no hay nada especial
    else:
        narrador "La sala está vacía. Solo se escucha el viento golpeando la ventana."
        
    jump hub_principal



    # ==========================================
# LOCACIÓN: COCINA (Planta Baja)
# ==========================================
label loc_cocina:
    scene fondo_casa with dissolve

    # === PRIORIDAD DE EVENTOS ===

    # 1. Evento nocturno especial con Roxane (nuevo)
    if momento_dia == "Noche" and evento_roxane_sala_visto and amor_roxane >= 5 and not evento_cocina_roxane_visto:
        jump evento_cocina_roxane_noche

    # 2. Evento normal de la Madre en la cocina (Mañana)
    elif momento_dia == "Mañana" and not evento_madre_cocina_visto:
        $ evento_madre_cocina_visto = True
        narrador "[madre_name] está sacando unas latas de los estantes inferiores."
        show madre_cocina1 at fullscreen with flash
        narrador "Tu [madre_rol] lleva un vestido de tirantes rojos. Sin darse cuenta, la tela se ha subido, exponiendo sus muslos y su trasero generoso."
        mc "Mierda... menuda vista."
        show madre_cocina2 at fullscreen with flash

        menu:
            "Quedarte mirando descaradamente sin disimular":
                $ tension_madre += 6
                narrador "No intentas disimular. Ella se da cuenta al voltear y te sostiene la mirada por varios segundos."
                show madre_cocina3 at fullscreen with flash
                madre "¿Te gusta lo que ves, [mc_name]?"
                mc "Si te pones así, es imposible mirar a otro lado. Ese culo me tiene la verga palpitando."
                madre "Eres un descarado... pero me gusta que prestes atención. Hace mucho que nadie me mira como tú lo haces."
                show madre_cocina4 at fullscreen with flash
                madre "Ven aquí y ayúdame... o quédate mirando. No sé qué me excita más."

            "Ofrecerle ayuda de forma considerada":
                $ amor_madre += 4
                mc "Déjame ayudarte con eso antes de que te caigas."
                show madre_cocina5 at fullscreen with flash
                madre "Gracias, [mc_name]. Qué considerado eres... siempre lo has sido. A veces me pregunto qué habría sido de mí sin ti."

            "Ignorarla y servirte café fríamente":
                $ odio_madre += 2
                narrador "Pasas de largo sin decir nada. Ella se acomoda el vestido rápidamente, visiblemente decepcionada y dolida por tu indiferencia."
                madre "(en voz baja) ...Siempre tan frío conmigo últimamente."

    # Si no hay ningún evento especial
    else:
        narrador "No hay nadie en la cocina. El fregadero está limpio."

    jump hub_principal