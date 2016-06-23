
from notexp.bases import TagHandler


class Section(TagHandler):
	def __call__(self, element, **kwargs):
		""" Just mark as being sectioning content handled by outliner. """


class ToCLocation(TagHandler):
	def __call__(self, element, **kwargs):
		""" Just mark as being the location of ToC handled by outliner. """


