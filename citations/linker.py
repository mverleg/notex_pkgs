
from bs4 import NavigableString, BeautifulSoup


class BibliographyLinker:
	def __init__(self, config, **kwargs):
		self.config = config

	def __call__(self, soup):
		for bibtag_id, attrs in self.config.bibliographies.items():
			bio_tag = soup.find(id=bibtag_id)
			for name, count in self.config.reference_counts.items():
				if name in self.config.citations:
					ptag = BeautifulSoup.new_tag(soup, 'p', ref_count=count)
					# todo: do something for unused references? if not config.reference_counts[name]...
					ptag.append(NavigableString(self.config.citations[name].render('tmp-json-style')))
					bio_tag.append(ptag)
				else:
					#todo: logging
					print('reference to citation {0:s} which is not defined'.format(name))
					ptag = BeautifulSoup.new_tag(soup, 'p')
					ptag.append(NavigableString('unknown citation "{0:s}"'.format(name)))
					bio_tag.append(ptag)


