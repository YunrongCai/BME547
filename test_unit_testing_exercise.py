# Written by Yunrong Cai
# Feb 6 2023

def test_ycoordinate():
    from unit_testing_exercise import ycoordinate
    input = [(1,2), (3,6), 2 ]
    answer = ycoordinate(input)
    expected = 4
    assert answer == expected

def test_intersection_check():
    from unit_testing_exercise import intersection_check
    input = [(1,2), (3,6), (2,4) ]
    answer = intersection_check(input)
    expected = True
    assert answer == expected
