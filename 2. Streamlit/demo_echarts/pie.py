from streamlit_echarts import st_echarts


def render_pie_simple():
    options = {
        "title": {
            "text": "Source of user visits to a certain site",
            "subtext": "Purely fictional",
            "left": "center",
        },
        "tooltip": {"trigger": "item"},
        "legend": {
            "orient": "vertical",
            "left": "left",
        },
        "series": [
            {
                "name": "Source of visits",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1048, "name": "Search engine"},
                    {"value": 735, "name": "Direct access"},
                    {"value": 580, "name": "Email marketing"},
                    {"value": 484, "name": "Affiliate ads"},
                    {"value": 300, "name": "Video ads"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options,
        height="600px",
    )


def render_pie_donutradius():
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "Source of visits",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {
                    "borderRadius": 10,
                    "borderColor": "#fff",
                    "borderWidth": 2,
                },
                "label": {"show": False, "position": "center"},
                "emphasis": {"label": {"show": True, "fontSize": "40", "fontWeight": "bold"}},
                "labelLine": {"show": False},
                "data": [
                    {"value": 1048, "name": "Search engine"},
                    {"value": 735, "name": "Direct access"},
                    {"value": 580, "name": "Email marketing"},
                    {"value": 484, "name": "Affiliate ads"},
                    {"value": 300, "name": "Video ads"},
                ],
            }
        ],
    }
    st_echarts(
        options=options,
        height="500px",
    )


def render_nightingale_rose_diagram():
    option = {
        "legend": {"top": "bottom"},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": False},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "series": [
            {
                "name": "Area mode",
                "type": "pie",
                "radius": [50, 250],
                "center": ["50%", "50%"],
                "roseType": "area",
                "itemStyle": {"borderRadius": 8},
                "data": [
                    {"value": 40, "name": "rose 1"},
                    {"value": 38, "name": "rose 2"},
                    {"value": 32, "name": "rose 3"},
                    {"value": 30, "name": "rose 4"},
                    {"value": 28, "name": "rose 5"},
                    {"value": 26, "name": "rose 6"},
                    {"value": 22, "name": "rose 7"},
                    {"value": 18, "name": "rose 8"},
                ],
            }
        ],
    }
    st_echarts(
        options=option,
        height="600px",
    )


ST_PIE_DEMOS = {
    "Pie: Simple Pie": (render_pie_simple),
    "Pie: Doughnut Chart": (render_pie_donutradius),
    "Pie: Nightingale Rose Diagram": (render_nightingale_rose_diagram),
}
