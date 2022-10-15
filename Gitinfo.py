"""
GitInfo.py
This file is demonstrate the fetch request to GitHub api.
"""

import requests
import json


def getNoOfCommits(user_id, repo_name):
    commit_url = "https://api.github.com/repos/" + user_id + "/" + repo_name + "/commits"
    commits = requests.get(commit_url)
    commits = json.loads(commits.text)
    print("Repo:", repo_name, '  Number of commits:', len(commits))
    return len(commits)


def getGitRepoInfo(user_id):
    if not isinstance(user_id, str):
        return "User ID is not valid"
    repo_url = "https://api.github.com/users/" + user_id + "/repos"
    repo_data = requests.get(repo_url)
    repo_data = json.loads(repo_data.text)
    repo_names = []
    for repo in repo_data:
        repo_names.append(repo["name"])
        getNoOfCommits(user_id, repo["name"])
    return repo_names


getGitRepoInfo("akashadarsh")
