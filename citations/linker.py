
from bs4 import NavigableString, BeautifulSoup


class BibliographyLinker:
	def __init__(self, config, **kwargs):
		self.config = config

	# def update_ref(self, element, name, order_map, style):
	# 	identifier = element.attrs['data-identifier']
	# 	element.attrs['class'].append('citstyle-{0:s}'.format(style))
	# 	index = order_map[identifier]
	# 	element.append(NavigableString(self.config.citations[identifier].refname(index, style)))

	def __call__(self, soup, style='tmp-json-style'):
		order_map = {identifier: index + 1 for index, identifier in enumerate(self.config.reference_counts.keys())}
		for bio_tag in soup.find_all('notex-bibliography'):
			if len(self.config.citations):
				ol_tag = BeautifulSoup.new_tag(bio_tag, 'ol', **{'class': 'bibliography-list'})
				for identifier, count in self.config.reference_counts.items():
					if identifier in self.config.citations:
						li_tag = BeautifulSoup.new_tag(soup, 'li', **{
							'id': 'cite-{0:d}'.format(order_map[identifier]),
							'class': 'citation-details',
							'ref-count': count,
						})
						li_tag.append(NavigableString(self.config.citations[identifier].render(style)))
						ol_tag.append(li_tag)
					else:
						#todo: logging
						print('reference to citation "{0:s}" which is not defined'.format(identifier))
						li_tag = BeautifulSoup.new_tag(soup, 'li')
						li_tag.append(NavigableString('unknown citation "{0:s}"'.format(identifier)))
						ol_tag.append(li_tag)
				bio_tag.append(ol_tag)
		tag_names = set()
		if self.config.has_ci_tag:
			tag_names.add('reference-ci')
		if self.config.has_cite_tag:
			tag_names.add('reference-cite')
		if tag_names:
			for ref_tag in soup.find_all(tag_names):
				identifier = ref_tag.attrs['data-identifier']
				if identifier in self.config.citations:
					citation = self.config.citations[identifier]
					ref_tag.attrs['class'].append('citstyle-{0:s}'.format(style))
					index = order_map[identifier]
					ref_tag.parent.attrs['href'] = '#cite-{0:d}'.format(index)
					if ref_tag.name == 'reference-cite':
						marker = BeautifulSoup.new_tag(ref_tag, 'cite')
						marker.append(NavigableString(self.config.citations[identifier].ref_title()))
					else:
						marker = NavigableString(citation.ref_name(index, style))
					ref_tag.append(marker)
				else:
					#todo: logging
					print('reference "{0:s}" not found'.format(identifier))
					ref_tag.attrs['class'].extend(['citstyle-{0:s}'.format(style),
						'citation-not-found', 'not-found'])
					ref_tag.append(NavigableString('[reference "{0:s}" ??]'.format(identifier)))
		# if self.config.has_cite_tag:
		# 	for cite_tag in soup.find_all('reference-cite'):
		# 		identifier = cite_tag.attrs['data-identifier']
		# 		cite_tag.attrs['class'].append('citstyle-{0:s}'.format(style))
		# 		cite_wrap = BeautifulSoup.new_tag(cite_tag, 'cite')
		# 		cite_tag.append(NavigableString(self.config.citations[identifier].ref_title()))


