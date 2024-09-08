# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List

from loguru import logger


# 1. 定义策略接口
class Strategy(ABC):
    @abstractmethod
    def execute(self, data: List[int]) -> None:
        pass


# 2. 具体策略类

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        # 升序排序
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)  # 降序排序


class ConcreteStrategyC(Strategy):
    def execute(self, data) -> List[int]:
        return list(set(data))  # 去重


# 3. 上下文类
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data: list):
        return self._strategy.execute(data)


if __name__ == '__main__':
    input_data = [5, 2, 9, 1, 5, 6]

    context = Context(ConcreteStrategyA())
    logger.info(f"升序排序：" + str(context.execute_strategy(input_data)))
    # 动态切换为降序排序策略
    context.set_strategy(ConcreteStrategyB())
    logger.info("降序排序:" + str(context.execute_strategy(input_data)))

    # 切换为去重策略
    context.set_strategy(ConcreteStrategyC())
    logger.info("去重后数据:" + str(context.execute_strategy(input_data)))
