import re

class parse_error(Exception):
	def __init__(self):
		pass

class parser_util:
	def __init__(self):
		self.func_patern = re.compile(r'\(.*\)')
		self.split_pattern = re.compile(r'[\(\)\']')
		
	def parse_func_params(self, str):
		matched = self.func_patern.search(str)
		if matched:
			params = self.split_pattern.sub('',matched[0]).split(',')
			if len(params) > 0:
				return params
			else :
				raise parse_error
		else :
			raise parse_error

	def trim_clean(self, str):
		return str.strip()

	def parse_weight(self, str):
		if str == '':
			raise ValueError
		try:
			searched = re.search(self.func_patern, str)
			diff = re.sub(r'[\(\)]', '', searched[0])
			weight = re.sub(self.func_patern, '', str)
			try:
				diff = int(diff)
			except:
				pass

			weight = int(weight)
		except:
			raise ValueError

		return weight, diff

	def get_number(self, str):
		try:
			return int(self.trim_clean(str))
		except :
			raise

	def get_float(self, str):
		try:
			return float(self.trim_clean(str))
		except:
			raise

		

