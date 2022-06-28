import re,time,logging,xbmc
from  resources.modules.client import get_html
from resources.modules import log
def get_youtube_link2(url):
        log.warning('start')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.onlinevideoconverter.com/youtube-converter',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.onlinevideoconverter.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        data = {
          'function': 'validate',
          'args[dummy]': '1',
          'args[urlEntryUser]': url,
          'args[fromConvert]': 'urlconverter',
          'args[requestExt]': 'mp4',
          'args[nbRetry]': '0',
          'args[videoResolution]': '-1',
          'args[audioBitrate]': '0',
          'args[audioFrequency]': '0',
          'args[channel]': 'stereo',
          'args[volume]': '0',
          'args[startFrom]': '-1',
          'args[endTo]': '-1',
          'args[custom_resx]': '-1',
          'args[custom_resy]': '-1',
          'args[advSettings]': 'false',
          'args[aspectRatio]': '-1'
        }

        response = get_html('https://www2.onlinevideoconverter.com/webservice', headers=headers, data=data).json()
        log.warning (response)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.onlinevideoconverter.com/youtube-converter',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.onlinevideoconverter.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        data = {
          'function': 'processVideo',
          'args[dummy]': '1',
          'args[urlEntryUser]': url,
          'args[fromConvert]': 'urlconverter',
          'args[requestExt]': 'mp4',
          'args[serverId]': response['result']['serverId'],
          'args[nbRetry]': '0',
          'args[title]': response['result']['title'],
          'args[keyHash]': response['result']['keyHash'],
          'args[serverUrl]': response['result']['serverUrl'],
          'args[id_process]': response['result']['id_process'],
          'args[videoResolution]': '-1',
          'args[audioBitrate]': '0',
          'args[audioFrequency]': '0',
          'args[channel]': 'stereo',
          'args[volume]': '0',
          'args[startFrom]': '-1',
          'args[endTo]': '-1',
          'args[custom_resx]': '-1',
          'args[custom_resy]': '-1',
          'args[advSettings]': 'false',
          'args[aspectRatio]': '-1'
        }

        response2 = get_html('https://www2.onlinevideoconverter.com/webservice', headers=headers, data=data).json()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.onlinevideoconverter.com/youtube-converter',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
        }

        data = {
          'id': response2['result']['dPageId']
        }

        html = get_html('https://www.onlinevideoconverter.com/success', headers=headers, data=data).content()
        
        regex="'url': '(.+?)'"
        match=re.compile(regex).findall(str(html))
        return match[0]
def get_youtube_link(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://qdownloader.io/',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }


    params = (
    ('url', url),
    )

    response = get_html('https://qdownloader.io/download', headers=headers, params=params).content()
    
    regex=' download="(.+?)" href="(.+?)"'
    match=re.compile(regex).findall(response)
    all_results=[]
    for name,link in match:
       
        return link.replace('&amp;','&')
        all_results.append((name,link.replace('&amp;','&')))
def get_youtube_link3(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }



    response = get_html('https://api.videograbber.net/api/video?uri='+url.encode('base64'), headers=headers).json()
    log.warning(response)
    log.warning('https://api.videograbber.net/api/video?uri='+url.encode('base64'))
    return response['data']['formats'][len(response['data']['formats'])-1]['url']

def get_youtube_link4(videoid):
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://keepvid.pro/download?video=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+videoid,
        'Content-Type': 'application/json',
        'Origin': 'https://keepvid.pro',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = '{"type":"crawler","params":{"video_url":"https://www.youtube.com/watch?v=%s"}}'%videoid
    
    response = get_html('https://v2api.keepvid.pro/v1/job', headers=headers, data=data).json()

    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://keepvid.pro/download?video=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+videoid,
        'Content-Type': 'application/json',
        'Origin': 'https://keepvid.pro',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('type', 'crawler'),
        ('job_id', response['data']['job_id']),
    )
    counter=0
    while 1:
        response = get_html('https://v2api.keepvid.pro/v1/check', headers=headers, params=params).json()
        if response['data']['state']!='active':
            break
     
        xbmc.sleep(10)
        counter+=1
        if counter>100:
            return ''
    return(response['data']['formats'][len(response['data']['formats'])-1]['url'])
def get_youtube_link5(url):
    import requests
    
    headers = {
        'authority': 'y2mate.guru',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://y2mate.guru',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://y2mate.guru/en7/',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        
    }
    x=get_html('https://y2mate.guru/en7/',headers=headers).content()
    regex='name="csrfmiddlewaretoken" value="(.+?)"'
    m=re.compile(regex).findall(x)
    cookies={'csrftoken':m[0]}
    data = '{"url":"%s"}'%url
   
    response = get_html('https://y2mate.guru/api/convert', headers=headers, data=data,cookies=cookies).json()
   
    max=0
    f_url=''
    for items in response['url']:
        if items['attr']['class']=='no-audio':
            continue
        if int(items['quality'])>max:
            max=int(items['quality'])
            f_url=items['url']
    log.warning(f_url)
    return f_url
def get_youtube5(videoid):
    import json
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://en.y2mate.guru',
        'Connection': 'keep-alive',
        'Referer': 'https://en.y2mate.guru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers',
    }

    data = {'url':'https://www.youtube.com/watch?v='+videoid}
    

    response = get_html('https://api.y2mate.guru/api/convert', headers=headers, json=data).json()
    max_q=0
    final_url=''
    for items in response['url']:
        if items['no_audio']==False and items['name']=='MP4':
            if int(items['quality'])>max_q:
                final_url=items['url']
    return final_url
