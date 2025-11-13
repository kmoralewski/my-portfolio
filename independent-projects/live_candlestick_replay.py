from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd
import datetime, time, random

# Load or simulate your 1s data
df = pd.read_csv("YOUR CSV PATH HERE")
df["Time"] = pd.to_datetime(df["Time"])

# --- Data sources ---cd Charting
source_up = ColumnDataSource(data=dict(Time=[], open=[], high=[], low=[], close=[]))
source_down = ColumnDataSource(data=dict(Time=[], open=[], high=[], low=[], close=[]))
forming_source = ColumnDataSource(data=dict(Time=[], open=[], high=[], low=[], close=[]))  # live candle

# --- Chart setup ---
p = figure(x_axis_type="datetime", width=1200, height=600, title="Live 5s Candle Formation")
p.segment("Time", "high", "Time", "low", source=source_up, color="white")
p.segment("Time", "high", "Time", "low", source=source_down, color="white")

# historical candles
p.vbar("Time", width=4000, top="open", bottom="close", source=source_up,
       fill_color="#15ff00", line_color="#15ff00")
p.vbar("Time", width=4000, top="open", bottom="close", source=source_down,
       fill_color="#ff2200", line_color="#ff2200")

# forming (live) candle — semi-transparent
p.vbar("Time", width=4000, top="open", bottom="close", source=forming_source,
       fill_color="#aaaaaa", line_color="#cccccc", alpha=0.5)

# --- State ---
cur_index = [0]
buffer = []  # holds up to 5 rows per candle

def update():
    if cur_index[0] >= len(df):
        return

    row = df.iloc[cur_index[0]]
    buffer.append(row)
    cur_index[0] += 1

    buf = pd.DataFrame(buffer)
    o = buf.iloc[0]["open"]
    h = buf["high"].max()
    l = buf["low"].min()
    c = buf.iloc[-1]["close"]
    t = buf.iloc[0]["Time"]

    # show current forming candle (gray)
    forming_source.data = dict(Time=[t], open=[o], high=[h], low=[l], close=[c])

    # when 5 seconds pass, finalize it
    if len(buffer) == 5:
        final = dict(Time=[t], open=[o], high=[h], low=[l], close=[c])
        if c >= o:
            source_up.stream(final, rollover=500)
        else:
            source_down.stream(final, rollover=500)
        buffer.clear()

curdoc().add_root(p)
curdoc().add_periodic_callback(update, 1000)
curdoc().title = "Live 5s Candle Formation"
