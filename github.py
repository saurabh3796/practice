import requests
import sys
import json

def getRepoList(username):
    try:
        headers = {"content-type": "application/json", "User-Agent" : ""}
        github = "https://api.github.com/users/" + username + "/events/public"
        print("calling to GITHUB URL:%s", github)
        response = requests.get(github, timeout=120, headers=headers)
        #print(response._content)
        repo_list = []
        #print(type(response._content))
        for i in json.loads(response._content):
            if i['repo']['url'] not in repo_list:
                repo_list.append(i['repo']['url'])
        print("repo list")
        print(repo_list)
    except Exception as exp:
        print("Some exception occured %s", response.status_code)

def getUserProfile(username):
    try:
        headers = {"content-type": "application/json", "User-Agent" : ""}
        github = "https://api.github.com/users/" + username
        print("calling to GITHUB URL:%s", github)
        response = requests.get(github, timeout=120, headers=headers)
        print(json.loads(response._content))
    except Exception as exp:
        print("Exception occurred during fetching profile %s", response._content)    

if __name__ == "__main__":
    if sys.argv[1] == 'repo':
        getRepoList(sys.argv[2])
    elif sys.argv[1] == 'user':
        getUserProfile(sys.argv[2])
    