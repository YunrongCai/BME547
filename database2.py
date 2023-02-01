def create_patient_entry(name,mrn,age):
    new_patient = [name,mrn,age,[]]
    return new_patient

def main_driver():
    db =[]
    db.append(create_patient_entry("Ann Ables",1,34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    add_test_to_patient(db,1,"HDL",120)
    add_test_to_patient(db,2, "LDL", 100)
    room_numbers = ["103","232","333"]
    """
    print('Get patient Ann')
    found_patient = get_patient_entry(db,1)
    if found_patient is False:
        print("Patient mrn {} not found".format(1))
    else:
        print(found_patient)
    """
    print(db)
    print_directory(db, room_numbers)
    testresult = find_test_value(db,2,'LDL')
    print("The test result for mrn of 2 is {}".format(testresult))

def find_test_value(db,mrn,testname):
    for patient in db:
        if patient[1] == mrn:
            if patient[3][0] ==testname:
                return patient[3][1]
            else:
                print("No test result for this patient")
        else:
            print("There's no such patient in the mrn of {}".format(mrn))
    return


def print_directory(db,roomnumbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], roomnumbers[i]))
    for patient, rn in zip(db, roomnumbers):
        print("Patient {} is in room {}".format(patient[0], rn))


def get_patient_entry(db,mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db,mrn_to_find,test_name,test_value):
    patient = get_patient_entry(db,mrn_to_find)
    if patient == False:
        print("Bad entry")
    else:
        patient[3].append(test_name)
        patient[3].append(test_value)
    return


if __name__ == "__main__":
    main_driver()