from . import parser as pr
from . import parser_util as pu
from . import parser_odds_waku as prow
from . import parser_post as prp


class parser_odds_trio(prow.parser_odds_waku):

    def parse_odds(self, matrix, tr):
        td = tr.find('td')
        odds = td.get_text()
        if odds != '':
            try :
                matrix['odds'] = pu.func_parser.get_float(odds)
            except:
                if odds == '取消':
                    pass

    def split_axis(self, axis):
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
        axis_list = soup.find_all("table", attrs = {'class' : 'ozSanrenUmaINTable'})

        trio_list = []

        j = 0
        for i, uma_list in enumerate(axis_list):
            tr = uma_list.find('tr')
            th = tr.find('th')
            try :
                axis1, axis2 = self.split_axis(th.get_text())
            except:
                print("発売なし")
                continue
            
            if len(trio_list) == 0 or trio_list[j]['number'] != axis1:
                trio_axis = {}
                trio_axis['number'] = axis1
                trio_list.append(trio_axis)
                trio_axis['matrix'] = []
                if trio_list[j]['number'] != axis1:
                    j = j + 1

            trio_axis2 = {'number':axis2, 'matrix' : []}
            #trio_axis['matrix'].append(trio_axis2 )
            trs = tr.find_next_siblings('tr')

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

            trio_axis2['matrix'] = self.sort_list(trio_axis2['matrix'], 'number')
            trio_axis['matrix'].append(trio_axis2)
            
        for list in trio_list:
            list['matrix'] = self.sort_list(list['matrix'], 'number')

        return trio_list


