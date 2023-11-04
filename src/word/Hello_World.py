# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2023/8/2 23:01
from flask import Flask
from docx import Document

app = Flask(__name__)


@app.route('/generate_document')
def generate_document():
    template_path = 'path_to_template/template.docx'  # 替换为实际的模板文件路径

    # 加载模板文档
    doc = Document(template_path)

    # 访问和修改模板文档的内容
    for paragraph in doc.paragraphs:
        if '<<placeholder>>' in paragraph.text:
            paragraph.text = paragraph.text.replace('<<placeholder>>', '替换文本')

    # 生成输出文档
    output_path = 'path_to_output/output.docx'  # 替换为输出文档的路径
    doc.save(output_path)

    return '文档生成成功！'


if __name__ == '__main__':
    app.run()
