import pandas as pd
import time

prof_high = []
prof_low = []
pos_al = []
prof_al = []
prof_pos = []

start_time = time.time()


t = time.localtime()
date = time.strftime("%D", t)


data= pd.read_csv("-- YOUR FILE PATH HERE --")

timee = data.Time.tolist()
openn = data.open.tolist()
high = data.high.tolist()
low = data.low.tolist()
close = data.close.tolist()
call = data.Call.tolist()
put = data.Put.tolist()

#High and Low of plays
#ald = high and low calculation 0 = no, 1 = yes (default 1)
#ent = entry adjustment amount (0.00 = no adjustment)

def alerthl(ald, ent):
    long = 0
    short = 0
    i = 0
    entry = 0.00
    high_all = 0.00
    low_all = 0.00
    for i in range(len(call)):
        if call[i] == 1:
            entry = openn[i + 1] + ent
            long = 1
            high_all = high[i + 1]
            low_all = low[i + 1]
            prof_pos.append("C")
        if long == 1:
            if high[i] > high_all:
                high_all = high[i]
            if low[i] < low_all:
                low_all = low[i]
            if call[i - 1] > 1 and call[i] == 0 and long == 1 and ald == 1:
                long = 0
                d = high_all - entry
                e = entry - low_all
                e = (e - e) - e
                prof_high.append(d)
                prof_low.append(e)
                high_all = 0.00
                low_all = 0.00
        if put[i] == 1:
            entry = openn[i + 1] + ent
            short = 1
            high_all = high[i + 1]
            low_all = low[i + 1]
            prof_pos.append("P")
        if short == 1:
            if high[i] > high_all:
                high_all = high[i]
            if low[i] < low_all:
                low_all = low[i]
            if put[i - 1] > 1 and put[i] == 0 and short == 1 and ald == 1:
                short = 0
                e = entry - high_all
                d = entry - low_all
                prof_high.append(d)
                prof_low.append(e)
                high_all = 0.00
                low_all = 0.00
    # return prof, pos

#Profit Calculation
#als = stop loss calculation 0 = no, 1 = yes
#alt = take profit calculation 0 = no, 1 = yes
#altd = daily exit calculation 0 = no, 1 = yes (default 1)
#tp = take profit amount (0.00 = no tp)
#sl = stop loss amount (0.00 = no sl)
#ent = entry adjustment amount (0.00 = no adjustment)
#prof = list to store profits
#pos = list to store position details

def alert(als, alt, ald, tp, sl, ent, prof, pos):
    long = 0
    short = 0
    hi = lo = stop = entry = profit = 0.00

    for i in range(len(call) - 1):  
        # Long Entry
        if call[i] == 1:
            entry = openn[i + 1] + ent
            stop = entry - sl
            hi = entry + tp
            long = 1
            pos.append(timee[i] + " EL")

        # Long Exit
        if long == 1:
            if low[i + 1] < stop and als == 1:  
                long = 0
                profit = -sl
                prof.append(profit)
                pos.append(timee[i] + " " + str(profit) + " S")
            elif high[i + 1] >= hi and alt == 1:  
                long = 0
                profit = tp -0.25
                prof.append(profit)
                pos.append(timee[i] + " " + str(profit) + " T")
            elif call[i] >= 1 and call[i + 1] == 0 and ald == 1:  
                long = 0
                profit = close[i + 1] - entry
                prof.append(profit)
                pos.append(timee[i + 1] + " " + str(profit) + " D")

        # Short Entry
        if put[i] == 1:
            entry = openn[i + 1] + ent
            stop = entry + sl
            lo = entry - tp
            short = 1
            pos.append(timee[i] + " ES")

        # Short Exit
        if short == 1:
            if high[i + 1] > stop and als == 1:  
                short = 0
                profit = -sl
                prof.append(profit)
                pos.append(timee[i] + " " + str(profit) + " S")
            elif low[i + 1] <= lo and alt == 1:  
                short = 0
                profit = tp -0.25
                prof.append(profit)
                pos.append(timee[i] + " " + str(profit) + " T")
            elif put[i] >= 1 and put[i + 1] == 0 and ald == 1:
                short = 0
                profit = entry - close[i + 1]
                prof.append(profit)
                pos.append(timee[i + 1] + " " + str(profit) + " D")

    # return prof, pos


alerthl(1, 0.00)
alert(0, 0, 1, 0.00, 0.00, 0.00, prof = prof_al, pos = pos_al)



prof_sum_al = sum(prof_al)
mo_al = prof_sum_al * 20

print("Al", prof_sum_al, " You would have made $", mo_al)

ccount = 0
pcount = 0
for i in range(len(call)):
    if call[i] == 2:
        ccount = ccount + 1
    elif put[i] == 2:
        pcount = pcount + 1

print("AL", prof_al, len(prof_al))
print("-------------------------------------------------------")

# # of long and short plays
print("Long ", ccount)
print("Short ", pcount)

daily_totals = []
total = 0.00

for i in range(len(prof_al)):
    total = total + prof_al[i]
    daily_totals.append(total)
print("Daily totals: ", daily_totals)



print("Prof_High: ", prof_high)
list.sort(prof_high)
print("Prof_High Sorted: ", prof_high)
print("Prof_Low: ", prof_low)
list.sort(prof_low)
print("Prof_low Sorted: ", prof_low)
print("Sum: ", sum(prof_low))


    

end_time = time.time()
total_time = end_time - start_time
print(total_time)