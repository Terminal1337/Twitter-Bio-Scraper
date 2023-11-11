import httpx
import json
from helpers.const import *




class Twitter:
    def __init__(self) -> None:
        with open("config.json","r") as f:
            self.config = json.load(f)
            self.auth_token = self.config["auth_token"]
            self.ct0 = self.config["ct0"]
     
    
    
    def scrape(self,user_id : str = "1517536143533027329"):
        with httpx.Client() as client:
            try:
                headers = base_headers
                headers["cookie"] = f"auth_token={self.auth_token}; ct0={self.ct0}"
                headers['X-CSRF-Token'] = self.ct0
                new_variables = variables
                new_variables["userId"] = user_id
                params = {
    'variables': json.dumps(new_variables),
    'features': json.dumps(features),
}
                # response = client.get('https://twitter.com/i/api/graphql/8cyc0OKedV_XD62fBjzxUw/Following', headers=headers, params=params)
                resp = client.get("https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=twitterdev&skip_status=true&include_user_entities=false",headers=base_headers)
                print(resp.text)
            except Exception as e:
                print(e)
                
                
if __name__ == "__main__":
    r = Twitter()
    r.scrape()