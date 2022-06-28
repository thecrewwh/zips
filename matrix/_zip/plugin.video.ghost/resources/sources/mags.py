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
    from resources.modules.general import Addon,get_imdb
except:
  import Addon
type=['tv','movie','api']

import urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
   
    
        
    if tv_movie=='tv':
        search_url=('{0}%20s{1}e{2}'.format(clean_name(original_title,1).replace(' ','%20'),season_n,episode_n)).lower()
    else:
        search_url=clean_name(original_title,1).replace(' ','%20')+'%20'+show_original_year
        
    if 1:
        x=get_html('https://api.magsearch.net/search?keywords=%s&itemn=200&start=0&filetype=video&sortby=hot&userid=99999999999999999999999999999999'%(search_url.replace(' ','%20')),headers=base_header,timeout=10).json()

        max_size=int(Addon.getSetting("size_limit"))
        dev_num=1024*1024*1024
        for items in x:
                    title=items['name']
                   
                    
                    lk=items['url']
                    size=(float(items['length'])/dev_num)
                    
               
                    
                    if int(size)<max_size:
                       if '2160' in title:
                              res='2160'
                       if '1080' in title:
                              res='1080'
                       elif '720' in title:
                              res='720'
                       elif '480' in title:
                              res='480'
                       elif '360' in title:
                              res='360'
                       else:
                              res='HD'

                     
                       all_links.append((title,lk,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    