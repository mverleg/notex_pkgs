
from bs4 import NavigableString, BeautifulSoup


def temporary_tag_replacement(soup, **kwargs):
	for tag in soup.find_all(('eq', 'var')):
		BeautifulSoup.insert(tag, 0, NavigableString('$['))  # necessary hack
		BeautifulSoup.append(tag, NavigableString(']$'))
	for tag in soup.find_all(('equation',)):
		BeautifulSoup.insert(tag, 0, NavigableString('$$['))  # necessary hack
		BeautifulSoup.append(tag, NavigableString(']$$'))
	return soup


