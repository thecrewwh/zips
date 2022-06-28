# -*- coding: utf-8 -*-
import re
import time
from  resources.modules.client import get_html
global global_var,stop_all#global
global_var=[]
stop_all=0
try:
 import xbmcgui
 local=False
except:
 local=True
 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib,logging,base64,json

color=all_colors[110]
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    
   

    if tv_movie=='movie':
     cat='4'
     search_url=[('%s+%s'%(clean_name(original_title,1).replace(' ','+'),show_original_year)).lower()]
    else:
     cat='8'
     if Addon.getSetting('debrid_select')=='0' :
        
        search_url=[('%s+s%se%s'%(clean_name(original_title,1).replace(' ','+'),season_n,episode_n)).lower(),('%s+s%s'%(clean_name(original_title,1).replace(' ','+'),season_n)).lower(),('%s-season-%s'%(clean_name(original_title,1).replace(' ','+'),season)).lower()]
     else:
        search_url=[('%s+s%se%s'%(clean_name(original_title,1).replace(' ','+'),season_n,episode_n)).lower()]
    regex='<tr class(.+?)</tr>'
    regex1=re.compile(regex,re.DOTALL)
    
    regex='a href="magnet(.+?)".+?td class="tli".+?title="(.+?)"'
    regex2=re.compile(regex,re.DOTALL)
            
    for itt in search_url:
      for page in range(1,4):
        
        x=get_html('https://extratorrent.si/search/?search=%s&s_cat=%s&page=%s'%(itt,cat,str(page)),headers=base_header).content()
        
        
        regex='<tr class(.+?)</tr>'
        macth_pre=regex1.findall(x)
       
        for items in macth_pre:
         
            if stop_all==1:
                break
            
            match=regex2.findall(items)
      
            
            try:
                size = re.findall('((?:\d+\,\d+\.\d+|\d+\.\d+|\d+\,\d+|\d+)\s*(?:GiB|MiB|GB|MB))', items)[0]
            except:
                size=0
            
            for link,title in match:
                     if stop_all==1:
                        break
                     title=title.replace('view ','')
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
                         o_size=size
                         size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                         if 'MB' in o_size:
                           size=size/1000
                     except:
                        size=0
                     max_size=int(Addon.getSetting("size_limit"))
              
                     if size<max_size:
                       
                       all_links.append((title,'magnet'+o_link,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    