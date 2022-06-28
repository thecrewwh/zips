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
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib,logging,base64,json


def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all

    x=get_html('http://www.magnetdl.com/',headers=base_header,timeout=10).content()
    regex='type="hidden" name="m" value="(.+?)"'
    match=re.compile(regex).findall(x)[0]
    
    
  
    
    
    all_links=[]
    if tv_movie=='movie':
     search_url=[('%s-%s'%(clean_name(original_title,1).replace(' ','-'),show_original_year)).lower()]
    else:
      if Addon.getSetting('debrid_select')=='0' :
        search_url=[('%s-s%se%s'%(clean_name(original_title,1).replace(' ','-'),season_n,episode_n)).lower(),('%s-s%s'%(clean_name(original_title,1).replace(' ','-'),season_n)).lower(),('%s-season-%s'%(clean_name(original_title,1).replace(' ','-'),season)).lower()]
      else:
        search_url=[('%s-s%se%s'%(clean_name(original_title,1).replace(' ','-'),season_n,episode_n)).lower()]
    x=get_html('http://www.magnetdl.com/search/?q=%s&m=%s'%(search_url,match),headers=base_header).geturl()
    
    regex='//www.magnetdl.com/(.+?)/'
    letter=re.compile(regex).findall(x)[0]
    regex='<tr>(.+?)</tr>'
    regex1=re.compile(regex)
    
    regex='<td class="m"><a href="(.+?)".+?a href.+?title="(.+?)".+?class=".+?">(.+?)</td><td>.+?</td><td>(.+?)</td><td class="s">(.+?)</td><td class="l">(.+?)<'
    regex2=re.compile(regex)
            
    for itt in search_url:
      for page in range(1,4):
        
        x=get_html('http://www.magnetdl.com/%s/%s/se/desc/%s/'%(letter,itt,str(page)),headers=base_header,timeout=10).content()
        
        regex='<tr>(.+?)</tr>'
        macth_pre=regex1.findall(x)
      
        for items in macth_pre:
            if stop_all==1:
                break
            regex='<td class="m"><a href="(.+?)".+?a href.+?title="(.+?)".+?class=".+?">(.+?)</td><td>.+?</td><td>(.+?)</td><td class="s">(.+?)</td><td class="l">(.+?)<'
            match=regex2.findall(items)
            
            for link,title,type,size,seed,peer in match:
                if stop_all==1:
                    break
                if type.lower()==tv_movie.lower():
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
                     except:
                        size=0
                     max_size=int(Addon.getSetting("size_limit"))
              
                     if size<max_size:
                  
                       all_links.append((title,o_link,str(size),res))
                   
                       global_var=all_links
    return global_var
        
    