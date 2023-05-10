#!/usr/bin/python3
"""Module for task 3"""

import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            count = title.count(word)
            if count > 0:
                if word in word_count:
                    word_count[word] += count
                else:
                    word_count[word] = count
    if data['data']['after'] is not None:
        count_words(subreddit, word_list, data['data']['after'], word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
