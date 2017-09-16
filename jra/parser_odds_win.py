from . import parser as pr
from . import parser_post as prp


class parser_odds_win(prp.parser_post):
    def parse_param(self, element):
        anchor = element.find("a")
        if anchor.has_attr('onclick'):
            params = pr.func_parser.parse_func_params(anchor['onclick'])
        else:
            return None

        return params

    def get_name_params(self, element):
        data = {}
        data['name'] = element.get_text()
        params = self.parse_param(element)
        if params and len(params) > 1:
            data['url'] = params[0]
            data['param'] = params[1]

        return data

    def parse_content(self, soup):
        print("odds win start parsing")

        umas = soup.find_all("th", attrs = {"class":"umaban"})

        uma_list = [{}] * len(umas)

        for i, uma in enumerate(umas) :
            #print(uma.parent)
            print("Uma ban : {}".format(uma.get_text()))
            tds = uma.parent.find_all('td')
            uma_data = {}
            uma_list[i] = uma_data
            uma_data['number'] = pr.func_parser.get_number(uma.get_text())
            uma_data['odds'] = {}

            for td in tds :
                #print(td)
                if td.has_attr('class'):
                    class_name = td['class']
                    if 'bamei' in class_name:
                        uma_data['uma'] = self.get_name_params(td)
                    elif 'oztan' in class_name:
                        #print("単勝 : {}".format(pr.func_parser.trim_clean(td.get_text())))
                        try:
                            win = pr.func_parser.get_float(td.get_text())
                            uma_data['odds']['win'] = win
                        except:
                            psss
                    elif 'fukuMin' in class_name:
                        #print("複勝（最低） : {}".format(td.get_text()))
                        try :
                            fuku_min = pr.func_parser.get_float(td.get_text())
                            uma_data['odds']['fuku_min'] = fuku_min
                        except:
                            pass
                    elif 'fukuMax' in class_name:
                        #print("複勝（最高） : {}".format(td.get_text()))
                        try :
                            fuku_max = pr.func_parser.get_float(td.get_text())
                            uma_data['odds']['fuku_max'] = fuku_max
                        except:
                            pass
                    elif 'seirei' in class_name:
                        #print("性齢 : {}".format(td.get_text()))
                        uma_data['sexage'] = td.get_text()
                    elif 'batai' in class_name:
                        #print("馬体重 : {}".format(td.get_text()))
                        try :
                            weight, diff = pr.func_parser.parse_weight(td.get_text())
                            uma_data['weight'] = weight
                            uma_data['diff'] = diff
                        except:
                            pass
                    elif 'futan' in class_name:
                        #print("斤量 : {}".format(td.get_text()))
                        uma_data['hande'] = td.get_text()
                    elif 'kishu' in class_name:
                        #print("騎手 : {}".format(td.get_text()))
                        #uma_data['jokey'] = td.get_text()
                        uma_data['jokey'] = self.get_name_params(td)
                    elif 'choukyou' in class_name:
                        #print("調教師 : {}".format(td.get_text()))
                        #uma_data['jokey'] = td.get_text()
                        uma_data['stable'] = self.get_name_params(td)
                        pass
                    else:
                        print(class_name)

        return uma_list
