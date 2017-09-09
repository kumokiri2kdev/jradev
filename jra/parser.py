from bs4 import BeautifulSoup
import parser_util as pu

func_parser = pu.func_param_parser()

class parser:
	def __init__(self, file_path):
		print("Parser Base Class")
		self.uri = self.gen_asb_uri(file_path)
		print(self.uri)

	def gen_asb_uri(self, file_path):
		return 'http://www.jra.go.jp{}'.format(file_path)
		
	def parse(self, content):
		soup = BeautifulSoup(content,"html.parser")
		self.parse_content(soup)
		
	def parse_content(self, soup):
		print("Base Class parse_content must not  be called")
		
				
	