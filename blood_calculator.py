def interface():
    print("Blood calculator")
    keep = True
    LDL_tag = False
    HDL_tag = False
    while keep :
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Select an option:")
        if choice =="9":
            keep = False
        elif choice =="1":
            HDL_in = HDL_driver()
            HDL_tag = True
        elif choice =="2":
            LDL_in =LDL_driver()
            LDL_tag = True
        if (HDL_tag) & (LDL_tag):
            print("##########################")
            Total_Cholesterol_analysis(HDL_in, LDL_in)
            HDL_tag = False
            LDL_tag = False
            print("##########################")

    print('Program ending')


def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)
    return HDL_in


def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)
    return LDL_in


def HDL_input():
    HDL_value = input("Enter the HDL result:")
    HDL_value = int(HDL_value)
    return  HDL_value

def LDL_input():
    LDL_value = input("Enter the LDL result:")
    LDL_value = int(LDL_value)
    return  LDL_value


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int <= 159:
        answer = "Borderline high"
    elif 160 <= LDL_int <= 189:
        answer = "High"
    else:
        answer = "very high"
    return answer

def Total_Cholesterol_analysis(HDL_in,LDL_in):
    Total_Cholesterol = HDL_in + LDL_in
    if Total_Cholesterol < 200:
        answer = "Normal"
    elif 200 <= Total_Cholesterol < 239:
        answer = "Borderline high"
    else:
        answer = "High"
    print("The Total_Cholesterol result of {} is considered {}".format(Total_Cholesterol,answer))
    return


def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
    return

def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value, LDL_analy))
    return

interface()
