__author__ = 'Andrew'
import os
from shutil import copyfile


def recurse():

    for item in os.listdir(os.getcwd()):
        #check for .ds_store
        if item[0] !='.':
            if not os.path.isfile(item):
                os.chdir(item)
                recurse()
            else:

                print item

                copyfile(item, "/Users/Andrew/.imgbackup/%s"%(item))
                # os.system("cp %s /Users/Andrew/.imgbackup/" %(item))
        # if not os.path.isfile(os.getcwd()+item):
        #     recurse(item)
        # else:
        #     print item

    os.chdir("../")
    return
_project_dir = os.getcwd()
os.chdir("/Users/Andrew/Library/Messages/Attachments")
for top_folder in os.listdir(os.getcwd()):
    if os.path.isdir(top_folder):
        os.chdir(top_folder)
        recurse()
    else:
        print top_folder

'/Users/Andrew/Library/Messages/Attachments/000666A604-DEE6-4907-8EB0-73EA05A711DA'
