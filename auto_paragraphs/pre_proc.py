
from re import sub


def insert_breakpoints(html):
	return sub(r'\s*\n\s*\n\s*', '<autop-split-here />', html)


