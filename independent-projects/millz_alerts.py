import discord
import nest_asyncio
import time
from millzvars import *

nest_asyncio.apply()

class MyClient(discord.Client):
    

    async def on_ready(self):
        print(f'Lets get it.')
    
        

        

    async def on_message(self, message):
        #print(f'{message.content}')
        global spy, qqq, tsla, amd, aapl, amzn, msft, nvda, meta, goog
        global spy1, qqq1, tsla1, amd1, aapl1, amzn1, msft1, nvda1, meta1, goog1
        global spy2, qqq2, tsla2, amd2, aapl2, amzn2, msft2, nvda2, meta2, goog2
        global spy3, qqq3, tsla3, amd3, aapl3, amzn3, msft3, nvda3, meta3, goog3
        global spy4, qqq4, tsla4, amd4, aapl4, amzn4, msft4, nvda4, meta4, goog4
        global spy5, qqq5, tsla5, amd5, aapl5, amzn5, msft5, nvda5, meta5, goog5
        global spy6, qqq6, tsla6, amd6, aapl6, amzn6, msft6, nvda6, meta6, goog6
        global spy7, qqq7, tsla7, amd7, aapl7, amzn7, msft7, nvda7, meta7, goog7
        global spy8, qqq8, tsla8, amd8, aapl8, amzn8, msft8, nvda8, meta8, goog8
        global spy9, qqq9, tsla9, amd9, aapl9, amzn9, msft9, nvda9, meta9, goog9
        global mess1, mess2, mess3, mess4, mess5, mess6, mess7, mess8, mess0
        global es1, es2, es3, es4, es5, es6, es7, es8, es9, es10, es11, es12, es13, es14, es15, es16
        global nq1, nq2, nq3, nq4, nq5, nq6, nq7, nq8, nq9, nq10, nq11, nq12, nq13, nq14, nq15, nq16
        global nqd1, nqd2, nqd3, nqd4, nqd5, nqd6, nqd7, nqd8, nqd9, nqd10, nqd11, nqd12

        t = time.localtime()
        current_time = time.strftime("%D %H:%M:%S", t)

        nqpf = 'NQProfit.csv'
        espf = 'ESProfit.csv'

        nqa = 'NQAlert.csv'
        esa = 'ESAlert.csv'
        nqpos = 'NQPosition.csv'
        espos = 'ESPosition.csv'
        nq5a = 'NQ5A.csv'
        nqd = 'NQD.csv'

        nq3pf = 'NQ3Profit.csv'
        es3pf = 'ES3Profit.csv'
        
        nq3a = 'NQ3Alert.csv'
        es3a = 'ES3Alert.csv'


        if message.content.startswith('NQP'):
            nq6 = message.content.split()[1]
            nq7 = message.content.split()[2]
            nq8 = message.content.split()[3]
            mess1 = message.content
            with open(nqpf,"a") as outff:
                print(current_time, mess1, file=outff)

        if message.content.startswith('NQ5SA'):
            mess0 = message.content
            with open(nq5a,"a") as outff:
                print(current_time, mess0, file=outff)
        
        if message.content.startswith('ESP'):
            es6 = message.content.split()[1]
            es7 = message.content.split()[2]
            es8 = message.content.split()[3]
            mess2 = message.content
            with open(espf,"a") as outfff:
                print(current_time, mess2, file=outfff)     

        if message.content.startswith('NQA'):
            nq1 = message.content.split()[1]
            nq2 = message.content.split()[2]
            nq3 = message.content.split()[3]
            nq4 = message.content.split()[4]
            nq5 = message.content.split()[5]
            mess3 = message.content
            with open(nqa,"a") as outff:
                print(current_time, mess3, file=outff)
        
        if message.content.startswith('ESA'):
            es1 = message.content.split()[1]
            es2 = message.content.split()[2]
            es3 = message.content.split()[3]
            es4 = message.content.split()[4]
            es5 = message.content.split()[5]
            mess4 = message.content
            with open(esa,"a") as outfff:
                print(current_time, mess4, file=outfff) 

        if message.content.startswith('NQLongIn') or message.content.startswith('NQLongOut'):
            mess5 = message.content
            channel6 = client.get_channel("YOUR CHANNEL ID")
            await channel6.send(f"{current_time} {mess5}")
            with open(nqpos,"a") as outfff:
                print(current_time, mess5, file=outfff) 

        if message.content.startswith('NQShortIn') or message.content.startswith('NQShortOut'):
            mess6 = message.content
            channel6 = client.get_channel("YOUR CHANNEL ID")
            await channel6.send(f"{current_time} {mess6}")
            with open(nqpos,"a") as outfff:
                print(current_time, mess6, file=outfff) 

        if message.content.startswith('ESLongIn') or message.content.startswith('ESLongOut'):
            mess7 = message.content
            channel7 = client.get_channel("YOUR CHANNEL ID")  
            await channel7.send(f"{current_time} {mess7}")
            with open(espos,"a") as outfff:
                print(current_time, mess7, file=outfff) 

        
        if message.content.startswith('ESShortIn') or message.content.startswith('ESShortOut'):
            mess8 = message.content
            channel7 = client.get_channel("YOUR CHANNEL ID")  
            await channel7.send(f"{current_time} {mess8}")
            with open(espos,"a") as outfff:
                print(current_time, mess8, file=outfff) 

        if message.content.startswith('NQ3A'):
            nq12 = message.content.split()[1]
            nq13 = message.content.split()[2]
            nq14 = message.content.split()[3]
            nq15 = message.content.split()[4]
            nq16 = message.content.split()[5]
            mess8 = message.content
            with open(nq3a,"a") as outfff:
                print(current_time, mess8, file=outfff) 
        
        if message.content.startswith('NQ3P'):
            nq9 = message.content.split()[1]
            nq10 = message.content.split()[2]
            nq11= message.content.split()[3]
            mess9 = message.content
            with open(nq3pf,"a") as outff:
                print(current_time, mess9, file=outff)
        
        if message.content.startswith('ES3P'):
            es9 = message.content.split()[1]
            es10 = message.content.split()[2]
            es11 = message.content.split()[3]
            mess10 = message.content
            with open(es3pf,"a") as outfff:
                print(current_time, mess10, file=outfff)     

        
        if message.content.startswith('ES3A'):
            es12 = message.content.split()[1]
            es13 = message.content.split()[2]
            es14 = message.content.split()[3]
            es15 = message.content.split()[4]
            es16 = message.content.split()[5]
            mess12 = message.content
            with open(es3a,"a") as outfff:
                print(current_time, mess12, file=outfff) 

        
        if message.content.startswith('1SPY'):
            spy1 = message.content.split()[1]
            spy2 = message.content.split()[2]
            spy3 = message.content.split()[3]
            spy4 = message.content.split()[4]
            spy9 = message.content.split()[5]
        elif message.content.startswith('1QQQ'):
            qqq1 = message.content.split()[1]
            qqq2 = message.content.split()[2]
            qqq3 = message.content.split()[3]
            qqq4 = message.content.split()[4]
            qqq9 = message.content.split()[5]
        elif message.content.startswith('1TSLA'):
            tsla1 = message.content.split()[1]
            tsla2 = message.content.split()[2]
            tsla3 = message.content.split()[3]
            tsla4 = message.content.split()[4]
            tsla9 = message.content.split()[5]
        elif message.content.startswith('1AMD'):
            amd1 = message.content.split()[1]
            amd2 = message.content.split()[2]
            amd3 = message.content.split()[3]
            amd4 = message.content.split()[4]
            amd9 = message.content.split()[5]
        elif message.content.startswith('1AAPL'):
            aapl1 = message.content.split()[1]
            aapl2 = message.content.split()[2]
            aapl3 = message.content.split()[3]
            aapl4 = message.content.split()[4]
            aapl9 = message.content.split()[5]
        elif message.content.startswith('1AMZN'):
            amzn1 = message.content.split()[1]
            amzn2 = message.content.split()[2]
            amzn3 = message.content.split()[3]
            amzn4 = message.content.split()[4]
            amzn9 = message.content.split()[5]
        elif message.content.startswith('1MSFT'):
            msft1 = message.content.split()[1]
            msft2 = message.content.split()[2]
            msft3 = message.content.split()[3]
            msft4 = message.content.split()[4]
            msft9 = message.content.split()[5]
        elif message.content.startswith('1NVDA'):
            nvda1 = message.content.split()[1]
            nvda2 = message.content.split()[2]
            nvda3 = message.content.split()[3]
            nvda4 = message.content.split()[4]
            nvda9 = message.content.split()[5]
        elif message.content.startswith('1META'):
            meta1 = message.content.split()[1]
            meta2 = message.content.split()[2]
            meta3 = message.content.split()[3]
            meta4 = message.content.split()[4]
            meta9 = message.content.split()[5]
        elif message.content.startswith('1GOOG'):
            goog1 = message.content.split()[1]
            goog2 = message.content.split()[2]
            goog3 = message.content.split()[3]
            goog4 = message.content.split()[4]
            goog9 = message.content.split()[5]
        elif message.content.startswith('5SPY'):
            spy5 = message.content.split()[1]
            spy6 = message.content.split()[2]
            spy7 = message.content.split()[3]
            spy8 = message.content.split()[4]
        elif message.content.startswith('1QQQ'):
            qqq5 = message.content.split()[1]
            qqq6 = message.content.split()[2]
            qqq7 = message.content.split()[3]
            qqq8 = message.content.split()[4]
        elif message.content.startswith('5TSLA'):
            tsla5 = message.content.split()[1]
            tsla6 = message.content.split()[2]
            tsla7 = message.content.split()[3]
            tsla8 = message.content.split()[4]
        elif message.content.startswith('5AMD'):
            amd5 = message.content.split()[1]
            amd6 = message.content.split()[2]
            amd7 = message.content.split()[3]
            amd8 = message.content.split()[4]
        elif message.content.startswith('5AAPL'):
            aapl5 = message.content.split()[1]
            aapl6 = message.content.split()[2]
            aapl7 = message.content.split()[3]
            aapl8 = message.content.split()[4]
        elif message.content.startswith('5AMZN'):
            amzn5 = message.content.split()[1]
            amzn6 = message.content.split()[2]
            amzn7 = message.content.split()[3]
            amzn8 = message.content.split()[4]
        elif message.content.startswith('5MSFT'):
            msft5 = message.content.split()[1]
            msft6 = message.content.split()[2]
            msft7 = message.content.split()[3]
            msft8 = message.content.split()[4]
        elif message.content.startswith('5NVDA'):
            nvda5 = message.content.split()[1]
            nvda6 = message.content.split()[2]
            nvda7 = message.content.split()[3]
            nvda8 = message.content.split()[4]
        elif message.content.startswith('5META'):
            meta5 = message.content.split()[1]
            meta6 = message.content.split()[2]
            meta7 = message.content.split()[3]
            meta8 = message.content.split()[4]
        elif message.content.startswith('5GOOG'):
            goog5 = message.content.split()[1]
            goog6 = message.content.split()[2]
            goog7 = message.content.split()[3]
            goog8 = message.content.split()[4]          



        if message.content.startswith('NQD'):
            nqd1 = message.content.split()[1]
            nqd2 = message.content.split()[2]
            nqd3 = message.content.split()[3]
            nqd4 = message.content.split()[4]
            nqd5 = message.content.split()[5]
            nqd6 = message.content.split()[6]
            nqd7 = message.content.split()[7]
            nqd8 = message.content.split()[8]
            nqd9 = message.content.split()[9]
            nqd10 = message.content.split()[10]
            nqd11 = message.content.split()[11]
            nqd12 = message.content.split()[12]
            with open(nqd, "a") as outff:
                print(current_time, ",", nqd1, ",",nqd2, ",",nqd3, ",",nqd4, ",",nqd5, ",",nqd6, ",",nqd7, ",",nqd8, ",",nqd9, ",",nqd10, ",",nqd11, ",",nqd12, file=outff)
            

        if message.content.startswith('1Min'): 
            channel1 = client.get_channel("YOUR CHANNEL ID")
            channel2 = client.get_channel("YOUR CHANNEL ID")
            channel3 = client.get_channel("YOUR CHANNEL ID")
            channel4 = client.get_channel("YOUR CHANNEL ID")
            await channel1.send(f"{current_time} \n NQ1 {nq1} {nq2} {nq3} {nq4}, {nq5} \n {nq6}, {nq7}, {nq8} \n ES1 {es1}, {es2}, {es3}, {es4}, {es5} \n {es6}, {es7}, {es8}")
            await channel4.send(f"{current_time} \n NQ3 {nq12} {nq13} {nq14} {nq15}, {nq16} \n {nq9}, {nq10}, {nq11} \n ES3 {es12}, {es13}, {es14}, {es15}, {es16} \n {es9}, {es10}, {es11}")
            await channel2.send(f"\n{current_time}\nSPY [{spy9}]     [{spy1} : {spy2}]     [{spy3} : {spy4}] \n \nQQQ [{qqq9}]     [{qqq1} : {qqq2}]     [{qqq3} : {qqq4}] \n \nTSLA [{tsla9}]     [{tsla1} : {tsla2}]     [{tsla3} : {tsla4}] \n \nAMD [{amd9}]     [{amd1} : {amd2}]     [{amd3} : {amd4}] \n \nAAPL [{aapl9}]     [{aapl1} : {aapl2}]     [{aapl3} : {aapl4}] \n \nAMZN [{amzn9}]     [{amzn1} : {amzn2}]     [{amzn3} : {amzn4}] \n \nMSFT [{msft9}]     [{msft1} : {msft2}]     [{msft3} : {msft4}] \n \nNVDA [{nvda9}]     [{nvda1} : {nvda2}]     [{nvda3} : {nvda4}] \n \nMETA [{meta9}]     [{meta1} : {meta2}]     [{meta3} : {meta4}]\n \nGOOG [{goog9}]     [{goog1} : {goog2}]     [{goog3} : {goog4}] \n")
            await channel3.send(f"\n{current_time}\nSPY [{spy9}]     [{spy5} : {spy6}]     [{spy7} : {spy8}] \n \nQQQ [{qqq9}]     [{qqq5} : {qqq6}]     [{qqq7} : {qqq8}] \n \nTSLA [{tsla9}]     [{tsla5} : {tsla6}]     [{tsla7} : {tsla8}] \n \nAMD [{amd9}]     [{amd5} : {amd6}]     [{amd7} : {amd8}] \n \nAAPL [{aapl9}]     [{aapl5} : {aapl6}]     [{aapl7} : {aapl8}] \n \nAMZN [{amzn9}]     [{amzn5} : {amzn6}]     [{amzn7} : {amzn8}] \n \nMSFT [{msft9}]     [{msft5} : {msft6}]     [{msft7} : {msft8}] \n \nNVDA [{nvda9}]     [{nvda5} : {nvda6}]     [{nvda7} : {nvda8}] \n \nMETA [{meta9}]     [{meta5} : {meta6}]     [{meta7} : {meta8}]\n \nGOOG [{goog9}]     [{goog5} : {goog6}]     [{goog7} : {goog8}] \n")
            
        if message.content.startswith('1MIN'):

            print("____________________________________________________________________________")
            print("Time: ", current_time, "____________________________________________________")
            print("NQ|", nq1, nq2, "|", nq3, nq4, "|", "  ES|", es1, es2, " |", es3, es4, "|                          |")
            print("|", nq5, nq6, " |", nq7, nq8, "|", "   |", es5, es6, " |", es7, es8, "|                          |")
            print("SPY|", spy1, spy2, "|", spy3, spy4, "|", "  QQQ|", qqq1, qqq2, " |", qqq3, qqq4, "|                          |")
            print("|", spy5, spy6, " |", spy7, spy8, "|", "   |", qqq5, qqq6, " |", qqq7, qqq8, "|                          |")
            print("-          -")
            print("TSLA |", tsla1, tsla2, " |", tsla3, tsla4, " |", "  MSFT |", msft1, msft2, " |", msft3, msft4, " |")
            print("|", tsla5, tsla6, " |", tsla7, tsla8, " |", "   |", msft5, msft6, " |", msft7, msft8, "|                          |")  
            print("-          -")
            print("AMD  |", amd1, amd2, " |", amd3, amd4, " |", "  NVDA |", nvda1, nvda2, " |", nvda3, nvda4, " |")      
            print("|", amd5, amd6, " |", amd7, amd8, " |","     |", nvda5, nvda6, " |", nvda7, nvda8, "|                          |")
            print("-          -")
            print("AAPL |", aapl1, aapl2, " |", aapl3, aapl4, " |", "  META |", meta1, meta2, " |", meta3, meta4, " |")
            print("|", aapl5, aapl6, " |", aapl7, aapl8, " |", "     |", meta5, meta6, " |", meta7, meta8, "|                          |")
            print("-          -")
            print("AMZN |", amzn1, amzn2, " |", amzn3, amzn4, " |", "  GOOG |", goog1, goog2, " |", goog3, goog4, " |")
            print("|", amzn5, amzn6, " |", amzn7, amzn8, " |", "     |", goog5, goog6, " |", goog7, goog8, "|                          |")
            print("-          -")
            print("Time: ", current_time)
            print("____________________________________________________________________________")

            
        return (spy, qqq, tsla, amd, aapl, amzn, msft, nvda, meta, goog, 
                spy1, qqq1, tsla1, amd1, aapl1, amzn1, msft1, nvda1, meta1, goog1,
                spy2, qqq2, tsla2, amd2, aapl2, amzn2, msft2, nvda2, meta2, goog2,
                spy3, qqq3, tsla3, amd3, aapl3, amzn3, msft3, nvda3, meta3, goog3,
                spy4, qqq4, tsla4, amd4, aapl4, amzn4, msft4, nvda4, meta4, goog4,
                spy5, qqq5, tsla5, amd5, aapl5, amzn5, msft5, nvda5, meta5, goog5,
                spy6, qqq6, tsla6, amd6, aapl6, amzn6, msft6, nvda6, meta6, goog6,
                spy7, qqq7, tsla7, amd7, aapl7, amzn7, msft7, nvda7, meta7, goog7,
                spy8, qqq8, tsla8, amd8, aapl8, amzn8, msft8, nvda8, meta8, goog8,
                spy9, qqq9, tsla9, amd9, aapl9, amzn9, msft9, nvda9, meta9, goog9,
                es1, es2, es3, es4, es5, es6, es7, es8, es9, es10, es11, es12, es13, es14, es15, es16,
                nq1, nq2, nq3, nq4, nq5, nq6, nq7, nq8, nq9, nq10, nq11, nq12, nq13, nq14, nq15, nq16)
        

    


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)






client.run('(INPUT YOUR API KEY HERE)')

