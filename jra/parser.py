from bs4 import BeautifulSoup
from . import parser_util as pu
import urllib.request
import os

if os.getenv('JRA_PRS_DEBUG', '0') == '1':
	DEBUG = True
else:
	DEBUG = False

class parser:
	def __init__(self, file_path, **kwargs):
		if DEBUG:
			self.base_uri = 'http://127.0.0.1:8080'
		else:
			self.base_uri = 'http://www.jra.go.jp'
		self.uri = self.gen_asb_uri(file_path)
		if 'data' in kwargs:
			self.method = 'POST'
			self.data = kwargs['data'].encode('utf-8')
		else:
			self.method = 'GET'

	def gen_asb_uri(self, file_path):
		return '{}{}'.format(self.base_uri, file_path)
		
	def parse_html(self, content):
		soup = BeautifulSoup(content,"html.parser")
		return self.parse_content(soup)

	def parse(self):
		if self.method == 'POST':
			request = urllib.request.Request(self.uri, data=self.data, method='POST')
		else:
			request = urllib.request.Request(self.uri)
		
		with urllib.request.urlopen(request) as response:
			response_body = response.read().decode("'shift_jis'")
		
		return self.parse_html(response_body)

		
	def parse_content(self, soup):
		print("Base Class parse_content must not  be called")
		
				
	