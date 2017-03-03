import sys
import numpy
from functools import reduce

def optBet(lstMoneyRaw, lstSps, littleCoin, offsetCoinNum):
    if offsetCoinNum == 0:
        return lstMoneyRaw
    
    ajustMoney = littleCoin
    if offsetCoinNum < 0:
        ajustMoney = -ajustMoney

    besti = 0
    bestfc = sys.maxsize
    for i in range(0, len(lstMoneyRaw)):
        tempLstMoneyRaw = lstMoneyRaw[:]
        tempLstMoneyRaw[i] += ajustMoney
        earn = []
        for j in range(0, len(lstMoneyRaw)):
            earn.append(tempLstMoneyRaw[j] * lstSps[j])
        nearn = numpy.array(earn)
        tempfc = numpy.var(nearn)
        if bestfc > tempfc:
            besti = i
            bestfc = tempfc
    lstMoneyRaw[besti] += ajustMoney
    return optBet(lstMoneyRaw, lstSps, littleCoin, offsetCoinNum - ajustMoney // littleCoin)


tempSpStr = input("Input sps, use space to separate(like 2.1 1.8 ....): ")
sps = [float(sp) for sp in tempSpStr.split(' ')]

littleCoin = 100
tempCoin = input("Input little coin, default is 100: ")
if len(tempCoin) != 0:
    littleCoin = int(tempCoin)

moneyPart = []
for i in range(0, len(sps)):
    tempOtherSps = sps[0:i] + sps[i+1:len(sps)]
    moneyPart.append(reduce(lambda x , y : x * y, tempOtherSps))
print(moneyPart)

totalHave = input("Input total bean, default is 10000: ")
if len(totalHave) == 0:
    totalHave = 10000
else:
    totalHave = int(totalHave)

moneyRaw = [int(round(x * totalHave // sum(moneyPart) // littleCoin)) * littleCoin for x in moneyPart]

offsetCoinNum = (totalHave - sum(moneyRaw)) // littleCoin
money = optBet(moneyRaw, sps, littleCoin, offsetCoinNum)
print(money)
print("Bet total:", sum(money))

earn = [int(round(sps[i] * money[i])) for i in range(0, len(moneyRaw))]
print("Earn:", earn)
