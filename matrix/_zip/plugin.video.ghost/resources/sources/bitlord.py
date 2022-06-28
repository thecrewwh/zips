# -*- coding: utf-8 -*-
import re
import time

global global_var,stop_all#global
global_var=[]
stop_all=0
from  resources.modules.client import get_html
 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
from  resources.modules import cache
from resources.modules import  PTN
try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib,logging,base64,json

def _get_token_and_cookies( url):
    headers = {
        'authority': 'bitlordsearch.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'dnt': '1',
        
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://bitlordsearch.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
       
        
        
    }
    token=''
    x,cook = get_html(url,get_cookies=True,headers=headers).content()
    
    regex='token: (.+?)\n'
    m=re.compile(regex).findall(x)
    
    regex="var %s = '(.+?)'"%m[0]
    m2=re.compile(regex).findall(x)
    token=m2[0]
    regex=">%s \+= '(.+?)'"%m[0]
    m3=re.compile(regex).findall(x)
    for itt in m3:
        token+=itt
    cookies = ''
    for cookie in cook:
        cookies += '%s=%s;' % (cookie, cook[cookie])
    return (token,cookies)
    
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    url='https://bitlordsearch.com'
    token,cookies=_get_token_and_cookies( url)
    
    #headers = {
    #    'x-request-token': token,
    #    'cookie': cookies
    #}
    
    headers = {
        'authority': 'bitlordsearch.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'dnt': '1',
        'x-request-token': token,
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://bitlordsearch.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
       
        
        'cookie': cookies,
    }

    if tv_movie=='tv':
        if Addon.getSetting('debrid_select')=='0' :
            query=[clean_name(original_title,1)+'+s%s'%(season_n),clean_name(original_title,1)+'+s%se%s'%(season_n,episode_n),clean_name(original_title,1)+'+season+' +season]
            query=[clean_name(original_title,1)+'+season+' +season]
        else:
            query=[clean_name(original_title,1)+'+s%se%s'%(season_n,episode_n)]
            
    else:
        query=[clean_name(original_title,1)+' '+show_original_year]
    for qrr in query:
      
        
        data = {
            'query': qrr,
            'offset': 0,
            'limit': 99,
            'filters[field]': 'seeds',
            'filters[sort]': 'desc',
            'filters[time]': 4,
            'filters[category]': 3 if tv_movie=='movie' else 4,
            'filters[adult]': False,
            'filters[risky]': False
        }

        response = get_html("https://bitlordsearch.com" + "/get_list", data=data, headers=headers,timeout=10).json()

        for el in response['content']:
        
            
                
                
                
               
            try:    
                size = int(el['size'])
                if size == 0:
                    continue
                else:
                    if size < 120 and el['source'] == 'thePirateBay':
                        size = size * 1024
                    elif size > 122880:
                        size = int(size / 1024)
                    elif size < 120:
                        continue
                size=size/1000
            except: pass
            
            
            
            if 1:#check and check1:
               
               
                max_size=int(Addon.getSetting("size_limit"))
                title=el['name']
              
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

                if size<max_size:
                              
                       all_links.append((el['name'],el['magnet'],str(size),res))
                   
                       global_var=all_links
    return global_var
        
    