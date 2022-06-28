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
type=['tv','torrent']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
   
    
    allow_debrid=True
    search_url=('%s-s%se%s'%(clean_name(original_title,1).replace(' ','-'),season_n,episode_n)).lower()
   
    x=get_html('https://showrss.info/browse',headers=base_header,timeout=10).content()
    
    regex_pre='option value="(.+?)">(.+?)<'
    m_pre=re.compile(regex_pre,re.DOTALL).findall(x)
    found=False
   
    
    for idd,title in m_pre:
        
        if title.lower()==clean_name(original_title,1).lower() or title.lower()==(clean_name(original_title,1).lower() +' (%s)'%show_original_year):
            found=True
            break
   
    if found:
        x=get_html('https://showrss.info/browse/'+idd,headers=base_header,timeout=10).content()
        regex='<li><a href="(.+?)".+?title="(.+?)"'
        m_pre=re.compile(regex,re.DOTALL).findall(x)
        
        for lk,ti in m_pre:

            seed='0'
       
       
            peer='0'
            if stop_all==1:
                break
            size='0'
            
           
            
            nam=ti
            
           
            
            
            if '1080' in nam:
                  res='1080'
            elif '720' in nam:
                  res='720'
            elif '480' in nam:
                  res='480'
            elif '360' in nam:
                  res='360'
            else:
                  res='HD'
            
  
            if 's%se%s '%(season_n,episode_n) not in ti.lower() and 's%se%s.'%(season_n,episode_n) not in ti.lower():
                continue
            if 'upcoming' in lk:
                continue
            
            all_links.append((ti,lk,str(size),res))
       
            global_var=all_links
    return global_var
        
    