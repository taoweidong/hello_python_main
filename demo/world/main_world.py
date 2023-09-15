from io import BytesIO

import plotly.graph_objects as go
from docxtpl import DocxTemplate


def get_line_image(x, y):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, text=y, textposition="top center", mode="lines+markers"))
    image_io = BytesIO()
    fig.write_image(image_io, format="jpeg")
    return image_io


# 初始化模板处理对象
tpl = DocxTemplate("./示例模板文件.docx")

# 图表静态文件对象调用上面的示例plotly方法生成
line_charts = get_line_image(x=["一班", "二班", "三班"], y=["75", "80", "82"])

# 待填充的示例字典数据，其中key对应word模板中的填充名，图片需要调用InlineImage类
context = {
    "average": 80,
    "class": "三年2班",
    "table": [{"name": "小红", "gender": "男", "grade": 80},
              {"name": "小白", "gender": "男", "grade": 79},
              {"name": "小黑", "gender": "女", "grade": 81}],
    # "line_image": InlineImage(tpl, line_charts, width=Mm(164), height=Mm(82.5)),

}
# 开始渲染context数据到模板文件中
tpl.render(context=context)
# 保存：这里依然可以写入的ByteIO对象，因为后端不需要保存文件，你也依然可以根据需要使用save('a.docx')的方式保存最终文件到本地
# file_io = BytesIO()
tpl.save("示例结果文档.docx")
