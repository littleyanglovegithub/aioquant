# -*- coding:utf-8 -*-

# 使用本级文件夹
from aioquant.utils import logger
import os
import sys
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = ROOT_PATH.partition('\strategy')[0]
sys.path.append(ROOT_PATH)

from aioquant.platform.binance import BinanceRestAPI
from aioquant.utils import logger
from aioquant.tasks import SingleTask



class FirstStrategy:

    def __init__(self) -> None:
        access_key = "kZwlGBXF0WMNvcJWYt4tm3xWGxKtUomWaI5IctCtuNtyCoSJgirYub8ojsHC4hbV"
        secret_key = "jrnyYhXJl0cOhWvrsDhrxzCdkkviFnD7079GtjlLTQ0E9lskZ3xxy5sqz7RHgP9e"
        host = "https://api.binance.com"
        self._rest_api = BinanceRestAPI(host, access_key, secret_key)
        SingleTask.run(self.get_asset_infomation)
        pass

    async def get_asset_infomation(self):
        success, error = await self._rest_api.get_user_account()
        logger.info("success: ", success, caller=self)
        logger.info("error: ", error, caller=self)
        pass

    async def create_new_order(self):
        pass