# ==========================================
# EVENTS/ROXY.RPY - Versión Mejorada y Extensa (Slow-Burn + Backstory Integrado)
# ==========================================

# ==========================================
# LOCACIÓN: Cuarto de Roxy
# ==========================================
label loc_cuarto_roxy:
    scene cuarto_roxy
    
    if momento_dia == "Mañana":
        show Roxy at right, zoom_sprite
        roxy "¡Cuidado donde pisas! Todavía no termino de arreglar mis cosas. Este cuarto parece un campo de batalla."
        mc "Parece que explotó una maleta aquí dentro."
        
        roxy "Es el precio de la belleza, [mc_name]. ¿Te gusta mi outfit o vas a seguir criticando como siempre?"
        roxy "Aunque... a veces me pregunto si realmente me ves como una chica o solo como tu [roxy_rol] rarita."
        
        menu:
            "Elogiar su apariencia con honestidad":
                $ amor_roxy += 5
                mc "La verdad es que te ves bien. Muy bien. Ese outfit te queda perfecto."
                roxy "Mmm... gracias. No sabes lo mucho que significa que me digas eso sin que suene a lástima."
                
            "Bromear de forma juguetona":
                $ tension_roxy += 3
                mc "Te ves como si hubieras robado el closet de una influencer."
                roxy "Ja, idiota. Pero al menos me miras. Eso ya es algo."
                
            "Ser directo sobre su feminidad":
                $ amor_roxy += 6
                mc "Te ves como una chica muy atractiva, Roxy. Punto."
                roxy "...No digas cosas así si no las sientes de verdad. Me pones nerviosa."
    
    else:
        narrador "El cuarto de [roxy_name] tiene un espejo enorme y ropa tirada por todas partes. Se nota que está intentando encontrar su identidad en medio de este caos."
    
    jump menu_planta_alta

# ==========================================
# EVENTO: Baño con Roxy (Tarde - Solo si contenido_gay activado)
# ==========================================
label loc_bano:
    scene fondo_casa
    if momento_dia == "Tarde" and contenido_gay_activado and not evento_roxy_bano_visto:
        $ evento_roxy_bano_visto = True
        narrador "La puerta está entreabierta. Escuchas agua correr. Es [roxy_name]."
        
        menu:
            "Entrar sin tocar.":
                $ tension_roxy += 4
                $ amor_roxy += 4
                show roxy_baño1 at fullscreen with flash
                roxy "¡Oye! ¿No sabes tocar?"
                
                show roxy_baño2 at fullscreen with flash
                mc "La puerta estaba abierta. Culpa tuya."
                
                show roxy_baño3 at fullscreen with flash
                roxy "Cierra la boca y pásame la toalla. Ya que estás aquí de mirón..."
                
                narrador "Roxy te mira con una sonrisa provocativa mientras el agua resbala por sus curvas. Sin embargo, notas un leve rubor de inseguridad en su rostro."
                
                show roxy_baño4 at fullscreen with flash
                roxy "Deja de verme el culo... soy tu [roxy_rol], parece que quieres comértelo. O... ¿realmente te gusta lo que ves?"
                
                menu:
                    "Ese cuerpo está para eso y más, [roxy_name]. Eres muy atractiva.":
                        $ amor_roxy += 5
                        roxy "Mmm... qué cosas dices de tu [roxy_rol]. No sabes lo mucho que necesitaba escuchar eso."
                        roxy "A veces dudo si alguien me puede desear tal como soy."
                        
                    "Eres sexy, Roxy. No tienes nada que envidiarle a nadie.":
                        $ amor_roxy += 6
                        roxy "Joder... me vas a hacer sonrojar de verdad. Ven, acércate un poco más."
                        
                    "Bájate de tu nube. Ni que fueras para tanto.":
                        $ amor_roxy -= 3
                        roxy "Idiota... siempre tan frío. Lárgate de aquí y cierra la puerta."
            
            "Cerrar la puerta e irte.":
                $ odio_roxy += 2
                narrador "Decides no buscar problemas y te vas en silencio."
                roxy "(desde dentro) ...Cobarde."
    
    elif momento_dia == "Tarde" and not contenido_gay_activado:
        narrador "El baño está ocupado. [roxy_name] está cantando desafinada bajo la ducha."
    else:
        narrador "El baño está libre y huele a humedad."
    jump hub_principal

# ==========================================
# EVENTO: Jugar a las cartas con Roxy (Strip Poker) - Versión Extensa
# ==========================================
label evento_cartas_roxy:
    $ evento_playcartas_visto = True

    show playcartas1 at fullscreen with dissolve
    roxy "¿Aburrido, [mc_name]? Juguemos unas manos. A ver si tienes agallas."
    
    show playcartas2 at fullscreen
    mc "¿Apostando qué? No hay un peso en esta casa."
    
    show playcartas3 at fullscreen
    roxy "Prendas. Strip poker de toda la vida. Pierdes y te quitas algo. Sin llorar. ¿O te da miedo verme desnuda?"
    
    show playcartas4 at fullscreen with flash
    narrador "Aceptas el reto. Ganas la primera ronda con facilidad."
    roxy "Mierda... bien, un trato es un trato."
    
    show playcartas5 at fullscreen
    narrador "[roxy_name] se quita su collar negro con una sonrisa desafiante y lo tira a la cama."
    
    show playcartas6 at fullscreen with flash
    narrador "Ganas la segunda ronda. Ella te mira cruzando los brazos."
    
    show playcartas7 at fullscreen
    roxy "Hoy vienes con suerte. Disfruta la vista, no durará."
    narrador "Se quita la playera blanca por la cabeza, dejando su sostén a la vista. Notas cómo intenta disimular su nerviosismo."
    
    show playcartas8 at fullscreen with flash
    narrador "Roxy gana la tercera ronda con una jugada perfecta."
    
    show playcartas9 at fullscreen
    roxy "Mi turno. Fuera esa camisa, [mc_name]. Quiero ver si estás tan duro por fuera como pareces."
    
    show playcartas10 at fullscreen
    narrador "Te quitas la camisa sin protestar. Notas cómo los ojos de [roxy_name] bajan rápidamente por tu torso."
    
    show playcartas11 at fullscreen with flash
    narrador "La suerte vuelve a ti. Ganas la cuarta ronda."
    
    show playcartas12 at fullscreen
    roxy "Vaya... me estás dejando sin defensas muy rápido."
    narrador "Roxy se desliza el short por las piernas lentamente, sin dejar de mirarte. Su respiración se ha vuelto más pesada."
    
    show playcartas14 at fullscreen with flash
    narrador "Roxy gana la quinta ronda."
    
    show playcartas15 at fullscreen
    roxy "Tus pantalones, [mc_name]. Quítatelos. Quiero ver cuánto te excita esto."
    
    show playcartas16 at fullscreen with flash
    narrador "Juegan una ronda rápida y muy agresiva. Las miradas están fijas. Ganas tú."
    
    show playcartas17 at fullscreen
    roxy "Bueno... creo que me quedé sin opciones, ¿no?"
    
    show playcartas18 at fullscreen
    narrador "Se quita su tanga rosa sin un gramo de vergüenza, aunque sus manos tiemblan ligeramente."
    
    show playcartas19 at fullscreen
    narrador "[roxy_name] está completamente desnuda. La habitación de pronto se siente mucho más caliente."
    
    show playcartas20 at fullscreen
    roxy "¿Te gusta lo que ves? Tienes la boca medio abierta. ¿O te da miedo admitir que te excita tu [roxy_rol] trans?"
    
    show playcartas21 at fullscreen
    mc "No pienses que la tienes fácil."
    roxy "Mírate... pareces un animal enjaulado."
    
    show playcartas22 at fullscreen
    roxy "Tan duro por fuera... me pregunto qué más estará duro ahora mismo."
    
    show playcartas23 at fullscreen
    narrador "Ella se inclina sobre la cama, mostrándose descaradamente para antojarte."
    
    show playcartas24 at fullscreen
    roxy "¿Qué vas a hacer, [mc_name]? ¿Vas a seguir mirando o vas a tocar?"
    
    show playcartas25 at fullscreen
    roxy "Vamos... dime. ¿Quieres follarme como a una chica de verdad?"
    
    show playcartas26 at fullscreen
    narrador "Los dedos de [mc_name] se introducen en el ano de [roxy_name]. Ella gime con una mezcla de placer y alivio."
    
    show playcartas27 at fullscreen
    roxy "Estoy lista para recibirte [mc_rol]... siempre he querido que juegues conmigo por ahí. Hazme tu puta. La puta de tu [roxy_rol] soy yo, [roxy_name]."
    roxy "Quiero sentir que me aceptas completamente... con todo lo que soy."
    
    show playcartas28 at fullscreen
    narrador "La tensión está a punto de reventar. Su cavidad anal está lista para recibirte cuando..."

    madre "¡Chicos! ¡La cena ya está caliente! ¡Bajen al comedor ahora mismo!"

    narrador "Ambos saltan del susto, separándose de golpe como si los hubieran quemado."
    
    mc "Mierda... [madre_name]."
    
    roxy "Jaja... salvado por la campana, Romeo. Vístete rápido. Te espero abajo."
    roxy "(en voz baja) ...Aunque la próxima vez no pienso dejar que nos interrumpan."

    $ amor_roxy += 8
    $ tension_roxy += 5

    jump avanzar_tiempo