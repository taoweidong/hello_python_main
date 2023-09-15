import concurrent.futures
import hashlib
import logging
import os


class FileSearchResult:
    def __init__(self, file_path, line_number, content):
        self.file_path = file_path
        self.line_number = line_number
        self.content = content
        self.id = self._generate_unique_id(os.path.basename(file_path), content)

    def _generate_unique_id(self, file_path, content):
        unique_id_str = file_path + content
        return hashlib.sha256(unique_id_str.encode()).hexdigest()


class FileSearchLogger:
    @staticmethod
    def setup_logging():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # 创建并配置控制台处理程序
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        return logger


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
                    if keyword in line:
                        result_obj = FileSearchResult(file_path, line_number, line.strip())
                        results.append(result_obj)
        except UnicodeDecodeError:
            self.logger.error("文件 %s 的编码异常，无法处理。", file_path)
        except Exception as e:
            self.logger.error("打开文件 %s 时发生错误：%s", file_path, str(e))


def main():
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


if __name__ == "__main__":
    main()
