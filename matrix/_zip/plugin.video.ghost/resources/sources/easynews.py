# -*- coding: utf-8 -*-
import re
import time,xbmc
from  resources.modules.client import get_html
global global_var,stop_all#global
global_var=[]
stop_all=0
import urllib,logging,base64,json
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    que=urllib.quote_plus
    url_encode=urllib.urlencode
else:
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus
from resources.modules import log
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
from  resources.modules import cache

try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','non_rd']
SORT = {'s1': 'relevance', 's1d': '-', 's2': 'dsize', 's2d': '-', 's3': 'dtime', 's3d': '-'}
SEARCH_PARAMS = {'st': 'adv', 'sb': 1, 'fex': 'mkv, mp4, avi, mpg, wemb', 'fty[]': 'VIDEO', 'spamf': 1, 'u': '1', 'gx': 1, 'pno': 1, 'sS': 3}
SEARCH_PARAMS.update(SORT)
# -*- coding: utf-8 -*-

import re
import datetime
import base64
try: from urllib import urlencode, quote # Python 2
except ImportError: from urllib.parse import urlencode, quote # Python 3
import json
def normalize(txt):
	import re
	txt = re.sub(r'[^\x00-\x7f]',r'', txt)
	return txt
def clean_file_name(s, use_encoding=False, use_blanks=True):
    try:
        hex_entities = [['&#x26;', '&'], ['&#x27;', '\''], ['&#xC6;', 'AE'], ['&#xC7;', 'C'],
                    ['&#xF4;', 'o'], ['&#xE9;', 'e'], ['&#xEB;', 'e'], ['&#xED;', 'i'],
                    ['&#xEE;', 'i'], ['&#xA2;', 'c'], ['&#xE2;', 'a'], ['&#xEF;', 'i'],
                    ['&#xE1;', 'a'], ['&#xE8;', 'e'], ['%2E', '.'], ['&frac12;', '%BD'],
                    ['&#xBD;', '%BD'], ['&#xB3;', '%B3'], ['&#xB0;', '%B0'], ['&amp;', '&'],
                    ['&#xB7;', '.'], ['&#xE4;', 'A'], ['\xe2\x80\x99', '']]
        special_encoded = [['"', '%22'], ['*', '%2A'], ['/', '%2F'], [':', ','], ['<', '%3C'],
                            ['>', '%3E'], ['?', '%3F'], ['\\', '%5C'], ['|', '%7C']]
        
        special_blanks = [['"', ' '], ['*', ' '], ['/', ' '], [':', ''], ['<', ' '],
                            ['>', ' '], ['?', ' '], ['\\', ' '], ['|', ' '], ['%BD;', ' '],
                            ['%B3;', ' '], ['%B0;', ' '], ["'", ""], [' - ', ' '], ['.', ' '],
                            ['!', ''], [';', ''], [',', '']]
        s = batch_replace(s, hex_entities)
        if use_encoding:
            s = batch_replace(s, special_encoded)
        if use_blanks:
            s = batch_replace(s, special_blanks)
        s = s.strip()
    except: pass
    return s
def get_release_quality(release_name, release_link=None):
	quality = 'default'
	try:
		try: release_name = release_name.encode('utf-8')
		except: pass
		try:
			fmt = replace_html_codes(release_name)
			fmt = unquote(fmt)
			fmt = fmt.lower()
			fmt = re.sub(r'[^a-z0-9]+', ' ', fmt)
			fmt = fmt + ' '
		except:
			fmt = str(release_name)
		if any(i in fmt for i in CAM): quality = 'CAM'
		elif any(i in fmt for i in SCR): quality = 'SCR'
		elif any(i in fmt for i in TELE): quality = 'TELE'
		elif any(i in fmt for i in RES_4K): quality = '4K'
		elif any(i in fmt for i in RES_1080): quality = '1080p'
		elif any(i in fmt for i in RES_720): quality = '720p'
		elif any(i in fmt for i in RES_SD): quality = 'SD'
	except: pass
	if quality == 'default':
		if release_link:
			try:
				try: release_link = release_link.encode('utf-8')
				except: pass
				fmt = release_link.lower()
				fmt = re.sub(r'[^a-z0-9]+', ' ', fmt)
				fmt = fmt + ' '
				if any(i in fmt for i in CAM): quality = 'CAM'
				elif any(i in fmt for i in SCR): quality = 'SCR'
				elif any(i in fmt for i in TELE): quality = 'TELE'
				elif any(i in fmt for i in RES_4K): quality = '4K'
				elif any(i in fmt for i in RES_1080): quality = '1080p'
				elif any(i in fmt for i in RES_720): quality = '720p'
				elif any(i in fmt for i in RES_SD): quality = 'SD'
			except: pass
		else: pass
	if quality == 'default': quality = 'SD'
	return quality
def get_file_info(url):
	try: url = url.encode('utf-8')
	except: pass
	try:
		url = replace_html_codes(url)
		url = unquote(url)
		url = url.lower()
		url = re.sub(r'[^a-z0-9]+', ' ', url)
		url = url + ' '
	except:
		url = str(url)
	info = ''
	if any(i in url for i in [' h 265 ', ' h256 ', ' x265 ', ' hevc ']):
		info += '[B]HEVC[/B] |'
	if ' hi10p ' in url:
		info += ' HI10P |'
	if ' 10bit ' in url:
		info += ' 10BIT |'
	if ' 3d ' in url:
		info += ' 3D |'
	if any(i in url for i in [' bluray ', ' blu ray ']):
		info += ' BLURAY |'
	if any(i in url for i in [' bd r ', ' bdr ', ' bd rip ', ' bdrip ', ' br rip ', ' brrip ']):
		info += ' BD-RIP |'
	if any(i in url for i in [' remux ', ' bdremux ', ' bd remux ']):
		info += ' REMUX |'
	if any(i in url for i in [' dvdrip ', ' dvd rip ']):
		info += ' DVD-RIP |'
	if any(i in url for i in [' dvd ', ' dvdr ', ' dvd r ']):
		info += ' DVD |'
	if any(i in url for i in [' webdl ', ' web dl ', ' web ', ' web rip ', ' webrip ']):
		info += ' WEB |'
	if ' hdtv ' in url:
		info += ' HDTV |'
	if ' sdtv ' in url:
		info += ' SDTV |'
	if any(i in url for i in [' hdrip ', ' hd rip ']):
		info += ' HDRIP |'
	if any(i in url for i in [' uhdrip ', ' uhd rip ']):
		info += ' UHDRIP |'
	if any(i in url for i in [' hdr ', ' hdr10 ', ' dolby vision ', ' hlg ']):
		info += ' HDR |'
	if ' imax ' in url:
		info += ' IMAX |'
	if any(i in url for i in [' ac3 ', ' ac 3 ']):
		info += ' AC3 |'
	if ' aac ' in url:
		info += ' AAC |'
	if ' aac5 1 ' in url:
		info += ' AAC | 5.1 |'
	if any(i in url for i in [' dd ', ' dolby ', ' dolbydigital ', ' dolby digital ']):
		info += ' DD |'
	if any(i in url for i in [' truehd ', ' true hd ']):
		info += ' TRUEHD |'
	if ' atmos ' in url:
		info += ' ATMOS |'
	if any(i in url for i in [' ddplus ', ' dd plus ', ' ddp ', ' eac3 ', ' eac 3 ']):
		info += ' DD+ |'
	if ' dts ' in url:
		info += ' DTS |'
	if any(i in url for i in [' hdma ', ' hd ma ']):
		info += ' HD.MA |'
	if any(i in url for i in [' hdhra ', ' hd hra ']):
		info += ' HD.HRA |'
	if any(i in url for i in [' dtsx ', ' dts x ']):
		info += ' DTS:X |'
	if any(i in url for i in [' dd5 1 ', ' dd5 1ch ']):
		info += ' DD | 5.1 |'
	if any(i in url for i in [' ddp5 1 ', ' ddp5 1ch ']):
		info += ' DD+ | 5.1 |'
	if ' opus ' in url:
		info += ' OPUS |'
	if any(i in url for i in [' 5 1 ', ' 5 1ch ', ' 6ch ']):
		info += ' 5.1 |'
	if any(i in url for i in [' 7 1 ', ' 7 1ch ', ' 8ch ']):
		info += ' 7.1 |'
	if ' korsub ' in url:
		info += ' HC-SUBS |'
	if any(i in url for i in [' subs ', ' subbed ', ' sub ']):
		info += ' SUBS |'
	if any(i in url for i in [' dub ', ' dubbed ', ' dublado ']):
		info += ' DUB |'
	info = info.rstrip('|')
	return info
class EasyNewsSource:
    def __init__(self):
        self.scrape_provider = 'easynews'
        self.title_filter = get_setting('%s.title_filter' % self.scrape_provider) == 'true'
        self.sources = []

    def results(self, info):
        log.warning('info::')
        log.warning(info)
        try:
            self.title = info.get('title')
            self.search_title = clean_file_name(self.title)
            self.db_type = info.get('db_type')
            self.year = info.get('year')
            self.years = '%s,%s,%s' % (str(int(self.year - 1)), self.year, str(int(self.year + 1)))
            self.season = info.get('season')
            self.episode = info.get('episode')
            search_name = self._search_name()
            files = EasyNewsAPI().search(search_name)
            
            
            aliases = json.loads(info.get('aliases', []))
            try: self.aliases = [i['title'] for i in aliases]
            except: self.aliases = []
            def _process():
                for item in files:
                    try:
                        file_name = normalize(item['name'])
                        if self.title_filter:
                            if not check_title(self.title, file_name, self.aliases, self.year, self.season, self.episode): continue
                        URLName = clean_file_name(file_name).replace('html', ' ').replace('+', ' ').replace('-', ' ')
                        url_dl = item['url_dl']
                        size = float(int(item['rawSize']))/1073741824
                        details = get_file_info(file_name)
                        video_quality = get_release_quality(file_name, url_dl)
                        source_item = {'name': file_name,
                                        'URLName': URLName,
                                        'quality': video_quality,
                                        'size': size,
                                        'size_label': '%.2f GB' % size,
                                        'extraInfo': details,
                                        'url_dl': url_dl,
                                        'id': url_dl,
                                        'local': False,
                                        'direct': True,
                                        'source': self.scrape_provider,
                                        'scrape_provider': self.scrape_provider}
                        yield source_item
                    except Exception as e:
                        log.warning('Error in Easynews:'+str(e))
            self.sources = list(_process())
        except Exception as e:
            from modules.utils import logger
            logger('FEN easynews scraper Exception', str(e))
        
        return self.sources

    def _search_name(self):
        if self.db_type == 'movie': search_name = '"%s" %s' % (self.search_title, self.years)
        else: search_name = '%s S%02dE%02d' % (self.search_title,  int(self.season), int(self.episode))
        return search_name

    def to_bytes(self, num, unit):
        unit = unit.upper()
        if unit.endswith('B'): unit = unit[:-1]
        units = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']
        try: mult = pow(1024, units.index(unit))
        except: mult = sys.maxint
        return int(float(num) * mult)
def to_utf8(obj):
    try:
        if isinstance(obj, unicode):
            obj = obj.encode('utf-8', 'ignore')
        elif isinstance(obj, dict):
            import copy
            obj = copy.deepcopy(obj)
            for key, val in obj.items():
                obj[key] = to_utf8(val)
        elif obj is not None and hasattr(obj, "__iter__"):
            obj = obj.__class__([to_utf8(x) for x in obj])
        else: pass
    except: pass
    return obj

get_setting=Addon.getSetting
set_setting=Addon.setSetting
_cache = cache

SORT = {'s1': 'relevance', 's1d': '-', 's2': 'dsize', 's2d': '-', 's3': 'dtime', 's3d': '-'}
SEARCH_PARAMS = {'st': 'adv', 'sb': 1, 'fex': 'mkv, mp4, avi, mpg, wemb', 'fty[]': 'VIDEO', 'spamf': 1, 'u': '1', 'gx': 1, 'pno': 1, 'sS': 3}
SEARCH_PARAMS.update(SORT)

def import_easynews():
    if get_setting('easynews.api_version') == '0':
        return EasyNewsAPI()
    else:
        return EasyNewsAPIv3()

class EasyNewsAPI:
    def __init__(self):
        self.base_url = 'https://members.easynews.com'
        self.search_link = '/2.0/search/solr-search/advanced'
        self.username = get_setting('easynews.user')
        self.password = get_setting('easynews.password')
        self.moderation = 1 if get_setting('easynews_moderation') == 'true' else 0
        self.auth = self._get_auth()
        self.account_link = 'https://account.easynews.com/editinfo.php'
        self.usage_link = 'https://account.easynews.com/usageview.php'
        self.timeout = 40.0
        self.base_get = self._get
        self.base_process = self._process_files
        self.base_resolver = self.resolver

    def _get_auth(self):
        try:
            auth = 'Basic ' + base64.b64encode('%s:%s' % (self.username, self.password))
        except:
            user_info = '%s:%s' % (self.username, self.password)
            user_info = user_info.encode('utf-8')
            auth = 'Basic ' + base64.b64encode(user_info).decode('utf-8')
        return auth

    def search(self, query):
        search_url, params = self._translate_search(query)
        
        results = self.base_get(search_url, params)
        files = to_utf8(self.base_process(results))
        
        return files

    def account(self):
        try:
            from bs4 import BeautifulSoup
            account_html = self._get(self.account_link)
            if account_html == None or account_html == '': raise Exception()
            account_html = BeautifulSoup(account_html, "html.parser")
            account_html = account_html.find_all('form', id='accountForm')[0]
            account_html = account_html.find_all('table', recursive=False)[0]
            account_html = account_html.find_all('tr', recursive=False)
            usage_html = self._get(self.usage_link)
            if usage_html == None or usage_html == '': raise Exception()
            usage_html = BeautifulSoup(usage_html, "html.parser")
            usage_html = usage_html.find_all('div', class_='table-responsive')[0]
            usage_html = usage_html.find_all('table', recursive=False)[0]
            usage_html = usage_html.find_all('tr', recursive=False)
            return account_html, usage_html
        except Exception:
            pass

    def _process_files(self, files):
        def _process():
            for item in files:
                try:
                    post_hash, size, post_title, ext, duration = item['0'], item['4'], item['10'], item['11'], item['14']
                    checks = [False] * 5
                    if 'alangs' in item and item['alangs'] and 'eng' not in item['alangs']: checks[1] = True
                    if re.match('^\d+s', duration) or re.match('^[0-5]m', duration): checks[2] = True
                    if 'passwd' in item and item['passwd']: checks[3] = True
                    if 'virus' in item and item['virus']: checks[4] = True
                    if 'type' in item and item['type'].upper() != 'VIDEO': checks[5] = True
                    if any(checks):
                        continue
                    stream_url = down_url + quote('/%s/%s/%s%s/%s%s' % (dl_farm, dl_port, post_hash, ext, post_title, ext))
                    file_name = post_title
                    file_dl = stream_url + '|Authorization=%s' % (quote(self.auth))
                    result = {'name': file_name,
                              'size': size,
                              'rawSize': item['rawSize'],
                              'url_dl': file_dl,
                              'version': 'version2',
                              'full_item': item}
                    yield result
                except: pass
        down_url = files.get('downURL')
        dl_farm = files.get('dlFarm')
        dl_port = files.get('dlPort')
        files = files.get('data', [])
        results = list(_process())
        return results

    def _process_files_v3(self, results):
        def _process():
            for item in files:
                try:
                    post_hash, size, post_title, ext, duration, sig = item['hash'], item['bytes'], item['filename'], item['extension'], item['runtime'], item['sig']
                    checks = [False] * 5
                    if 'alang' in item and item['alang'] and 'eng' not in item['alang']: checks[1] = True
                    if re.match('^\d+s', duration) or re.match('^[0-5]m', duration): checks[2] = True
                    if 'passwd' in item and item['passwd']: checks[3] = True
                    if 'virus' in item and item['virus']: checks[4] = True
                    if 'type' in item and item['type'].upper() != 'VIDEO': checks[5] = True
                    if any(checks):
                        continue
                    url_dl = self.stream_url % (post_hash, ext, post_title, sid, sig)
                    result = {'name': post_title,
                              'size': size,
                              'rawSize': size,
                              'url_dl': url_dl,
                              'version': 'version3',
                              'full_item': item}
                    yield result
                except: pass
        files = results.get('data', [])
        sid = results.get('sid')
        results = list(_process())
        return results

    def _translate_search(self, query):
        params = SEARCH_PARAMS
        params['pby'] = 100
        params['safeO'] = self.moderation
        params['gps'] = params['sbj'] = query
        url = self.base_url + self.search_link
        return url, params

    def _get(self, url, params={}):
        headers = {'Authorization': self.auth}
        response = get_html(url, params=params, headers=headers).content()
        try: return to_utf8(json.loads(response))
        except: return to_utf8(response)

    def _get_v3(self, url, params={}):
        headers = {'Authorization': self.auth}
        response = get_html(url, params=params, headers=headers).content()
        response = re.compile(self.regex,re.DOTALL).findall(response)[0]
        response = response + '}'
        try: return to_utf8(json.loads(response))
        except: return to_utf8(response)

    def resolve_easynews(self, url_dl):
        return self.base_resolver(url_dl)

    def resolver(self, url_dl):
        return url_dl

    def resolver_v3(self, url_dl):
        headers = {'Authorization': self.auth}
        stream_url = get_html(url_dl, headers=headers, stream=True).url()
        
        resolved_link = stream_url + '|Authorization=%s' % (quote(self.auth))
        return resolved_link








def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'video',
       
        'Accept-Language': 'en-US,en;q=0.9',
     
    }
    if tv_movie=='movie':
        info={'tmdb_id': id, 'season': '', 'tvdb_id': u'None', 'imdb_id': '', 'ep_name': None, 'year': int(show_original_year), 'aliases': '[]', 'episode': '', 'language': u'en', 'title': original_title, 'db_type': 'movie', 'premiered': show_original_year}
        
    else:
        info={'tmdb_id': id, 'season': season, 'tvdb_id': u'None', 'imdb_id': '', 'ep_name': None, 'year': int(show_original_year), 'aliases': '[]', 'episode': episode, 'language': u'en', 'title': original_title, 'db_type': 'tv', 'premiered': show_original_year}
    a=EasyNewsSource().results(info)
    log.warning(json.dumps(a))
    max_size=int(Addon.getSetting("size_limit"))
    for items in a:
        
        size=items['size']
        title=items['name']
        if '4k' in title:
            res='2160'
        elif '2160' in title:
              res='2160'
        elif '1080' in title:
              res='1080'
        elif '720' in title:
              res='720'
        elif '480' in title:
              res='480'
        elif '360' in title:
              res='360'
        else:
              res='HD'
        link=items['url_dl']
        all_lk_data={}
        all_lk_data['link']=link
        all_lk_data['headers']=headers
        all_lk_data['cookie']=EasyNewsAPI().auth
        
        if size<max_size:
          
           all_links.append((title,json.dumps(all_lk_data),str(size),res))
       
           global_var=all_links
    
   

    
    return global_var
        
    