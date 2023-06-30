# is argparse standard?
import argparse

# thanks, tutorial!
parser = argparse.ArgumentParser()

# a couple tries
parser.add_argument("--parse", type=str, required=True)

# parse!
args = parser.parse_args()

# because we are parsing a file with a parser and names are horrible
filename = args.parse

# check if add argument has any input data.
# If it has, then print sum of the given numbers
if len(args.parse) != 0:
	print("ok we start fun now ", filename)
#	parse_file(filename)
	