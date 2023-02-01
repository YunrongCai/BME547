def create_patient_entry(name,mrn,age):
    new_patient = [name,mrn,age]
    return new_patient

def main_driver():
    db =[]
    db.append(create_patient_entry("Ann Ables",1,34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    print('Get patient Ann')
    found_patient = get_patient_entry(db,1)
    if found_patient is False:
        print("Patient mrn {} not found".format(1))
    else:
        print(found_patient)


def get_patient_entry(db,mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False


if __name__ == "__main__":
    main_driver()