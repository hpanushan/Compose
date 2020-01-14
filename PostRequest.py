import requests

def postRequest(APIEndpoint,JSONData):
    response = requests.post(url=APIEndpoint, json=JSONData)

    responseText = response.text

    return responseText

# Attributes
APIEndpoint = 'http://127.0.0.1:5001/'
data = {'key':'value pairs'}

res = postRequest(APIEndpoint,data)

print(res)
