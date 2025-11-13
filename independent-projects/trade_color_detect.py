import discord,time,pyautogui,cv2
import asyncio
from datetime import datetime
import numpy as np

TOKEN = "-- Your Discord Bot Token Here --"
CHANNEL_ID = "Your channel ID"  # integer
RESTART_INTERVAL_SEC = 10   # 10 minutes

global move

intents = discord.Intents.default()
intents.message_content = True

async def run_bot_once():
    move = 0
    client = discord.Client(intents=intents)

    # region = {"top": 700, "left": 780, "width": 10, "height": 20}  # 4 window side trade
    region = {"top": 635, "left": 805, "width": 15, "height": 20}  # 4 window side trade


    def take_screenshot(region):
        screenshot = pyautogui.screenshot(region=region)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        return screenshot

    def detect_color(image):
        move = 0
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define red ranges
        lower_red1 = np.array([0, 70, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 70, 50])
        upper_red2 = np.array([180, 255, 255])

        # Define green range
        lower_green = np.array([40, 70, 50])
        upper_green = np.array([90, 255, 255])

        # Create masks
        red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)

        red_count = cv2.countNonZero(red_mask)
        green_count = cv2.countNonZero(green_mask)

        if red_count > green_count and red_count > 50:
            move = 2
            return move
        if green_count > red_count and green_count > 50:
            move = 1
            return move 

            
        

    async def trade():
        global run_trade 
        run_trade = True
        while run_trade:
            current_sec = time.localtime().tm_sec
            if current_sec == 58:
                img = take_screenshot((region['left'], region['top'], region['width'], region['height']))
                cv2.imwrite("latest_trade_region.png", img)  # Save screenshot
                move = detect_color(img)
                print("Trade Signal:", move)
                if move == 1 or move == 2:
                    break
                time.sleep(170)
        return move

    #times is a list of all start times of candles on the timeframe you are trading
    times = ["(INPUT YOUR TRADE TIMES HERE)"]  # e.g., "0930", "0945", etc.






    @client.event
    async def on_ready():
        print(f"[{datetime.now().strftime('%I:%M:%S %p')}] Bot ready, sending restart message.")
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send(f"Bot restarted at {datetime.now().strftime('%I:%M:%S %p')}")

        while True:
            
            t = time.localtime()
            start_hour = time.strftime("%H" , t)
            start_minute = time.strftime("%M" , t)
            start_seconds = time.strftime("%S" , t)
            check_time = start_hour + start_minute
            for i in range(len(times)):
                if check_time == times[i]:
                    print("Go: ", check_time)
                    move = await trade()
                    if move == 1:
                        await channel.send("Call")
                            
                    if move == 2:
                        await channel.send("Put")
            time.sleep(30)


   
        
    @client.event
    async def on_message(message):
        if message.content.startswith('Switch'):
            print("Got Message.")
            await client.close()  # Cleanly exit client after message

    await client.start(TOKEN)

async def main_loop():
    while True:
        await run_bot_once()
        # await asyncio.sleep(RESTART_INTERVAL_SEC)

asyncio.run(main_loop())
