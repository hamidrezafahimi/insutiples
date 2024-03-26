import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print("current file is: ", os.path.realpath(__file__))
print("parent dir for the current file is: ", dir_path)
cwd = os.getcwd()
print("current working dir is: ", dir_path)

# Then, to add relative path's to system path, do:
# sys.path.insert(0, <path-string>)
