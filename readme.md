Extract all archives in a folder such that each archive map to a single folder with its contents

e.g if an archive has a single folder with all its contents that's what will be extracted, otherwise, create a folder with the archive name and extract the contents of the archive to it.

# Setup 

* using python 3

* add 7z to the path

  control panel -> env -> user variables -> edit path -> add C:\Program Files\7-Zip

* install pyunpack

  in the console:

  ```
  pip install pyunpack
  pip install patool
  pip install entrypoint2
  ```

* move the script to the folder with all the archives and run it 
