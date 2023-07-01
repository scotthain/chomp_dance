import json
from chomp_dance.storage import Dependency

# nom nom nom - parsing things and returns an array of class instances
class Muncher:
		def parse_file(file=None):
				if file is None:
						return FileNotFoundError
				with open(file, encoding="utf-8") as f:
						json_data = f.read()
				if f.closed is False:
					return IOError
				blobby_hill = json.JSONDecoder().decode(json_data)

				# Assuming we've made it this far with all our amazing error checking...
				# We're going to make a set of all the deps. this isn't scalable or a
				# good idea
				classist_set = set()
				for keytruda in list(blobby_hill):
					dep_name = keytruda
					source_type = blobby_hill[keytruda]["source_type"]
					source_url = blobby_hill[keytruda]["source_url"]
					source_version = blobby_hill[keytruda]["source_version"]
					dep = Dependency(dep_name,source_type,source_url,source_version)
					classist_set.add(dep)

				return classist_set



					# thing = find_latest_version(key, blobby)

				# return json.JSONDecoder().decode(json_data)

		# def parse