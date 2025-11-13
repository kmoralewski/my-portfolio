# my-portfolio
Repository of my projects from my BS in Software Development and individual work

# DeVry University Projects

Contains a collection of academic projects completed during my BS in Software Development at DeVry University.

## Files
-**/major-project** - Projects built with multiple languages.
	- Car Sale Inventory Tracker:
		- C++ checkout system and inventory tracker for a car dealership
		- Allows the user to choose their vehicle and available upgrades
		- Software Used: Visual Studio
		- Languages Used: C++
	- GB Systems:
		- Group project that I worked on alone due to inproper communication from assigned team
		- Includes entire lifecycle from documentation to working program
		- Software Used: Visual Studio, MySQL
		- Languages Used: VB.NET, SQL
	- Moralewski Landscaping:
		- Java GUI application for a landscaping checkout form
		- Logs customer orders and keeps a record of all transactions using MySQL database.
		- Software Used: NetBeans IDE, MySQL
		- Languages Used: Java, SQL
	- Perfect Pet Finder:
		- Group project creating documentation only for a pet finder app
		- Includes all software requirements and diagrams
-**/mini-projects** - Fundamental practice in multiple languages.
	-Includes projects in C#, C++, Java, and a machine learning experiment

# Independent Projects

This repository contains a collection of projects I created myself with the assistance of AI. AI was used to expand on ideas, conduct research, test functions, debugging, and iteration. The tools allowed me to experiment with numerous different scenarios quickly while learning new methods and libraries in Python. 

## Files
- chartanalysis.py
	- Stock chart analyzer that takes screenshots of live charts 
	- Copies screenshots into an AI chatbot application for analysis
- click_windows.py
	- Simple use of pyautogui to click on trading windows periodically to avoid a timeout
- live_candlestick_replay.py
	- Live candlestick replay using Bokeh and tick data
	- Allows adjustment for any timeframe 
- millz_alerts.py
	- This was my first use of the Discord API to send and receive messages with a bot token
	- Receives webhook stock data for multiple tickers from Tradingview and writes it to a file 
- MillzTrader.png
	- Indicator created to find trading setups by following trends and momentum breaks
	- Works on all timeframes with proper risk management
- mod_assist_gui.py
	- Whatnot moderator GUI assistant for sending size announcements during live shows
	- Includes buttons for all sizes and messages for certain actions
- morning_setup.py
	- Simple pyautogui script to move all my trading windows into their positions before market open
- news_scraper.py
	- Web scraper for stock related news from a X account.
	- Writes new posts to csv and sends to discord channel
- profit_calc.py
	- Profit calculator for any ticker using csv data 
	- Adjustments include any take profit, any stop loss, and any ticker
	- Prints profits and max drawdown for all plays
- sim_trader.py
	- Simulated trading with Bokeh using csv data
	- Includes buy and sell buttons with profit tracker
	- Easier to use compared to trading platforms bar replay simulated trading
- tesseract_trader.py
	- This was my first use of pytesseract and allowed me expand its use into my other scripts
	- Checks parts of the screen for a change from 0 to 1 where 1 initiates a trade entry
	- A change back to 0 before candle close will initiate a trade exit
- tos_excel.py
	- Stock data writer using Thinkorswim's Excel addon
	- Uses pytesseract to extract price values 
- trade_color_detect.py
	- Trade detector using screenshots and numpy for chart analysis
	- Initates trade entry or close based on color detected
- trading_gui_8.py
	- GUI trader for 8 acoounts 
	- Includes buttons for long entries, short entries, and exits
- TrendAlert.png
	- Indicator created to follow trends between multiple tickers intraday 
	- Two versions are available with options of tracking 8 tickers or 40 tickers
	- Works on all timeframes
- tv_chart.py
	- Price chart visualization using Bokeh 
	- Shows candlesticks, momentum, and volume of anytime timeframe from csv data
- whatnot_order_csv.py
	- Csv order management for whatnot sellers
	- Uses pytesseract to extract order information and writes it to a file
	
