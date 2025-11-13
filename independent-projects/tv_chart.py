import pandas as pd
from bokeh.plotting import figure, save, output_file, show
from bokeh.layouts import column
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io.export import export_png
from datetime import timedelta
import os


# === Folder Path ===
folder_path = "YOUR FOLDER PATH HERE"

# === Loop Through All CSV Files ===
for file_name in os.listdir(folder_path):
    if not file_name.endswith(".csv"):
        continue  # skip non-CSV files

    file_path = os.path.join(folder_path, file_name)
    print(f"Processing: {file_name}")

    try:
        # === Load Data ===
        df = pd.read_csv(file_path, parse_dates=["Time"])
        df = df.sort_values("Time")

        # ---------- Column Detection and Momentum Calculation ----------
        col_bvb = next((c for c in df.columns if c.lower() in {"bvb", "bv b", "bullbear", "bull_vs_bear"}), None)
        col_call = next((c for c in df.columns if c.lower() in {"call"}), None)
        col_put  = next((c for c in df.columns if c.lower() in {"put"}), None)

        length = 10
        df["Momentum"] = df["close"] - df["close"].shift(length)
        col_mom = "Momentum"

        if len(df) > 2:
            dt = (df["Time"].diff().median() or pd.Timedelta(seconds=5))
        else:
            dt = pd.Timedelta(seconds=5)
        bar_w_ms = int(dt.total_seconds() * 1000 * 0.80)

        inc = df["close"] > df["open"]
        dec = df["open"] > df["close"]
        doj = df["open"].round(10) == df["close"].round(10)

        median_range = float((df["high"] - df["low"]).median() or 5)
        y_off = median_range * 0.35

        df["_time_str"] = df["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
        source = ColumnDataSource(df)

        BG = "#0b0e11"
        FG = "#d2d7e1"
        UP = "#15ff00"
        DN = "#ff2200"
        GRID = "#2a2f38"

        TOOLS = "xpan,xwheel_zoom,box_zoom,reset,save,crosshair"
        from bokeh.models import WheelZoomTool, PanTool

        # ---------- Main Chart ----------
        p_main = figure(
            x_axis_type="datetime",
            width=4000,               # <-- very wide fixed width
            height=420,
            background_fill_color=BG,
            border_fill_color=BG,
            tools=TOOLS,
            toolbar_location="above",
            active_drag="xpan",
            active_scroll="xwheel_zoom",
            title="TV Chart"
        )
        p_main.title.text_color = FG
        p_main.xaxis.major_label_text_color = FG
        p_main.yaxis.major_label_text_color = FG
        p_main.xgrid.grid_line_color = GRID
        p_main.ygrid.grid_line_color = GRID
        p_main.grid.grid_line_alpha = 0.35

        yzoom_main = WheelZoomTool(dimensions="height")
        ypan_main  = PanTool(dimensions="height")
        p_main.add_tools(yzoom_main, ypan_main)
        p_main.toolbar.active_scroll = yzoom_main

        p_main.segment(x0="Time", y0="high", x1="Time", y1="low",
                    source=source, color=FG, line_width=1)
        p_main.vbar(x=df["Time"][inc], width=bar_w_ms,
                    top=df["close"][inc], bottom=df["open"][inc],
                    fill_color=UP, line_color=UP)
        p_main.vbar(x=df["Time"][dec], width=bar_w_ms,
                    top=df["open"][dec], bottom=df["close"][dec],
                    fill_color=DN, line_color=DN)
        p_main.segment(df["Time"][doj], df["close"][doj],
                    df["Time"][doj], df["close"][doj],
                    color="#cccccc", line_width=2)

        if col_call:
            calls = df[df[col_call] == 1]
            p_main.triangle(x=calls["Time"], y=calls["low"] - y_off, size=8, color=UP)
        if col_put:
            puts = df[df[col_put] == 1]
            p_main.inverted_triangle(x=puts["Time"], y=puts["high"] + y_off, size=8, color=DN)

        # ---------- Momentum ----------
        p_mom = figure(
            x_axis_type="datetime",
            width=4000,
            height=140,
            x_range=p_main.x_range,
            tools=TOOLS,
            toolbar_location=None,
            background_fill_color=BG,
            border_fill_color=BG,
            title="Momentum"
        )
        p_mom.title.text_color = FG
        p_mom.xaxis.visible = False
        p_mom.yaxis.major_label_text_color = FG
        p_mom.xgrid.grid_line_color = GRID
        p_mom.ygrid.grid_line_color = GRID
        p_mom.grid.grid_line_alpha = 0.25

        yzoom_mom = WheelZoomTool(dimensions="height")
        ypan_mom  = PanTool(dimensions="height")
        p_mom.add_tools(yzoom_mom, ypan_mom)
        p_mom.toolbar.active_scroll = yzoom_mom

        p_mom.vbar(
            x=df["Time"],
            top=df[col_mom],
            width=bar_w_ms,
            line_color=None,
            fill_color=df[col_mom].apply(lambda x: UP if x >= 0 else DN)
        )
        p_mom.y_range.start = df[col_mom].min() * 1.2
        p_mom.y_range.end   = df[col_mom].max() * 1.2

        # ---------- BvB ----------
        p_bvb = figure(
            x_axis_type="datetime",
            width=4000,
            height=140,
            x_range=p_main.x_range,
            tools=TOOLS,
            toolbar_location=None,
            background_fill_color=BG,
            border_fill_color=BG,
            title="BvB"
        )
        p_bvb.title.text_color = FG
        p_bvb.yaxis.major_label_text_color = FG
        p_bvb.xaxis.major_label_text_color = FG
        p_bvb.xgrid.grid_line_color = GRID
        p_bvb.ygrid.grid_line_color = GRID
        p_bvb.grid.grid_line_alpha = 0.25

        yzoom_bvb = WheelZoomTool(dimensions="height")
        ypan_bvb  = PanTool(dimensions="height")
        p_bvb.add_tools(yzoom_bvb, ypan_bvb)
        p_bvb.toolbar.active_scroll = yzoom_bvb

        if col_bvb:
            b_pos = df[col_bvb].clip(lower=0)
            b_neg = df[col_bvb].clip(upper=0)
            p_bvb.vbar(x=df["Time"], top=b_pos, width=bar_w_ms,
                    line_color=None, fill_color=UP)
            p_bvb.vbar(x=df["Time"], top=b_neg, width=bar_w_ms,
                    line_color=None, fill_color=DN)

        # ---------- Layout & Output ----------
        # wrap inside a Div container to allow scroll bar
        from bokeh.models import Div
        from bokeh.layouts import column

        layout = column(p_mom, p_main, p_bvb)
        layout.sizing_mode = None  # disables auto resizing (keeps large width)

        # simpler: set fixed width and enable scrolling automatically
        p_mom.width = 1800
        p_main.width = 1800
        p_bvb.width = 1800

        
        p_main.height = 1000
        

        show(layout)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")
        continue


