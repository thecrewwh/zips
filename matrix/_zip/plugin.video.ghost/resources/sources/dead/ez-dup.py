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
type=['tv','torrent']

import urllib2,urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    if tv_movie=='movie':
        return []
    
    allow_debrid=True
    search_url=('%s-s%se%s'%(clean_name(original_title,1).replace(' ','-'),season_n,episode_n)).lower()
   
    x=requests.get('https://eztv.io/search/{0}'.format(search_url),headers=base_header,timeout=10).content
   
    regex_pre='<tr name="hover"(.+?)</tr>'
    m_pre=re.compile(regex_pre,re.DOTALL).findall(x)
    for items in m_pre:
        regex='<td class="forum_thread_post".+?class="epinfo">(.+?)<.+?a href="(.+?)".+?<td align="center" class="forum_thread_post">(.+?)<.+?<td align="center" class="forum_thread_post_end"><font color="green">(.+?)<'
        m2=re.compile(regex,re.DOTALL).findall(items)
        if len (m2)==0:
            
            regex='<td class="forum_thread_post".+?class="epinfo">(.+?)<.+?a href="(.+?)".+?<td align="center" class="forum_thread_post">(.+?)<.+?<td align="center" class="forum_thread_post_end">(.+?)<'
            m2=re.compile(regex,re.DOTALL).findall(items)
        

        for title,links,size,seed in m2:
                seed=seed.replace('-','0')
           
           
                peer=0
                if stop_all==1:
                    break
                size=size.replace('&nbsp;'," ")
                
                try:
                     o_size=size
                     size=float(o_size.replace('GiB','').replace('MiB','').replace('GB','').replace('MB','').replace(",",'').strip())
                     if 'MB' in o_size or 'MiB' in o_size:
                       size=size/1000
                except:
                    size=0
                regex='dn=(.+?)&'
                
                nam=title
                max_size=int(Addon.getSetting("size_limit"))
                if '.TS.' in nam:
                    continue
                
                if int(size)<max_size:
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

                   if clean_name(original_title,1).lower() not in title.lower():
                        continue
                  
                   if 0:#allow_debrid:
                        x=requests.get('https://eztv.io'+links,headers=base_header,timeout=10).content
                        regex='"magnet(.+?)"'
                        mm=re.compile(regex).findall(x)
                        if len(mm)==0:
                            continue
                        lk='magnet'+mm[0]
                   else:
                        lk=links
                   all_links.append((title,lk,str(size),res))
               
                   global_var=all_links
    return global_var
        
    