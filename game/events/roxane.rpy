# ==========================================
# EVENTS/ROXANE.RPY
# Todos los eventos relacionados con Roxane (hermana mayor / tsundere)
# ==========================================

# ==========================================
# LOCACIÓN: Cuarto de Roxane
# ==========================================
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

# ==========================================
# EVENTO: Yoga con Roxane (Mañana - Sala)
# ==========================================
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

# ==========================================
# EVENTO: Noche en la Sala con Roxane (cuando no hay evento de la madre)
# ==========================================
label loc_sala:
    scene fondo_casa
    
    # Prioridad a otros eventos
    if momento_dia == "Mañana" and not evento_roxane_yoga_visto:
        jump evento_yoga_roxane
        
    elif momento_dia == "Tarde" and not evento_kiry_platica_visto:
        jump evento_platica_kiry
        
    elif momento_dia == "Noche":
        if amor_madre >= 1 and not evento_madre_noche_visto:
            jump evento_noche_madre
        else:
            # Escena normal con Roxane en la sala por la noche
            narrador "La sala está oscura. [h_mayor_name] está sentada en el sofá con una copa de vino."
            show Roxane at right, zoom_sprite
            roxane "¿No puedes dormir, [mc_name]?"
            
            menu:
                "Hacerle compañía":
                    mc "No. El frío no me deja."
                    roxane "Si tienes frío, acércate. No muerdo. Al menos, no siempre."
                    $ amor_roxane += 1
                    $ tension_roxane += 2
                    narrador "Te sientas a su lado. Su pierna roza la tuya bajo la manta. El ambiente se siente más cargado de lo normal."
                    
                "Dejarla sola":
                    mc "Solo iba por agua. Ya me voy."
                    roxane "Qué aburrido eres."
                    $ amor_roxane -= 1
            hide Roxane
    else:
        narrador "La sala está vacía. Solo se escucha el viento golpeando la ventana."
        
    jump hub_principal