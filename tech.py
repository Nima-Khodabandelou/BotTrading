def atr(ch, cl, cc, cnd, period):
    '''This function calculates ATR indicator.'''
    # tr: True Range
    tr = []
    for i in range(cnd, cnd - period, -1):
        tr.append(max(ch[i] - cl[i], abs(ch[i] - cc[i-1]),
                      abs(cl[i] - cc[i-1])))

    atr = sum(tr)/period
    return atr


def average(data, Period):
    '''This function calculates average value of a series.'''
    ave = sum([data[i] for i in range(Period)])/Period

    return ave


def ma(useMA, cc1h, periods):
    '''This function calculates moving average vector of given data for
    different periods.'''
    nod = len(cc1h)
    if useMA is True:
        ma_vecs = [[] for i in range(len(periods))]
        for j in range(len(ma_vecs)):
            for i in range(periods[j], nod):
                # mean = average(cc1h[i: i - periods[j]: -1], periods[j])
                mean = average(cc1h[i - periods[j]: i], periods[j])
                ma_vecs[j].append(mean)
    else:
        ma_vecs = [0, 0, 0]

    return ma_vecs
