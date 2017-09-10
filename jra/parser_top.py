import parser as pr

class parser_top(pr.parser):
	def __init__(self):
		print("parser_top")
		super(parser_top,self).__init__('/')
		
	def parse_content(self, soup):
		print("start parsing")
		qmenu = soup.find("div", attrs={"id": "quick_menu"})
		if qmenu:
			content = qmenu.find("div", attrs = {"class":"content"})
			if content :
				links = content.find_all("li")
				for link in links:
					anchor = link.find("a")
					if anchor.has_attr('onclick'):
					#if 'onclick' in anchor:
						#print(anchor['onclick'])
						params = pr.func_parser.parse(anchor['onclick'])
						print(params)
					
		
		