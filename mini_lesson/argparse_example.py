import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input_file', help="name of the input file")

args = parser.parse_args()

print(args.input_file)
