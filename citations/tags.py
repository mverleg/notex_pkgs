
from bibtexparser import loads
from bs4 import BeautifulSoup
from copy import copy
from notexp.bases import TagHandler
from .citation import Citation


class CiTagHandler(TagHandler):
	"""
	A reference to a citation by identifier (will show a number or whatever the format dictates).
	"""
	def __call__(self, element, **kwargs):
		identifier = element.decode_contents().strip()
		self.config.add_reference(identifier)
		anchor = BeautifulSoup.new_tag(element, 'a', href='#cite-{0:s}'.format(identifier))
		anchor.append(BeautifulSoup.new_tag(element, 'reference-ci', **{
			'data-identifier': identifier,
			'class': ['citation-reference', 'citation-{0:s}'.format(identifier)],
		}))
		element.replace_with(anchor)
		self.config.has_ci_tag = True


class CiteTagHandler(TagHandler):
	"""
	A reference to a citation by identifier (will show the name of the work, as per the specification of the <cite> tag.
	"""
	def __call__(self, element, **kwargs):
		identifier = element.decode_contents().strip()
		self.config.add_reference(identifier)
		anchor = BeautifulSoup.new_tag(element, 'a', href='#cite-{0:s}'.format(identifier))
		anchor.append(BeautifulSoup.new_tag(element, 'reference-cite', **{
			'data-identifier': identifier,
			'class': ['citation-reference', 'citation-{0:s}'.format(identifier)],
		}))
		element.replace_with(anchor)
		self.config.has_cite_tag = True


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
	def __call__(self, element, **kwargs):
		citations = loads(element.decode_contents())
		for citation in citations:
			identity = citation.pop('ID')
			typ = citation.pop('ENTRYTYPE')
			self.config.add_citation(identity, Citation(type=typ, **element.attrs))
		element.extract()


class BibliographyTagHandler(TagHandler):
	"""
	An overview of all citations.
	Bibliography cannot be created at tag-time, because not all references may have been found.
	(E.g. some that appear after the bibliography, or in other Sections, or search order may change).
	"""
	def __call__(self, element, **kwargs):
		tag_id = 'bibliography-{0:}'.format(len(self.config.bibliographies) + 1)
		article = BeautifulSoup.new_tag(element, 'article')
		article.append(BeautifulSoup.new_tag(element, 'notex-bibliography', id=tag_id))
		self.config.bibliographies[tag_id] = copy(element.attrs)
		element.replace_with(article)


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


