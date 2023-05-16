import requests
from datetime import datetime

USERNAME = "your username"
TOKEN = "create a token"
GRAPH_ID = "name your graph"

headers = {
    "X-USER-TOKEN": TOKEN,
}
today = datetime.now()
TODAY_FORMATTED = today.strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"

#==================USER_CREATION ====================================

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

#==================GRAPH_CREATION ===================================

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "name for your graph",
#     "unit": "input units, m, Kn, days,m seconds whatever",
#     "type": "float",
#     "color": "choose for the documentation of pixela",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

#==================PIXEL_INPUT ====================================

# pixel_config = {
#     "date": TODAY_FORMATTED,
#     "quantity": "2",
# }
#
# post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)


#==================PIXEL_UPDATE ====================================

# update_pixel_config = {
#     "quantity": "number you wish to update",
# }
#
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_FORMATTED}"  #Note that you don't have to use todays date, you can change {TODAY_FORMATTED} into yyyyMMdd format.
#
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)

#==================DELETE_PIXEL ====================================

# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_FORMATTED}" #Same as above for the date.
# response = requests.delete(url=delete_pixel_endpoint,  headers=headers)


