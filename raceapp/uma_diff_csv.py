import os
import json


dir = '../test/tmp/20171029/東京/11/'

def get_latest(category):
    files = os.listdir(dir + category + '/')
    return files[-1]

file = get_latest('win')
with open(dir + 'win/' + file, 'rt') as rfp:
    win_data = json.load(rfp)

file = get_latest('uma')
with open(dir + 'uma/' + file, 'rt') as rfp:
    uma_data = json.load(rfp)

def check_uma(axis):
    summary = 0
    axis_win = win_data['odds'][axis - 1]
    odds_list = ""
    for i in range(axis - 1):
        #print(uma_data['odds'][i]['matrix'][axis - i - 1 - 1])
        odds = uma_data['odds'][i]['matrix'][axis - i - 1 - 1]['odds']
        #print('{} - {} : {}'.format(i + 1,  axis, odds))
        odds_list += str(odds) + ','
        summary = summary + odds

    odds_list += ','

    if len(uma_data['odds']) > (axis - 1):
        for matrix in uma_data['odds'][axis - 1]['matrix']:
            #print(matrix)
            #print('{} - {} : {}'.format(axis, matrix['number'], matrix['odds']))
            odds_list += str(matrix['odds']) + ','
            summary = summary + matrix['odds']

    avg = summary / (len(win_data['odds']) - 1)
    avg = round(avg, 1)
    odds_list = str(axis) + ',' + axis_win['name'] + ',' + str(axis_win['odds']['win']) + ',' +  str(avg) + ',' + odds_list
    print(odds_list)


names = ""
for i, uma in enumerate(win_data['odds']):
    names += win_data['odds'][i]['name'] + ','
    check_uma(i + 1)

print(names)

