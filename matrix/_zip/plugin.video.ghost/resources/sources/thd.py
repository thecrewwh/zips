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

   
    
  
    
    
    all_links=[]
    if tv_movie=='movie':
     search_url=('%s+%s'%(clean_name(original_title,1).replace(' ','+'),show_original_year)).lower()
     type='load'
    else:
     
        search_url='%s'%(clean_name(original_title,1).replace(' ','+')).lower()
        type='publ'
    
    
    
    if 1:
        
        x=get_html('https://torrenthood.net/search/?q=%s&m=%s&t=0'%(search_url,type),headers=base_header,timeout=10).content()
      
        
        regex='<tr>(.+?)</tr>'
        macth_pre=re.compile(regex,re.DOTALL).findall(x)
        regex=' href="(.+?)"'
        regex1=re.compile(regex)
        
        regex='<div class="table-row-equal"(.+?)</form>'
        regex2=re.compile(regex,re.DOTALL)
        
        regex='<span class="info2">(.+?)<.+?Size: <b>(.+?)<.+?magnet:(.+?)\''
        regex3=re.compile(regex,re.DOTALL)
        
        
        regex='<div class="table-row-equal">(.+?)</form></div>'
        regex4=re.compile(regex,re.DOTALL)
                
        regex='<span class="info2" id="episode-(.+?)".+?onClick="(.+?)"'
        regex5=re.compile(regex,re.DOTALL)
        
        regex='<span id="blue">Full Season.+?span class="info4">(.+?)<'
        regex6=re.compile(regex,re.DOTALL)
                         
                         
        for itm in macth_pre:
            
            regex=' href="(.+?)"'
            ittm=regex1.findall(itm)[0]
            
            if clean_name(original_title,1).lower().replace(' ','-') not in ittm:
                continue
            y=get_html(ittm,headers=base_header,timeout=10).content()
            if tv_movie=='movie':
                regex='<div class="table-row-equal"(.+?)</form>'
                m_p=regex2.findall(y)
                for mpp in m_p:
                    
                    regex='<span class="info2">(.+?)<.+?Size: <b>(.+?)<.+?magnet:(.+?)\''
                    m_pre=regex3.findall(mpp)
                    if len(m_pre)==0:
                        continue
                    nm=m_pre[0][0]
                    title=nm
                    size=m_pre[0][1]
                    lk='magnet:'+m_pre[0][2]
                    if len(title)>0:
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
                    else:
                        res='720'
                    
                   
                     
                    try:
                         o_size=size
                         size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                         if 'MB' in o_size:
                           size=size/1000
                    except:
                        size=0
                    max_size=int(Addon.getSetting("size_limit"))
              
                    if size<max_size:
                  
                       all_links.append((nm,lk,str(size),res))
                   
                       global_var=all_links
                
            else:
                
                if 'season-%s-'%season not in ittm and '-s%s'%season_n not in ittm:
                    continue
    
                
                regex='<div class="table-row-equal">(.+?)</form></div>'
                m_pre=regex4.findall(y)
                
                for ittm2 in m_pre:
           
                    regex='<span class="info2" id="episode-(.+?)".+?onClick="(.+?)"'
                    m_in=regex5.findall(ittm2)
                    for idd,lk in m_in:
                         
                         if stop_all==1:
                            break
                         if tv_movie=='tv':
                            
                            if episode != idd:
                                continue
                         if 'magnet' not in lk:
                            continue
                         regex='<span id="blue">Full Season.+?span class="info4">(.+?)<'
                         title=regex6.findall(y)
                         lk=lk.replace("self.location='",'').replace("'",'')
                         nm=clean_name(original_title,1)
                         if len(title)>0:
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
                         else:
                            res='720'
                        
                       
                         regex='Download Size\: <b>(.+?) \(per episode\)'
                         size=re.compile(regex).findall(y)
                         if len(size)>0:
                            try:
                                 o_size=size[0]
                                 size=float(o_size.replace('GB','').replace('MB','').replace(",",'').strip())
                                 if 'MB' in o_size:
                                   size=size/1000
                            except:
                                size=0
                         else:
                            size=0
    
                         max_size=int(Addon.getSetting("size_limit"))
                  
                         if size<max_size:
                      
                           all_links.append((nm,lk,str(size),res))
                       
                           global_var=all_links
    return global_var
        
    