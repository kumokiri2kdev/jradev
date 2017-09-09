import re

class parse_error(Exception):
	def __init__(self):
		pass

class func_param_parser:
	def __init__(self):
		self.func_patern = re.compile(r'\(.*\)')
		self.split_pattern = re.compile(r'[\(\)\']')
		
	def parse(self, str):
		matched = self.func_patern.search(str)
		if matched:
			params = self.split_pattern.sub('',matched[0]).split(',')
			if len(params) > 0:
				return params
			else :
				raise parse_error
		else :
			raise parse_error

