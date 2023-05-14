import requests
import json
import os

def download_file(url, file_path):
    with open(file_path, "wb") as f:
        response = requests.get(url)
        f.write(response.content)

def get_latest_release_files(owner, repo, keywords):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    data = json.loads(response.text)
    assets = data["assets"]
    for asset in assets:
        if all(keyword in asset["name"] for keyword in keywords):
            download_file(asset["browser_download_url"], asset["name"])

get_latest_release_files("owner", "repo", ["keyword1","keyword2"])