# ==========================================
# EVENTS/MADRE.RPY - Versión Mejorada (Slow-Burn)
# ==========================================

# ==========================================
# LOCACIÓN: Cuarto de la Madre
# ==========================================
label loc_cuarto_madre:
    scene cuarto_madre 
    
    if momento_dia == "Noche" and amor_roxy >= 10:
        jump evento_madrexroxy
    elif momento_dia == "Noche":
        narrador "La puerta está entreabierta. [madre_name] está sentada en su cama aplicándose crema en las piernas."
        show Madre at right, zoom_sprite
        madre "¿Necesitas algo antes de dormir, [mc_name]?"
        mc "Solo pasaba a ver si todo estaba en orden."
        madre "Todo bien. Aunque esta cama se siente demasiado grande para una sola persona con este frío..."
        jump menu_planta_alta
    else:
        narrador "El cuarto de tu [madre_rol] está impecable y huele a su perfume."
        jump menu_planta_alta

# ==========================================
# EVENTO: Madre y Roxy (espía)
# ==========================================
label evento_madrexroxy:
    narrador "Te acercas a la habitación. La puerta no está cerrada del todo. Escuchas jadeos ahogados y el sonido húmedo de piel contra piel."
    
    scene mom_roxy at fullscreen with flash 
    narrador "Te asomas con cuidado. [roxy_name] está sobre la cama, dominando a tu [madre_rol]."
    
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

# ==========================================
# EVENTO: Cocina con la Madre (Mañana)
# ==========================================
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
                mc "Si te pones así, es imposible mirar a otro lado. Ese culo me tiene la verga palpitando."
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

# ==========================================
# EVENTO NOCHE MADRE - VERSIÓN MEJORADA (SLOW-BURN)
# ==========================================
label evento_noche_madre:
    $ evento_madre_noche_visto = True
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
    madre "Ni una ni la otra. Estoy harta de verte mirar a Roxane. Me hierve la sangre ver cómo buscas su atención, cómo la deseas..."
    
    show madre_noche_7 at fullscreen with dissolve
    madre "Soy mucho más mujer que ella. Tengo más experiencia, más hambre... Tengo más años deseándote en silencio de los que ella lleva viva. Y esta noche, te lo voy a demostrar."

    # === FASE DE TEASE (más lenta e interactiva) ===
    show madre_noche_propuesta1 at fullscreen with flash
    narrador "[madre_name] comienza a bajarse lentamente un tirante del camisón, sin dejar de mirarte."

    menu:
        "Quedarte en silencio y mirar":
            $ tension_madre += 4
            show madre_noche_propuesta2 at fullscreen
            madre "Llevo tanto tiempo esperando este momento... ¿vas a seguir fingiendo que no me deseas?"
            
        "Decirle que esto es una locura":
            $ tension_madre += 2
            show madre_noche_propuesta3 at fullscreen
            mc "Dios... sabes que esto es una locura absoluta."
            madre "La única locura es haber esperado tanto."

    show madre_noche_propuesta4 at fullscreen
    madre "Mírame, [mc_name]. ¿Acaso no soy lo que siempre has querido?"

    show madre_noche_propuesta5 at fullscreen
    madre "¿Crees que Roxane te miraría con este hambre? ¿Crees que ella sabría cómo usar a un hombre de verdad?"

    menu:
        "Admitir que la deseas":
            $ amor_madre += 3
            $ tension_madre += 3
            mc "Maldita sea... sí."
            madre "Entonces deja de hablar y ven por lo que es tuyo."
            
        "Mantener distancia (tease)":
            $ tension_madre += 5
            mc "Esto no debería estar pasando..."
            madre "Pero lo está. Y te estás poniendo duro solo de verme."

    show madre_noche_propuesta6 at fullscreen
    mc "Cállate... no lo hagas más difícil."
    
    show madre_noche_propuesta7 at fullscreen
    madre "Házmelo difícil tú. Tómame. Hazme tuya como solo tú sabes hacerlo."

    # Más progresivo
    show madre_noche_propuesta8 at fullscreen
    narrador "Se desliza el camisón completamente. Su cuerpo maduro y voluptuoso queda expuesto ante ti en la penumbra."

    show madre_noche_propuesta9 at fullscreen
    madre "He imaginado tus manos en mí... tus labios... cada noche que pasabas cerca de mi cuarto."

    show madre_noche_propuesta10 at fullscreen
    mc "He querido esto... pero no así."

    show madre_noche_propuesta11 at fullscreen
    madre "Mientes. Tu cuerpo no miente."

    # CLÍMAX DEL TEASE - Tu imagen favorita
    show madre_noche_propuesta22 at fullscreen with flash
    madre "Mírame bien, [mc_name]... Soy tuya. Todo mi ser está a tu disposición."
    madre "Solo tienes que decir que sí..."

    menu:
        "Tomarla sin piedad (ruta dominante)":
            $ tension_madre += 8
            jump madre_noche_sexo_duro
            
        "Dejar que ella tome el control":
            $ amor_madre += 5
            jump madre_noche_sexo_suave
            
        "Parar en este momento":
            jump madre_noche_rechazo

# ==========================================
# RAMAS DE SEXO (mantengo tus imágenes originales)
# ==========================================
label madre_noche_sexo_duro:
    show madre_noche_oral at fullscreen with flash
    narrador "Sin más palabras, la tomas del cabello y la obligas a arrodillarse."
    # ... aquí puedes seguir añadiendo tus imágenes madre_noche_oral2, oral3, etc.
    jump madre_noche_sexo_continuar

label madre_noche_sexo_suave:
    show madre_noche_oral at fullscreen with flash
    narrador "Ella se arrodilla voluntariamente, mirándote con hambre."
    # ... imágenes orales
    jump madre_noche_sexo_continuar

label madre_noche_sexo_continuar:
    show madre_noche_sexo1 at fullscreen with flash
    narrador "La sala se llena de jadeos y el sonido húmedo de piel contra piel."
    
    show madre_noche_sexo2 at fullscreen
    madre "¡Ahhh! ¡Por fin... Dios, [mc_name], por fin estás dentro!"
    
    show madre_noche_sexo3 at fullscreen
    mc "Eres una zorra... siempre supe que querías esto."
    
    show madre_noche_sexo4 at fullscreen
    madre "¡Sí, soy tu zorra, cariño! ¡Trátame como la ruda que soy! ¡Rompe a tu [madre_rol]!"
    
    # ... resto de imágenes sexo5 y sexo6

    jump madre_noche_arrepentimiento

label madre_noche_arrepentimiento:
    show madre_noche_sexo_arrepentimiento at fullscreen with dissolve
    narrador "El silencio cae pesado después del clímax."
    
    show madre_noche_sexo_arrepentimiento2 at fullscreen
    narrador "[madre_name] se queda inmóvil, con la mirada perdida."
    
    show madre_noche_sexo_arrepentimiento3 at fullscreen
    madre "Mierda... ¿qué hemos hecho?"
    
    # ... resto del arrepentimiento (imágenes 4 a 10)
    
    narrador "Se viste a trompicones y sale corriendo hacia su cuarto."
    
    $ tension_madre += 10
    $ amor_madre += 2 
    jump hub_principal

label madre_noche_rechazo:
    mc "No... esto no puede pasar."
    madre "..."
    narrador "La expresión de [madre_name] cambia a decepción y vergüenza. Se cubre rápidamente y sube a su habitación sin decir una palabra."
    $ tension_madre += 5
    jump hub_principal