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
    from resources.modules.general import Addon,get_imdb,get_vstram_title
except:
  import Addon
type=['movie','tv','non_rd']

import urllib,logging,base64,json





color=all_colors[112]
        



def resolve_solaris(url,action,season,episode,original_title,id,id_s):
    global global_var,stop_all,all_links
   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': url+'-watch-online-free.html',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    x=get_html('https://ww1.solarmovie.id/user/servers/%s?ep=%s'%(id,id_s),headers=headers).content()
    regex='data-server="(.+?)"'
    match=re.compile(regex).findall(x)
    
    for num in match:
    
        
        params = (
            ('number', num),
            ('r', '0.8965728513584835undefined'),
            ('_', str(time.time())),
        )

        response = get_html(url, headers=headers, params=params).json()
        logging.warning(response)
        headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': url+'-watch-online-free.html',
        'Origin': 'https://www1.solarmovie.id/',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
        }
        head=urllib.urlencode(headers2)
       
        try:
            
            y=get_html(response[0]['src'],headers=headers2,stream=True).headers()
            logging.warning(y)
            if y.status_code==200:
                if 'label' in y:
                    res=y['label']
                else:
                    res='720'
                all_links.append((original_title,response[0]['src']+"|"+head,'Direct',res))
                global_var=all_links
        except:
            pass
    return all_links

def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all,all_links

    all_links=[]
    if tv_movie=='tv':
      url=domain_s+'solarmovie.id/search/%s'%(original_title.replace("Marvel's ",'').replace("%20","+").replace(" ","+")+'+season+'+season)
    else:
      url=domain_s+'solarmovie.id/search/%s'%(original_title.replace("%20","+").replace(" ","+")+'+'+show_original_year)
    
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    #'Host': 'solarmovie.id',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    }
    html=get_html(url,headers=headers).content()

    regex='data-id="(.+?)".+?data-href="(.+?)".+?data-name="(.+?)"'
    match=re.compile(regex,re.DOTALL).findall(html)
    
    for id,link,name in match:
        logging.warning(name)
        check=False
        if tv_movie=='tv':
         if 'Season '+season in name:
            x=get_html('https://solarmovie.id'+link,headers=headers).content()
         
            regex='data-ep-id="(.+?)".+?href="(.+?)".+?title="(.+?)"'
            match_ep=re.compile(regex,re.DOTALL).findall(x)
           
            check=False
            for id_ep,link_ep,name_ep in match_ep:
                if 'Episode %s:'%episode_n in name_ep:
                    id_s=id_ep
                  
                    check=True
              
        else:
           check=True
       
        if clean_name(original_title,1).lower() in name.lower() and check==True:
    
         link='https://solarmovie.id'+link
         logging.warning(link)
         if tv_movie=='movie':
           resolve_solaris(link,'getmovie','0','0',original_title,id,'0')
         else:
           
           resolve_solaris(link,'getEpisodeEmb',season,episode_n,original_title,id,id_s)
    return global_var
    