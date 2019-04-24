import shutil
from os import listdir
from os.path import isfile, join, isdir

desktop_path = '/Users/dajkatal/Desktop'

path_name = desktop_path + '/Static Files/'
final_path = desktop_path + '/Static Files Unpacked/'


onlyfiles = [f for f in listdir(path_name) if isfile(join(path_name, f))]
onlydir = [path_name + f for f in listdir(path_name) if isdir(join(path_name, f))]

print('')
print(onlyfiles if len(onlyfiles) > 0 else None)
print(onlydir if len(onlydir) > 0 else None)
print('')


def unpack_files(dir_path):
    directories_here = [dir_path + '/' + f for f in listdir(dir_path) if isdir(join(dir_path, f))]
    files_here = [dir_path + '/' + f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    for file in files_here:
        shutil.copy(file, final_path)
    if len(directories_here) > 0:
        print(dir_path, directories_here)
        for dir in directories_here:
            unpack_files(dir)

for dir in onlydir:
    unpack_files(dir)
