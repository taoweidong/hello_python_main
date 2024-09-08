# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


# 1. 定义抽象类
class DataProcessor(ABC):

    # 模板方法，定义算法骨架
    def process(self):
        self.load_data()
        self.process_data()
        self.save_data()

    # 这些方法可以由子类实现具体行为
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


# 2. 具体类1 - 处理CSV数据
class CSVDataProcessor(DataProcessor):

    def load_data(self):
        print("从CSV文件中加载数据...")

    def process_data(self):
        print("处理CSV数据...")

    def save_data(self):
        print("将处理后的数据保存到CSV文件中...")


# 3. 具体类2 - 处理数据库数据
class DatabaseDataProcessor(DataProcessor):

    def load_data(self):
        print("从数据库中加载数据...")

    def process_data(self):
        print("处理数据库数据...")

    def save_data(self):
        print("将处理后的数据保存到数据库中...")


# 使用示例
if __name__ == "__main__":
    print("CSV数据处理:")
    csv_processor = CSVDataProcessor()
    csv_processor.process()
    print("*" * 20)
    print("\n数据库数据处理:")
    db_processor = DatabaseDataProcessor()
    db_processor.process()
