 # -*- coding: utf-8 -*-
import  json, re, time,logging,sys,xbmcgui,xbmc,os
from  resources.modules.client import get_html
global play_status_rd,break_window_rd
from resources.modules import log
play_status_rd=''
break_window_rd=False
base_header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',

            'Pragma': 'no-cache',
            
           
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            }

import xbmcaddon
Addon = xbmcaddon.Addon()
try:
    resuaddon=xbmcaddon.Addon('script.module.resolveurl')
except Exception as e:
    resuaddon=None
    pass
log.warning('resuaddon:'+str(resuaddon))
def copy2clip(txt):
    import subprocess
    platform = sys.platform

    if platform == 'win32':
        try:
            cmd = 'echo ' + txt.strip() + '|clip'
            return subprocess.check_call(cmd, shell=True)
            pass
        except:
            pass
    elif platform == 'linux2':
        try:
            from subprocess import Popen, PIPE

            p = Popen(['xsel', '-pi'], stdin=PIPE)
            p.communicate(input=txt)
        except:
            pass
    else:
        pass
    pass
def colorString(text, color=None):
    

    if color == 'default' or color== '' or color == None:
        color = ''
        if color == '':
            color = 'deepskyblue'

    try:
        return '[COLOR ' + str(color) + ']' + text + '[/COLOR]'
    except:
        return '[COLOR ' + str(color) + ']' + text   + '[/COLOR]'
class RealDebrid:
    
    def __init__(self):
        self.count_rd=0
        self.count_refresh=0
        try:
            self.ClientID = resuaddon.getSetting('RealDebridResolver_client_id') 
        except:
            self.ClientID = Addon.getSetting('rd.client_id')
        if self.ClientID == '':
            self.ClientID = 'X245A4XAIBGVM'
        self.OauthUrl = 'https://api.real-debrid.com/oauth/v2/'
        self.DeviceCodeUrl = "device/code?%s"
        self.DeviceCredUrl = "device/credentials?%s"
        self.TokenUrl = "token"
        try:
            self.token = resuaddon.getSetting('RealDebridResolver_token') 
        except:
            self.token = Addon.getSetting('rd.auth')
        try:
            self.ClientSecret = resuaddon.getSetting('RealDebridResolver_client_secret') 
        except:
            self.ClientSecret = Addon.getSetting('rd.secret')
        if self.ClientSecret=='':
            self.auth()
        try:
            self.refresh = resuaddon.getSetting('RealDebridResolver_refresh') 
        except:
            self.refresh = Addon.getSetting('rd.refresh')
        self.DeviceCode = ''
        
        self.OauthTimeout = 0
        self.OauthTimeStep = 0
        self.BaseUrl = "https://api.real-debrid.com/rest/1.0/"

    def auth_loop(self,dp):
        
        if dp.iscanceled():
            dp.close()
            return
        
        time.sleep(self.OauthTimeStep)
        url = "client_id=%s&code=%s" % (self.ClientID, self.DeviceCode)
        url = self.OauthUrl + self.DeviceCredUrl % url
  
        response = get_html(url).json()

        error=response.get("error","OK")
        if error==1 or 'client_id' not in response:
            
            return
        else:
            dp.close()
            
            Addon.setSetting('rd.client_id', response['client_id'])
            Addon.setSetting('rd.secret', response['client_secret'])
            try:
                resuaddon.setSetting('RealDebridResolver_client_id', response['client_id'])
                resuaddon.setSetting('RealDebridResolver_client_secret', response['client_secret'])
            except:
                pass
            self.ClientSecret = response['client_secret']
            self.ClientID = response['client_id']
            log.warning('All Good')
            return
    def list_torrents(self):
        url = "torrents"
        response = self.get_url(url)
        return response
        
    def get_history(self,page):
        
        
        return self.get_url("downloads?page=" + page)
    def auto_auth(self,code,o_response):
        import time
        username=Addon.getSetting("rd_user")
        password=Addon.getSetting("rd_pass")
        import datetime
        dp = xbmcgui . DialogProgress ( )
        dp.create("Real Debrid Auth","Please Wait....", 'Wait...Auto Auth...')
        dp.update(0, "Real Debrid Auth", 'Auto Auth...')
        
        now=int(time.mktime(datetime.datetime.now().timetuple())) * 1000
        cookies = {
            'https': '1',
            'lang': 'en',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://real-debrid.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        params = (
            ('user', username),
            ('pass', password),
            ('pin_challenge', ''),
            ('pin_answer', 'PIN: 000000'),
            ('time', now),
                     
        )

        response = get_html('https://real-debrid.com/ajax/login.php', headers=headers, params=params, cookies=cookies).json()
        if response['error']==1:
            xbmcgui.Dialog().ok('Error', response['message'])
            return 'bad'
        if response['captcha']==1:
            xbmcgui.Dialog().ok('Error', 'Error in Auto connection')
            return 'bad'
        dp.update(int(30), Addon.getLocalizedString(32072),Addon.getLocalizedString(32258), 'Ok' )

        cookies = {
            'https': '1',
            'lang': 'en',
            'auth': response['cookie'].split('=')[1],
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://real-debrid.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        data = {
          'usercode': code,
          'action': 'Continue'
        }
        
        response2 = get_html('https://real-debrid.com/device', headers=headers, cookies=cookies, data=data)
        dp.update(int(60), Addon.getLocalizedString(32072),Addon.getLocalizedString(32298)+code, 'Ok' )
        cookies = {
            'https': '1',
            'lang': 'en',
            'auth': response['cookie'].split('=')[1],
            'language': 'en_GB',
            'amazon-pay-connectedAuth': 'connectedAuth_general',
            'session-set': 'true',
            'amazon-pay-abtesting-new-widgets': 'true',
            'amazon-pay-abtesting-apa-migration': 'true',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://real-debrid.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        params = (
            ('client_id', self.ClientID),
            ('device_id', o_response['device_code']),
        )

        data = {
          'action': 'Allow'
        }

        response = get_html('https://real-debrid.com/authorize', headers=headers, params=params, cookies=cookies, data=data)

        dp.update(int(90), Addon.getLocalizedString(32072),Addon.getLocalizedString(32079), 'Ok' )
       
        self.OauthTimeout = int(o_response['expires_in'])
        self.OauthTimeStep = int(o_response['interval'])
        self.DeviceCode = o_response['device_code']
        counter=0
        while self.ClientSecret == '':
            dp.update(int(100), Addon.getLocalizedString(32072),Addon.getLocalizedString(32080), str(counter) )
            self.auth_loop(dp)
            
            counter+=1
            if dp.iscanceled():
              dp.close()
              return 0
            xbmc.sleep(100)
 
        self.token_request()
        
        xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), Addon.getLocalizedString(32081))).encode('utf-8'))
        return 'ok'
    def auth(self):

        self.ClientSecret = ''
        self.ClientID = 'X245A4XAIBGVM'
        url = ("client_id=%s&new_credentials=yes" % self.ClientID)
        url = self.OauthUrl + self.DeviceCodeUrl % url
     
        response = get_html(url).json()

        if 1:
            copy2clip(response['user_code'])

        
            dp = xbmcgui . DialogProgress ( )
            dp.create("Real Debrid "+Addon.getLocalizedString(32282),Addon.getLocalizedString(32283) + ' %s' % colorString('https://real-debrid.com/device')+'\n'+ Addon.getLocalizedString(32284)  + ' %s' % colorString(response['user_code'])+'\n'+ Addon.getLocalizedString(32285))
            dp.update(-1, Addon.getLocalizedString(32283) + ' %s' % colorString('https://real-debrid.com/device')+'\n'+ Addon.getLocalizedString(32284) + ' %s' % colorString(response['user_code'])+'\n'+Addon.getLocalizedString(32285))
            
        
            self.OauthTimeout = int(response['expires_in'])
            self.OauthTimeStep = int(response['interval'])
            self.DeviceCode = response['device_code']
            while self.ClientSecret == '':
                self.auth_loop(dp)
                if dp.iscanceled():
                  dp.close()
                  return 0
                xbmc.sleep(300)
                
            self.token_request()

            return 0
    def token_request(self):
        import time

        if self.ClientSecret == '':
            return

        postData = {'client_id': self.ClientID,
                    'client_secret': self.ClientSecret,
                    'code': self.DeviceCode,
                    'grant_type': 'http://oauth.net/grant_type/device/1.0'}

        url = self.OauthUrl + self.TokenUrl
        response = get_html(url, data=postData).json()

       
 
        Addon.setSetting('rd.auth', response['access_token'])
        Addon.setSetting('rd.refresh', response['refresh_token'])
        try:
            resuaddon.setSetting('RealDebridResolver_token', response['access_token'])
            resuaddon.setSetting('RealDebridResolver_refresh', response['refresh_token'])
        except:
            pass
        self.token = response['access_token']
        self.refresh = response['refresh_token']

        Addon.setSetting('rd.expiry', str(time.time() + int(response['expires_in'])))

       
   

    def refreshToken(self):
        import time
        
        postData = {'grant_type': 'http://oauth.net/grant_type/device/1.0',
                    'code': self.refresh,
                    'client_secret': self.ClientSecret,
                    'client_id': self.ClientID
                    }
        url = self.OauthUrl + 'token'
        response = get_html(url, data=postData).json()
        #response =self.post_url(url, postData=postData)
        log.warning(response)
        if 'error_code' in response:
            xbmcgui.Dialog().ok(Addon.getAddonInfo('name'), Addon.getLocalizedString(32286)+', [B]'+'error_code'+'[/B]')
            self.auth()
            return '0'
        try:
            if 'access_token' not in response:
                if 'error' in response:
                    added=str(response['error'])
                else:
                    added=''
                xbmcgui.Dialog().ok(Addon.getAddonInfo('name'), Addon.getLocalizedString(32286)+', [B]'+added+'[/B]')
                self.auth()
                return '0'
        except:
            pass
        self.token = response['access_token']
        self.refresh = response['refresh_token']
        try:
            resuaddon.setSetting('RealDebridResolver_token', self.token)
            resuaddon.setSetting('RealDebridResolver_refresh', self.refresh)
            resuaddon.setSetting('RealDebridResolver_refresh', self.refresh)
        except:
            pass
            
        Addon.setSetting('rd.auth', self.token)
        Addon.setSetting('rd.refresh', self.refresh)
        Addon.setSetting('rd.expiry', str(time.time() + int(response['expires_in'])))
 
        ###############################################
        # To be FINISHED FINISH ME
        ###############################################
    def check_link(self,media_id):
        
        unrestrict_link_path = 'unrestrict/check'
        url =  ( unrestrict_link_path)
        postData = {'link': media_id}
        result = self.post_url(url, postData)
        return result
    def get_link(self,media_id):
        
        unrestrict_link_path = 'unrestrict/link'
        url =  ( unrestrict_link_path)
        postData = {'link': media_id}
        result = self.post_url(url, postData)
        return result
    def post_url(self, url, postData, fail_check=False,dp=None):
        global play_status_rd
        original_url = url
        url = self.BaseUrl + url
        if not fail_check:
            if '?' not in url:
                url += "?auth_token=%s" % self.token
            else:
                url += "&auth_token=%s" % self.token
        if dp:
            dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ "send req."+'\n'+ '')
            play_status_rd="send req."
        response = get_html(url, data=postData).json()
        if dp:
            dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ str(response)+'\n'+ '')
            play_status_rd=str(response)
        if 'error_code' in response:
            self.count_rd+=1
                
            if self.count_rd>4:
                xbmcgui.Dialog().ok(str(response['error_code']), 'Error in RD8 comm Try another link or check subscription')
                return '0'
            log.warning('response2:'+str(response))
            if dp:
                dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ str('refreshToken')+'\n'+ '')
                play_status_rd=str('refreshToken')
            self.refreshToken()
            response = self.post_url(original_url,postData, fail_check=False,dp=dp)
            if 'error_code' in response:
                xbmcgui.Dialog().ok('Error', original_url)
                return '0'
            xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'Refresh Token:'+str(self.count_refresh))))
            self.count_refresh+=1
            if self.count_refresh>4:
                    xbmcgui.Dialog().ok('Error', 'Error in RD7 comm')
                    return '0'
                    
        jresonce= (response)
        if type(jresonce)!=dict:
           
        
            jresonce=False
        if jresonce:
         if 'error' in jresonce:
          if 'bad_token' in jresonce['error'] or 'Bad Request' in jresonce['error']:
 
            
            if not fail_check:
                self.count_rd+=1
                
                if self.count_rd>4:
                    xbmcgui.Dialog().ok('Error', jresonce['error'])
                    return '0'
                self.refreshToken()
                if dp:
                    dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ str('refreshToken post_url')+'\n'+ '')
                    play_status_rd=str('refreshToken post_url')
                response = self.post_url(original_url,postData, fail_check=False)
                if dp:
                    dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ str(response)+'\n'+ '')
                    play_status_rd=str(response)
        return response
    def get_url_new1(self, url,data, fail_check=False):
        
        original_url = url
        url = self.BaseUrl + url
        url += "?auth_token=%s" % self.token

        response = get_html(url,data=data,timeout=20).json()
    
     
        
        return response
    def get_url_new(self, url,data, fail_check=False):
        
        original_url = url
        url = self.BaseUrl + url
        url += "?auth_token=%s" % self.token

        response = get_html(url,data=data,put=True).json()
    
     
        
        return response
    def get_url(self, url, fail_check=False):
        
        original_url = url
        url = self.BaseUrl + url
        if not fail_check:
            
            if '?' not in url:
                url += "?auth_token=%s" % self.token
            else:
                url += "&auth_token=%s" % self.token
        a=time.time()
        log.warning('Send req time:'+str(a))
       
        response = get_html(url,headers=base_header).json()
        log.warning('Got req time:'+str(a))
        
        if 'error_code' in response:
            self.count_rd+=1
            if self.count_rd>4:
                        xbmcgui.Dialog().ok('Error', 'Error in  RD')
                        return '0'
            self.refreshToken()
            response = self.get_url(original_url, fail_check=False)
        jresonce= response
        if type(jresonce)!=dict:
          
            jresonce=False
        if jresonce:
          if 'error' in jresonce:
            
            log.warning(jresonce)
            if 'bad_token' in jresonce['error'] or 'Bad Request' in jresonce['error']:
   
               
                if not fail_check:
                    self.count_rd+=1
                    if self.count_rd>4:
                        xbmcgui.Dialog().ok('Error', 'Error in  RD')
                        return '0'
                    self.refreshToken()
                    response = self.get_url(original_url, fail_check=False)
        
        return response

    def checkHash(self, hashList):
        log.warning('making hash list')
        all_h=[]
        hashString = ''
        if isinstance(hashList, list):
            for i in hashList:
               if len(i)>5:
                hashString += '/%s' % i
        else:
            hashString = "/" + hashList
        log.warning('Sending hash list')
        return self.get_url("torrents/instantAvailability" + hashString.replace('//','/'))

    def addMagnet(self, magnet,dp=None):
        global play_status_rd
        postData = {'magnet': magnet}
        url = 'torrents/addMagnet'
        if dp:
            dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+"Send Post"+'\n'+ '')
        play_status_rd="Send Post"
        response = self.post_url(url, postData,dp=dp)
        if dp:
            dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ "Got Post"+'\n'+ '')
        play_status_rd="Got Post"
        return response

    def list_torrents(self):
        url = "torrents"
        response = self.get_url(url)
        return response

    def torrentInfo(self, id):
        url = "torrents/info/%s" % id
        return self.get_url(url)

    def torrentSelect(self, torrentID, fileID):
        url = "torrents/selectFiles/%s" % torrentID
        postData = {'files': fileID}
        return self.post_url(url, postData)

    def unrestrict_link(self, link):
        url = 'unrestrict/link'
        postData = {'link': link}
        response = self.post_url(url, postData)
        try:
            return response['download']
        except:
            return None
    def select_torrent_files(self,torrent_id, file_ids):
        uri = 'torrents/selectFiles/' + torrent_id
        if type(file_ids) is list:
            files = ','.join(file_ids)
        else:
            files = file_ids
        #RD.request(uri, data={"files": str(files)}, auth=True, encode_data=False)

        return self.post_url(uri, {"files": str(files['id'])})
       
    def deleteTorrent(self, id):
        
        url = "torrents/delete/%s&auth_token=%s" % (id, self.token)
        response = get_html(self.BaseUrl + url,delete=True)
        
        
    def remove_history(self, id):
        
        url = "downloads/delete/%s&auth_token=%s" % (id, self.token)
        response = get_html(self.BaseUrl + url,delete=True)
       
    def addtorrent(self,url):
        
        uri = 'torrents/addTorrent'
        file = open(url, 'rb') 
        dp = xbmcgui . DialogProgress ( )
        dp.create("Real Debrid","Starting"+'\n'+ ""+'\n'+ '')
        
    
        torrent=(self.get_url_new(uri,file))

       
        
        if 'id' in torrent:#try:
            res = self.torrentInfo(torrent['id'])
     
            if res['status']=='waiting_files_selection':
                   
                    fileIDString = ''
                    
                
                    if len(res['files'])>0:
                        max_size=0
                        for items in res['files']:
                            if items['bytes']>max_size:
                                max_size=items['bytes']
                                f_id=items['id']
                        start_file=f_id
                        
                       
                        self.torrentSelect(torrent['id'], start_file)#go
            f_size=0
            size=0
            status=''
            while status!='downloaded':
               
                status=res['status']
                size=res['bytes']
                unit=''
                unit2=''
                f_size=0
                f_size2=0
                if size>1024:
                    f_size=float(size)/1024
                    unit='Kb'
                if size>(1024*1024):
                    f_size=float(size)/(1024*1024)
                    unit='Mb'
                if size>(1024*1024*1024):
                    f_size=float(size)/(1024*1024*1024)
                    unit='Gb'
                size2=res['original_bytes']
                if size2>1024:
                    f_size2=float(size2)/1024
                    unit2='Kb'
                if size2>(1024*1024):
                    f_size2=float(size2)/(1024*1024)
                    unit2='Mb'
                if size2>(1024*1024*1024):
                    f_size2=float(size2)/(1024*1024*1024)
                    unit2='Gb'
                seed=''
                if 'seeders' in res:
                
                    seed='S-'+str(res['seeders'])
                if 'speed' in res:
                    unit3='b/s'
                    f_size3=res['speed']
                    if res['speed']>1024:
                        f_size3=float(res['speed'])/1024
                        unit3='Kb/s'
                    if res['speed']>(1024*1024):
                        f_size3=float(res['speed'])/(1024*1024)
                        unit3='Mb/s'
                    if res['speed']>(1024*1024*1024):
                        f_size3=float(res['speed'])/(1024*1024*1024)
                        unit3='Gb/s'
                    
                    speed=str(round(f_size3,2))+unit3
                else:
                    speed=''
                prog=0
                if 'progress' in res:
                    prog=res['progress']
                dp.update(prog, res['status']+' [COLOR yellow]'+seed+' '+speed+'[/COLOR]', res['original_filename']+'\n'+ str(round(f_size,2))+' '+unit+'/'+str(round(f_size2,2))+' '+unit2)
                xbmc.sleep(1000)
                res= get_html(torrent['uri']+ "?auth_token=%s" % self.token).json()
                
            link = self.torrentInfo(torrent['id'])
            

            link = self.unrestrict_link(link['links'][0])
            
            
            self.deleteTorrent(torrent['id'])
            dp.close()
       
        
        #except:
        #    self.deleteTorrent(torrent['id'])
        #    return None
        
        return link
    def stop_play(self):
        KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
        if KODI_VERSION>17:
            return 'forceexit'
        else:
            return 'return'
    def singleMagnetToLink(self, magnet):
        global break_window_rd,play_status_rd
        torrent=''
        try:
            if Addon.getSetting('new_play_window')=='false':
                dp = xbmcgui . DialogProgress ( )
                dp.create("Real Debrid",Addon.getLocalizedString(32287)+'\n'+ ""+'\n'+ '')
            else:
                dp=None
            play_status_rd=Addon.getLocalizedString(32287)
            
            
            if self.ClientSecret == '':
                self.auth()
            '''
            hash = str(re.findall(r'btih:(.*?)&', magnet)[0].lower())
            hashCheck = self.checkHash(hash)
            fileIDString = ''

            if hash in hashCheck:
                
                if 'rd' in hashCheck[hash]:
                    if len(hashCheck[hash]['rd'])>0:
                        for key in hashCheck[hash]['rd'][0]:
                            fileIDString += ',' + key
            '''
            torrent = self.addMagnet(magnet,dp=dp)
            if 'uri' not in torrent:
                xbmcgui.Dialog().ok(str(response['error_code']), 'Error in RD8 comm Try another link or check subscription')
                return '0'
            '''
            if 'uri' not in torrent:
                xbmcgui.Dialog().ok("error in RD",torrent)
                s=self.stop_play()
                if s=='forceexit':
                    sys.exit(1)
                else:
                    return 0
            '''
            if Addon.getSetting('new_play_window')=='false':
                dp.create("Real Debrid",Addon.getLocalizedString(32288)+'\n'+""+'\n'+ '')
            play_status_rd=Addon.getLocalizedString(32288)
            if Addon.getSetting('new_play_window')=='false':
                if dp.iscanceled() :
                        self.deleteTorrent(torrent['id'])
                        dp.close()
                        return 'stop'
            elif break_window_rd:
                    self.deleteTorrent(torrent['id'])
                     
                    return 'stop'
            res= get_html(torrent['uri']+ "?auth_token=%s" % self.token).json()
            if Addon.getSetting('new_play_window')=='false':
                dp.create("Real Debrid","Got Answer"+'\n'+ ""+'\n'+ '')
            play_status_rd="Got Answer"
            jump=False
            log.warning(res)
            if 'status' not in res: 
                if 'error' in res:
                    xbmcgui.Dialog().ok("error in RD1",res['error'])
                    
            if res['status']=='waiting_files_selection':
                   
                fileIDString = ''
                
                f_id=''
                if len(res['files'])>0:
                    max_size=0
                    for items in res['files']:
                        if items['bytes']>max_size:
                            max_size=items['bytes']
                            if 'id' in items:
                                f_id=items['id']
                    start_file=f_id
                    
                    if f_id=='':
                      xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), Addon.getLocalizedString(32288))).encode('utf-8'))
                    if 'id' in torrent:
                    
                        #self.torrentSelect(torrent['id'], start_file)#go
                        jump=True
                            
            f_size=0
            size=0
            status=''
            
             
            
            try:
                if Addon.getSetting('new_play_window')=='false':
                    dp.create("Real Debrid",Addon.getLocalizedString(32290)+'\n'+ ""+'\n'+ '')
                play_status_rd=Addon.getLocalizedString(32290)
                link = self.torrentSelect(torrent['id'], start_file)
                if Addon.getSetting('new_play_window')=='false':
                    dp.create("Real Debrid",Addon.getLocalizedString(32291)+'\n'+ ""+'\n'+ '')
                play_status_rd=Addon.getLocalizedString(32291)
                link = self.torrentInfo(torrent['id'])
                if Addon.getSetting('new_play_window')=='false':
                    dp.create("Real Debrid",Addon.getLocalizedString(32292)+'\n'+ ""+'\n'+'')
                play_status_rd=Addon.getLocalizedString(32292)
                link = self.unrestrict_link(link['links'][0])
                if Addon.getSetting('new_play_window')=='false':
                    dp.create("Real Debrid",Addon.getLocalizedString(32293)+'\n'+ ""+'\n'+ '')
                play_status_rd=Addon.getLocalizedString(32293)
                self.deleteTorrent(torrent['id'])
            except Exception as e:
                xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), str(e))).encode('utf-8'))
                if 'id' in torrent:
                    self.deleteTorrent(torrent['id'])
                return None
            if Addon.getSetting('new_play_window')=='false':
                dp.close()
            return link
      
        except Exception as e:
            if 'id' in torrent:
                self.deleteTorrent(torrent['id'])
            import linecache
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            if 'error' in torrent:
                log.warning(torrent)
                if 'permission_denied' in torrent['error']:
                    error_n=torrent['error']+'\n Try reauth. debrid or check subscription'
                else:
                    error_n=torrent['error']
                xbmcgui.Dialog().ok("error in RD2",error_n)
                
            log.warning(torrent)
            line = linecache.getline(filename, lineno, f.f_globals)
            #xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'Line:'+str(lineno)+' E:'+str(e))).encode('utf-8'))
            log.warning('ERROR IN RD3 torrent :'+str(lineno))
            log.warning('inline:'+line)
            log.warning(e)
            log.warning(torrent)
            log.warning('BAD RD torrent')
            if Addon.getSetting('new_play_window')=='false':
                dp.close()
            try:
                if 'id' in torrent:
                    self.deleteTorrent(torrent['id'])
                if 'error' in torrent:
                    xbmcgui.Dialog().ok("error in RD4",torrent['error'])
            except:
                pass
            return None
    def singleMagnetToLink_season(self, magnet,tv_movie,season,episode,dp=None):
        global break_window_rd,play_status_rd
        try:
            if Addon.getSetting('new_play_window')=='false':
                if not dp:
                    dp = xbmcgui . DialogProgress ( )
                    dp.create("Real Debrid","addMagnet Season"+'\n'+ ""+'\n'+ '')
            play_status_rd="addMagnet Season"
            
            if self.ClientSecret == '':
                self.auth()
            '''
            hash = str(re.findall(r'btih:(.*?)&', magnet)[0].lower())
            hashCheck = self.checkHash(hash)
            fileIDString = ''
        
            if hash in hashCheck:
                
                if 'rd' in hashCheck[hash]:
                    if len(hashCheck[hash]['rd'])>0:
                        for key in hashCheck[hash]['rd'][0]:
                            fileIDString += ',' + key
            '''
          
            try:
                #hash = str(re.findall(r'btih:(.*?)&', link)[0].lower())
                hash=magnet.split('btih:')[1]
                if '&' in hash:
                    hash=hash.split('&')[0]
            except:
                hash =magnet.split('btih:')[1]
                    
            hashCheck = self.checkHash(hash)
      
            all_paths=[]
            key_list=[]

            for storage_variant in hashCheck[hash.lower()]['rd']:
                key_list = key_list+list(storage_variant.keys())
                
            for itt in storage_variant:
                if  not ('.mkv' in storage_variant[itt]['filename'] or '.avi' in storage_variant[itt]['filename']  or '.mp4' in storage_variant[itt]['filename']) :
                    
                
                    if itt in key_list:
                        key_list.remove(itt)
            counter_index=0
            found=False
            
           
     
           
            torrent = self.addMagnet(magnet)
            if Addon.getSetting('new_play_window')=='false':
                dp.create("Real Debrid",Addon.getLocalizedString(32193)+'\n'+ ""+'\n'+ '')
            play_status_rd=Addon.getLocalizedString(32193)
            res= get_html(torrent['uri']+ "?auth_token=%s" % self.token).json()
            jump=False
            
            if res['status']=='waiting_files_selection':
                   
                fileIDString = ''
                
                f_id=''
                if len(res['files'])>0:
                    max_size=0
                    sel=[]
                    countet_index=0
                   
                    for items in res['files']:
                        if tv_movie=='tv':
                           a=1
                        else:
                            
                            if items['bytes']>max_size:
                                max_size=items['bytes']
                              
                                if 'id' in items:
                                    f_id=str(items['id'])
                                    
                            key_list=[f_id]
                        
                    start_file=','.join(key_list)
                    
                    if len(key_list)==0:
                      xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name').encode('utf-8'), 'No key_list')).encode('utf-8'))
                    if 'id' in torrent:
                        
                        self.torrentSelect(torrent['id'], start_file)#go
                        jump=True
                            
            f_size=0
            size=0
            status=''
         
            if not jump:
                while status!='downloaded':
                   
                    status=res['status']
                    size=res['bytes']
                    unit=''
                    unit2=''
                    f_size=0
                    f_size2=0
                    if size>1024:
                        f_size=float(size)/1024
                        unit='Kb'
                    if size>(1024*1024):
                        f_size=float(size)/(1024*1024)
                        unit='Mb'
                    if size>(1024*1024*1024):
                        f_size=float(size)/(1024*1024*1024)
                        unit='Gb'
                    size2=res['original_bytes']
                    if size2>1024:
                        f_size2=float(size2)/1024
                        unit2='Kb'
                    if size2>(1024*1024):
                        f_size2=float(size2)/(1024*1024)
                        unit2='Mb'
                    if size2>(1024*1024*1024):
                        f_size2=float(size2)/(1024*1024*1024)
                        unit2='Gb'
                    seed=''
                    if 'seeders' in res:
                    
                        seed='S-'+str(res['seeders'])
                    if 'speed' in res:
                        unit3='b/s'
                        f_size3=res['speed']
                        if res['speed']>1024:
                            f_size3=float(res['speed'])/1024
                            unit3='Kb/s'
                        if res['speed']>(1024*1024):
                            f_size3=float(res['speed'])/(1024*1024)
                            unit3='Mb/s'
                        if res['speed']>(1024*1024*1024):
                            f_size3=float(res['speed'])/(1024*1024*1024)
                            unit3='Gb/s'
                        
                        speed=str(round(f_size3,2))+unit3
                    else:
                        speed=''
                    prog=0
                    if 'progress' in res:
                        prog=res['progress']
                    if Addon.getSetting('new_play_window')=='false':
                        dp.update(prog, res['status']+' [COLOR yellow]'+seed+' '+speed+'[/COLOR]', res['original_filename']+'\n'+ str(round(f_size,2))+' '+unit+'/'+str(round(f_size2,2))+' '+unit2)
                    xbmc.sleep(1000)
                    res= get_html(torrent['uri']+ "?auth_token=%s" % self.token).json()
                    
                    if res['status']=='waiting_files_selection':
                       
                        fileIDString = ''
                        
                        f_id=''
                        if len(res['files'])>0:
                            max_size=0

                            for items in res['files']:
                                if items['bytes']>max_size:
                                    max_size=items['bytes']
                                    if 'id' in items:
                                        f_id=items['id']
                                sel.append(f_id)
                            start_file=f_id
                            
                            if f_id=='':
                              xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'No file')).encode('utf-8'))
                            if 'id' in torrent:
                            
                                self.torrentSelect(torrent['id'], start_file)#go
                            else:
                                xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'No file id')).encode('utf-8'))
                                return
                    if Addon.getSetting('new_play_window')=='false':
                        if dp.iscanceled() or break_window_rd:
                            if 'id' in torrent:
                                self.deleteTorrent(torrent['id'])
                            dp.close()
                            return
                    elif break_window_rd:
                            if 'id' in torrent:
                                self.deleteTorrent(torrent['id'])
                            
                            return
            if Addon.getSetting('new_play_window')=='false':
                if not dp:
                    dp.close()
            try:
                #link = self.torrentSelect(torrent['id'],  start_file)
                
                link = self.torrentInfo(torrent['id'])
           
                counter_index=0
                if tv_movie=='movie':
                    selected_index=0
                for items in link['files']:
        
             
                   if str(items['id']) in key_list:
                    #log.warning('in1')
                    if  '.mkv' in items['path'] or '.avi' in items['path']  or '.mp4' in items['path'] :
                        
                      if 's%se%s.'%(season,episode)  in items['path'].lower() or 's%se%s '%(season,episode)  in items['path'].lower():
                        #log.warning(items)
                        selected_index=counter_index
                        #log.warning('in2')
                        found=True
                        break
                    if items['selected']==1:
                      #log.warning(items)
                      counter_index+=1
                  
                if 'links' not in link:
                    xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'),'No links')).encode('utf-8'))
                    if Addon.getSetting('new_play_window')=='false':
                        if dp.iscanceled() :
                            self.deleteTorrent(torrent['id'])
                            dp.close()
                            return 'stop'
                    elif  break_window_rd:
                        self.deleteTorrent(torrent['id'])
                        
                        return 'stop'
                    self.deleteTorrent(torrent['id'])
                    return None
                #log.warning('selected_index::'+str(selected_index))
                if 'links' in link and len(link['links'])>0:
                    link = self.unrestrict_link(link['links'][selected_index])
                    if  not ('.mkv' in link or '.avi' in link  or '.mp4' in link) :
                        self.deleteTorrent(torrent['id'])
                        return None
                else:
                    xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'No streamable link found_2')).encode('utf-8'))
                    self.deleteTorrent(torrent['id'])
                    return None
                self.deleteTorrent(torrent['id'])
            except Exception as e:
                
                xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), str(e))).encode('utf-8'))
                if 'id' in torrent:
                    self.deleteTorrent(torrent['id'])
                return None
          
            return link
      
        except Exception as e:
            
            import linecache
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            
            
            line = linecache.getline(filename, lineno, f.f_globals)
            log.warning('ERROR IN RD5 torrent :'+str(lineno))
            #xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name').encode('utf-8'), 'Line:'+str(lineno)+' E:'+str(e))).encode('utf-8'))
            
            log.warning('inline:'+line)
            log.warning(e)
           
            log.warning('BAD RD torrent')
            try:
                if 'id' in torrent:
                    self.deleteTorrent(torrent['id'])
                if 'error' in torrent:
                    xbmcgui.Dialog().ok("error in RD6",torrent['error'])
          
            except:
                pass
            return None
    '''
    def magnetToLink(self, torrent, args):
        try:
            log.warning('Magnet to link')
            if torrent['package'] == 'single':
                return self.singleMagnetToLink(torrent['magnet'])

            hash = str(re.findall(r'btih:(.*?)&', torrent['magnet'])[0].lower())
            hashCheck = self.checkHash(hash)
            torrent = self.addMagnet(torrent['magnet'])
            episodeStrings, seasonStrings = source_utils.torrentCacheStrings(args)
            file_key = None
            log.warning('Magnet to link1111')
            for storage_variant in hashCheck[hash]['rd']:
                if len(storage_variant) > 1:
                    continue
                else:
                    key = list(storage_variant.keys())[0]
                    filename = storage_variant[key]['filename']

                    if any(source_utils.cleanTitle(episodeString) in source_utils.cleanTitle(filename) for episodeString in episodeStrings):
                        if any(filename.lower().endswith(extension) for extension in
                               source_utils.COMMON_VIDEO_EXTENSIONS):
                            file_key = key
                            break
            if file_key == None:
                log.warning('Magnet to link2222')
                self.deleteTorrent(torrent['id'])
                return None
            log.warning('Magnet to link3333')
            self.torrentSelect(torrent['id'], file_key)
            log.warning("torrent['id']")
            log.warning(torrent['id'])
            link = self.torrentInfo(torrent['id'])
            log.warning(link)
            
            link = self.unrestrict_link(link['links'][0])
            log.warning(link)
            if link.endswith('rar'):
                link = None

            if Addon.getSetting('rd.autodelete') == 'true':
                self.deleteTorrent(torrent['id'])
            return link
        except:
            import traceback
            traceback.print_exc()
            self.deleteTorrent(torrent['id'])
            return None
    '''
    def getRelevantHosters(self):
        
        try:
            host_list = self.get_url('hosts/status')
            valid_hosts = []
            for domain, status in host_list.iteritems():
                if status['supported'] == 1 and status['status'] == 'up':
                    valid_hosts.append(domain)
            return valid_hosts
        except:
            
            return []
