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
from resources.modules import log

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all

   
    
  
    imdb_id=cache.get(get_imdb, 999,tv_movie,id,table='pages')
    
    all_links=[]
    if tv_movie=='tv':
     
      tv_movie='show'
    x=get_html('https://api.apipop.net/%s?cb=&quality=720p,1080p,2160p&page=1&imdb=%s&ver=100.0.0.0.&os=windows&app_id=T4P_ONL'%(tv_movie,imdb_id),headers=base_header).json()
    #log.warning('https://api.apipop.net/%s?cb=&quality=720p,1080p,2160p&page=1&imdb=%s&ver=100.0.0.0.&os=windows&app_id=T4P_ONL'%(tv_movie,imdb_id))
    #log.warning(json.dumps(x))
    div_value=1024*1024*1024
    if tv_movie=='movie':
        for items in x['items']:
                     link=items['torrent_magnet']
                     title=items['file']
                    
                     if stop_all==1:
                        break
                    
                     res=items['quality'].replace('p','')
                    
                     o_link=link
                   
                     try:
                         
                         size=items['size_bytes']/div_value
                     except:
                        size=0
                     max_size=int(Addon.getSetting("size_limit"))
                     log.warning(size)
                     
                     if size<max_size:
                  
                       all_links.append((title,o_link,str(size),res))
                   
                       global_var=all_links
    else:
        for itt in x:
            
            for itt2 in x[itt]:
              if season==itt2['season'] and episode==itt2['episode']:
                for items in itt2['items']:
                     link=items['torrent_magnet']
                     title=items['file']
                    
                     if stop_all==1:
                        break
                    
                     res=items['quality'].replace('p','')
                    
                     o_link=link
                   
                     try:
                         
                         size=items['size_bytes']/div_value
                     except:
                        size=0
                     max_size=int(Addon.getSetting("size_limit"))
               
                     
                     if size<max_size:
                  
                       all_links.append((title,o_link,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    