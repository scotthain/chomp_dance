# is argparse standard?
import argparse
from chomp_dance.muncher import Muncher
from chomp_dance.network.utils import find_latest_version

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
	deps = Muncher.parse_file(filename)
	print("size?", deps.__len__())

# how the hell else do you do this?
while deps.__len__() > 0:
	dep = deps.pop()
	if dep is None:
		break
	version_string = find_latest_version(dep)
	print("ugh version", version_string)


# MOAR COMMENTS BECAUSE I AM NOT A FAN OF INDENTATION
