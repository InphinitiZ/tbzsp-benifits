import sys
import numpy

def multiListSelp(lst):
    s = 1
    for i in lst:
        s *= i
    return s

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


sps = []
tempSp = float(input("Input sp, end with nonpositive number: "))
while tempSp > 0:
    sps.append(tempSp)
    tempSp = float(input("Input sp, end with nonpositive number: "))
littleCoin = 100
tempCoin = input("Input little coin, default is 100: ")
if len(tempCoin) != 0:
    littleCoin = int(tempCoin)

moneyPart = []

for i in range(0, len(sps)):
    tempOtherSps = sps[0:i] + sps[i+1:len(sps)]
    moneyPart.append(multiListSelp(tempOtherSps))
print(moneyPart)

totalHave = input("Input total bean, default is 10000: ")
if len(totalHave) == 0:
    totalHave = 10000
else:
    totalHave = int(totalHave)

moneyRaw = []
for x in moneyPart:
    moneyRaw.append(int(round(x * totalHave // sum(moneyPart) // littleCoin)) * littleCoin)

offsetCoinNum = (totalHave - sum(moneyRaw)) // littleCoin
money = optBet(moneyRaw, sps, littleCoin, offsetCoinNum)
print(money)
print("Bet total:", sum(money))

earn = []
for i in range(0, len(moneyRaw)):
    earn.append(int(round(sps[i] * money[i])))
print("Earn:", earn)
