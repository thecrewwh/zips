# -*- coding: utf-8 -*-

'''
    Genesis Add-on
    Copyright (C) 2015 lambda

    -Mofidied by The Crew
    -Copyright (C) 2019 The Crew


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import random
import re
import urllib
import urlparse

from resources.lib.modules import client
from resources.lib.modules import utils


def request(url, check, close=True, redirect=True, error=False, proxy=None, post=None, headers=None, mobile=False, XHR=False, limit=None, referer=None, cookie=None, compression=True, output='', timeout='30'):
    try:
        r = client.request(url, close=close, redirect=redirect, proxy=proxy, post=post, headers=headers, mobile=mobile, XHR=XHR, limit=limit, referer=referer, cookie=cookie, compression=compression, output=output, timeout=timeout)
        if r is not None and error is not False: return r
        if check in str(r) or str(r) == '': return r

        proxies = sorted(get(), key=lambda x: random.random())
        proxies = sorted(proxies, key=lambda x: random.random())
        proxies = proxies[:3]

        for p in proxies:
            p += urllib.quote_plus(url)
            if post is not None:
                if isinstance(post, dict):
                    post = utils.byteify(post)
                    post = urllib.urlencode(post)
                p += urllib.quote_plus('?%s' % post)
            r = client.request(p, close=close, redirect=redirect, proxy=proxy, headers=headers, mobile=mobile, XHR=XHR, limit=limit, referer=referer, cookie=cookie, compression=compression, output=output, timeout='20')
            if check in str(r) or str(r) == '': return r
    except:
        pass


def geturl(url):
    try:
        r = client.request(url, output='geturl')
        if r is None: return r

        host1 = re.findall('([\w]+)[.][\w]+$', urlparse.urlparse(url.strip().lower()).netloc)[0]
        host2 = re.findall('([\w]+)[.][\w]+$', urlparse.urlparse(r.strip().lower()).netloc)[0]
        if host1 == host2: return r

        proxies = sorted(get(), key=lambda x: random.random())
        proxies = sorted(proxies, key=lambda x: random.random())
        proxies = proxies[:3]

        for p in proxies:
            p += urllib.quote_plus(url)
            r = client.request(p, output='geturl')
            if r is not None: return parse(r)
    except:
        pass


def parse(url):
    try: url = client.replaceHTMLCodes(url)
    except: pass
    try: url = urlparse.parse_qs(urlparse.urlparse(url).query)['u'][0]
    except: pass
    try: url = urlparse.parse_qs(urlparse.urlparse(url).query)['q'][0]
    except: pass
    return url


def get():
    return [

    'https://www.3proxy.us/index.php?hl=2e5&q=',
    'https://www.4proxy.us/index.php?hl=2e5&q=',
    'https://www.xxlproxy.com/index.php?hl=3e4&q=',
    'https://free-proxyserver.com/browse.php?b=20&u=',
    'https://proxite.net/browse.php?b=20&u=',
    'https://proxydash.com/browse.php?b=20&u=',
    'https://webproxy.stealthy.co/browse.php?b=20&u=',
    'https://sslpro.eu/browse.php?b=20&u=',
    'https://webtunnel.org/browse.php?b=20&u=',
    'https://proxycloud.net/browse.php?b=20&u=',
    'https://sno9.com/browse.php?b=20&u=',
    'https://www.onlineipchanger.com/browse.php?b=20&u=',
    'https://www.pingproxy.com/browse.php?b=20&u=',
    'https://www.ip123a.com/browse.php?b=20&u=',
    'https://buka.link/browse.php?b=20&u=',
    'https://zend2.com/open18.php?b=20&u=',
    'https://proxy.deals/browse.php?b=20&u=',
    'https://freehollandproxy.com/browse.php?b=20&u=',
    'https://proxy.rocks/browse.php?b=20&u=',
    'https://proxy.discount/browse.php?b=20&u=',
    'https://proxy.lgbt/browse.php?b=20&u=',
    'https://proxy.vet/browse.php?b=20&u=',
    'https://www.unblockmyweb.com/browse.php?b=20&u=',
    'https://onewebproxy.com/browse.php?b=20&u=',
    'https://pr0xii.com/browse.php?b=20&u=',
    'https://mlproxy.science/surf.php?b=20&u=',
    'https://www.prontoproxy.com/browse.php?b=20&u=',
    'https://fproxy.net/browse.php?b=20&u=',

    #'https://www.ruby-group.xyz/browse.php?b=20&u=',
    #'https://securefor.com/browse.php?b=20&u=',
    #'https://www.singleclick.info/browse.php?b=20&u=',
    #'https://www.socialcommunication.xyz/browse.php?b=20&u=',
    #'https://www.theprotected.xyz/browse.php?b=20&u=',
    #'https://www.highlytrustedgroup.xyz/browse.php?b=20&u=',
    #'https://www.medicalawaregroup.xyz/browse.php?b=20&u=',
    #'https://www.proxywebsite.us/browse.php?b=20&u=',
    'https://www.mybriefonline.xyz/browse.php?b=20&u=',
    'https://www.navigate-online.xyz/browse.php?b=20&u='

    ]


