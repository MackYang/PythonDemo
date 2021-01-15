import os
import sys
print(os.getcwd())  # Return the current working directory
print(os.chdir('D:/soft'))   # Change current working directory
print(os.system('mkdir today'))  # Run the command mkdir in the system shell

import glob
print(glob.glob('D:/Learn/Python/Basis/*.py'))

import shutil
shutil.copyfile('data.db', 'archive.db')

shutil.move('/build/executables', 'installdir')

from urllib.request import urlopen
with urlopen('http://www.baidu.com') as response:
    print(response.headers)