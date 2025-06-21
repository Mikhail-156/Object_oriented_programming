from src.smartphone import Smartphone


def test_smartphone(fixture_smartphone: Smartphone):
    """Тест"""
    assert fixture_smartphone.color == "Синий"
    assert fixture_smartphone.model == "Note 11"
    assert fixture_smartphone.memory == 1024
    assert fixture_smartphone.efficiency == 90.3
