
from json import dumps


class Citation:
	def __init__(self, **attrs):
		self.attrs = attrs

	def render(self, style):
		return dumps(self.attrs, indent=4)

	def ref_name(self, index, style):
		return '[{0:d}]'.format(index)

	def ref_title(self):
		if 'title' in self.attrs:
			return self.attrs['title']
		elif 'author' in self.attrs:
			return '[no title by {0:}]'.format(self.attrs['author'])
		else:
			return '[no title]'


