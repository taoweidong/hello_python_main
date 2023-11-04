# !/usr/bin/env python
# -*- coding:utf-8 -*-
# https://www.cnblogs.com/shouke/p/16975025.html
from dataclasses import dataclass
import os
import re
import pandas as pd
from concurrent.futures import ProcessPoolExecutor


@dataclass
class MatchInfo:
    file_name: str
    line_number: int
    line_text: str


class FileParser:
    def __init__(self, root_path, match_str):
        self.root_path = root_path
        self.match_str = match_str
        self.matches = []

    def parse_file(self, file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if re.search(self.match_str, line):
                    match_info = MatchInfo(file_path, i + 1, line.strip())
                    self.matches.append(match_info)

    def parse_directory(self):
        file_paths = []
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                file_paths.append(os.path.join(root, file))

        with ProcessPoolExecutor() as executor:
            executor.map(self.parse_file, file_paths)

    def write_to_excel(self, excel_path):
        df = pd.DataFrame([(m.file_name, m.line_number, m.line_text) for m in self.matches],
                          columns=['文件名', '行号', '匹配信息'])
        df.to_excel(excel_path, index=False)


# 使用示例
root_path = '/path/to/directory'
match_str = r'regex_pattern'
excel_path = '/path/to/output/excel.xlsx'

parser = FileParser(root_path, match_str)
parser.parse_directory()
parser.write_to_excel(excel_path)
