import argparse
import os

# Parse a list of file names and access them through python

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read in a file or set of files, and return the result.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('path', nargs='+', help='Path of a file or a folder of files.')
    args = parser.parse_args()
    full_paths = [os.path.join(os.getcwd(), path) for path in args.path]
    files = set()
    for path in full_paths:
        if os.path.isfile(path):
            files.add(path)
    print(files)