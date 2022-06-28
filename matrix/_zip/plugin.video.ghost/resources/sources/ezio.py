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
type=['tv','torrent']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    if tv_movie=='movie':
        return []
    imdb_id=cache.get(get_imdb, 999,tv_movie,id,table='pages')
        
    allow_debrid=True
    search_url=('%s-s%se%s'%(clean_name(original_title,1).replace(' ','-'),season_n,episode_n)).lower()
    for pages in range(0,5):
        x=get_html('https://eztv.re/api/get-torrents?imdb_id=%s&limit=100&page=%s'%(imdb_id.replace('tt',''),str(pages)),headers=base_header,timeout=10).json()
        
        max_size=int(Addon.getSetting("size_limit"))
        dev_num=1024*1024*1024
        for items in x['torrents']:
                    title=items['filename']
                   
                    if 's%se%s.'%(season_n,episode_n) not in title.lower():
                        continue
                    lk=items['magnet_url']
                    size=(float(items['size_bytes'])/dev_num)
                    
               
                    
                    if int(size)<max_size:
                       if '2160' in title:
                              res='2160'
                       if '1080' in title:
                              res='1080'
                       elif '720' in title:
                              res='720'
                       elif '480' in title:
                              res='480'
                       elif '360' in title:
                              res='360'
                       else:
                              res='HD'

                     
                      
                       all_links.append((title,lk,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    