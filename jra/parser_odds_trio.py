from . import parser as pr
from . import parser_post as prp


class parser_odds_trio(prp.parser_post):
    def sort_list(self, list, key):
        for i in range(0, len(list)):
            j = len(list) - 1
            while j > i:
                if list[j][key] < list[j-1][key]:
                    tmp = list[j-1]
                    list[j-1] = list[j]
                    list[j] = tmp
                j = j - 1

        return list

    def parse_odds(self, matrix, tr):
        td = tr.find('td')
        odds = td.get_text()
        if odds != '':
            try :
                matrix['odds'] = pr.func_parser.get_float(odds)
            except:
                if odds == '取消':
                    pass

    def split_axis(self, axis):
        axes = axis.split('-')
        if len(axes) < 2:
            raise ValueError

        try :
            axes1 = pr.func_parser.get_number(axes[0])
            axes2 = pr.func_parser.get_number(axes[1])   
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
            trio_axis['matrix'].append(trio_axis2 )
            trs = tr.find_next_siblings('tr')

            for k, tr in enumerate(trs):
                trix_axis_value = {}
                try :
                    th = tr.find('th')
                    pair = pr.func_parser.get_number(th.get_text())
                except:
                    continue
                try :
                    td = tr.find('td')
                    value = pr.func_parser.get_float(td.get_text())
                except:
                    value = '発売無し'

                trio_axis2['matrix'].append({'number': pair, 'odds': value}) 

        return trio_list


