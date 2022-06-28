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
type=['movie','tv','torrent','api']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    if tv_movie=='movie':
      search_url=[clean_name(original_title,1).replace(' ','%20')]
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
    
    
    all_links=[]
    
    all_l=[]
    idd_table=['6','8']
    for idd in idd_table:
     for itt in search_url:
      
        if stop_all==1:
            break
            
        x=get_html('https://torrmonk.in/api/torrent/search?ID=%s&query=%s'%(str(idd),itt),headers=base_header,timeout=10).json()

   
        
     
      
        if 'errorCode' in x:
          if x['errorCode']==404:
            continue
          
            continue
        if 'data' not in x:
            continue
        if len(x['data'])==0:
            continue
        if 'result' not in x['data']:
            continue
        if len(x['data']['result'])==0:
            continue
        
        for items in x['data']['result']:
                         title=items['name']
                         link=items['magnetLink']
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
                        
                         try:
                             o_size=size.decode('utf8','ignore')
                             
                             size=float(o_size.replace('GiB','').replace('MiB','').replace(",",'').strip())
                             if 'MiB' in o_size:
                               size=size/1000
                         except Exception as e:
                            
                            size=0
                         max_size=int(Addon.getSetting("size_limit"))
                        
                         if size<max_size:
                         
                           all_links.append((title,link,str(size),res))
                       
                           global_var=all_links
                         
    
    return global_var
        
    