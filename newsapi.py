
import requests

NEWSAPI_KEY = 'THISISNOTAREALKEYPUTYOURKEYHERE' 
base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "apiKey": NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
print(result)
