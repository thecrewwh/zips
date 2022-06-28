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
type=['tv','torrent']

import urllib2,urllib,logging,base64,json


def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all

   
    
    all_links=[]
    
    
    search_url=('%s s%se%s'%(clean_name(original_title,1),season_n,episode_n)).lower()
    
    if 1:
        
        x=get_html('http://eztv.show/?s='+search_url.replace(' ','%20'),headers=base_header,timeout=10).content()
        logging.warning('http://eztv.show/?s='+search_url)
        regex='h2 class="entry-title"><a href="(.+?)".+?>(.+?)<'
        macth_pre=re.compile(regex).findall(x)
        regex='strong>Download Torrent: </strong> <a href="(.+?)"'
        regex1=re.compile(regex)
                     
        for link,title in macth_pre:
                
                
                if clean_name(original_title,1).lower() in title.lower() and 's%se%s'%(season_n,episode_n) in title.lower() :
                     y=get_html(link,headers=base_header,timeout=10).content()
        
                     regex='strong>Download Torrent: </strong> <a href="(.+?)"'
                     lk=regex1.findall(y)
                     if len(lk)>0:
                         lk=lk[0]
                        
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
                            regex='Filesize:(.+?)<'
                            size=re.compile(regex).findall(y)[0]
                            o_size=size
                            size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                            if 'MB' in o_size:
                               size=size/1000
                         except:
                            size=0
                         
                         max_size=int(Addon.getSetting("size_limit"))
                  
                         if size<max_size:
                      
                           all_links.append((title,lk,str(size),res))
                       
                           global_var=all_links
    return global_var
        
    