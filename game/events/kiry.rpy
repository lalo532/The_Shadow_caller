# ==========================================
# EVENTS/KIRY.RPY
# Todos los eventos relacionados con Kiry (hermana menor / energética)
# ==========================================

# ==========================================
# LOCACIÓN: Cuarto de Kiry
# ==========================================
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

# ==========================================
# EVENTO: Plática con Kiry en la Sala (Tarde)
# ==========================================
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

# ==========================================
# EVENTO ESPECIAL: Kiry entra a tu cama (Día 2 - Mañana)
# ==========================================
label evento_kiry_cama:
    # Este evento se activa automáticamente en avanzar_tiempo cuando es Día 2 Mañana
    scene fondo_casa
    show Kiri at right, zoom_sprite
    kiry "¡Despierta, [mc_name]! Me aburro."
    mc "¿Qué quieres, enana?"
    kiry "No me digas enana. Tengo frío, hazme un espacio."
    narrador "Se mete bajo tus sábanas antes de que puedas protestar, pegando sus piernas frías a las tuyas."
    $ amor_kiry += 2
    jump hub_principal