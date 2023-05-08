from histDataPrep import BullBearMrks, initialDataConfig
from tech import ma, atr


path = "C:\\historical_data\\"
asset = 'SOLUSDT'
ts = ''
# tf: time frame
tf = '1m'
# nod: number Of data (rows) extracted from csv file and used for calculation
nod = 10000
(t, tInc, tDec, cc, ch, cl, ccDec, ccInc, coDec,
 coInc) = BullBearMrks(asset, tf, ts, path, nod)[0:10]
# ma_p: periods used for calculating moving averages
ma_p = [100, 130, 500]
# mas: all moving averages calculated for each MA period and stored in a list of lists
mas = ma(True, cc, ma_p)

atrp = 10
# gt: global trend defined as a slow moving average
gt = mas[2]
# lm: local momentum defined as a fast moving average
lm1 = mas[0]
lm2 = mas[1]



