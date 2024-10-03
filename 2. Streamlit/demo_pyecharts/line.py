import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from streamlit_echarts import st_pyecharts


def render_basic_line_chart():
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("Merchant A", Faker.values())
        .add_yaxis("Merchant B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Line - Basic Example"))
    )
    st_pyecharts(c)


ST_LINE_DEMOS = {"Line: Basic Line": (render_basic_line_chart)}
