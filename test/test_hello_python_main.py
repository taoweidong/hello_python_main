#!/usr/bin/env python

"""Tests for `src` package."""
import sys
import unittest

from loguru import logger


# logger.add(
#     sys.stdout,
#     level="INFO",
#     format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
# )


class TestHello_python_main(unittest.TestCase):
    """Tests for `src` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        list_data = [12, 34, 6, 7, 89]
        for i in list_data:
            # logging.info(i)
            logger.info(i)
        for index, value in enumerate(list_data):
            logger.info(f"{index}---{value}")
