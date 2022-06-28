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
type=['movie','torrent']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    try:
        que=urllib.quote_plus
    except:
        que=urllib.parse.quote_plus
    
    if tv_movie=='movie':
      search_url=clean_name(original_title,1).replace(' ','%20')+'%20'
      s_type='Movies'
      type='207'
      type2='201'
    else:
      return []
      
    
    
    all_links=[]
    
    all_l=[]
    idd_table=['3','7']
    if 1:
      
        
            
        x=get_html('https://yts.mx/api/v2/list_movies.json?query_term=%s&page=1&limit=300&order_by=desc&sort_by=rating'%(search_url),headers=base_header,timeout=10,verify=False).json()
        
        
   
        
     
      
       
        
                
        
        for items in x['data']['movies']:
                        title=items['slug'].replace('-','.')
                        for te in items['torrents']:
                         hash=te['hash']
                         link='magnet:?xt=urn:btih:%s&dn=%s'%(hash,que(title))
                         
                         size=te['size']
                         res=te['quality'].replace('p','')
                        
                         
                         
                     
                         
                        
                         o_link=link
                        
                         try:
                             o_size=size.decode('utf8','ignore')
                             
                             size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                             if 'MB' in o_size:
                               size=size/1000
                         except Exception as e:
                            
                            size=0
                         max_size=int(Addon.getSetting("size_limit"))
                        
                         if size<max_size:
                         
                           all_links.append((title,link,str(size),res))
                       
                           global_var=all_links
                         
    
    return global_var
        
    