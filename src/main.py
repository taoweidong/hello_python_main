# -*- coding: utf-8 -*-
from src.file_search import FileSearchTool

if __name__ == "__main__":
    directory = r"E:\GitHub\test"  # 替换为您要搜索的目录路径
    keyword = "npm"  # 替换为您要搜索的关键字
    file_types = (".txt", ".md")  # 替换为您要搜索的文件类型的元组，例如 (".txt", ".doc")

    file_search_tool = FileSearchTool(directory)
    search_results = file_search_tool.search_files(keyword, file_types)
    for result in search_results:
        file_search_tool.logger.info("ID: %s", result.id)
        file_search_tool.logger.info("文件名：%s", result.file_path)
        file_search_tool.logger.info("行号：%s", result.line_number)
        file_search_tool.logger.info("内容：%s", result.content)
        file_search_tool.logger.info("=" * 30)
