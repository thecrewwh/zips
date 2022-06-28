# -*- coding: utf-8 -*-
import re
import time
from  resources.modules.client import get_html
global global_var,stop_all#global
global_var=[]
stop_all=0

 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
from  resources.modules import cache
try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib,logging,base64,json


def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all

   
    
  
    
    
    all_links=[]
    if tv_movie=='movie':
     search_url=('%s %s'%(clean_name(original_title,1),show_original_year)).lower()
    else:
     search_url=('%s s%se%s'%(clean_name(original_title,1),season_n,episode_n)).lower()
    
   
    
    for page in range(0,4):
        
        params = (
        ('sort', 'seeders'),
        ('q', search_url),
        ('category', 'all'),
        ('skip', str(page*40)),
        ('fuv', 'yes'),
        )

        x = get_html('https://solidtorrents.net/api/v1/search', headers=base_header, params=params,timeout=10).json()
        
   
        
        
       
        for items in x['results']:
            if stop_all==1:
                break
            link=items['magnet']
            size=float(items['size'])/(1024*1024*1024)
           
            title=items['title']
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
            
            
           
             
            max_size=int(Addon.getSetting("size_limit"))
      
            if size<max_size:
              
               all_links.append((title,link,str(size),res))
           
               global_var=all_links
    return global_var
        
    