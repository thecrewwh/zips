# -*- coding: utf-8 -*-
import re
import time,random
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

from resources.modules import log


import urllib,logging,base64,json


color=all_colors[112]
def random_str():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP1234567890"
    s = ""
    for x in range(0,8):
        i = random.randint(0,len(chars)-1)
        s += chars[i]
    
    return s
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    
    
    if tv_movie=='movie':
     search_url=((clean_name(original_title,1).replace(' ','%20')+'%20'+show_original_year)).lower()
    elif tv_movie=='tv':
     search_url=((clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n)).lower()
    time.sleep(0.4)
  
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://snowfl.com/',
    'TE': 'Trailers',
    }
    non_magnet=[]
    x= get_html('https://snowfl.com',headers=headers).content()
    regex='src="b.min.js(.+?)"'
    m=re.compile(regex).findall(x)[0]
    x= get_html('https://snowfl.com/b.min.js'+m,headers=headers).content()
    regex='isMobile\=!1,.+?\="(.+?)"'
    code=re.compile(regex).findall(x)[0]
    log.warning(code)
    for page in range(1,4):
        if stop_all==1:
            break
       
        rand_str= random_str()
        params = (
            ('_', str(time.time()*100)),
        )          
       
        response = get_html('https://snowfl.com/%s/%s/%s/%s/NONE/NONE/1'%(code,search_url,rand_str,str(page)), headers=headers, params=params).json()
       
        for results in response:
            if stop_all==1:
                break
            if 'magnet' in results:
                nam=results['name']
                size=results['size']
                peer=results['leecher']
                seed=results['seeder']
                links=results['magnet']
                if '4k' in nam:
                      res='2160'
                elif '2160' in nam:
                      res='2160'
                elif '1080' in nam:
                          res='1080'
                elif '720' in nam:
                      res='720'
                elif '480' in nam:
                      res='480'
                elif '360' in nam:
                      res='360'
                else:
                      res='HD'
                try:
                     o_size=size.decode('utf8','ignore')
                     
                     size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                     if 'MB' in o_size:
                       size=size/1000
                except Exception as e:
                    
                    size=0
                max_size=int(Addon.getSetting("size_limit"))
             
             
                if (size)<max_size:
                    all_links.append((nam,links,str(size),res))

                    global_var=all_links
            else:
                
                non_magnet.append(results)
            for results in non_magnet:
                if stop_all==1:
                    break
                
      

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Connection': 'keep-alive',
                    'Referer': 'https://snowfl.com/',
                }

                params = (
                    ('_', str(time.time()*100)),
                )
                site=results['site']
                
                ur=urllib.quote_plus(results['url']).encode('base64').replace(' ','').replace('\n','').replace('\r','').replace('\t','')
               
                response = get_html('https://snowfl.com/OIcObqNfqpHTDvLKWQDNRlzQPbtqRcoKhtlled/%s/%s'%(site,ur), headers=headers, params=params).json()
                
                if 1:
                    nam=results['name']
                    
                    size=results['size']
                    peer=results['leecher']
                    seed=results['seeder']
                    links=response['url']
                   
                    if '4k' in nam:
                          res='2160'
                    elif '2160' in nam:
                          res='2160'
                    elif '1080' in nam:
                              res='1080'
                    elif '720' in nam:
                          res='720'
                    elif '480' in nam:
                          res='480'
                    elif '360' in nam:
                          res='360'
                    else:
                          res='HD'
                    try:
                         o_size=size.decode('utf8','ignore')
                         
                         size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                         if 'MB' in o_size:
                           size=size/1000
                    except Exception as e:
                        
                        size=0
                    max_size=int(Addon.getSetting("size_limit"))
                 
                 
                    if (size)<max_size:
                        all_links.append((nam,links,str(size),res))

                        global_var=all_links
                
    return global_var