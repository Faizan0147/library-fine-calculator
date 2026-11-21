from app import calculate_fine


def test_boundaries():
    assert calculate_fine("-1") == (False, "Invalid input")
    assert calculate_fine("0") == (True, "Fine: Rs 0")
    assert calculate_fine("3") == (True, "Fine: Rs 0")
    assert calculate_fine("4") == (True, "Fine: Rs 10")
    assert calculate_fine("20") == (True, "Fine: Rs 170")
    assert calculate_fine("21") == (False, "Invalid input")


def test_non_integer():
    for bad in ("abc", "2.5", ""):
        assert calculate_fine(bad)[0] is False
