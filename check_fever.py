def test_check_fever():
    from blood_calculator import check_fever
    input_temps = [97, 98.6, 100.1]
    answer = check_fever(input_temps)
    expected = False
    assert answer == expected
