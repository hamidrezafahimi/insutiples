# Read in the file
with open('text_example.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('[41m', '')
filedata = filedata.replace('[0m', '')
filedata = filedata.replace('', '')

# Write the file out again
with open('log.txt', 'w') as file:
  file.write(filedata)