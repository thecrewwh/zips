# -*- coding: utf-8 -*-
import urllib2,re,logging,urllib,xbmc,sys
from resources.modules import log
from resources.modules import mediaurl
__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
def fix_q(quality):
    
    
    if '1080' in quality:
      f_q=0
    elif '720' in quality:
      f_q=1
    elif '480' in quality:
      f_q=2
   
    elif '360' in quality or 'sd' in quality.lower():
      f_q=3
   
    return f_q
def __getIdFromUrl( sUrl):
        sPattern = 'google.+?([a-zA-Z0-9-_]{20,40})'
        
        aResult = re.compile(sPattern).findall(sUrl)
        if (aResult[0] == True):
            return aResult[1][0]

        return ''
def getPublicStream_vstream(o_url):
        url = []
        qua = []
        api_call = ''

        # reformatage du lien
        #sId = __getIdFromUrl(o_url)
        sUrl =o_url# 'https://drive.google.com/file/d/' + sId + '/view'
        log.warning(sUrl)
        req = urllib2.Request(sUrl)
        response = urllib2.urlopen(req)
        sHtmlContent = response.read()

        Headers = response.headers
        response.close()

        # listage des cookies
        c = Headers['Set-Cookie']
        c2 = re.findall('(?:^|,) *([^;,]+?)=([^;,\/]+?);', c)
        if c2:
            cookies = ''
            for cook in c2:
                cookies = cookies + cook[0] + '=' + cook[1] + ';'

        sPattern = '\["fmt_stream_map","([^"]+)"]'


        aResult = re.compile(sPattern).findall(sHtmlContent)
        log.warning(aResult)
        if not aResult[0]:
            if '"errorcode","150"]' in sHtmlContent:
                log.warning("Eroor")
            return False, False

        sListUrl = aResult[1][0]

        if sListUrl:
            aResult2 = oParser.parse(sHtmlContent, '([0-9]+)\/([0-9]+x[0-9]+)\/')

        # liste les qualitee
            r = oParser.parse(sListUrl, '([0-9]+)\|([^,]+)')
            for item in r[1]:
                url.append(item[1].decode('unicode-escape'))
                for i in aResult2[1]:
                    if item[0] == i[0]:
                        qua.append(i[1])

        # Affichage du tableau
        
        log.warning(qua)
        log.warning(url)
        api_call = dialog().VSselectqual(qua, url)
        api_call = api_call + '|User-Agent=' + UA + '&Cookie=' + cookies

        if (api_call):
            return True, api_call

        return False, False
def getPublicStream(url):
        import cookielib
        

        pquality=-1
        pformat=-1
        acodec=-1

        mediaURLs = []
  
       
        cookies = cookielib.LWPCookieJar()
        handlers = [
            urllib2.HTTPHandler(),
            urllib2.HTTPSHandler(),
            urllib2.HTTPCookieProcessor(cookies)
            ]
        opener = urllib2.build_opener(*handlers)
        req = urllib2.Request(url)

        req.add_header('User-agent',__USERAGENT__)
        result= opener.open(req)
        for cookie in cookies:
            if cookie.name=='DRIVE_STREAM':
              value=cookie.value
        regex='https://drive.google.com/file/d/(.+?)(?:/view|$)'
        
        google_id=re.compile(regex).findall(url)
        if len(google_id)==0:
            google_id=url.split('id=')[1]
        else:
            google_id=google_id[0]
        url='https://drive.google.com/get_video_info?docid='+google_id
        
              
        
        

        pquality=-1
        pformat=-1
        acodec=-1

        mediaURLs = []
  
       
        
        
        
        #response.close()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        

        log.warning(cookies)
        log.warning(url)
        req = urllib2.Request(url)

        req.add_header('User-agent',__USERAGENT__)
        response_data= opener.open(req).read()
        log.warning(response_data)
        #response_data = requests.get(url, headers=headers, cookies=cookies).content
        response_data=urllib.unquote_plus(response_data)
        

        fmtlist=None
        regex='fmt_list\=(.+?)\&'
        m=re.compile(regex).findall(response_data)

        log.warning('Found m')
        log.warning(m)
        if len(m)==0:
            if 'reason=' in response_data:
                reason=re.compile('reason\=(.+?)&').findall(response_data)[0]
                #xbmc.executebuiltin((u'Notification(%s,%s)' % ('Mando', reason)))
                return 'false',value
                sys.exit(1)
        for r in re.finditer('fmt_list\=(.+?)\&' ,
                             response_data, re.DOTALL):
            fmtlist = r.group(1)
        if not fmtlist:

            fmtlist = re.compile('"fmt_list","(.+?)"').findall(response_data)
        title = ''
        for r in re.finditer('title\=(.+?)&' ,
                             response_data, re.DOTALL):
            title = r.group(1)

 
        itagDB={}
        containerDB = {'x-flv':'flv', 'webm': 'WebM', 'mp4;+codecs="avc1.42001E,+mp4a.40.2"': 'MP4'}
        for r in re.finditer('(\d+)/(\d+)x(\d+)/(\d+/\d+/\d+)\&?\,?' ,
                               fmtlist, re.DOTALL):
              (itag,resolution1,resolution2,codec) = r.groups()

              if codec == '9/0/115':
                itagDB[itag] = {'resolution': resolution2, 'codec': 'h.264/aac'}
              elif codec == '99/0/0':
                itagDB[itag] = {'resolution': resolution2, 'codec': 'VP8/vorbis'}
              else:
                itagDB[itag] = {'resolution': resolution2}

        for r in re.finditer('url_encoded_fmt_stream_map\=(.+?)\&timestamp' ,
                             response_data, re.DOTALL):
            urls = r.group(1)


        log.warning(urls)
        urls = urllib.unquote(urllib.unquote(urllib.unquote(urllib.unquote(urllib.unquote(urls)))))
        urls = re.sub('\\\\u003d', '=', urls)
        urls = re.sub('\\\\u0026', '&', urls)


#        urls = re.sub('\d+\&url\='+self.PROTOCOL, '\@', urls)
        urls = re.sub('\&url\='+ 'https://', '\@', urls)

#        for r in re.finditer('\@([^\@]+)' ,urls):
#          videoURL = r.group(0)
#        videoURL1 = self.PROTOCOL + videoURL


        # fetch format type and quality for each stream
        count=0
        
        for r in re.finditer('\@([^\@]+)' ,urls):
                videoURL = r.group(1)
                for q in re.finditer('itag\=(\d+).*?type\=video\/([^\&]+)\&quality\=(\w+)' ,
                             videoURL, re.DOTALL):
                    (itag,container,quality) = q.groups()
                    count = count + 1
                    order=0
                    if pquality > -1 or pformat > -1 or acodec > -1:
                        if int(itagDB[itag]['resolution']) == 1080:
                            if pquality == 0:
                                order = order + 1000
                            elif pquality == 1:
                                order = order + 3000
                            elif pquality == 3:
                                order = order + 9000
                        elif int(itagDB[itag]['resolution']) == 720:
                            if pquality == 0:
                                order = order + 2000
                            elif pquality == 1:
                                order = order + 1000
                            elif pquality == 3:
                                order = order + 9000
                        elif int(itagDB[itag]['resolution']) == 480:
                            if pquality == 0:
                                order = order + 3000
                            elif pquality == 1:
                                order = order + 2000
                            elif pquality == 3:
                                order = order + 1000
                        elif int(itagDB[itag]['resolution']) < 480:
                            if pquality == 0:
                                order = order + 4000
                            elif pquality == 1:
                                order = order + 3000
                            elif pquality == 3:
                                order = order + 2000
                    try:
                        if itagDB[itag]['codec'] == 'VP8/vorbis':
                            if acodec == 1:
                                order = order + 90000
                            else:
                                order = order + 10000
                    except :
                        order = order + 30000

                    try:
                        if containerDB[container] == 'MP4':
                            if pformat == 0 or pformat == 1:
                                order = order + 100
                            elif pformat == 3 or pformat == 4:
                                order = order + 200
                            else:
                                order = order + 300
                        elif containerDB[container] == 'flv':
                            if pformat == 2 or pformat == 3:
                                order = order + 100
                            elif pformat == 1 or pformat == 5:
                                order = order + 200
                            else:
                                order = order + 300
                        elif containerDB[container] == 'WebM':
                            if pformat == 4 or pformat == 5:
                                order = order + 100
                            elif pformat == 0 or pformat == 1:
                                order = order + 200
                            else:
                                order = order + 300
                        else:
                            order = order + 100
                    except :
                        pass
 
                    
                    try:
                        mediaURLs.append( mediaurl.mediaurl('https://' + videoURL, itagDB[itag]['resolution'] + ' - ' + containerDB[container] + ' - ' + itagDB[itag]['codec'], str(itagDB[itag]['resolution'])+ '_' + str(order+count), order+count, title=title))
                    except KeyError:
                        mediaURLs.append(mediaurl.mediaurl('https://'+ videoURL, itagDB[itag]['resolution'] + ' - ' + container, str(itagDB[itag]['resolution'])+ '_' + str(order+count), order+count, title=title))
                    log.warning('mediaURLs')
                    log.warning(mediaURLs)
        return mediaURLs,value
        
def googledrive_resolve(url):
    
    global tv_mode
    
    links_data,cookie=getPublicStream(url)
    if links_data=='false':
        return False,[]
    mediaURLs = sorted(links_data)
    options = []
    all_mediaURLs=[]
   
    for mediaURL in mediaURLs:

        if '4k' in mediaURL.qualityDesc:
           
           options.append(4000)
        elif '1080' in mediaURL.qualityDesc:
           
           options.append(1080)
        elif '720' in mediaURL.qualityDesc:
           
           options.append(720)
        elif '480' in mediaURL.qualityDesc:
           
           options.append(480)
        elif '360' in mediaURL.qualityDesc:
           
           options.append(360)
        elif '240' in mediaURL.qualityDesc:
           
           options.append(240)
        else:
           
           options.append(0)
        all_mediaURLs.append((mediaURL.url,fix_q(mediaURL.qualityDesc)))
    
    qualities=options
    qualities.sort(reverse=True)
    all_mediaURLs=sorted(all_mediaURLs, key=lambda x: x[1], reverse=True)
    playbackURL,qul = all_mediaURLs[len(all_mediaURLs)-1]
    if 0:
            f_l=qualities[0]
            max_q='2160'
            
            xx=0
            p_qualities=[]
            for items in qualities:
               
               if fix_q(items)<max_q:
                
                 p_qualities.append(xx)
               xx+=1
            yy=0
            f_q=[]
            for items in qualities:
                 if yy not in p_qualities:
                  f_q.append(items)
                 yy+=1
            qualities=f_q
            if len(qualities)>0:
              f_l=len(qualities)-1
            
            playbackURL,qul = all_mediaURLs[f_l]
         
    


    final_link=playbackURL
    return (final_link+'||Cookie=DRIVE_STREAM%3D'+cookie),qualities
   
