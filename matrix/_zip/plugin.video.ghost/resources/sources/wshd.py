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
type=['tv','non_rd']

import urllib,logging,base64,json
from resources.modules import log

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    import xbmc,sys
    path=xbmc.translatePath('special://home/addons/script.module.resolveurl/lib')
    sys.path.append( path)
    path=xbmc.translatePath('special://home/addons/script.module.six/lib')
    sys.path.append( path)
    path=xbmc.translatePath('special://home/addons/script.module.kodi-six/libs')
    sys.path.append( path)
    import resolveurl
    
    
    
    
   
    
  
   
    
    all_links=[]
    if tv_movie=='movie':
        return []
    

    y = get_html('http://www1.watchserieshd.tv/series/%s-season-%s-episode-%s'%(clean_name(original_title,1).replace(' ','-'),season,episode), headers=base_header).content()
    log.warning(y)
    regex='data-video="(.+?)"'
    lk_pre=re.compile(regex,re.DOTALL).findall(y)
    
    for f_lk in lk_pre:
        f_lk_r=False

        if 'vev.io' in f_lk.lower() or 'vidup.me' in f_lk.lower():
            continue
        try:
            if '#caption=' in f_lk:
                f_lk=f_lk.split('#caption=')[0]
            f_lk_r= resolveurl.resolve(f_lk)
            
        except:
            pass
        size=0
       
        title=clean_name(original_title,1)+'.S%sE%s'%(season_n,episode_n)
        if f_lk_r:
            all_links.append((title,'Direct_link$$$'+f_lk_r,str(size),'HD'))
   
            global_var=all_links
    return global_var
        
    