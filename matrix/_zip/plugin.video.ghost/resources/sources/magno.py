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
from resources.modules import log
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    if tv_movie=='movie':
      search_url=[clean_name(original_title,1).replace(' ','%20')+'%20']
      s_type='Movies'
      type='207'
      type2='201'
    else:
      if Addon.getSetting('debrid_select')=='0' :
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n,clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n,clean_name(original_title,1).replace(' ','%20')+'%20season%20'+season]
      else:
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n]
      s_type='TV'
      type='208'
      type2='205'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://magno.netlify.app/',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }


    all_links=[]
    
    all_l=[]
    
    regex="magnet(.+?)'"
    regex1=re.compile(regex)
    for itt in search_url:
      
        if stop_all==1:
            break
        params = (
            ('term', itt),
        )
        try:
            
           
            x = get_html('https://magno.netlify.app/.netlify/functions/stop', headers=headers, params=params).json()
            
            #x=get_html('https://magno.netlify.app/.netlify/functions/api?keyword=%s'%(itt),headers=base_header,timeout=10).json()
        except Exception as e:
            
            continue
   
        
     
      
       
        
        log.warning(x)
        div_size=1024*1024*1024
        for items in x:
                         log.warning(items)
                         title=items['title']
                         
                         link=items['link']
                         
                         if 'magnet' not in str(link):
                           continue
                           try:
                            link=get_html(link,stream=True).url
                           except Exception as e:
                               
                               regex="magnet(.+?)'"
                               link='magnet'+regex1.findall(str(e))[0]
                               
                              
                        
                         size=items['size']
                         
                        
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
                         
                         o_link=link
                         size=(float(size)/(div_size))
                        
                         max_size=int(Addon.getSetting("size_limit"))
                        
                         if size<max_size:
                         
                           all_links.append((title,link,str(size),res))
                       
                           global_var=all_links
                         
    
    return global_var
        
    