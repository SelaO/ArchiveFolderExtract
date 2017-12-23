# by Sela Oren Dec 2017
import os
import shutil

tmpFolder = './tmp/'
shutil.rmtree(tmpFolder, True)

files = [f for f in os.listdir('.') if os.path.isfile(f) and (
    f.endswith('.7z') or f.endswith('.zip') or f.endswith('.rar')
)]

for filename in files:
    try:
        zip_file = "7z x \"%s\" -o\"%s\" -r" % (filename, tmpFolder)
        os.system(zip_file)
        dirElements = [e for e in os.listdir(tmpFolder)]
        if len(dirElements) > 1:  # archive doesn't fit my pattern
            # rename tmp to filename instead of extracting again
            os.rename(tmpFolder, os.path.splitext(filename)[0])
        else:   # archive fit so just move it out of tmp
            shutil.move(tmpFolder + dirElements[0], '.')
    except Exception as e:
        print("error: " + str(e))

    shutil.rmtree(tmpFolder, True)  # clean tmp folder
    continue

# TODO delete the script file
# os.remove("extract.py")
