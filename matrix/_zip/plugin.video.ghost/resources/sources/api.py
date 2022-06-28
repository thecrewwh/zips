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
type=['movie','tv','torrent']

import urllib,logging,base64,json

from resources.modules import log


color=all_colors[112]
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    imdb_id=cache.get(get_imdb, 999,tv_movie,id,table='pages')
        

    x=get_html("https://torrentapi.org/pubapi_v2.php?app_id=me&get_token=get_token",headers=base_header,timeout=10).json()
    token=x['token']
    if tv_movie=='movie':
     search_url=[((clean_name(original_title,1).replace(' ','%20')+'%20'+show_original_year)).lower()]
    elif tv_movie=='tv':
    
     if Addon.getSetting('debrid_select')=='0' :
            
            search_url=[clean_name(original_title,1).replace(' ','%20')+'%20'+'S'+season_n,clean_name(original_title,1).replace(' ','%20')+'%20'+'s'+season_n+'e'+episode_n,clean_name(original_title,1).replace(' ','%20')+'%20'+'season '+season]
     else:
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20'+'s'+season_n+'e'+episode_n]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    }

    for itt in search_url:
        time.sleep(0.4)
        ur='https://torrentapi.org/pubapi_v2.php?app_id=Torapi&mode=search&search_imdb=%s&token=%s&sort=seeders&ranked=0&limit=100&format=json_extended&search_string=%s'%(imdb_id,token,itt)
        log.warning('API:'+ur)
        y=get_html(ur,headers=headers,timeout=10).json()
        if 'torrent_results' not in y:
           
            continue
        for results in y['torrent_results']:
            
      
              
            if stop_all==1:
                break
            nam=results['title']
            size=(float(results['size'])/(1024*1024*1024))
            peer=results['leechers']
            seed=results['seeders']
            links=results['download']
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
               
                all_links.append((nam,links,str(size),res))

                global_var=all_links
    return global_var