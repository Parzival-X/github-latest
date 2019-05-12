import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get('https://api.github.com/users/{}/events'.format(username))

    activity = json.loads(response.text)

    event_type = activity[0]['type']
    repo = activity[0]['repo']['name']
    timestamp = activity[0]['created_at']

    print(" Username: {}\n Event type: {} \n Repo: {} \n time stamp: {}".format(
        username, event_type, repo, timestamp))
