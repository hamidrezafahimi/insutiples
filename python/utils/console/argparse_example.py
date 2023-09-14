import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='The Username for authentication.')

args, unknown = parser.parse_known_args()

print(args.username)