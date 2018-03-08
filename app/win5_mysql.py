import sys

sys.path.append('../')

from jra import parser_win5_kaisai as prwk

import mysql.connector

use_network = True
param = 'pw17hde01201104241/18'
#param = 'pw17hde01201105011/75'

conn = mysql.connector.connect(
  host='localhost',
  port=3306,
  user='root',
  database='jra_try',
)
cur = conn.cursor()

while True:
    _parser = prwk.parser_win5_kaisai('/JRADB/access5.html',param)

    if use_network:
        kaisai = _parser.parse()
    else:
        args = sys.argv

        if len(args) < 2:
            print("Specify Test File Name")
            sys.exit()

        with open(args[1],'rb') as rfp:
            response_body = rfp.read().decode("'shift_jis'")
            kaisai = _parser.parse_html(response_body)


    if param == None:
        break

    print(kaisai)

    cur.execute("INSERT INTO win5_list VALUES (%s, %s)",
      [kaisai['date'].replace("年","/").replace("月","/").replace("日",""), kaisai['pay_back'] if 'pay_back' in kaisai else 0,]
    )
    conn.commit()

    if "next" in kaisai:
        param = kaisai['next']
    else:
        break

    #break

conn.close()

