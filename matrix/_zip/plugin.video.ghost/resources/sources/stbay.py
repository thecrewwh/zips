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
type=['movie','tv','torrent']

import urllib,logging,base64,json




color=all_colors[112]
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
 
    imdb_id=cache.get(get_imdb, 999,tv_movie,id,table='pages')
    try:
        que=urllib.quote_plus
    except:
        que=urllib.parse.quote_plus
    seed=''
    f_seeds=False
    use_debrid=Addon.getSetting('debrid_use')=='true'

    if (Addon.getSetting('torrents')=='true' and use_debrid==False):
        f_seeds=True
        seed='S: >>'
    x=get_html("https://torrentapi.org/pubapi_v2.php?app_id=me&get_token=get_token",headers=base_header,timeout=10).json()
    token=x['token']
    if tv_movie=='movie':
     ur='https://torrentio.strem.fun/stream/movie/%s.json'%imdb_id
    elif tv_movie=='tv':
     ur='https://torrentio.strem.fun/stream/movie/{0}%3A{1}%3A{2}.json'.format(imdb_id,season,episode)
     
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    }
    if 1:
        
        y=get_html(ur,headers=headers,timeout=10).json()
       
        for results in y['streams']:
            
            nam=results['title']
            if f_seeds:
                regex='👤 (.+?) 💾'
                
                seeds=re.compile(regex).findall(nam)
                if len(seeds)>0:
                    seed=seeds[0]
                else:
                    continue
                if int(Addon.getSetting('min_seed'))>int(seed):
                    continue
                seed='S:%s>>,'%str(seed)
            if stop_all==1:
                break
            
            regex='💾(.+?)⚙️'
            s=re.compile(regex).findall(nam)
            size=0
            if len(s)>0:
                size=float(s[0].replace('GB','').replace('MB','').replace(",",'').strip())
                if 'MB' in s:
                   size=size/1000
            
            links=results['infoHash']
            try:
                lk='magnet:?xt=urn:btih:%s&dn=%s'%(links,que(nam))
            except:
                lk='magnet:?xt=urn:btih:%s&dn=%s'%(links,que(nam.encode('utf-8')))
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
            max_size=int(Addon.getSetting("size_limit"))
            
            
            if (size)<max_size:
               
                all_links.append((seed+nam,lk,str(size),res))

                global_var=all_links
    return global_var