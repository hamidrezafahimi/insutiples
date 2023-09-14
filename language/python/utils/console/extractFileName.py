import os

files = {'/media/hamid/Workspace/technical_utils/python/console/file3.txt', 
         '/media/hamid/Workspace/technical_utils/python/console/file1.txt', 
         '/media/hamid/Workspace/technical_utils/python/console/file2.txt'}

names = set()
pure_names = set()
for path in files:
    name = os.path.basename(path)
    names.add(name)
    pure_name = os.path.splitext(name)[0]
    pure_names.add(pure_name)

print(names)
print(pure_names)