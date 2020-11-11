# -*- coding=utf-8 -*-
from jdlogger import logger
from urllib.parse import unquote
'''
测试 https://c0.3.cn/stock?skuId=100003406321&area=19_1607_4773_0&venderId=1000000946&buyNum=1&choseSuitSkuIds=&cat=9192,9197,12588&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery4291064
请看教程寻找自己的url
'''
url = 'https://c0.3.cn/stocks?callback=jQuery8871615&type=getstocks&skuIds=67824255573%2C68072485536%2C68072485537%2C10023258449437%2C10023258449436%2C10023258449435%2C68072485535%2C10023258449438%2C68072485538%2C10023258449440%2C10023258449439%2C68072485539%2C69299739429%2C10023258449442%2C69299739430%2C10023258449441%2C68072485540%2C68072485541%2C10023258449444%2C10023258449443&area=1_2800_2851_0&_=1603683218818'
skuId = url.split('skuIds=')[1].split('&')[0]
area = url.split('area=')[1].split('&')[0]
logger.info('你的area是[ %s ]，链接的商品id是[ %s ]', area, unquote(skuId))
