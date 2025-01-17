from streamlit_echarts import st_echarts


def render_custom_funnel():
    option = {
        "title": {"text": "Funnel Chart", "subtext": "Purely Fictional"},
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
        "toolbox": {
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            }
        },
        "legend": {"data": ["Display", "Click", "Visit", "Inquiry", "Order"]},
        "series": [
            {
                "name": "Expected",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "label": {"formatter": "{b} Expected"},
                "labelLine": {"show": False},
                "itemStyle": {"opacity": 0.7},
                "emphasis": {"label": {"position": "inside", "formatter": "{b} Expected: {c}%"}},
                "data": [
                    {"value": 60, "name": "Visit"},
                    {"value": 40, "name": "Inquiry"},
                    {"value": 20, "name": "Order"},
                    {"value": 80, "name": "Click"},
                    {"value": 100, "name": "Display"},
                ],
            },
            {
                "name": "Actual",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "maxSize": "80%",
                "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                "emphasis": {"label": {"position": "inside", "formatter": "{b} Actual: {c}%"}},
                "data": [
                    {"value": 30, "name": "Visit"},
                    {"value": 10, "name": "Inquiry"},
                    {"value": 5, "name": "Order"},
                    {"value": 50, "name": "Click"},
                    {"value": 80, "name": "Display"},
                ],
                "z": 100,
            },
        ],
    }
    st_echarts(option, height="500px")


ST_FUNNEL_DEMOS = {
    "Funnel: Customized funnel": (render_custom_funnel),
}

