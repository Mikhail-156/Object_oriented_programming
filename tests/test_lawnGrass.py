from src.lawngrass import LawnGrass

def test_lawnGrass(fixture_lawnGrass: LawnGrass):
    """Тест"""
    assert fixture_lawnGrass.name == "Газонная трава"
    assert fixture_lawnGrass.description == "Элитная трава для газона"
    assert fixture_lawnGrass.price == 500.0
    assert fixture_lawnGrass.quantity == 20
    assert fixture_lawnGrass.country == "Россия"
    assert fixture_lawnGrass.germination_period == "7 дней"
    assert fixture_lawnGrass.color == "Зеленый"
