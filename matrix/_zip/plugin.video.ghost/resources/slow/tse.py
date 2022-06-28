# -*- coding: utf-8 -*-
import requests,re
import time
import threading
global global_var,stop_all#global
global_var=[]
stop_all=0

 
from resources.modules.general import clean_name,check_link,server_data,replaceHTMLCodes,domain_s,similar,cloudflare_request,all_colors,base_header
from  resources.modules import cache
try:
    from resources.modules.general import Addon
except:
  import Addon
type=['movie','tv','torrent']

import urllib2,urllib,logging,base64,json
class Thread(threading.Thread):
    def __init__(self, target, *args):
       
        self._target = target
        self._args = args
        
        
        threading.Thread.__init__(self)
        
    def run(self):
        
        self._target(*self._args)
def get_results(ur,all_links):
            global global_var,stop_all
            y=requests.get(ur,headers=base_header,timeout=10).content
            
            try:
                y=json.loads(y)
            except:
                return
            
            if stop_all==1:
                return 
            title=y['title']
            link=y['magnet']
            size=(float(y['size'])/(1024*1024*1024))
            
           
        
                
                
            
            
             
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
           
            
            max_size=int(Addon.getSetting("size_limit"))
            
            if size<max_size:
               
               all_links.append((title,link,str(size),res))
           
               global_var=all_links
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    import xbmc
    global_var=[]
    if tv_movie=='movie':
      search_url=[clean_name(original_title,1).replace(' ','%20')+'%20'+show_original_year]
      s_type='movies'
    else:
      if Addon.getSetting('debrid_select')=='0' :
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n,clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n,clean_name(original_title,1).replace(' ','%20')+'%20season%20'+season]
      else:
        search_url=[clean_name(original_title,1).replace(' ','%20')+'%20s'+season_n+'e'+episode_n]
      s_type='tv'
  
    
    
    all_links=[]
    
    thread=[]
    for itt in search_url:
                       
        x=requests.get('http://tse-api.gianlu.xyz/search?q='+(itt),headers=base_header,timeout=10).json()
        
        
        
        for items in x['result']:
            if stop_all==1:
                break
            
           
            ur=('http://tse-api.gianlu.xyz/getTorrent?e=%s&url=%s'%(items['engine'],items['url'].encode('base64'))).replace(' ','').replace('\n','').replace('\r','').replace('\t','')
            thread.append(Thread(get_results,ur,all_links))
            thread[len(thread)-1].setName('fill_table')
           
            thread[len(thread)-1].start()
            
    still_alive=True
    while(still_alive):
        still_alive=False
        for trd in thread:
            if trd.isAlive():
                still_alive=True
        if stop_all==1:
                break
        xbmc.sleep(100)
    return global_var
        
    