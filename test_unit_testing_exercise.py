# Written by Yunrong Cai
# Feb 6 2023

def test_ycoordinate():
    from unit_testing_exercise import ycoordinate
    input = [(1,2), (3,6), 2 ]
    answer = ycoordinate(input)
    expected = 4
    assert answer == expected
