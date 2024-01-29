# random python script which creates symbolinc links in the current folder to all files in the folder given as argument
# also removes all hungarian specific characters

import os
import re
import sys

def rename_files(directory):
    for filename in os.listdir(directory):
        new_filename = filename.replace('\u00E1','a')
        new_filename = new_filename.replace('\u00E9','e')
        new_filename = new_filename.replace('\u00ED','i')
        new_filename = new_filename.replace('\u00F3','o')
        new_filename = new_filename.replace('\u00F6','o')
        new_filename = new_filename.replace('\u0151','o')
        new_filename = new_filename.replace('\u00FA','u')
        new_filename = new_filename.replace('\u00FC','u')
        new_filename = new_filename.replace('\u0171','u')
        # file specific cases (here example remove some prefix)
        new_filename = re.sub(r'^[0-9_.()\s]+','',new_filename)
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)

def link_to_files(link_dir, target):
    for filename in os.listdir(link_dir):
        target_path=os.path.join(link_dir, filename)
        link_path=os.path.join(target, filename)
        os.symlink(target_path, link_path)

if len(sys.argv) > 1:
    folder_to_link_to=sys.argv[1]
else:
    print("No arguments provided.")
    sys.exit(1)

link_to_files(folder_to_link_to, './')
rename_files('./')
