# ==========================================
# EVENTS/ROXANE.RPY
# ==========================================

# Evento Sala con Roxane (Tarde)
label evento_sala_roxane:
    $ evento_roxane_sala_visto = True
    
    scene fondo_casa with dissolve
    narrador "Entras a la sala y ves a [h_mayor_name] sentada en el sofá, completamente concentrada en un libro."

    show ROXANE_SALA1 at fullscreen with dissolve
    narrador "El silencio solo se rompe por el viento afuera y el pasar de las páginas."

    show ROXANE_SALA2 at fullscreen
    mc "Sigues leyendo... ¿No te cansas de estar tan seria todo el tiempo?"

    show ROXANE_SALA3 at fullscreen
    roxane "Alguien tiene que mantener la mente ocupada en este encierro. No todos podemos pasarnos el día mirando la nieve como idiotas."

    # Se estira sin querer
    show ROXANE_SALA4 at fullscreen with flash
    narrador "Roxane se estira un poco para acomodarse mejor. Su camisa se levanta ligeramente, dejando ver parte de su abdomen suave."

    show ROXANE_SALA5 at fullscreen
    mc "..."

    show ROXANE_SALA6 at fullscreen
    narrador "La vista es breve, pero suficiente para que se te note la mirada."

    menu:
        "Decirle directamente que se ve hermosa":
            $ amor_roxane += 4
            $ tension_roxane += 3
            show ROXANE_SALA7 at fullscreen with dissolve
            mc "Sabes... te ves hermosa cuando te concentras así. Y ese estirón de hace un momento no ayudó a que me concentre."

            show ROXANE_SALA8 at fullscreen
            roxane "¡¿Qué?! ¡No digas idioteces!"
            
            show ROXANE_SALA9 at fullscreen
            narrador "Su cara se pone completamente roja. Intenta esconderse detrás del libro, pero es obvio que le afectó."

        "Mantenerlo casual":
            $ tension_roxane += 2
            show ROXANE_SALA7 at fullscreen
            mc "Te ves cómoda... se nota que el libro te gusta de verdad."
            roxane "Obvio que me gusta. Es mejor que hablar con gente molesta."

    show ROXANE_SALA10 at fullscreen with dissolve
    roxane "...Bueno, si tanto quieres molestar, siéntate. Pero no hagas ruido."

    narrador "Te sientas a su lado. El sofá se siente más pequeño de lo normal."

    show ROXANE_SALA11 at fullscreen
    narrador "Roxane está claramente apenada. Sus dedos aprietan el libro con más fuerza de la necesaria."

    show ROXANE_SALA12 at fullscreen
    roxane "No... no me mires tanto. Hace frío y... y ya."

    show ROXANE_SALA13 at fullscreen
    narrador "Se queda callada, pero no se aleja. Su pierna roza la tuya ligeramente y no la retira."

    $ amor_roxane += 2
    jump hub_principal


# Evento Cocina Nocturna con Roxane
label evento_cocina_roxane_noche:
    $ evento_cocina_roxane_visto = True
    
    scene fondo_casa with dissolve
    narrador "Bajas a la cocina tarde en la noche. La luz es tenue y solo se escucha el viento."

    show cocina_roxane1 at fullscreen with dissolve
    narrador "[h_mayor_name] está sola, tomando una taza de café caliente. Parece pensativa."

    show cocina_roxane2 at fullscreen
    mc "No esperaba encontrarte aquí a esta hora."

    show cocina_roxane3 at fullscreen
    roxane "No podía dormir. El café ayuda... un poco."

    show cocina_roxane4 at fullscreen
    roxane "Este encierro me está volviendo loca. Antes podía fingir que todo estaba bien... pero aquí no hay donde esconderse."

    show cocina_roxane5 at fullscreen
    mc "Tú siempre pareces tener todo bajo control."
    roxane "Eso es lo que quiero que crean los demás."

    show cocina_roxane6 at fullscreen with flash
    narrador "Roxane baja la mirada. Su expresión cambia."

    show cocina_roxane7 at fullscreen
    roxane "...Eres el único que me habla como si no fuera una perra fría todo el tiempo. No sé si me molesta o... me gusta."

    show cocina_roxane8 at fullscreen
    narrador "Su voz se suaviza. Se ve genuinamente nerviosa."

    show cocina_roxane9 at fullscreen
    roxane "No sé qué me pasa contigo, [mc_name]. Desde que estamos atrapados aquí... pienso demasiado en ti."

    show cocina_roxane10 at fullscreen
    mc "Yo también pienso en ti. Más de lo que debería."

    show cocina_roxane11 at fullscreen
    narrador "El silencio se vuelve pesado, pero agradable. Roxane no responde de inmediato, solo te mira."

    show cocina_roxane12 at fullscreen with dissolve
    roxane "...Idiota. No digas cosas así si no las piensas de verdad."
    narrador "Su mirada dice todo lo contrario. Está claramente flechada, aunque todavía lucha contra ello."

    $ amor_roxane += 6
    $ tension_roxane += 4

    narrador "Terminan la plática en voz baja. Cuando subes a tu cuarto, sientes que algo importante acaba de empezar entre ustedes."

    jump hub_principal