import pytest

@pytest.mark.parametrize("HDL_input, expected",
[(65,"Normal"),(45,"Borderline Low"),(20,"Low")] )
def test_HDL_analysis(HDL_input, expected):
    from blood_calculator import HDL_analysis
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected

@pytest.mark.parametrize("LDL_input, expected",
[(190,"Very High"),(170,"High"),(140,"Borderline High"),(100,"Normal")] )
def test_LDL_analysis(LDL_input, expected):
    from blood_calculator import LDL_analysis
    # Act
    answer = LDL_analysis(LDL_input)
    # Assert
    assert answer == expected


'''
def test_HDL_analysis_Borderline_Low():
    from blood_calculator import HDL_analysis
    # Arrange
    HDL_input = 45
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Borderline Low"

def test_HDL_analysis_Low():
    from blood_calculator import HDL_analysis
    # Arrange
    HDL_input = 30
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Low"
'''