# ==========================================
# LOCATIONS/PLANTA_ALTA.RPY
# ==========================================

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