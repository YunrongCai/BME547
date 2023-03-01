import requests
'''
out_data = {"name":"Yunrong Cai", "net_id":"yc551", "e-mail":"yunrong.cai@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)
print(r.status_code)
print(r.text)
'''

out_data = {"user": "Isha", "message": "18 pizzas"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json = out_data )
print(r.status_code)
r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Isha")
print(r1.text)