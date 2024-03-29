#!/usr/bin/env python3
import sys
import os
import shutil
import asyncio
import aioconsole

from datetime import datetime

SCREENSHOTS_PATH = "/Users/weicheng/Desktop" # CHANGE THIS TO YOUR SCREENSHOTS PATH
# Windows default: "/Users/<username>/Pictures/Screenshots"
# Mac default: "/Users/<username>/Desktop"

#TO_PATH = "/Users/weicheng/weicheng783/assets/notes-photos"  # Full path where you want to move the files
#REL_PATH = "assets/notes-photos" # Relative path to where you want to move the files (used for insertion links)

def determine_path():
    ### DETERMINE THE TO_PATH TO MOVE THE IMAGES TO
    global TO_PATH
    global REL_PATH
    global description

    path = "/Users/weicheng/weicheng783/assets/notes-photos/"

    if(len(sys.argv) == 1): # if no path given in command line arg, assume "."
        path = path
    else:
        path = path + sys.argv[1]
        description = sys.argv[1]

    REL_PATH = os.path.relpath(path, start = os.getcwd())
    TO_PATH = os.getcwd() + "/" + REL_PATH

    if(not os.path.exists(TO_PATH)):
        print("ERROR: THE PATH YOU ENTERED DOES NOT EXIST")
        quit()

    print(f"USING PATH {TO_PATH}")

async def monitor_input():
    while True:
        q = await aioconsole.ainput("Type 'q' or 'quit' and enter to exit \n")
        if q == "q" or q == "quit":
            quit()

async def monitor_screenshot(set_files):
    while(True):
        await asyncio.sleep(1)
        ls_screenshots = os.listdir(SCREENSHOTS_PATH)
        for filename in ls_screenshots: 
            if filename not in set_files:
                move_file(filename)

def move_file(filename):
    # move the file from SCREENSHOTS_PATH to TO_PATH
    from_file_path = SCREENSHOTS_PATH + "/" + filename
    date_time = datetime.fromtimestamp(datetime.now().timestamp())
    d = date_time.strftime("%Y%m%d_%H%M%S") + ".png"
    
    to_file_path = TO_PATH + "/" + d
    
    if(os.path.exists(from_file_path)): # just in case
        shutil.move(from_file_path, to_file_path)
        print("MARKDOWN INSERT:")
        if(description != None):
             #print("!["+sys.argv[1]+"](" + REL_PATH.replace(" ", "%20") + "/" + filename.replace(" ", "%20") + ")")
             print("!["+description+"](" + REL_PATH.replace(" ", "%20") + "/" + d + ")")
        else:
              print("![](" + REL_PATH.replace(" ", "%20") + "/" + d + ")")
    else:
        print("Error when trying to move " + filename)

def main():
    determine_path()
     # keeps track of the images in SCREENSHOTS_PATH at start of run time
    set_files = set(os.listdir(SCREENSHOTS_PATH)) 

    asyncio.get_event_loop().run_until_complete(asyncio.wait([
                                                            monitor_input(), 
                                                            monitor_screenshot(set_files)
                                                            ]))

if __name__ == "__main__":
    main()


