#!/usr/bin/python3
"""Querying Reddit API"""


def number_of_subscribers(subreddit):
    """Function that queries reddit API and returns number of
subs to subreddit"""
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
