
# just here to check that lxml is installed
from lxml.etree import XMLParser
from bs4 import BeautifulSoup, SoupStrainer


# class LXML_Parser:
# 	def __init__(self):
# 		self.parser = XMLParser(remove_blank_text=True, remove_comments=False)
#
# 	def parse(self, text):
# 		return fromstring('<leaf>' + text + '</leaf>', parser=self.parser)
# 		# return BeautifulSoup(text, 'lxml')


class LXML_Parser:
	def __init__(self, config):
		pass

	def parse(self, text, only=None):
		if only is not None:
			filter = SoupStrainer(only)
			return BeautifulSoup(text, 'lxml', parse_only=filter, from_encoding='utf8')
		return BeautifulSoup(text, 'lxml')


