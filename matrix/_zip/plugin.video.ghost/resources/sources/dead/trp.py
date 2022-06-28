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
type=['movie','non_rd']

import urllib2,urllib,logging,base64,json

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    
    search_url=clean_name(original_title,1).replace(' ','%20')
     
      
    
      
    
    
    all_links=[]
    
    all_l=[]
    
    if 1:
      
        
            
        x=requests.get('https://theaterplus.xyz/api/get_search_results1/?api_key=dda11uT8cBLzm6a1YvsiUWOEgrFowk95K2DM3tHAPRCX4ypGjN&search='+(search_url),headers=base_header,timeout=10,verify=False).json()
       
   
        
     
      
       
        
                
        
        for items in x['posts']:
                         title=str(items['category_name']).replace('-','.')

                         link=items['channel_url']
                         if tv_movie=='movie':
                            res_c=items['channel_name']
                            if show_original_year not in items['channel_name']:
                                continue
                         else:
                            res_c=link
                            if 'Season %s - Episode %s$$'%(season,episode) not in items['channel_name']+'$$':
                                continue
                            title=title+'.S%sE%s'%(season_n,episode_n)
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
                              
                         try_head = requests.get(link,headers=base_header, stream=True,verify=False,timeout=15)
                         size=0
                         
                         if 'Content-Length' in try_head.headers:
          
                            if int(try_head.headers['Content-Length'])>(1024*1024):
                                size=float(try_head.headers['Content-Length'])/(1024*1024*1024)
                     
                         max_size=int(Addon.getSetting("size_limit"))
                         
                         if size<max_size:
                           
                           all_links.append((title,link,str(size),res))
                       
                           global_var=all_links
                         
    
    return global_var
        
    