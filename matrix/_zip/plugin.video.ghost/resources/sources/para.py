# -*- coding: utf-8 -*-
import re
import time

global global_var,stop_all#global
global_var=[]
stop_all=0
from  resources.modules.client import get_html
 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
from  resources.modules import cache
try:
    from resources.modules.general import Addon,get_imdb
except:
  import Addon
type=['movie','tv','torrent','api']

import urllib,logging,base64,json



color=all_colors[112]
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    
    try:
        que=urllib.quote_plus
    except:
        que=urllib.parse.quote_plus

   
    if tv_movie=='movie':
     ur='https://torrent-paradise.ml/api/search?q='+(original_title+'%20'+show_original_year)
    elif tv_movie=='tv':
     ur='https://torrent-paradise.ml/api/search?q='+(original_title+'%20'+'S%sE%s'%(season_n,episode_n))
     
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    }
    if 1:
        
        y=get_html(ur,headers=headers,timeout=10).json()
       
        div_value=1024*1024*1024
        for results in y:            
      
            
            if stop_all==1:
                break
            nam=results['text']
            
            
            
            size=float(results['len'])/div_value
               
            
            links=results['id']
            lk='magnet:?xt=urn:btih:%s&dn=%s'%(links,'www')
            
            if '4k' in nam:
                  res='2160'
            elif '2160' in nam:
                  res='2160'
            elif '1080' in nam:
                      res='1080'
            elif '720' in nam:
                  res='720'
            elif '480' in nam:
                  res='480'
            elif '360' in nam:
                  res='360'
            else:
                  res='HD'
            max_size=int(Addon.getSetting("size_limit"))
            
            
            if (size)<max_size:
               
                all_links.append((nam,lk,str(size),res))

                global_var=all_links
    return global_var