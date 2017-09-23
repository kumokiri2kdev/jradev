from . import parser as pr
from . import parser_util as pu
from . import parser_odds as pro


class parser_odds_trioexacta(pro.parser_odds):
    def parse_odds(self, matrix, tr):
        td = tr.find('td')
        odds = td.get_text()
        if odds != '':
            try :
                matrix['odds'] = pu.func_parser.get_float(odds)
            except:
                if odds == '取消':
                    pass

    def parse_odds_content(self, axis):
        axes = axis.split('-')
        if len(axes) < 2:
            raise ValueError

        try :
            axes1 = pu.func_parser.get_number(axes[0])
            axes2 = pu.func_parser.get_number(axes[1])   
        except:
            raise         

        return axes1, axes2


    def parse_content(self, soup):
        axis_list = soup.find_all("table", attrs = {'class' : 'santanOddsHyo'})

        trio_list = []

        j = 0
        for i, axis in enumerate(axis_list):
            tr = axis.find('tr')
            th = tr.find('th').find_next('th')
            axis1 = pu.func_parser.get_number(th.get_text())

            if len(trio_list) == 0 or trio_list[j]['number'] != axis1:
                trio_axis = {}
                trio_axis['number'] = axis1
                trio_list.append(trio_axis)
                trio_axis['matrix'] = []
                if trio_list[j]['number'] != axis1:
                    j = j + 1

            tr = tr.find_next('tr')
            ths = tr.find('th').find_next_siblings('th')

            odds_tbls = axis.find_all('table', attrs = {'class' : 'oddsTbl'})

            for th, odds_tbl  in zip(ths,odds_tbls):
                axis2 = pu.func_parser.get_number(th.get_text())
                trio_axis2 = {'number':axis2, 'matrix' : []}
                trio_axis['matrix'].append(trio_axis2)

                trs = odds_tbl.find_all('tr')
                
                for k, tr in enumerate(trs):
                    trix_axis_value = {}
                    try :
                        th = tr.find('th')
                        pair = pu.func_parser.get_number(th.get_text())
                    except:
                        continue
                    try :
                        td = tr.find('td')
                        value = pu.func_parser.get_float(td.get_text())
                    except:
                        value = '発売無し'

                    trio_axis2['matrix'].append({'number': pair, 'odds': value}) 
                    
        return trio_list


