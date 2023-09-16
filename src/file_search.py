# -*- coding: utf-8 -*-
import concurrent.futures
import hashlib
import os
import re

from src.logger_utils import FileSearchLogger


class FileSearchResult:
    def __init__(self, file_path, line_number, content):
        self.file_path = file_path
        self.line_number = line_number
        self.content = content
        self.id = self._generate_unique_id(os.path.basename(file_path), content)

    def _generate_unique_id(self, file_path, content):
        unique_id_str = file_path + content
        return hashlib.sha256(unique_id_str.encode()).hexdigest()


class FileSearchTool:
    def __init__(self, directory):
        self.directory = directory
        self.logger = FileSearchLogger.setup_logging()

    def search_files(self, keyword, file_types=None):
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for root, dirs, files in os.walk(self.directory):
                for file in files:
                    if file_types is None or file.endswith(file_types):
                        file_path = os.path.join(root, file)
                        executor.submit(self._process_file, file_path, keyword, results)
        return results

    def _process_file(self, file_path, keyword, results):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line_number, line in enumerate(lines, 1):
                    if isinstance(keyword, str):  # 字符串匹配模式
                        if keyword in line:
                            result_obj = FileSearchResult(file_path, line_number, line.strip())
                            results.append(result_obj)
                    elif isinstance(keyword, re.Pattern):  # 正则表达式匹配模式
                        if re.search(keyword, line):
                            result_obj = FileSearchResult(file_path, line_number, line.strip())
                            results.append(result_obj)
        except UnicodeDecodeError:
            self.logger.error("文件 %s 的编码异常，无法处理。", file_path)
        except Exception as e:
            self.logger.error("打开文件 %s 时发生错误：%s", file_path, str(e))
