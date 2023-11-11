import json
base_headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.7',
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Host': 'twitter.com',
    'Sec-Ch-UA': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-UA-Mobile': '?0',
    'Sec-Ch-UA-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    # 'X-Client-Transaction-ID': 'hCgdQiyZA81URQ4wQVi210TVnjib/6+5ycuKjex8V5bmm8T7f8THG4mXDGJtXY/w34xWe4Qb1sZjlYa6Bz6Vs9tX7MkEhQ',
    # 'X-Twitter-Active-User': 'yes',
    # 'X-Twitter-Auth-Type': 'OAuth2Session',
    # 'X-Twitter-Client-Language': 'en'
}

variables = {
    'count': 20,
    'includePromotedContent': False
}

features = {
    'responsive_web_graphql_exclude_directive_enabled': True,
    'verified_phone_label_enabled': True,
    'responsive_web_home_pinned_timelines_enabled': True,
    'creator_subscriptions_tweet_preview_api_enabled': True,
    'responsive_web_graphql_timeline_navigation_enabled': True,
    'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
    'c9s_tweet_anatomy_moderator_badge_enabled': True,
    'tweetypie_unmention_optimization_enabled': True,
    'responsive_web_edit_tweet_api_enabled': True,
    'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
    'view_counts_everywhere_api_enabled': True,
    'longform_notetweets_consumption_enabled': True,
    'responsive_web_twitter_article_tweet_consumption_enabled': False,
    'tweet_awards_web_tipping_enabled': False,
    'freedom_of_speech_not_reach_fetch_enabled': True,
    'standardized_nudges_misinfo': True,
    'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
    'longform_notetweets_rich_text_read_enabled': True,
    'longform_notetweets_inline_media_enabled': True,
    'responsive_web_media_download_video_enabled': False,
    'responsive_web_enhance_cards_enabled': False
}

