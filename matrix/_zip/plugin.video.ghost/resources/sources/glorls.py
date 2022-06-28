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

   
    
  
    
    
    all_links=[]
    if tv_movie=='movie':
     search_url=[('%s+%s'%(clean_name(original_title,1).replace(' ','+'),show_original_year)).lower()]
     type_s='1'
    else:
      type_s='41'
      if Addon.getSetting('debrid_select')=='0' :
        search_url=[('%s+s%se%s'%(clean_name(original_title,1).replace(' ','+'),season_n,episode_n)).lower(),('%s+s%s'%(clean_name(original_title,1).replace(' ','+'),season_n)).lower(),('%s+season+%s'%(clean_name(original_title,1).replace(' ','+'),season)).lower()]
      else:
        search_url=[('%s+s%se%s'%(clean_name(original_title,1).replace(' ','+'),season_n,episode_n)).lower()]
    
    div=1024*1024*1024
    regex='class="showthecross".+?<b>(.+?)<.+?"magnet(.+?)".+?align=\'center\'>(.+?)</td>'
    regex1=re.compile(regex,re.DOTALL)
    for itt in search_url:
      for page in range(0,3):
        
        x=get_html('http://glodls.to/search_results.php?cat=%s&search=%s&sort=seeders&order=desc&page=%s'%(type_s,itt,page),headers=base_header,timeout=10).content()
        
        m=regex1.findall(x)
      
        for title,link,size in m:
            
                     
                    
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
                    
                    
                   
                     try:
                         o_size=size.decode('utf8','ignore')
                         
                         size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                         if 'MB' in o_size:
                           size=size/1000
                     except Exception as e:
                        
                        size=0
                     max_size=int(Addon.getSetting("size_limit"))
              
                     if size<max_size:
                  
                       all_links.append((title,'magnet'+link,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    