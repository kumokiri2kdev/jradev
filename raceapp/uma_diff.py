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


    axis_win = win_data['odds'][axis - 1]

    print('軸 : [{}] : {}'.format(axis, axis_win['name']))
    print(' - 単勝 : {}'.format(axis_win['odds']['win']))
    print(' - 複勝 : {} - {}'.format(axis_win['odds']['fuku_min'], axis_win['odds']['fuku_max']))

    summary = 0

    for i in range(axis - 1):
        #print(uma_data['odds'][i]['matrix'][axis - i - 1 - 1])
        odds = uma_data['odds'][i]['matrix'][axis - i - 1 - 1]['odds']
        #print('{} - {} : {}'.format(i + 1,  axis, odds))
        summary = summary + odds

    if len(uma_data['odds']) > (axis - 1):
        for matrix in uma_data['odds'][axis - 1]['matrix']:
            #print(matrix)
            #print('{} - {} : {}'.format(axis, matrix['number'], matrix['odds']))
            summary = summary + matrix['odds']

    avg = summary / (len(win_data['odds']) - 1)
    avg = round(avg, 1)
    print(' - 馬蓮平均 : {}'.format(avg))

    

for i, uma in enumerate(win_data['odds']):
    check_uma(i + 1)

