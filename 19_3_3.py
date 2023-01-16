# import requests
#
# petId = input('введите номер питомца: ')
#
# res1 = requests.get(f"https://petstore.swagger.io/v2/pet/{petId}", params={'petId': 'petId'}, headers={'accept': 'application/json'})
# print(res1.text)
# res2 = requests.post(f"https://petstore.swagger.io/v2/pet{petId}", headers={'accept': 'application/json'}, data={'petId': 'name'})
# print(res2.text)
# res3 = requests.put(f"https://petstore.swagger.io/v2/pet", data={'petId': 'name2'})
# print(res3.text)
# res4 = requests.delete(f"https://petstore.swagger.io/v2/pet{petId}", params={'petId': 'petId'})
# print(res4.text)
#
