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
type=['movie','tv','non_rd']

import urllib,logging,base64,json





color=all_colors[112]
def get_vstram_title(original_name,html2):
    name1=original_name
   
    regex='"og:title" content="(.+?)"'
    match4=re.compile(regex).findall(html2)
  
    
    if len( match4)==0:
        
        regex='<Title>(.+?)</Title>'
        
        match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)==0:
         regex='name="fname" value="(.+?)"'
         match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)==0:
         regex='<title>(.+?)</title>'
         match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)==0:
         regex="title: '(.+?)',"
         match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)==0:
         regex='><span title="(.+?)"'
         match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)==0:
         regex='description" content="(.+?)"'
         match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)==0:
        regex='"title","(.+?)"'
        match4=re.compile(regex,re.DOTALL).findall(html2)
    if len(match4)>0:
        name1=match4[0]

    return name1.replace("."," ").replace('Watch','').replace('watch','').replace(' mp4','').replace('watch','').replace(' MP4','').replace(' mkv','').replace(' MKV','').replace("_",".")
    
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all
    all_links=[]
    if tv_movie=='tv':
        type_s='it'
    else:
        type_s='im'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.goojara.to',
        'Connection': 'keep-alive',
        
        'TE': 'Trailers',
    }

    data = {
      'q': original_title
    }

    x = get_html('https://www.goojara.to/xhrr.php', headers=headers, data=data).content()
    regex='a href="(.+?)".+?div class="(.+?)"><strong>(.+?)</strong>'

    m=re.compile(regex,re.DOTALL).findall(x)
    
    for lk,ty,name in m:
        if tv_movie=='tv':
            if ty==type_s and original_title.lower()==name.lower():
                y = get_html('https://www.goojara.to'+lk+'?s='+season, headers=headers).content()
                regex='<span class="sea"> (.+?)</span><span>Season (.+?)</span></div><div class="snfo"><h1><a href="(.+?)"'
                
                m2=re.compile(regex).findall(y)

                for ep,se,lk2 in m2:
                    if ep==episode_n and season==se:
                        z,cook = get_html('https://www.goojara.to'+lk2, headers=headers,get_cookies=True).content()
         
                        regex='a class="bcg" href="(.+?)"'
                        
                        m3=re.compile(regex).findall(z)
                        regex="\('(.+?)','(.+?)'\);"
                        m_cook=re.compile(regex).findall(z)
                        for lkk in m3:
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Connection': 'keep-alive',
                                'Upgrade-Insecure-Requests': '1',
                                
                            }
                          
                            cook[m_cook[0][0]]=m_cook[0][1]
                            try:
                                lkk,html=get_html(lkk.replace('Direct_link$$$','').replace('resolveprime','').replace('resolveurl',''),headers=headers,cookies=cook,get_content=True).geturl()
                            except:
                                continue
                          
                            if tv_movie=='tv':
                                nm=clean_name(original_title,1)+'.S%sE%s'%(season,episode)
                            title=get_vstram_title(nm,html)
                            if tv_movie=='tv' and 's%se%s'%(season_n,episode_n) not in title:
                                title=original_title+'.s%se%s'%(season_n,episode_n)
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
                            if '404' in title:
                                continue
                            if len(title)<2:
                                continue
                            all_links.append((title,'Direct_link$$$resolveurlresolveprime'+lkk,str(0),res))

                            global_var=all_links
        else:
            if ty==type_s and original_title.lower()==name.lower():
                y,cook = get_html('https://www.goojara.to'+lk, headers=headers,get_cookies=True).content()
                regex='a class="bcg" href="(.+?)"'
                        
                m3=re.compile(regex).findall(y)
                regex="\('(.+?)','(.+?)'\);"
                m_cook=re.compile(regex).findall(y)
                for lkk in m3:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        
                    }
                  
                    cook[m_cook[0][0]]=m_cook[0][1]
                    try:
                        lkk,html=get_html(lkk.replace('Direct_link$$$','').replace('resolveprime','').replace('resolveurl',''),headers=headers,cookies=cook,get_content=True).geturl()
                    except:
                        continue
                    
                    nm=clean_name(original_title,1)+'.'+show_original_year
                    title=get_vstram_title(nm,html)
                    if tv_movie=='tv' and 's%se%s'%(season_n,episode_n) not in title:
                            title=original_title+'.s%se%s'%(season_n,episode_n)
                    if len(title)<2:
                        continue
                    if '404' in title:
                        continue
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
                    if '404' in title:
                        continue
                    if len(title)<2:
                        continue
                    
                    all_links.append((title,'Direct_link$$$resolveurlresolveprime'+lkk,str(0),str(res)))

                    global_var=all_links
                            
    return global_var