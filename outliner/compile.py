
from bs4 import BeautifulSoup
from copy import deepcopy
from html5_outliner import outline
from slugify import UniqueSlugify


class ToCBuilder:
	def __init__(self, config, **kwargs):
		self.config = config

	def __call__(self, soup):
		"""  """
		ToC = self.make_toc(soup)
		""" Insert the ToC. """
		for placeholder in soup.find_all('table-of-content'):
			elem = deepcopy(ToC)
			# elem.attrs.update(placeholder.attrs)
			placeholder.replace_with(elem)
		""" Add floating ToC """
		if getattr(self.config, 'SIDE_TOC', True):
			print('  adding table of content in sidebar')
			elem = deepcopy(ToC)
			elem.insert(0, self.config.parser.parse_partial('<a href="#">Back to top</a>'))
			elem.attrs['id'] = elem.attrs.get('id', '')
			elem.attrs['id'] = (elem.attrs['id'] + ' floating-toc').strip(' ')
			soup.html.body.insert(0, elem)
		return soup

	def make_toc(self, soup):
		""" Add sections and create outline. """
		def skip_hidden(elem):
			return 'toc-hidden' not in elem.attrs.get('class', ())
		top = outline(soup, filter=skip_hidden)
		""" Add slugs to each section. """
		slugifier = UniqueSlugify(to_lower=True)
		for item in top.flat():
			item.slug = 'ch-' + slugifier(item.name)
			if item.header:
				link = BeautifulSoup.new_tag(item.header, 'a', href='#{0:s}'.format(item.slug))
				for part in item.header.children:
					link.append(part)
				item.header.append(link)
			item.elem.attrs['id'] = (item.elem.attrs.get('id', '') + ' ' + item.slug).strip(' ')
		""" Generate the table of content. """
		def toc_level(section, show=False):
			html = ''
			if show:
				html = '<li><a href="#{0:s}">{1:s}</a></li>'.format(section.slug, section.name)
			if section.children:
				html += '<ol>' + '\n'.join(toc_level(child, show=True) for child in section.children) + '</ol>'
			return html
		html = '<nav class="table-of-contents" role="navigation">' + toc_level(top) + '</nav>'
		return self.config.parser.parse_partial(html)


