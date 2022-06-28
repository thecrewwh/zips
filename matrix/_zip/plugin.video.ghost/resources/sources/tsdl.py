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
        que=urllib.quote_plus
    except:
        que=urllib.parse.quote_plus
    
    
  
    
   
    
    all_links=[]
    domains = ['torrentdownloads.me', 'torrentdownloads.info']
    search = '{0}/rss.xml?new=1&type=search&cid={1}&search={2}'
    for domain in domains:
        try:
            url = 'https://%s' % domain
            result = client.request(url, timeout='10')
            search_n = re.findall('alt="Torrent Downloads"', result, re.DOTALL)[0]
            if search_n:
                break
        except Exception:
            pass
            
    if tv_movie=='tv':
        cid='8'
        if Addon.getSetting('debrid_select')=='0' :
            search_sting=[clean_name(original_title,1).replace(' ','+')+'+s%se%s'%(season_n,episode_n),clean_name(original_title,1).replace(' ','+')+'+s%s'%(season_n),clean_name(original_title,1).replace(' ','+')+'+season+%s'%(season)]
        else:
            search_sting=[clean_name(original_title,1).replace(' ','+')+'+s%se%s'%(season_n,episode_n)]
    else:
        cid='4'
        search_sting=[clean_name(original_title,1).replace(' ','+')+'+%s'%(show_original_year)]
    regex='<item>(.+?)</item'
    data_regex=re.compile(regex,re.DOTALL)
    regex='<title>(.+?)<.+?<size>(.+?)<.+?<info_hash>(.+?)<'
    data_regex2=re.compile(regex,re.DOTALL)
        
    for itt in search_sting:
        url_f=search.format(url,cid,itt)
       
        x=get_html(url_f,headers=base_header).content()
       
        
        m_pre=data_regex.findall(x)
        count=0
        
        for items in m_pre:
         
            count+=1
            
            m=data_regex2.findall(items)
            
            
            for title,size,hash in m:
                 
                    size = float(int(size))/1073741824
                    
                    lk='magnet:?xt=urn:btih:%s&dn=%s'%(hash,que(title))
                
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
                    
                    
                    max_size=int(Addon.getSetting("size_limit"))
                   
                    if size<max_size:
                        all_links.append((title,lk,str(size),res))
                        
                        global_var=all_links
  
    return global_var
        
    