import requests

server = "http://vcm-7631.vm.duke.edu:5002"

patients = requests.get(server + "/get_patients/yc551")
patients = patients.json()
print(patients)
bt_don =  requests.get(server + "/get_blood_type/M7")
bt_rec =  requests.get(server + "/get_blood_type/F6")
print(bt_don.text)
print(bt_rec.text)
if bt_don.text == bt_rec.text:
    match = "Yes"
else:
    match = "No"
out_put = {"Name":"yc551", "Match":match}
r = requests.post(server + "/match_check", json = out_put)
print(r.text)