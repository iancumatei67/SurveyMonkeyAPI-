import http.client
import ssl; ssl._create_default_https_context = ssl._create_unverified_context
import json

conn = http.client.HTTPSConnection("api.surveymonkey.com")
access_token = ("urWDCwflLyeddsRvRyq0azEJd5v5pM8TP.WSZkJf5pP34-nYm9EoqD0QEiFT6fYRkO7NsS5rgbyw5Nx6OYRcgcO2gw2A5rBus5QVX5k2v3JSf3nWkrm1WelVaDmCO4jw")

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {access_token}"
    }
with open('survey.json', 'r') as f:
    payload = (json.load(f))

conn.request("POST", "/v3/surveys", json.dumps(payload), headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
