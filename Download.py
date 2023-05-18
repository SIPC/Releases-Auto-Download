import requests
import json
import os

def download_file(url, file_path):
    with open(file_path, "wb") as f:
        response = requests.get(url)
        f.write(response.content)

def get_release_files(owner, repo, keywords):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    response = requests.get(url)
    data = json.loads(response.text)
    for release in data:
        assets = release["assets"]
        for asset in assets:
            if all(keyword in asset["name"] for keyword in keywords):
                print("Download: " + asset["name"])
                download_file(asset["browser_download_url"], asset["name"])

get_release_files("owner", "repo", ["keyword1","keyword2"])
