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
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib,logging,base64,json


def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    try:
        que=urllib.quote_plus
    except:
        que=urllib.parse.quote_plus
   
    
  
    
    
    all_links=[]
    if tv_movie=='movie':
     search_url=[('%s+%s'%(clean_name(original_title,1).replace(' ','+'),show_original_year)).lower()]
    else:
      if Addon.getSetting('debrid_select')=='0' :
        search_url=[('%s+s%se%s'%(clean_name(original_title,1).replace(' ','+'),season_n,episode_n)).lower(),('%s-s%s'%(clean_name(original_title,1).replace(' ','-'),season_n)).lower(),('%s-season-%s'%(clean_name(original_title,1).replace(' ','-'),season)).lower()]
      else:
        search_url=[('%s+s%se%s'%(clean_name(original_title,1).replace(' ','+'),season_n,episode_n)).lower()]
    
    div=1024*1024*1024
    for itt in search_url:
      
        
        x=get_html('https://torrent-paradise.ml/api/search?q='+(itt),headers=base_header,timeout=10).json()
       
        
        
        for itm in x:
            
                     hash=itm['id']
                     title=itm['text']
                     size=itm['len']/(div)
                    
                     if stop_all==1:
                        break
                     try:
                        lk='magnet:?xt=urn:btih:%s&dn=%s'%(hash,que(title))
                     except:
                        lk='magnet:?xt=urn:btih:%s&dn=%s'%(hash,que(clean_name(original_title,1)))
                     if stop_all==1:
                        break
                    
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
                  
                       all_links.append((title,lk,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    