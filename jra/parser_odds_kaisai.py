from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp


class parser_odds_kaisai(prp.parser_post):
    def parse_content(self, soup):
        races = soup.find_all("td", attrs = {"class":"raceNo"})

        race_list = [{} for i in range(len(races))]

        for i, race in enumerate(races):
            race_data = race_list[i]
            anchor = race.find("a")
            params = pu.func_parser.parse_func_params(anchor['onclick'])
            #print(params)
            race_id = race.find("img")['alt']
            #print(race_id)
            tr = race.parent
            tds = tr.find_all('td')
            for td in tds :
                #print(td)
                if td.has_attr('class'):
                    class_name = td['class']
                    #print(class_name)
                    if 'raceNo' in class_name:
                        category = td.find("img")
                        #print(category['alt'])
                        race_data['no'] = category['alt']
                        params = pu.func_parser.parse_func_params(anchor['onclick'])
                        #print(params)
                    elif 'raceTitleUpper' in class_name:
                        #print(td.get_text())
                        prevtd = td.parent.find_next('tr').find('td')
                        prev_class_name = prevtd['class']
                        if 'raceTitleLower' in prev_class_name:
                            #print(prevtd.get_text())
                            lower_value = pu.func_parser.trim_clean(prevtd.get_text())
                            if lower_value == "":
                                race_data['condition']  = td.get_text()
                            else:
                                race_data['name'] = td.get_text()
                                race_data['condition'] = lower_value
                        else:
                            race_data['condition'] = td.get_text()
                    elif 'hsj' in class_name:
                        race_data['status'] = td.get_text()

                else :
                    anchor = td.find("a")
                    if anchor:
                        category = td.find("img")['alt']
                        params = pu.func_parser.parse_func_params(anchor['onclick'])
                        #print(params)
                        #print(category)
                        if category == '単勝複勝':
                            race_data['win'] = params[1]
                        elif category == '枠連':
                            race_data['waku'] = params[1]
                        elif category == '馬連':
                            race_data['uma'] = params[1]
                        elif category == 'ワイド':
                            race_data['wide'] = params[1]
                        elif category == '馬単':
                            race_data['exacta'] = params[1]
                        elif category == '３連複':
                            race_data['trio'] = params[1]
                        elif category == '３連単':
                            race_data['trioexacta'] = params[1]
        return race_list

