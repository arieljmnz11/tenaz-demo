def carga_aguda(cargas_diarias):
    """Suma la carga de los ultimos siete dias."""
    ultimos_siete = cargas_diarias[-7:]
    return sum(ultimos_siete)