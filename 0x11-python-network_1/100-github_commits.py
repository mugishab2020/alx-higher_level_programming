#!/usr/bin/python3
"""using the GitHub API to list commits"""

from sys import argv
import requests
if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo_name)
    params = {'per_page': 10}
    response = requests.get(url, params=params)
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
