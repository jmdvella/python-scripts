import os
import shutil
import random

# source directory for files to copy from
while True:
    source_dir = input('Type the directory of your music (or copy and paste):\n')
    # check the directory exists 
    if os.path.isdir(source_dir):
        break
    else:
        print('\n#####\nThis diretory does not exist, please check you have typed the path correctly\n')

# create output directory, if exists add to this directory
os.makedirs(os.path.expanduser('~\Desktop\\CollectedMusic'), exist_ok=True)

# target directory for files to copy to
target_dir = os.path.expanduser('~\Desktop\\CollectedMusic')

# empty list for collecting files
source_files = []  

# exclude directories
exclude_dir = input('\nEnter a directory that you would like to exclude:\n(to add multiple directories use a comma example: Michael Jackson, Tina Turner etc)\n(press Enter if you wish to include all directories):\n')
exclude_dir = exclude_dir.split(", ")

# continue if no directory is selected
if exclude_dir == '':
    exclude_dir = None

# walk through directory tree 
# select files that are not in excluded directory
for dirpath, dirnames, filenames in os.walk(source_dir, topdown=True):
    try:
        [dirnames.remove(d) for d in list(dirnames) if d in exclude_dir]
    except TypeError:
        continue
    # find file names that end with .mp3
    for file in filenames:
        if file.endswith(".mp3"):
            source_files.append(os.path.join(dirpath, file))

# ask user to select how many files to copy  
while True:
    try:
        choices = random.sample(source_files, int(input('How many songs would you like to collect? (must be a number not a word):\n')))
        break
    # if more files requested than exist give user another chance to select the amount of files to select
    except ValueError:
        print('\n#####\nYou have selected more songs than you have in this directory, try a lower number\n')

# copy files to target directory
for files in choices:
    shutil.copy(files, target_dir)

# print each song name
for songs in choices:
    print(songs)
