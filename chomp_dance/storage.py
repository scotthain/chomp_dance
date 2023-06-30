from collections.abc import Sequence

class Dependency(Sequence):
		def __init__(self, key, source_type, source_url, source_version):
				self.key = key
				self.source_type = source_type
				self.source_url = source_url
				self.source_version = source_version

		def __len__(self) -> int:
			return super().__len__()
		
		def __getitem__(self, index):
			return super().__getitem__()