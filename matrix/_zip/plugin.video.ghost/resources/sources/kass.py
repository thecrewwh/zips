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
type=['movie','tv','torrent']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    try:
        unque=urllib.unquote_plus
    except:
        unque=urllib.parse.unquote_plus
    
    if tv_movie=='movie':
      search_url=[clean_name(original_title,1).replace(' ','%20')+'%20'+show_original_year]
      s_type='movies'
    else:
      if Addon.getSetting('debrid_select')=='0' :
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n,clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n,clean_name(original_title,1).replace(' ','%20')+'%20season%20'+season]
      else:
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n]
      s_type='tv'
  
    
    
    all_links=[]
    
    regex='-- Start of Loop -->(.+?)-- End of Loop -->'
    regex1=re.compile(regex,re.DOTALL)
    
    regex_pre='<tr (.+?)</tr>'
    regex2=re.compile(regex_pre,re.DOTALL)
    
    regex='title="Torrent magnet link" href="(.+?)".+?class="cellMainLink">(.+?)<.+?class="nobr center">(.+?)<.+?lass="green center">(.+?)<.+?class="red lasttd center">(.+?)<'
    regex3=re.compile(regex,re.DOTALL)
            
    for itt in search_url:
                       
        x=get_html('https://kick4ss.net/usearch/{0}/'.format(itt),headers=base_header,timeout=10).content()
      
        regex='-- Start of Loop -->(.+?)-- End of Loop -->'
        m=regex1.findall(x)
        
        regex_pre='<tr (.+?)</tr>'
        m_pre=regex2.findall(m[0])
       
        for items in m_pre:
           
            if stop_all==1:
                break
            regex='title="Torrent magnet link" href="(.+?)".+?class="cellMainLink">(.+?)<.+?class="nobr center">(.+?)<.+?lass="green center">(.+?)<.+?class="red lasttd center">(.+?)<'
            macth_pre=regex3.findall(items)
           
        
                
                
            for link,title,size,seed,peer in macth_pre:
                         if stop_all==1:
                            break
                         seed=seed.replace('N/A','0')
                         peer=peer.replace('N/A','0')
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
                         except Exception as e:
                           
                            size=0
                         max_size=int(Addon.getSetting("size_limit"))
                        
                         if size<max_size:
                           f_link=unque(o_link.split('url=')[1])
                           all_links.append((title,f_link,str(size),res))
                       
                           global_var=all_links
    return global_var
        
    