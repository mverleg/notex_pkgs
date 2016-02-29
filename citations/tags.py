
from bs4 import BeautifulSoup
from copy import copy
from re import findall, MULTILINE, DOTALL
from notexp.bases import TagHandler
from .citation import Citation


class ReferTagHandler(TagHandler):
	"""
	A reference to a citation by name.
	"""
	def __call__(self, element, **kwargs):
		self.config.add_reference(element.decode_contents().strip())
		element.extract()


class CitationTagHandler(TagHandler):
	"""
	A citation specified as tag attributes, with the content being the name.
	"""
	def __call__(self, element, **kwargs):
		self.config.add_citation(element.decode_contents(), Citation(**element.attrs))
		element.extract()


class BibtexTagHandler(TagHandler):
	"""
	A citation specified in bibtex format (as the content of the tag).
	"""
	def parse_bibtex(self, txt):
		#todo this goes wrong as soon as there's a } in the title; find a python package to do this
		#todo: bibtex tag should accept `src` attribute to load external file
		found = findall(r'@([\w\-]+)\s*\{(.*?)\}', txt, DOTALL | MULTILINE)
		return found

	def __call__(self, element, **kwargs):
		name, citation = self.parse_bibtex(element.decode_contents())
		self.config.add_citation(name, Citation(**element.attrs))
		element.extract()
		raise NotImplementedError('bibtex style input does not work yet')


class BibliographyTagHandler(TagHandler):
	"""
	An overview of all citations.
	Bibliography cannot be created at tag-time, because not all references may have been found.
	(E.g. some that appear after the bibliography, or in other Sections, or search order may change).
	"""
	def __call__(self, element, **kwargs):
		tag_id = 'bibliography-{0:}'.format(len(self.config.bibliographies) + 1)
		bio_tag = BeautifulSoup.new_tag(element, 'notex-bibliography', id=tag_id)
		self.config.bibliographies[tag_id] = copy(element.attrs)
		element.replace_with(bio_tag)


# def refer_to_citation(self, element, config, **kwargs):
# 	"""
# 	A reference to a citation by name.
# 	"""
# 	config.add_reference(element.encode_contents().strip())
# 	element.extract()
#
#
# def register_citation(self, element, config, **kwargs):
# 	"""
# 	A citation specified as tag attributes, with the content being the name.
# 	"""
# 	config.add_citation(element.encode_contents(), Citation(**element.attrs))
# 	element.extract()
#
#
# def register_bibtex_citation(self, element, config, **kwargs):
# 	"""
# 	A citation specified in bibtex format (as the content of the tag).
# 	"""
# 	bibtex_txt = element.encode_contents()
# 	found = findall(r'@(\w\-)\{([^\{\}]*)\}', bibtex_txt)
# 	print(found)
# 	for name, citation in ['hi', {}]:
# 		config.add_citation(name, Citation(**element.attrs))
# 	element.extract()
#
#
# def bibliography_tag(self, element, config, **kwargs):
# 	"""
# 	An overview of all citations.
# 	Bibliography cannot be created at tag-time, because not all references may have been found.
# 	(E.g. some that appear after the bibliography, or in other Sections, or search order may change).
# 	"""
# 	tag_id = 'bibliography-{0:}'.format(len(config.bibliographies) + 1)
# 	bio_tag = BeautifulSoup.new_tag(element, 'notex-bibliography', id=tag_id)
# 	config.bibliographies[tag_id] = copy(element.attrs)
# 	element.replace_with(bio_tag)


