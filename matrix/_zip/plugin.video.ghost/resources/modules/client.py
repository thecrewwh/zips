

import urllib,xbmc
import logging,json
from resources.modules import log
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])

base_header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',

            'Pragma': 'no-cache',
            
           
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            }
class get_html():
    
    def __init__(self, *args, **kwargs):#, url,headers=base_header,cookies={},data={},json={},params='',verify=False,get_cookies=False,timeout=10):
        
        
        self.url=args[0].replace(' ','%20')
  
        if len(self.url)>1:
            self.final_url=''
            self.html_in=''
            self.get_content=kwargs.get('get_content',False)
            self.head=kwargs.get('headers',base_header)
            self.cookies=kwargs.get('cookies',{})
            self.data=kwargs.get('data',{})
            self.verify=kwargs.get('verify',False)
            self.params=kwargs.get('params','')
            self.get_cookies=kwargs.get('get_cookies',False)
            self.json_data=kwargs.get('json',{})
            self.timeout=kwargs.get('timeout',10)
            self.status_code=0
            self.headers_return_dict={}
            self.delete=kwargs.get('delete',False)
            self.put=kwargs.get('put',False)
            
            self.cookies_get={}
            self.stream=kwargs.get('stream',False)
            self.post=kwargs.get('post',False)
        
            self.result=self.result()
        else:
            self.result=''
    def result(self):
       if KODI_VERSION>18:
            import urllib.error
            err_url=urllib.error
       else:
            import urllib
            import urllib2
            err_url=urllib2
       try:
    
        try:
            import cookielib
        except:
            import http.cookiejar
            cookielib = http.cookiejar
        if KODI_VERSION<=18:#kodi18
                cookjar = cookielib.CookieJar()
                handlers = [urllib2.HTTPCookieProcessor(cookjar),urllib2.HTTPHandler(), urllib2.HTTPSHandler()]
               
                opener = urllib2.build_opener(*handlers)
                added_params=''
                if self.cookies!={}:
                 
                    cookie_string = "; ".join([str(x)+"="+str(y) for x,y in self.cookies.items()])
               
                    self.head["Cookie"]=cookie_string
                if self.params!='':
                    try:
                        added_params='?'+urllib.urlencode( self.params ) 
                    except:
                        added_params='?'+( self.params ) 
                
                if self.data!={}:
                    try:
                        data=urllib.urlencode(self.data)
                    except Exception as e:
                        log.warning("error in client:"+str(e))
                        data=self.data
                    request = urllib2.Request(self.url+added_params,  headers=self.head,data=data)
                elif self.json_data!={}:
                    
                    
                    
                    request = urllib2.Request(self.url+added_params,  headers=self.head,data=json.dumps(self.json_data))
                else:
                  
                    request = urllib2.Request(self.url+added_params,  headers=self.head)
                
                if self.post:
                    request.get_method = lambda: 'POST'
                elif self.put:
                    request.get_method = lambda: 'PUT'
                elif self.delete:
                    request.get_method = lambda: 'DELETE'
                elif self.data=={} and self.json_data=={}:
                   
                    request.get_method = lambda: 'GET'
                else:
                    
                    request.get_method = lambda: 'POST'
        else:#kodi 19
                cookjar = cookielib.CookieJar()
                handlers = [urllib.request.HTTPCookieProcessor(cookjar),urllib.request.HTTPHandler(), urllib.request.HTTPSHandler()]
               
                opener = urllib.request.build_opener(*handlers)
                added_params=''
                if self.cookies!={}:
                 
                    cookie_string = "; ".join([str(x)+"="+str(y) for x,y in self.cookies.items()])
               
                    self.head["Cookie"]=cookie_string
                if self.params!='':
                    try:
                        added_params='?'+urllib.parse.urlencode( self.params ) 
                    except:
                            added_params='?'+( self.params ) 
                if self.data!={}:
                    try:
                        data=urllib.parse.urlencode(self.data).encode("utf-8")
                   
                    except:
                        data=self.data.encode("utf-8")
                    request = urllib.request.Request(self.url+added_params,  headers=self.head,data=data)
                    
                elif self.json_data!={}:
                    
                    
                    
                    request = urllib.request.Request(self.url+added_params,  headers=self.head,data=json.dumps(self.json_data).encode("utf-8"))
                else:
                  
                    request = urllib.request.Request(self.url+added_params,  headers=self.head)
                
                if self.post:
                    request.get_method = lambda: 'POST'
                elif self.put:
                    request.get_method = lambda: 'PUT'
                elif self.delete:
                    request.get_method = lambda: 'DELETE'
                elif self.data=={} and self.json_data=={}:
                   
                    request.get_method = lambda: 'GET'
                else:
                    
                    request.get_method = lambda: 'POST'
        
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
    
        prehtml = opener.open(request,timeout=self.timeout)
        
        self.final_url=prehtml.geturl()
        headers_return=prehtml.info().items()
        self.headers_return_dict={}
      
        for key,value in headers_return:
            self.headers_return_dict[key]=value
        
        self.status_code=prehtml.getcode()
        if self.stream==False:
            try:
                html=prehtml.read().decode('utf-8','ignore')
            except:
                html=prehtml.read()
           
            
            try:
                html=json.loads(str(html))
            except:
                pass
        else:
            html=''
        

        cookie_new={}
        for cook in cookjar:
          cookie_new[cook.name]=cook.value
        self.cookies_get=cookie_new
        self.html_in=html
        if self.get_cookies:
           
            return html,cookie_new
        else:
            return html
        
       except err_url.HTTPError as e:
            self.status_code=e.code
            return {'error_code':e.code}
    def json(self):
        return self.result
    def content(self):
        
        
        
       
        return (self.result)
    def text(self):
        return (self.result)
    
    def headers(self):
        
        
        
        return self.headers_return_dict
    def status_code(self):
        
        return self.status_code
    def geturl(self):
        if self.get_content:
            return self.final_url,self.html_in
        else:
            return self.final_url
    def cookies_get_only(self):
        return self.cookies_get