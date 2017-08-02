import requests
from lxml import html
import os

amount = 1

for p in range(1,303):
    url = 'http://www.mzitu.com/zipai/comment-page-' + str(p) + '/#comments'

    r = requests.get(url).content
    s = html.fromstring(r)

    link = s.xpath('//li[@class="comment byuser comment-author-abu bypostauthor odd alt thread-odd thread-alt depth-1"]/div/p/img/@src')
    n = 1
    for l in link:
        try:
            filename = '%s.jpg' % (amount)
            print('正在下载图片--第{}页/第{}张|总共第{}'.format(p,n,amount))
            with open(filename, 'wb') as f:
                f.write(requests.get(l).content)
                n = n + 1
                amount = amount + 1
        except:
            pass
