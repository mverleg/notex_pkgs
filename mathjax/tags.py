
from bs4 import NavigableString, BeautifulSoup
from notexp.bases import TagHandler


class InlineEquation(TagHandler):
	def __call__(self, element, **kwargs):
		BeautifulSoup.insert(element, 0, NavigableString('$['))
		BeautifulSoup.append(element, NavigableString(']$'))
		element.name = 'math-{0:s}'.format(element.name)


class BlockEquation(TagHandler):
	def __call__(self, element, **kwargs):
		BeautifulSoup.insert(element, 0, NavigableString('$$['))
		BeautifulSoup.append(element, NavigableString(']$$'))
		element.name = 'math-{0:s}'.format(element.name)


