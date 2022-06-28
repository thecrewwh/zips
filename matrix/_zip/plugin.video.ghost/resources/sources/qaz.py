# -*- coding: utf-8 -*-
#frome MediaBoxHD
import re
import time

global global_var,stop_all#global
global_var=[]
stop_all=0

from  resources.modules.client import get_html
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,all_colors,base_header
from  resources.modules import cache
try:
    from resources.modules.general import Addon,get_imdb
except:
  import Addon
type=['movie','non_rd']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    
    search_url=clean_name(original_title,1).replace(' ','%20')
    imdb_id=cache.get(get_imdb, 999,tv_movie,id,table='pages')
    
      
    
      
    
    
    all_links=[]
    
    all_l=[]
    
    if 1:
      
        
            
        x=get_html('https://qazwsxedcrfvtgb.info/show/'+(imdb_id),headers=base_header,timeout=10,verify=False).json()

        for items in x['episodes']:
                         title=clean_name(original_title,1)
                         if tv_movie=='tv':
                            res_c='720'
                            title=title+'.S%sE%s'%(season_n,episode_n)
                            if not(episode==str(items['episode']) and season==str(items['season'])):
                                continue
                         else:
                            res_c='1080'
                         if 'mb_stream' in items:
                            for key in items['mb_stream']:
                                id_lk=items['mb_stream'][key]
                         else:
                            continue
                         
                         link='https://drive.google.com/file/d/'+id_lk+'/view'
                         
                               
                         if '4k' in res_c:
                              res='2160'
                         elif '2160' in res_c:
                              res='2160'
                         elif '1080' in res_c:
                              res='1080'
                         elif '720' in res_c:
                              res='720'
                         elif '480' in res_c:
                              res='480'
                         elif '360' in res_c:
                              res='360'
                         else:
                              res='HD'
                              
                      
                         
                   
                         if 1:
                           
                           all_links.append((title,link,str(0),res))
                       
                           global_var=all_links
                         
    
    return global_var
        
    