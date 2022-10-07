#Akash Adarsh
#CWID: 2009617
import requests
import json

"""
You should write a function that will take as input a GitHub user ID. 
The output from the function will be a list of the names of the repositories that the user has, 
along with the number of commits that are in each of the listed repositories.
"""
def getUserRepos(userName):       
    API = ("https://api.github.com/users/" + userName + "/repos")
    userData = requests.get(API)
    repositories = json.loads(userData.text)
    userRepos = []
    
    for repository in repositories:
        try:
            userRepos.append(repository.get("name"))
        except:
            userRepos = []
         
    return userRepos

def getCommitnum(userName, repoName):          #  number of commits that are in each of the listed repositories.
    API = "https://api.github.com/repos/" + userName + "/" + repoName + "/commits"
    repoData = requests.get(API)
    commits = json.loads(repoData.text)
    Commitnum = len(commits)

    return Commitnum
        
"""
Main function that lists all the repos and lists each commit count given a specific
github user name.
"""
if __name__ == "__main__":
    userName = input("Enter Github username: ")     #Ask username
    userRepos = getUserRepos(userName) # Get Respos according to the username
    print("User: " + userName)
    for repository in userRepos:              #Use for Loop to printing name and their commit in associated repos 
        Commitnum = getCommitnum(userName, repository)
        print("Repo: " + repository + " Number of Commits: " + str(Commitnum))