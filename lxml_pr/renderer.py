
from bs4 import Comment
# here to check that beautifulsoup is installed


class LXML_Renderer:
	def __init__(self, config):
		pass

	def render(self, soup, formatter='minimal', strip_comments=False):
		if strip_comments:
			for comment in soup.find_all(text=lambda elem: isinstance(elem, Comment)):
				comment.extract()
		# return soup.prettify(formatter='formatter', encoding='utf8')
		# return soup.tostring(soup, pretty_print=False, encoding='unicode')
		return str(soup)


