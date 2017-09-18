from . import parser as pr
from . import parser_util as pu

class parser_top(pr.parser):
	def __init__(self):
		super(parser_top,self).__init__('/')
		
	def parse_content(self, soup):
		param_list = {}
		qmenu = soup.find("div", attrs={"id": "quick_menu"})
		if qmenu:
			content = qmenu.find("div", attrs = {"class":"content"})
			if content :
				links = content.find_all("li")
				for link in links:
					anchor = link.find("a")
					if anchor.has_attr('onclick'):
						params = pu.func_parser.parse_func_params(anchor['onclick'])
						#print(params)
						if params[0].endswith('accessI.html'):
							#print("開催情報 : {}".format(params[1]))
							param_list['kaisai'] = params[1]
						elif params[0].endswith('accessD.html'):
							#print("出馬表 : {}".format(params[1]))
							param_list['shutuba'] = params[1]
						elif params[0].endswith('accessO.html'):
							#print("オッズ : {}".format(params[1]))
							param_list['odds'] = params[1]
						elif params[0].endswith('accessH.html'):
							#print("払い戻し : {}".format(params[1]))
							param_list['haraimodoshi'] = params[1]
						elif params[0].endswith('accessS.html'):
							#print("レース結果 : {}".format(params[1]))
							param_list['race'] = params[1]
						elif params[0].endswith('accessT.html'):
							#print("特別レース登録馬 : {}".format(params[1]))
							param_list['tokubetu'] = params[1]
		
		return param_list