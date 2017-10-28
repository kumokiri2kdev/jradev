from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
from enum import Enum

class odds_status(Enum):
    WORKING = 1
    FIXED = 2
    FIXED_1DAY_BEFORE = 3
    FIXED_2DAY_BEFORE = 4
    UNKNOWN = 99

class parser_odds(prp.parser_post):

    def parse_content(self, soup):
        status = odds_status.UNKNOWN

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
                                status = odds_status.WORKING
                                odds_info['log'] = 'Value OK 0001'
                                break
                            except:
                                print("ValueError : {}".format(span.get_text()))
                                odds_info['log'] = 'Value Error 0002 : {}'.format(span.get_text())
                        else:
                            print(">> 最終オッズ")
                            if "前々日" in value:
                                status = odds_status.FIXED_2DAY_BEFORE
                                stamp = 9999999997.9
                            elif "前日" in value:
                                status = odds_status.FIXED_1DAY_BEFORE
                                stamp = 9999999998.9
                            else:
                                status = odds_status.FIXED
                                stamp = 9999999999.9

                            odds_info['log'] = 'Value OK 0002'
                    else:
                        print(">>> 最終オッズ")
                        odds_info['log'] = 'Value OK 0003'

        odds_info['timestamp'] = stamp

        if status != odds_status.FIXED:
            odds_info['fixed'] = False
            #print("{} 現在のオッズ({})".format(time_value, full))            
        else:
            odds_info['fixed'] = True

        odds_list = self.parse_odds_content(soup)
        odds_info['odds'] = odds_list

        return odds_info
