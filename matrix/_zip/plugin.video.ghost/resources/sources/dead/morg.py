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
type=['movie','tv','non_rd']

import urllib2,urllib,logging,base64,json


import urllib2,urllib,logging,base64,json


color=all_colors[112]
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    tmdbKey='653bb8af90162bd98fc7ee32bcbbfb3d'

    if tv_movie=='tv':
      
       url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
    else:
       
       url2='http://api.themoviedb.org/3/movie/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
    try:
        
        imdb_id=get_html(url2,timeout=10).json()['external_ids']['imdb_id']
    except:
        imdb_id=" "
        
    if tv_movie=='tv':
        x=get_html("https://movies.org/api/releases/tv/%s/%s000%s"%(imdb_id,season,episode_n),headers=base_header,timeout=10).json()

    else:
        
        x=get_html("https://movies.org/api/releases/movie/"+(imdb_id),headers=base_header,timeout=10).json()
        
        
    

    check_rd=False
    if Addon.getSetting('debrid_use')=='true' and Addon.getSetting('debrid_select')=='0':
        from resources.modules import real_debrid
        rd = real_debrid.RealDebrid()
        check_rd=True
    max_size=int(Addon.getSetting("size_limit"))
    for results in x:
       
            nam=results['Release']
            
            link_pre=results['Link']
            
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
            if 'gounlimited.to' in link_pre:
                
                y=get_html(link_pre,headers=base_header,timeout=10).content()
                regex="<script type='text/javascript'>(.+?)</script>"
                m2=re.compile(regex,re.DOTALL).findall(y)[0]
                from resources.modules.jsunpack import unpack
                try:
                    
                    data=unpack(m2)
                    
                    data = re.findall('sources:(\[\{.+?\}\])',data, re.DOTALL)[0]
                    
                    try:
                        data = json.loads(data)
                    except:
                        data=data.replace('file','"file"').replace('label','"label"')
                        data = json.loads(data)
                    data = [(i['file']) for i in data if data]
                except:
                    regex='src:"(.+?)"'
                    link=re.compile(regex).findall(data)[0]
                    data=[link]
                
                for link_in in data:
                    link='Direct_link$$$'+link
                    try:
                        try_head = get_html(link_in,headers=base_header, stream=True,verify=False,timeout=3)
                    
       
                        if 'Content-Length' in try_head.headers:
                           if int(try_head.headers['Content-Length'])>(1024*1024):
                            size=(round(float(try_head.headers['Content-Length'])/(1024*1024*1024), 2))
                    
                                
                    
                    except:
                        size=0
                 
                    
                    if (size)<max_size:
            
                        all_links.append((nam,link,str(size),res))

                        global_var=all_links
                        
            else:
              
                if 'clipwatching.com' in link_pre:
                  y=get_html(link_pre,headers=base_header,timeout=10).content()
                  regex='src: "(.+?)"'
                  m2=re.compile(regex,re.DOTALL).findall(y)[0]
                  
                        
                  all_links.append((nam,'Direct_link$$$'+m2,str(0),res))

                  global_var=all_links
    return global_var