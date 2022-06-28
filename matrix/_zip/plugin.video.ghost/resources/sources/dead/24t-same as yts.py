# -*- coding: utf-8 -*-
import requests,re
import time

global global_var,stop_all#global
global_var=[]
stop_all=0

 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,cloudflare_request,all_colors,base_header
from  resources.modules import cache
try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib2,urllib,logging,base64,json


def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all

   
    
  
    
    
    all_links=[]
    if tv_movie=='movie':
     search_url=('%s+%s'%(clean_name(original_title,1),show_original_year)).lower()
    else:
      
        search_url=('%s+s%se%s'%(clean_name(original_title,1).replace(' ','%20'),season_n,episode_n)).lower()
    
    
    
    for page in range(1,4):
        
        x=requests.get(('https://24tor.com/v2/?word=%s&page=%s'%(search_url,str(page))).replace(' ','%20'),headers=base_header,timeout=10).content
        logging.warning(('https://24tor.com/v2/?word=%s&page=%s'%(search_url,str(page))).replace(' ','%20'))
        regex='<tr>(.+?)</tr>'
        macth_pre=re.compile(regex,re.DOTALL).findall(x)
        
        for itm in macth_pre:
            
            regex='</a><a href="(.+?)">(.+?)<.+?td class="coll-4 size mob-uploader">(.+?)<'
            macth_pre2=re.compile(regex,re.DOTALL).findall(itm)
          
            for hash,title,size in macth_pre2:
                     
                     
                     y=requests.get('https://24tor.com/v2/'+hash,headers=base_header,timeout=10).content
                    
                     regex='form="myInput">(.+?)<'
                     lk=re.compile(regex,re.DOTALL).findall(y)[0]
                     if stop_all==1:
                        break
                     
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
        
    