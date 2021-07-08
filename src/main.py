# -*- coding:utf-8 -*-

# 使用本级文件夹
import os
import sys
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
print(ROOT_PATH)
ROOT_PATH = ROOT_PATH.partition('\src')[0]
print(ROOT_PATH)
sys.path.append(ROOT_PATH)
print(sys.path)

from aioquant import quant


def first_strategy():
    print("I'm here")
    from strategy.strategy1 import FirstStrategy
    FirstStrategy()

if __name__ == "__main__":
    config_name = "config.json"
    quant.start(config_name, first_strategy)