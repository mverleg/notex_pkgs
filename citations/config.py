
from collections import OrderedDict, defaultdict
from .citation import Citation
from notexp.bases import Configuration


class Config(Configuration):
	def __init__(self, options):
		super(Config, self).__init__(options)
		self.reference_counts = defaultdict(int)
		self.citations = OrderedDict()
		self.bibliographies = OrderedDict()

	def add_reference(self, name):
		self.reference_counts[name] += 1

	def add_citation(self, name, citation):
		assert isinstance(citation, Citation)
		if name in self.citations:
			#todo: warning
			print('citation {0:s} already exists'.format(name))
		self.citations[name] = citation


