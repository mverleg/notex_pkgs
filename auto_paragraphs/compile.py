
from bs4 import BeautifulSoup, NavigableString, Comment, Tag


"""
An incomplete set of inline elements that I consider to occur in normal text.

Excludes for example `br`, `img`, all form-related tags and some deprecated tags.

Also includes some non-existent tags, like `c`.

https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements
"""
paragraph_inline_tags = {'b', 'big', 'i', 'small', 'abbr', 'acronym', 'cite', 'code', 'em', 'strong', 'time', 'var',
	'a', 'bdo', 'q', 'span', 'sub', 'sup', 'c'}


def add_paragraphs(soup, **kwargs):
	def _group_paragraph(soup, content):
		if content:
			ptag = BeautifulSoup.new_tag(soup, 'p')  # a necessary hack, somehow
			content[0].replace_with(ptag)
			for txttag in content[1:]:
				txttag.extract()
			for txttag in content:
				ptag.append(txttag)

	containers = soup.find_all(('article', 'section', 'notex-leaf', 'notex-section',))
	for container in containers:
		while True:
			content, found = [], 0
			for child in container.children:
				# print('>>', child)
				# print(list(q for q in dir(child) if (not q.startswith('_'))))# and isinstance(getattr(child, q), str))))
				if isinstance(child, NavigableString) and not isinstance(child, Comment):
					if len(child.string.strip()) > 3:
						# print('*******', type(child), isinstance(child, NavigableString), child.string)
						found += 1
					content.append(child)
				elif isinstance(child, Tag):
					if child.name in paragraph_inline_tags:
						found += 1
						content.append(child)
					else:
						if found:
							_group_paragraph(soup, content)
							break
						content, found = [], 0
				else:
					""" This includes comments and unknown tags. """
					#todo: logging
					content.append(child)
			else:
				""" Break the outer loop as soon as the inner one completes). """
				if found:
					_group_paragraph(soup, content)
				break
	for split_tag in soup.find_all('autop-split-here'):
		split_tag.extract()
	return soup


