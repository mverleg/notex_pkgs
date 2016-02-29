
from json import dumps


class Citation:
	def __init__(self, **attrs):
		self.attrs = attrs

	def render(self, style):
		return dumps(self.attrs, indent=4)


