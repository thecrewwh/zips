# -*- coding: utf-8 -*-
import re
import time
from  resources.modules.client import get_html
global global_var,stop_all#global
global_var=[]
stop_all=0

 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
from  resources.modules import cache
from  resources.modules.furk_api import FurkAPI 
try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','non_rd']
Furk = FurkAPI()
import urllib,logging,base64,json
def to_utf8(obj):
    try:
        import copy
        if isinstance(obj, unicode):
            obj = obj.encode('utf-8', 'ignore')
        elif isinstance(obj, dict):
            obj = copy.deepcopy(obj)
            for key, val in obj.items():
                obj[key] = to_utf8(val)
        elif obj is not None and hasattr(obj, "__iter__"):
            obj = obj.__class__([to_utf8(x) for x in obj])
        else: pass
    except: pass
    return obj
    
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
def _seas_ep_query_list( season, episode):
        
        return ['s%02de%02d' % (season, episode),
                '%dx%02d' % (season, episode),
                '%02dx%02d' % (season, episode),
                '"season %d episode %d"' % (season, episode),
                '"season %02d episode %02d"' % (season, episode)]
def _search_name(tv_movie,year,season,episode,title):
        search_title = clean_file_name(to_utf8(title))
        search_title = search_title.replace(' ', '+')
        db_type = tv_movie
        if db_type == 'movie':
            pre_year=str(int(year) - 1)
            next_year=str(int(year) + 1)
            years = '{0}|+{1}+|+{2}' .format (pre_year, str(year),next_year )
            search_name = '@name+%s+%s' % (search_title, years)
        else:
           
            queries = _seas_ep_query_list(int(season), int(episode))
            search_name = '@name+%s+@files+%s+|+%s+|+%s+|+%s+|+%s' % (search_title, queries[0], queries[1], queries[2], queries[3], queries[4])
        return search_name

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    if Addon.getSetting("provider.furk")=='false':
        return []
    
    
  
    
    
    all_links=[]
    search_name = _search_name(tv_movie,str(show_original_year),season,episode,clean_name(original_title,1))
   
    files = Furk.search(search_name)
    
    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    }

    for items in files:
       if 'is_ready' in items:
           if items['is_ready']=='1':
           
            
            if stop_all==1:
                break
            title=items['name']
            if items['type']=='video':
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
                lk=items['url_pls']
                #head=urllib.urlencode(headers)
                #lk=lk+"|"+head
                size = float(int(items['size']))/1073741824
                max_size=int(Addon.getSetting("size_limit"))
                  
                if size<max_size:
                    all_links.append((title,lk,str(size),res))
               
                    global_var=all_links
    return global_var
        
    