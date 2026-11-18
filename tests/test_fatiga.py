from fatiga import carga_aguda


def test_carga_aguda_no_es_negativa():
    cargas_diarias = [40, 0, 55, 60, 0, 30, 45]
    assert carga_aguda(cargas_diarias) >= 0


def test_carga_aguda_suma_siete_dias():
    cargas_diarias = [40, 0, 55, 60, 0, 30, 45]
    assert carga_aguda(cargas_diarias) == 230