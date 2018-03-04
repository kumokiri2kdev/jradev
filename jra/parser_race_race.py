from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
import re

def parse_race_name(race_str):
  info = race_str.split(" ")
  
  info[0] = int(info[0].replace("R", ""))

  if len(info) > 2:
    return info[0], info[2], info[1]
  elif len(info) > 1:
    return info[0], info[1], None
  else:
    return info[0], None, None

def parse_race_time(time_str):
  times = time_str.split(":")
  time_sec = int(times[0]) * 600 + int(float(times[1]) * 10)

  return time_sec


class parser_race_race(prp.parser_post):
    def parse_content(self, soup):
        ret = {}

        kaisai = soup.find("div",  attrs = {"class":"heading1Text"})
        date, weekday, kaisuu, place, day =  pu.parser_util_parse_kaisai(kaisai.get_text())

        ret['date'] = date
        ret['weekday'] = weekday
        ret['kaisuu'] = kaisuu
        ret['place'] = place
        ret['nichisuu'] = day

        ret['race'] = race_info = {}

        race_name_text = soup.find("div",  attrs = {"class":"heading2Text"})
        race_num, race_name, _ = parse_race_name(race_name_text.get_text())
        race_info['number'] = race_num
        if race_name:
          race_info['name'] = race_name

        grade = race_name_text.find("img", attrs = {"class":"gradeIconImageTtl"})
        if grade:
          race_info['grade']  = grade['alt']

        odds_link = soup.find("div",  attrs = {"class":"heading2BtnDiv"})
        anchor = odds_link.find("a")
        if anchor:
          params = pu.func_parser.parse_func_params(anchor['onclick'])
          race_info['odds_param'] = params[1]

        
        race_info_div = soup.find("div",  attrs = {"class":"raceInfoAreaOutDiv"})
        race_class_1= race_info_div.find("div",  attrs = {"class":"raceSyubetsu"})
        race_class_2= race_info_div.find("div",  attrs = {"class":"raceJoken"})
        race_class_3= race_info_div.find("div",  attrs = {"class":"raceJuryou"})


        race_info['cond_age'] = race_class_1.get_text()
        class_info = race_class_2.get_text().split(" ")
        race_info['class'] =  class_info[-1]
        race_info['cond_additional'] =  class_info[0]
        race_info['cond_hande'] = race_class_3.get_text()
        

        course = race_info_div.find("div",  attrs = {"class":"raceKyoriTrack"})

        course_info = course.get_text().replace("\xa0"," ").replace("\u3000"," ").split(" ")
        race_info['distance'] = int(course_info[1].replace("m",""))
        race_info['course'] = course_info[2]

        weather = race_info_div.find("div",  attrs = {"class":"raceTenkou"})
        weather_info = weather.get_text().replace("\u3000", "").split(" ")
        race_info['weather'] = weather_info[0].split("：")[1]
        race_info['course_cond'] = weather_info[1].split("：")[1]

        mainList =  soup.find("table",  attrs = {"class":"mainList"})
        uma_list = mainList.find_all("tr")

        ret['umas'] = umas = []

        
        for i in range(1, len(uma_list)):
          info_list = uma_list[i].find_all("td")
          uma = {}
          umas.append(uma)
          for info_ent in info_list:
            class_name = info_ent['class']
            if "umameiCol" in class_name:
              uma['name'] = info_ent.get_text()
            elif "chakuCol" in class_name:
              try:
                uma['rank'] = int(info_ent.get_text())
              except :
                uma['rank_info'] =  info_ent.get_text()

            elif "umabanCol" in class_name:
              uma['uma_nam'] = int(info_ent.get_text())
            elif "seireiCol" in class_name:
              seirei = info_ent.get_text()
              uma['sex'] = re.sub(r"[0-9]*","",seirei)
              uma['age'] = int(re.sub(r"[牡|牝|せん]", "",seirei))
            elif 'hutanCol' in class_name:
              uma['hande'] = float(info_ent.get_text())
            elif "kigouCol" in class_name:
              mark = info_ent.get_text()
              if mark != "":
                uma['mark'] = mark
            elif "jocCol" in class_name:
              uma['jyokey'] = info_ent.get_text().strip('\n')
              anchor = info_ent.find("a")
              if anchor:
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                uma['jokey_param'] = params[1]

            elif "timeCol" in class_name:
              time = info_ent.get_text()
              try :
                uma['time'] = parse_race_time(time)
              except:
                pass
            elif "chakusaCol" in class_name:
              diff = info_ent.get_text()
              if diff != "":
                uma['diff'] = diff
            elif "suiteiCol" in class_name:
              agari = info_ent.get_text()
              if agari != "":
                uma['agari'] = int(float(agari) * 10)
            elif "bataiCol" in class_name:
              weight = info_ent.get_text().replace(" ","")
              if weight != "":
                try:
                  uma['weight'] = int(weight)
                except:
                  pass
            elif "zougenCol" in class_name:
              weight_diff = info_ent.get_text()
              if weight_diff != "":
                try : 
                  uma['weight_diff'] = int(weight_diff)
                except :
                  uma['weight_diff_info'] = weight_diff

            elif "choukyoCol" in class_name:
              uma['trainer'] = info_ent.get_text().strip('\n')
              anchor = info_ent.find("a")
              if anchor:
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                uma['trainer_param'] = params[1]

            elif "ninkiCol" in class_name:
              ninki = info_ent.get_text()
              if ninki != "":
                uma['ninki'] = int(ninki)

        time_info = soup.find("table",  attrs = {"class":"timeList"})
        if time_info:
          trs = time_info.find_all("tr")
          for tr in trs:
            th = tr.find("th")
            if th.get_text() == "ハロンタイム":
              td = tr.find("td")
              raps = td.get_text().replace(" ","").split("-")

              if len(raps) > 0 :
                race_info['raps'] = []
          
              for rap in raps: 
                race_info['raps'].append(float(rap))

            elif th.get_text() == "上り":
              td = tr.find("td")
              agaris = re.sub(r" +"," ", td.get_text()).replace("\u3000"," ").split(" - ")
              for agari in agaris[-2::1]:
                agari_splited = agari.split(" ")
                race_info[agari_splited[0]] = float(agari_splited[-1])

        possition_info = soup.find("table",  attrs = {"class":"cornerJuniList"})
        if possition_info:
          trs = possition_info.find_all("tr")
          if len(trs) > 0 :
            race_info['poss'] = {}
            for tr in trs :
              possition_tag = tr.find("th")
              possition = tr.find("td")
              race_info['poss'][possition_tag.get_text()] = possition.get_text()


        dividends = soup.find_all("table",  attrs = {"class":"haraimodoshiList"})
        if dividends:
          race_info['dividend'] = {}
          for dividend in dividends:
            trs = dividend.find_all("tr")
            for tr in trs :
              th = tr.find("th")
              if th :
                category = th.get_text()
                value = []
                race_info['dividend'][category] = value

              tds = tr.find_all("td")
              dividend_info = {}

              for td in tds :
                if "umabanCol" in td['class']:
                  dividend_info['tag'] = td.get_text()
                elif "haraimodoshiCol" in td['class']:
                  price = td.get_text()
                  if price != "":
                    dividend_info['price'] = int(price.replace("円","").replace(",",""))
                elif "ninkiCol" in td['class']:
                  ninki = td.get_text()
                  if ninki != "":
                    dividend_info['ninki'] = int(ninki.replace("番人気",""))

              if 'price' in dividend_info:
                value.append(dividend_info)

        return ret




