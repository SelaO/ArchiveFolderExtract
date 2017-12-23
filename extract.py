// by Sela Oren Dec 2017
import os
import shutil
from pyunpack import Archive

tmpFolder = './tmp/'
shutil.rmtree(tmpFolder, True)

files = [f for f in os.listdir('.') if os.path.isfile(f) and (
    f.endswith('.7z') or f.endswith('.zip') or f.endswith('.rar')
)]

for filename in files:
    try:
        Archive(filename).extractall(tmpFolder, True)
        dirElements = [e for e in os.listdir(tmpFolder)]
        if len(dirElements) > 1:  # archive doesn't fit so extract it to a folder with the archive name
            folderName = './' + os.path.splitext(filename)[0]
            Archive(filename).extractall(folderName, True)
        else:   # archive fit so just move it out of tmp
            shutil.move(tmpFolder + dirElements[0], '.')
    except Exception as e:
        print("error: " + str(e))
    # clean tmp folder
    shutil.rmtree(tmpFolder, True)
    continue

# TODO delete the script file
# os.remove("extract.py")