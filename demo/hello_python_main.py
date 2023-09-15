"""Main module."""
import logging

from src import Test

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    print("*" * 100)
    i = 0
    while i < 100:
        logging.info('我爱我的老婆............我的老婆是个小可爱')
        i += 1
    print("*" * 100)
    test = Test()
    test.out()
