import requests

server = " http://127.0.0.1:5000"

patient = {"id":1, "name": "Yunrong", "blood_type": "O+", "test": []}
r = requests.post(server+'/new_patient', json=patient)
patient = {"id":1, "test_name": "Blood", "test_result": 1}
r = requests.post(server+'/add_test', json=patient)
print(r.status_code)
print(r.text)