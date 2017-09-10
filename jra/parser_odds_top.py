import parser as pr

class parser_odds_top(pr.parser):
    def __init__(self, path, param):
        param = "cname={}".format(param)
        super(parser_odds_top,self).__init__(path, data=param)
        pass
        
    def parse_content(self, soup):
        print("odds top start parsing")
        print(soup)
        areas = soup.find_all("div", attrs = {"class":"joSelectArea"})
		
        for area in areas:
            buttons = area.find_all("td", attrs = {"class":"kaisaiBtn"})
            for button in buttons :
                anchor = button.find("a")
                params = pr.func_parser.parse(anchor['onclick'])
                print(params)
                kaisai_id = button.find("img").get_text()
                print(kaisai_id)