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
type=['tv','non_rd']

import urllib2,urllib,logging,base64,json


def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    import xbmc,sys
    path=xbmc.translatePath('special://home/addons/script.module.resolveurl/lib')
    sys.path.append( path)
    path=xbmc.translatePath('special://home/addons/script.module.six/lib')
    sys.path.append( path)
    
    import resolveurl
    all_links=[]
    if tv_movie=='movie':
        search_string=clean_name(original_title,1).replace(' ','%20')+'%20'+show_original_year
    else:
        search_string=clean_name(original_title,1).replace(' ','%20')+'%20season%20'+season
    

    response = get_html('https://gowatchseries.tv/search.html?keyword='+search_string, headers=base_header).content()
    
    regex='<li>(.+?)</li>'
    m_pre=re.compile(regex,re.DOTALL).findall(response)
    for itt in m_pre:
        
        regex='a href="(.+?)".+?<div class="name">(.+?)<'
        m=re.compile(regex,re.DOTALL).findall(itt)
        for lk,nm in m:
            
            check=False
            if tv_movie=='movie':
                if clean_name(original_title,1).lower() in nm.lower() and show_original_year in nm.lower():
                    check=True
            else:
                if clean_name(original_title,1).lower() in nm.lower() and ' season %s$$$'%season in (nm.lower()+'$$$'):
                    check=True
            
            
            if check:
                x=get_html('https://gowatchseries.tv'+lk, headers=base_header).content()
                
                if tv_movie=='movie':
                    title=clean_name(original_title,1)
                    regex='<span>Latest Episode:  </span>.+?<a href="(.+?)"'
                    m2=re.compile(regex,re.DOTALL).findall(x)[0]
                else:
                    title=clean_name(original_title,1)+'.S%sE%s'%(season_n,episode_n)
                    regex='<li class="child_episode">.+?a href="(.+?)"'
                    m2_pre=re.compile(regex,re.DOTALL).findall(x)
                    
                    found=False
                    for m2 in m2_pre:
                        
                       
                        if 'season-%s-episode-%s$$$'%(season,episode) in m2.lower()+'$$$':
                            found=True
                            break
                   
                    if not found:
                        return []
                
                y=get_html('https://gowatchseries.tv'+m2, headers=base_header).content()
                regex='data-video="(.+?)"'
                lk_pre=re.compile(regex,re.DOTALL).findall(y)
                
                for f_lk in lk_pre:
                    f_lk_r=False
                    try:
                        if '#caption=' in f_lk:
                            f_lk=f_lk.split('#caption=')[0]
                        f_lk_r= resolveurl.resolve(f_lk)
                        
                    except:
                        pass
                    size=0
                    
                    if f_lk_r:
                        all_links.append((title,'Direct_link$$$'+f_lk_r,str(size),'HD'))
               
                        global_var=all_links
    return global_var
        
    