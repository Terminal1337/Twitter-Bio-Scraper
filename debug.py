import json


with open('data.json','r') as f:
    data = json.load(f)
    
    
i = data["data"]["user"]["result"]['legacy']['entities']['url']['urls'][0]['display_url']
print(i)