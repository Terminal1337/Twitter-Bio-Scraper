import tls_client
import random
import httpx
from helpers.const import *
def get_followers(screen_name,min_followers):
    client= httpx.Client(proxies=f"http://{random.choice(proxies)}")
    # client = tls_client.Session(client_identifier="chrome119",random_tls_extension_order=True)
    # client.proxies = f"http://{random.choice(proxies)}"
    
    token = random.choice(open('input/tokens.txt', 'r').read().splitlines())

    cookies = {'auth_token': token}        
    ct0_response = client.post('https://twitter.com/i/api/1.1/account/update_profile.json', cookies=cookies,
                               headers=ct0_headers)
    ct0 = ct0_response.cookies['ct0']
    headers = base_headers
    headers['x-csrf-token'] = ct0
    cookies['ct0'] = ct0
    


    resp = client.get('https://twitter.com/i/api/graphql/G3KGOASz96M-Qu0nwmGXNg/UserByScreenName?variables={"screen_name":"[screen]","withSafetyModeUserFields":true}&features={"hidden_profile_likes_enabled":true,"hidden_profile_subscriptions_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":true,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}&fieldToggles={"withAuxiliaryUserLabels":false}'.replace('[screen]', screen_name), headers=headers,
                       cookies=cookies)
    if resp.status_code == 200:
        followers = resp.json()['data']['user']['result']['legacy']['followers_count']
        if followers >= min_followers:
            return True,followers,resp.json()["data"]["user"]["result"]['legacy']['entities']['url']['urls'][0]['display_url']
        return True,followers,False
    if resp.status_code == 429:
        print(f"Rate limited [{token}]")
    return False,False,False


