from streamlit_echarts import st_echarts


def render_wordcloud():
    data = [
        {"name": name, "value": value}
        for name, value in [
            ("Life Resources", "999"),
            ("Heat Supply Management", "888"),
            ("Gas Quality", "777"),
            ("Domestic Water Management", "688"),
            ("Primary Water Supply Issues", "588"),
            ("Transportation", "516"),
            ("Urban Traffic", "515"),
            ("Environmental Protection", "483"),
            ("Real Estate Management", "462"),
            ("Urban and Rural Construction", "449"),
            ("Social Security and Welfare", "429"),
            ("Social Security", "407"),
            ("Cultural and Educational Management", "406"),
            ("Public Safety", "406"),
            ("Public Transportation Management", "386"),
            ("Taxi Operation Management", "385"),
            ("Heat Supply Management", "375"),
            ("City Appearance and Sanitation", "355"),
            ("Natural Resource Management", "355"),
            ("Dust Pollution", "335"),
            ("Noise Pollution", "324"),
        ]
    ]
    wordcloud_option = {"series": [{"type": "wordCloud", "data": data}]}
    st_echarts(wordcloud_option)


def render_liquidfill():
    liquidfill_option = {"series": [{"type": "liquidFill", "data": [0.6, 0.5, 0.4, 0.3]}]}
    st_echarts(liquidfill_option)


ST_EXTENSIONS_DEMOS = {
    "Extension: Wordcloud": (render_wordcloud),
    "Extension: Liquidfill": (render_liquidfill),
}
