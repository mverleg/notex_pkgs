
from collections import OrderedDict
from .citation import Citation
from notexp.bases import Configuration


class CitationConfig(Configuration):
	def __init__(self, options):
		super(CitationConfig, self).__init__(options)
		self.reference_counts = OrderedDict()
		self.citations = OrderedDict()
		self.bibliographies = OrderedDict()
		self.has_ci_tag = self.has_cite_tag = False

	def add_reference(self, name):
		if name not in self.reference_counts:
			self.reference_counts[name] = 1
		else:
			self.reference_counts[name] += 1

	def add_citation(self, name, citation):
		assert isinstance(citation, Citation)
		if name in self.citations:
			#todo: warning
			print('citation {0:s} already exists'.format(name))
		self.citations[name] = citation


