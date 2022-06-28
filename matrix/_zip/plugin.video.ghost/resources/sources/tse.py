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
    if tv_movie=='movie':
      search_url=[clean_name(original_title,1).replace(' ','%20')+'%20']
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
    
    seed=''
    f_seeds=False
    use_debrid=Addon.getSetting('debrid_use')=='true'

    if (Addon.getSetting('torrents')=='true' and use_debrid==False):
        f_seeds=True
        seed='S: >>'
    all_links=[]
    
    all_l=[]
    id_table=['20','4','7','24','2','32','13']
    for idd in id_table:
     for itt in search_url:
      
        if stop_all==1:
            break
        try:
            x=get_html('http://157.230.67.147/t_api/simplehtmldom_1_5/my_parsers/scraping/my_scraper3.php?query=%s&sort=0&category=0&page=0&adult=0&key=halyoa&concurrent=0&provider_ids[]=%s'%(itt,idd),headers=base_header,timeout=10).json()
        except:
            
            continue
   
        
     
      
       
        
                
        
        for items in x['results']:
                         title=items['title']
                         link=items['magnet']
                         size=items['size']
                         if f_seeds:
                            
                            seed=items['seeds'].replace(",","")
                            if int(Addon.getSetting('min_seed'))>int(seed):
                                continue
                            seed='S:%s>>,'%str(seed)
                        
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
                             
                             size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                             if 'MB' in o_size:
                               size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())/1000
                         except Exception as e:
                            
                            size=0
                         max_size=int(Addon.getSetting("size_limit"))
                        
                         if size<max_size:
                         
                           all_links.append((seed+title,link,str(size),res))
                       
                           global_var=all_links
                         
    
    return global_var
        
    