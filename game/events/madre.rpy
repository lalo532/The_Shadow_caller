# ==========================================
# EVENTS/MADRE.RPY - Versión Extensa y Mejorada (Slow-Burn Profundo)
# ==========================================

# ==========================================
# LOCACIÓN: Cuarto de la Madre
# ==========================================
label loc_cuarto_madre:
    scene cuarto_madre 
    
    if momento_dia == "Noche" and amor_roxy >= 10:
        jump evento_madrexroxy
    
    elif momento_dia == "Noche":
        narrador "La puerta está entreabierta. [madre_name] está sentada en su cama, aplicándose crema en las piernas con movimientos lentos."
        show Madre at right, zoom_sprite
        
        madre "¿Necesitas algo antes de dormir, [mc_name]?"
        mc "Solo pasaba a ver si todo estaba en orden."
        
        madre "Todo está... en orden. Aunque esta cama se siente cada vez más grande y fría."
        madre "A veces me quedo despierta pensando en cómo han cambiado las cosas... en cómo tú has cambiado."
        
        menu:
            "Preguntarle qué quiere decir":
                $ tension_madre += 6
                mc "Qué quieres decir con eso?"
                madre "Que ya no te veo solo como mi hijo... y eso me aterra y me excita al mismo tiempo."
                
            "Ofrecerle compañía":
                $ amor_madre += 4
                mc "Si quieres, puedo quedarme un rato contigo."
                madre "No digas eso... porque una parte de mí quiere aceptar esa oferta más de lo que debería."
                
            "Cambiar de tema rápidamente":
                mc "Bueno, descansa. Mañana será otro día."
                madre "Sí... otro día más fingiendo que no siento lo que siento."
        
        jump menu_planta_alta
    
    else:
        narrador "El cuarto de tu [madre_rol] está impecable y huele a su perfume favorito."
        jump menu_planta_alta

# ==========================================
# EVENTO: Madre y Roxy (espía) - Más emocional y largo
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
    
    madre "He criado a ese chico... lo he visto convertirse en todo lo que su padre nunca fue. Y ahora no puedo dejar de imaginar cómo sería sentirlo dentro de mí."
    
    scene mom_roxy3 at fullscreen with dissolve
    roxy "Te equivocas. Él tiene esa misma mirada ruda conmigo. Y me encanta."
    roxy "Me gusta que no tiene filtros, me trata como quiere... necesito sentir cómo me agarra duro contra la pared y me revienta."
    
    scene mom_roxy4 at fullscreen with flash
    madre "Mmmhhh... dios... entonces méntelo más profundo, perra. Imagina que es él quien te está usando así."
    roxy "Ahhh... joder, sí. Las dos estamos igual de enfermas por él."
    
    narrador "El sonido de los gemidos se vuelve más intenso. Sientes una erección a punto de rasgarte el pantalón."
    
    mc "(Mierda... mi propia madre diciendo esas cosas... Lleva años sufriendo en silencio y ahora lo admite en voz alta.)"
    
    narrador "Te alejas lentamente por el pasillo, con el corazón latiendo con fuerza y un torbellino de emociones que no sabes cómo manejar."
    jump menu_planta_alta

# ==========================================
# EVENTO: Cocina con la Madre (Mañana) - Más tensión y opciones
# ==========================================
# EVENTO NOCHE MADRE - Versión Extensa y Orgánica (Usando TODAS las imágenes)
# ==========================================
label evento_noche_madre:
    $ evento_madre_noche_visto = True
    scene sala night with dissolve
    narrador "Bajas a la sala a oscuras. Las sombras apenas dejan ver la silueta de tu [madre_rol] en el sofá. Lleva un camisón que no oculta casi nada de sus curvas maduras."
    
    show madre_noche_1 at fullscreen with dissolve
    narrador "Se pone de pie lentamente cuando te ve. Su mirada es pesada, cargada de años de deseo reprimido."
    
    show madre_noche_2 at fullscreen with dissolve
    madre "Pensé que estabas dormido, [mc_name]..."
    
    show madre_noche_3 at fullscreen with dissolve
    madre "No podía dormir. El frío, el encierro... todo esto me está volviendo loca."
    
    show madre_noche_4 at fullscreen with dissolve
    madre "He pasado años cuidándote, viéndote crecer... y viéndome a mí misma marchitarme al lado de un hombre que nunca me valoró como mujer."
    
    show madre_noche_5 at fullscreen with dissolve
    mc "Estás borracha o delirando."
    
    show madre_noche_6 at fullscreen with dissolve
    madre "Ni una ni la otra. Estoy harta de fingir. Harta de verte mirar a Roxane y a las demás... cuando yo soy la que te ha deseado en silencio durante años."
    
    show madre_noche_7 at fullscreen with dissolve
    madre "Soy tu madre... y sé que esto es un pecado. Pero ya no puedo seguir negándolo. Esta noche... solo quiero sentirme deseada por el único hombre que realmente me ha hecho sentir viva."

    # Fase de tease extensa usando todas las imágenes
    show madre_noche_propuesta1 at fullscreen with flash
    narrador "[madre_name] comienza a bajarse lentamente un tirante del camisón, con las manos temblando por la mezcla de miedo y excitación."
    
    menu:
        "Quedarte en silencio y mirar fijamente":
            $ tension_madre += 7
            show madre_noche_propuesta2 at fullscreen
            madre "Dime algo, [mc_name]... ¿alguna vez me has deseado como mujer y no solo como tu madre?"
            
        "Decirle que esto es una locura absoluta":
            $ tension_madre += 4
            show madre_noche_propuesta3 at fullscreen
            mc "Esto es una locura... eres mi madre."
            madre "Lo sé mejor que nadie. Y aun así no puedo dejar de imaginarte dentro de mí."

    show madre_noche_propuesta4 at fullscreen
    madre "Mírame, [mc_name]. ¿Acaso no soy lo que siempre has querido en secreto?"

    show madre_noche_propuesta5 at fullscreen
    madre "¿Crees que Roxane o cualquiera de ellas podría darte lo que yo puedo darte?"

    menu:
        "Admitir que la has deseado durante años":
            $ amor_madre += 7
            $ tension_madre += 8
            mc "Sí... te he deseado más de lo que debería. Desde hace mucho tiempo."
            madre "Entonces ven aquí... y tómame. Hazme sentir mujer por una noche."
            
        "Mantener distancia y provocarla":
            $ tension_madre += 9
            mc "Esto no debería estar pasando... pero no puedo negar que te miro diferente."
            madre "Entonces deja de hablar y actúa. Te estás poniendo duro solo de verme... lo sé."

    show madre_noche_propuesta6 at fullscreen
    mc "Cállate... no lo hagas más difícil."
    
    show madre_noche_propuesta7 at fullscreen
    madre "Házmelo difícil tú. Tómame. Hazme tuya como solo tú sabes hacerlo."

    show madre_noche_propuesta8 at fullscreen
    narrador "Se desliza el camisón completamente. Su cuerpo maduro y voluptuoso queda totalmente expuesto ante ti en la penumbra."

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
            $ tension_madre += 12
            jump madre_noche_sexo_duro
            
        "Dejar que ella tome el control (ruta emocional)":
            $ amor_madre += 8
            jump madre_noche_sexo_suave
            
        "Rechazarla (por ahora)":
            jump madre_noche_rechazo

# ==========================================
# RAMAS DE SEXO - Más extensas y emocionales
# ==========================================
label madre_noche_sexo_duro:
    show madre_noche_oral at fullscreen with flash
    narrador "Sin más palabras, la tomas del cabello y la obligas a arrodillarse."
    madre "¡Sí! ¡Úsame! ¡Hazme sentir viva aunque sea una vez!"
    jump madre_noche_sexo_continuar

label madre_noche_sexo_suave:
    show madre_noche_oral at fullscreen with flash
    narrador "Ella se arrodilla voluntariamente, mirándote con ojos llenos de deseo y miedo."
    madre "Ven aquí, mi niño... déjame mostrarte cuánto te he deseado todos estos años."
    jump madre_noche_sexo_continuar

label madre_noche_sexo_continuar:
    show madre_noche_sexo1 at fullscreen with flash
    narrador "La sala se llena de jadeos y el sonido húmedo de piel contra piel."
    
    show madre_noche_sexo2 at fullscreen
    madre "¡Ahhh! ¡Por fin... Dios, [mc_name], por fin estás dentro de mí!"
    
    show madre_noche_sexo3 at fullscreen
    mc "Eres una zorra... siempre supe que querías esto."
    
    show madre_noche_sexo4 at fullscreen
    madre "¡Sí! ¡Soy tu zorra! ¡Trátame como la mujer que nunca fui tratada!"

    show madre_noche_sexo5 at fullscreen with dissolve
    madre "Más fuerte... no te detengas... ¡Quiero sentir que soy tuya!"

    show madre_noche_sexo6 at fullscreen with dissolve
    mc "Eres mía esta noche... aunque mañana nos arrepintamos."

    jump madre_noche_arrepentimiento

label madre_noche_arrepentimiento:
    show madre_noche_sexo_arrepentimiento at fullscreen with dissolve
    narrador "El silencio cae pesado después del clímax. La realidad golpea con fuerza."
    
    show madre_noche_sexo_arrepentimiento2 at fullscreen
    narrador "[madre_name] se queda inmóvil, con la mirada perdida en el techo."
    
    show madre_noche_sexo_arrepentimiento3 at fullscreen
    madre "Dios mío... ¿qué hemos hecho? Eres mi hijo..."
    
    mc "Madre..."
    madre "No me llames así ahora... duele demasiado."
    
    show madre_noche_sexo_arrepentimiento4 at fullscreen
    narrador "Se viste a trompicones, evitando mirarte a los ojos."
    
    show madre_noche_sexo_arrepentimiento5 at fullscreen
    madre "Esto nunca debió pasar... Olvídalo todo, por favor."
    
    narrador "Sale corriendo hacia su habitación, dejando atrás un silencio pesado y cargado de culpa."
    
    $ tension_madre += 15
    $ amor_madre += 4 
    jump hub_principal

label madre_noche_rechazo:
    mc "No... esto no puede pasar."
    madre "..."
    narrador "La expresión de [madre_name] se rompe en decepción y profunda vergüenza."
    show madre_noche_sexo_arrepentimiento at fullscreen with dissolve
    narrador "Se cubre rápidamente y sube a su habitación sin decir una palabra más."
    $ tension_madre += 8
    jump hub_principal