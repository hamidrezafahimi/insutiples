rm -f file_names.txt
ls -d */*.pdf | xargs -d '\n' -n 1 basename >> file_names.txt
ls -d */*/*.pdf | xargs -d '\n' -n 1 basename >> file_names.txt
ls -d */*/*/*.pdf | xargs -d '\n' -n 1 basename >> file_names.txt
ls -d */*/*/*/*.pdf | xargs -d '\n' -n 1 basename >> file_names.txt