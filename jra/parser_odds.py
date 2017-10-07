from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp

class parser_odds(prp.parser_post):

    def parse_content(self, soup):
        fixed = True
        div = soup.find('div', attrs={'class' : 'raceTtlTable'})
        odds_info = {}
        if div:
            spans = div.find_all('span')
            for span in spans:
                if span.has_attr('class'):
                    if 'headerOdds2' in span['class']:
                        value = span.get_text()
                        if not "最終" in value:
                            try:
                                time_value = pu.func_parser.parse_time(value)
                                full, stamp = pu.parser_util_convert_timestr_full_and_stamp(time_value)
                                fixed = False
                                odds_info['log'] = 'Value OK 0001'
                                break
                            except:
                                print("ValueError : {}".format(span.get_text()))
                                odds_info['log'] = 'Value Error 0002 : {}'.format(span.get_text())
                        else:
                            print(">> 最終オッズ")
                            odds_info['log'] = 'Value OK 0002'
                    else:
                        print(">>> 最終オッズ")
                        odds_info['log'] = 'Value OK 0003'

        odds_info['fixed'] = fixed
        if fixed == False:
            odds_info['timestamp'] = stamp
            #print("{} 現在のオッズ({})".format(time_value, full))            

        odds_list = self.parse_odds_content(soup)
        odds_info['odds'] = odds_list

        return odds_info
