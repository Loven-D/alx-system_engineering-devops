#!/usr/bin/python3
"""
a function that queries the Reddit API and 
returns the number of subscribers 
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'error' in data:
            return 0  # Invalid subreddit, return 0

        subscribers = data['data']['subscribers']
        return subscribers
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = number_of_subscribers(subreddit)
        print(result)
