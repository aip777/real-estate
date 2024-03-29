import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "img-5.jpg")

headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'palash',
    'password': 'palash'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']


# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']

# print(new_token)




headers = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    data = {
        "content": "Updated description"
    }
    json_data = json.dumps(data)
    posted_response = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers, files=file_data)
    print(posted_response.text)


headers = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

data = {
    "content": "Updated description"
}
json_data = json.dumps(data)
posted_response = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers)
print(posted_response.text)











# import json
# import requests
# import os
#
#
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
# ENDPOINT = "http://127.0.0.1:8000/api/status/"
#
# image_path = os.path.join(os.getcwd(), "img-5.jpg")
#
# headers = {
#     "Content-Type": "application/json"
# }
#
# data = {
#     'username': 'palash',
#     'password': 'palash'
# }
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()['token']
#
# #print(token)
#
# refresh_data = {
#     'token': token
# }
#
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']
#
# print(new_token)












# import json
# import requests
# import os
#
#
# ENDPOINT = "http://127.0.0.1:8000/api/listings/4/"
#
# image_path = os.path.join(os.getcwd(), "img-5.jpg")
# image_path_1 = os.path.join(os.getcwd(), "img-5.jpg")
#
#
# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as photo_main:
#             file_data = {
#                 'photo_main': photo_main
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
#
#
#
# do_img(
#     method='put',
#     data={
#         "id": 4,
#         "realtor": 2,
#         "title": "18 JaffSon",
#         "address": "109 Woodrow State",
#         "city": "New Jaffson",
#         "state": "CA",
#         "zipcode": "3030303",
#         "description": "A house is a building that functions as a home. They can range from simple dwellings such as rudimentary huts of nomadic tribes and the improvised shacks in shantytowns to complex, fixed structures of wood, brick, concrete or other materials containing plumbing, ventilation, and electrical systems",
#         "price": 30000,
#         "bedrooms": 4,
#         "bathrooms": "3.0",
#         "garage": 2,
#         "sqft": 2500,
#
#         "lot_size": "2.0",
#         "list_date": "2019-06-25T12:21:17Z"
#
#           },
#     is_json=False,
#     img_path=image_path
#     )
#
#
#
#
#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r























# import json
# import requests
#
# ENDPOINT = "http://127.0.0.1:8000/api/listings/"
#
#
#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


#do(data={'id': 500})

# do(method='delete', data={'id': 8})

# do(method='put', data={'id': 20, "content": "some cool new content", 'user': 1})

# do(method='post', data={"content": "some cool new content", 'user': 1})

# create
# retrieve / list
# update
# delete