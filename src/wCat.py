import scratchattach as scratch3
import requests
import json
import os
import time

debug = False #if debug is on you can see indev debug msgs (that make no sense)
uDebug = True #with this you can see what the script is doing right now
showIntro = True #if this is on the intro is shown
usePredefinedInfo = True #if this is false wCat will ask you every time you start the script for the username, password and tagetProjectId

# User information 
username = "wCatProjectAcc"
with open("password.txt", "r") as password: #to set the password, you have to go into the password txt file and paste your password there.
    password = password.read()

targetProjectId = "123456" #id of the project you want to know the title and instructions

if usePredefinedInfo == False:
    print("\033[91mBecause \033[95musePredefinedInfo\033[91m is \033[94mFalse\033[91m, you have to put your username, password and the id of the project.")
    print("\033[91mIf you want to change this, go into the script and set it to \033[94mTrue\033[91m. (If you do that, dont forget to change the username, password and targetProjectId variables in the Script.)")
    print("")
    username = input("\033[92mUsername: ")
    password = input("\033[92mPassword: ")
    targetProjectId = str(input("\033[92mProject Id: "))

def startIntro(): #function that prints the intro
    logo = """    \033[34m        ____         _   
\033[33m__      __\033[34m / ___|  __ _ | |_ 
\033[33m\ \ /\ / /\033[34m| |     / _` || __|
\033[33m \ V  V / \033[34m| |___ | (_| || |_ 
\033[33m  \_/\_/  \033[34m \____| \__,_| \__|"""
    os.system("clear")
    print(logo)
    print("\033[95m   -who Cares about tokens-")
    print("")
    print("\033[90mThe thingy with that you can get the instructions and title from an unpulished project.\033[0m")
    time.sleep(0.5)
    os.system("clear")

# Function for debug messages
def printDebugMsg(msg):
    if debug:
        print(f"\033[93mDebug:\033[0m \033[96m{msg}\033[0m")

# Function for usefulDebug messages
def printUDebugMsg(msg):
    if uDebug:
        print(f"\033[93muDebug:\033[0m \033[96m{msg}\033[0m")

# General headers
gHeaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://scratch.mit.edu",
}

# Function to convert cookies to a dictionary
def cookieToDict(cookie):
    cookieDict = {}
    splittedCookie = cookie.split("; ")
    for param in splittedCookie:
        paramList = param.split("=")
        cookieDict[paramList[0]] = paramList[1]
    return cookieDict

# Function to convert a dictionary to a cookie string
def dictToCookie(cookieDict):
    params = []
    for param in cookieDict:
        params.append("=".join([param, cookieDict[param]]))
    cookieStr = "; ".join(params)
    return cookieStr

# Function to get the CSRF token
def getCsrftoken():
    response = requests.get("https://scratch.mit.edu/csrf_token/").headers
    csrftoken = response["Set-Cookie"].split("scratchcsrftoken=")[1].split(";")[0]
    return csrftoken

printDebugMsg("Indev debug is on. The indev debug msgs will show up in the format.")
printUDebugMsg("Useful debug is on. The useful debug msg will show up in this format.")
if showIntro:
    startIntro() #starts intro

# Login
session = scratch3.login(username, password)
printUDebugMsg(f"Logged in as {username}. Session id: {session.session_id}")
printDebugMsg(session.session_id)
printUDebugMsg(f"Got csrf token: {getCsrftoken()}")
printDebugMsg(getCsrftoken())

# Function to remix a project
def remixProject(id):
    url = "https://projects.scratch.mit.edu/"
    params = {
        "is_remix": "1",
        "original_id": id,
        "title": "Scratch Project"
    }

    cookieDict = {
        'scratchsessionsid': f'{session.session_id}',
        'scratchcsrftoken': getCsrftoken()
    }
    cookie = dictToCookie(cookieDict)
    
    printDebugMsg(cookie)

    headers = {
        "Host": "projects.scratch.mit.edu",
        "Cookie": cookie,
        "Content-Type": "application/json",
    }

    with open("defaultProject.json", "r") as defaultProj:
        defaultProj = json.loads(defaultProj.read())

    payload = defaultProj
    response = requests.post(url, params=params, headers=headers, json=payload)

    projectId = response.json()["content-name"]

    printDebugMsg(response.status_code)
    printDebugMsg(response.text)
    printDebugMsg(projectId)
    
    return projectId

# Remix the project (you can remix unpublished projects and thats basically how this thing works)
newProjId = remixProject(targetProjectId)
printUDebugMsg(f"Remixed project {targetProjectId} and got new id: {newProjId}.")
# Connect with the new project
newProject = session.connect_project(newProjId)
printUDebugMsg(f"Connected to {newProjId}.")
printUDebugMsg(f"URL of new project: https://scratch.mit.edu/projects/{newProjId}/.")
printUDebugMsg("Done!\n\n")

# Display project information
projTitle = newProject.title.split(" remix")[0]
projInstr = newProject.instructions

print(f"\033[95mThe Project Title:\033[0m '\033[94m{projTitle}\033[0m'")
print(f"\033[95mThe Project Instructions:\033[0m '\033[94m{projInstr}\033[0m'")
print("")
if username != "wCatProjectAcc":
    print("\033[92mInfo: You have to go into your projects and delete the new project in your files.\033[0m")
print("\033[92mInfo: BTW the 'remix' at the end of the title of the project in your stuff isn't in the original title.\033[0m")
