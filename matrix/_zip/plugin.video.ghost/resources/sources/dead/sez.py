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
type=['tv','non_rd']

import urllib,logging,base64,json

def unescape( text):
        import htmlentitydefs
        def fixup(m):
            text = m.group(0)
            if text[:2] == '&#':
                # character reference
                try:
                    if text[:3] == '&#x':
                        return unichr(int(text[3:-1], 16))
                    else:
                        return unichr(int(text[2:-1]))
                except ValueError:
                    pass
            else:
                # named entity
                try:
                    text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
                except KeyError:
                    pass
            return text  # leave as is
        return re.sub('&#?\w+;', fixup, text)

def removeHtmlTags(sValue, sReplace=''):
        p = re.compile(r'<.*?>')
        return p.sub(sReplace, sValue)
def get_links(tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id):
    global global_var,stop_all

   
    
  
    if tv_movie=='movie':
        return []
    
    all_links=[]
    search_string=clean_name(original_title,1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        
        'Connection': 'keep-alive',
        
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    data = {
      'q': search_string
    }

    response = get_html('https://sezonlukdizi.vip/ajax/arama.asp', headers=headers, data=data).json()

    new_url=None
    regex='<tr>(.+?)</tr>'
    regex1=re.compile(regex,re.DOTALL)
    
    regex2=re.compile('src="(.+?)"')
    
    regex='data-options="(.+?)" data-player-container'
    regex3=re.compile(regex)
            
    for itt in response['results']['diziler']['results']:

        c_title=itt['title']
        if '(' in itt['title']:
            c_title=itt['title'].split(' (')[0]
        if not c_title.lower()==clean_name(original_title,1).lower():
            continue
        next_add='https://sezonlukdizi.vip'+itt['url'].replace('diziler','bolumler')


        x=get_html(next_add,headers=headers).content()
        
        m=regex1.findall(x)
        
        for item in m:
            
            regex="a href='(.+?)'"
            m2=re.compile(regex,re.DOTALL).findall(item)
            if len(m2)>0:
             if '/%s-sezon-%s-'%(season,episode)  in m2[0]:
            
                new_url='https://sezonlukdizi.vip'+m2[0]
                break
    if new_url:
        y=get_html(new_url,headers=headers).content()
        regex='div bid="(.+?)"'
        idd=re.compile(regex).findall(y)[0]
       
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://sezonlukdizi.vip',
            'Connection': 'keep-alive',
            'Referer': new_url,
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
        }

        data = {
          'bid': idd,
          'dil': '1'
        }
     
        response = get_html('https://sezonlukdizi.vip/ajax/dataAlternatif.asp', headers=headers, data=data).json()

    
        
        for itt in response['data']:
            data = {
              'id': itt['id']
            }

            response = get_html('https://sezonlukdizi.vip/ajax/dataEmbed.asp', headers=headers, data=data).content()
         
            e_url=regex2.findall(response)
        
            e_url=e_url[0].replace('odnoklassniki','ok')
            if 'http' not in e_url:
                e_url='http:'+e_url
          
            if 'ok.ru' not in e_url:
                continue
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            
            'Connection': 'keep-alive',
            
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
            }

            z=get_html(e_url,headers=headers).content()
            
            sHtmlContent=regex3.findall(z)[0]
            sHtmlContent = removeHtmlTags(sHtmlContent)
            sHtmlContent = unescape(sHtmlContent)#.decode('utf-8'))
                
           
            page = json.loads(sHtmlContent)
            page = json.loads(page['flashvars']['metadata'])
            url = []
            qua = []
            title=clean_name(original_title,1)+'.S%sE%s'%(season_n,episode_n)
            HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
            for x in page['videos']:
                
                api_call = '%s|User-Agent=%s&Accept=%s' % (x['url'], HEADERS['User-Agent'], HEADERS['Accept'])
                api_call = api_call + '&Referer=' + e_url + '&Origin=http://ok.ru'
                url.append(api_call)
                qua.append(x['name'])
                res=x['name'].replace('mobile','480').replace('lowest','480').replace('low','480').replace('sd','480').replace('hd','720')
                '''
                try_head = requests.head(x['url'],headers=base_header, stream=True,verify=False,timeout=15)
                f_size2=0
                
                if 'Content-Length' in try_head.headers:
          
                    if int(try_head.headers['Content-Length'])>(1024*1024):
                        f_size2=str(round(float(try_head.headers['Content-Length'])/(1024*1024*1024), 2))
                '''
                all_links.append((title,'Direct_link$$$'+api_call,str(0),res))
                       
                global_var=all_links
                
    return global_var
        
    