# wCat
This is a little script that lets you see the title and instructions of an unpuplished scratch project.

## dont use this, this is old and probably the worst code I've ever written and then published
(It isnt even a real cli lol)

I dont even know if this trick still works, but you can use [scratchattach](https://github.com/TimMcCool/scratchattach)s `create_remix` function of the `sa.PartialProject` class. That should also work and would be way less clunky.

(I just left this as a notice before archiving this "thing")

## Requirements
To use wCat you have to have [python installed](https://www.python.org/downloads/).
Also you have to have installed `requests` and `scratchattach`.   
This is how you install a python library:
```
pip install libraryName
```

To download this just type this into the command prompt:
```
git clone https://github.com/Antonabi/wCat.git
```

Also you have to have a scratch account. If you dont have one and for some reason dont wont to create one, you can use this test account that i made for wCat:  
username: `wCatProjectAcc`  
password: `charisma-risc-sundry-acerbity-cogitate78+!`  
PLEASE DONT USE THIS ACCOUNT FOR ANYTHING ELSE

## How to use this
There are 3 ways to use this:

### 1
This is quick way:  
Just download the `wCatOnefile.py` file and run it. This will ask you for your scratch password, username and the project id of the project.
To run the script just go into the folder and type this:
```
python wCatOnefile.py
```
### 2
This is the more complicated but more useful way to use this.  
Also download the `wCatOnefile.py` file.
Now go into the file and change `usePredefinedInfo` in line 10 from False to True. (“True” MUST be written in capital letters or the programm wont work.)
The next step is to change the username variable to your username, the password to your password and the targetProjectId to the project you want to have the info about.
Now if you run the project, the script wont ask you for the username, password and project id anymore.

### 3
(This just makes you cool but its overcomplicated so dont use this)
The cleaner code is from my perspective just the coolest way to use this.  
Because this has cleaner code. Yay.  
How to use this the cool way:  

Download the cleanerCode folder in any way you want. Than go into the `wCat.py` file and change the `username` variable on line  to your username and the `targetProjectId` to the project id.  
Now go into the password.txt file and enter your password there.
If you run the `wCat.py` file now, you will get the same result as way 2. And you have gained 42 points of coolness.  
If you want to have the same result as way one, you can just change the `usePredefinedInfo` to `False`.

## Extra info
There are some values at the beginning of the script that can be modified to change this programm:

| Parameter           | Description                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------|
| debug               | This lets you see random indev messages that make no sense, so don't turn this on.                   |
| uDebug              | This lets you see what the program is doing right now.                                                |
| showIntro           | This lets you enable/disable the intro.                                                               |
| usePredefinedInfo   | This lets you switch if the user is asked for the credentials and ID.                                 |

## How this thing works
This remixes the unpublished project, what lets you get the project name and instructions. To get the project itself, you still need the token.
(The name comes from "who Cares about tokens" because scratches last api change made it imposible to get the projects token when it is unpublished. The token is needed to get the project file and info.)
And please ignore the terrability of this code. Please.
