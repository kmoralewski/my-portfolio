from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Button, Slider, Div
from bokeh.plotting import figure
from bokeh.layouts import column, row
import pandas as pd

#Command to run the bokeh server:

# python -m bokeh serve --show csv_replay.py


# Load your historical data
df = pd.read_csv("YOUR CSV FILE PATH HERE")

df["Time"] = pd.to_datetime(df["Time"])

# --- Candle Width ---
if len(df) > 1:
    avg_gap = (df["Time"].iloc[1] - df["Time"].iloc[0]).total_seconds() * 1000
else:
    avg_gap = 10_000
bar_width = avg_gap * 0.8

# --- Sources ---
source_up = ColumnDataSource(data=dict(Time=[], open=[], high=[], low=[], close=[]))
source_down = ColumnDataSource(data=dict(Time=[], open=[], high=[], low=[], close=[]))
trades = ColumnDataSource(data=dict(Time=[], Price=[], Type=[], Color=[]))
sma9_source = ColumnDataSource(data=dict(Time=[], sma9=[]))
sma21_source = ColumnDataSource(data=dict(Time=[], sma21=[]))

# --- Chart Setup ---
p = figure(x_axis_type="datetime", title="Trading Playback Simulator",
           width=1500, height=800, background_fill_color="#111")
p.segment("Time", "high", "Time", "low", source=source_up, color="white")
p.segment("Time", "high", "Time", "low", source=source_down, color="white")

p.vbar(x="Time", width=bar_width, top="open", bottom="close",
       source=source_up, fill_color="#15ff00", line_color="#15ff00")
p.vbar(x="Time", width=bar_width, top="open", bottom="close",
       source=source_down, fill_color="#ff2200", line_color="#ff2200")


# Buy/Sell markers (triangles)
p.scatter(
    x="Time",
    y="Price",
    source=trades,
    marker="triangle",
    size=30,
    fill_color="Color",
    line_color="Color",
    alpha=0.8
)

# --- Variables ---
cur_index = [0]
callback_id = [None]
active_trade = [None]
trade_log = []

# --- Core Functions ---
def draw_until(index):
    subset = df.iloc[:index + 1]
    up = subset[subset["close"] >= subset["open"]]
    down = subset[subset["close"] < subset["open"]]
    source_up.data = dict(Time=up["Time"], open=up["open"], high=up["high"], low=up["low"], close=up["close"])
    source_down.data = dict(Time=down["Time"], open=down["open"], high=down["high"], low=down["low"], close=down["close"])
    subset["sma9"] = subset["close"].rolling(9).mean()
    subset["sma21"] = subset["close"].rolling(21).mean()
    sma9_source.data = dict(Time=subset["Time"], sma9=subset["sma9"])
    sma21_source.data = dict(Time=subset["Time"], sma21=subset["sma21"])

def update():
    if cur_index[0] < len(df) - 1:
        cur_index[0] += 1
        draw_until(cur_index[0])
    else:
        stop_playback()

# --- Controls ---
def start_playback():
    if callback_id[0] is None:
        callback_id[0] = curdoc().add_periodic_callback(update, speed_slider.value)
        play_button.label = "⏸ Pause"

def stop_playback():
    if callback_id[0] is not None:
        curdoc().remove_periodic_callback(callback_id[0])
        callback_id[0] = None
        play_button.label = "▶️ Play"

def toggle_play():
    if callback_id[0] is None:
        start_playback()
    else:
        stop_playback()

def reset_playback():
    stop_playback()
    cur_index[0] = 0
    for src in [source_up, source_down, sma9_source, sma21_source]:
        src.data = {k: [] for k in src.data.keys()}
    trades.data = dict(Time=[], Price=[], Type=[])
    trade_log.clear()
    update_stats()

# --- Trading Actions ---
def place_trade(trade_type):
    if cur_index[0] >= len(df):
        return
    price = df.iloc[cur_index[0]]["close"]
    time = df.iloc[cur_index[0]]["Time"]
    color = "green" if trade_type == "Buy" else "red"

    new = dict(Time=[time], Price=[price], Type=[trade_type], Color=[color])
    trades.stream(new)
    trade_log.append((trade_type, price))
    update_stats()

def update_stats():
    pnl = 0
    open_trade = None
    open_side = None

    for t, price in trade_log:
        # Open new trade
        if open_trade is None:
            open_trade = price
            open_side = t
        else:
            # Close long
            if open_side == "Buy" and t == "Sell":
                pnl += price - open_trade
                open_trade = None
                open_side = None
            # Close short
            elif open_side == "Sell" and t == "Buy":
                pnl += open_trade - price
                open_trade = None
                open_side = None

    trade_count = len(trade_log)
    pnl_text.text = f"<b>Trades:</b> {trade_count} &nbsp;&nbsp; <b>PnL:</b> {pnl:.2f}"


# --- Buttons ---
play_button = Button(label="▶️ Play", width=90, button_type="success")
reset_button = Button(label="🔁 Reset", width=90, button_type="warning")
buy_button = Button(label="🟢 Buy", width=90, button_type="primary")
sell_button = Button(label="🔴 Sell", width=90, button_type="danger")
speed_slider = Slider(title="Speed (ms per bar)", start=50, end=2000, step=50, value=300)
pnl_text = Div(text="<b>Trades:</b> 0 &nbsp;&nbsp; <b>PnL:</b> 0.00", width=400, height=20)

play_button.on_click(toggle_play)
reset_button.on_click(reset_playback)
buy_button.on_click(lambda: place_trade("Buy"))
sell_button.on_click(lambda: place_trade("Sell"))
speed_slider.on_change("value", lambda attr, old, new: (stop_playback(), start_playback()) if callback_id[0] else None)

# --- Layout ---
layout = column(p, row(play_button, buy_button, sell_button, reset_button, speed_slider), pnl_text)
curdoc().add_root(layout)
curdoc().title = "Trading Playback Simulator"