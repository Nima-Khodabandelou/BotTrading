from strategy import strategy

'''
Abbreviations

tf:    time frame
nod:   number Of data (rows) extracted from csv file and used for calculation
gt:    global trend
lm:    local momentum
'''

path = "C:\\historical_data\\"
asset = 'SOLUSDT'
ts = ''
tf = '1m'
nod = 10000

[gt, lm1, lm2] = strategy(path, asset, ts, tf, nod)

