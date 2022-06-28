import os,logging,json
import re,sys,xbmcgui
import socket
from  resources.modules import pyqrcode

import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
from resources.modules import log
ADDON = xbmcaddon.Addon()
Addon=ADDON
ADDONID = ADDON.getAddonInfo('id')
ADDONNAME = ADDON.getAddonInfo('name')
ADDONVERSION = ADDON.getAddonInfo('version')
CWD = ADDON.getAddonInfo('path')
PROFILE = ADDON.getAddonInfo('profile')



URL = 'https://paste.kodi.tv/'
LOGPATH = xbmc.translatePath('special://logpath')
LOGFILE = os.path.join(LOGPATH, 'kodi.log')
OLDLOG = os.path.join(LOGPATH, 'kodi.old.log')
REPLACES = (('//.+?:.+?@', '//USER:PASSWORD@'),('<user>.+?</user>', '<user>USER</user>'),('<pass>.+?</pass>', '<pass>PASSWORD</pass>'),)
class IterableToFileAdapter(object):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.length = len(iterable)

    def read(self, size=-1): # TBD: add buffer for `len(data) > size` case
        return next(self.iterator, b'')

    def __len__(self):
        return self.length
        
class upload_in_chunks(object):
    def __init__(self, filename, chunksize=1 << 13,dp=[]):
        self.filename = filename
        self.chunksize = chunksize
        self.totalsize = os.path.getsize(filename)
        self.readsofar = 0
        self.dp=dp

    def __iter__(self):
        with open(self.filename, 'rb') as file:
            while True:
                data = file.read(self.chunksize)
                if not data:
                    sys.stderr.write("\n")
                    break
                self.readsofar += len(data)
                percent = self.readsofar * 1e2 / self.totalsize
                self.dp.update(int(percent), Addon.getLocalizedString(32072),Addon.getLocalizedString(32151), "\r{percent:3.0f}%".format(percent=percent) )
                #sys.stderr.write("\r{percent:3.0f}%".format(percent=percent))
                yield data

    def __len__(self):
        return self.totalsize
        
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
def log(txt):
    message = u'%s: %s' % (ADDONID, txt)
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)


class QRCode(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        self.image = kwargs["image"]
        self.text = kwargs["text"]

    def onInit(self):
        self.imagecontrol = 501
        self.textbox = 502
        self.okbutton = 503
        self.showdialog()

    def showdialog(self):
        self.getControl(self.imagecontrol).setImage(self.image)
        self.getControl(self.textbox).setText(self.text)
        self.setFocus(self.getControl(self.okbutton))

    def onClick(self, controlId):
        if (controlId == self.okbutton):
            self.close()

class LogView(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.content = kwargs["content"]

    def onInit(self):
        self.header = 501
        self.textbox = 502
        self.showdialog()

    def showdialog(self):
        self.getControl(self.header).setLabel(self.name)
        self.getControl(self.textbox).setText(self.content)
        self.setFocusId(503)
def showResult_new( message, url=None):
        if url:
            copy2clip(url)
            platform = sys.platform
            added_txt=''
            if platform == 'win32':
                added_txt='\n[COLOR lightblue][I]link was copied to clipboard[/I][/COLOR]'
            imagefile = os.path.join(xbmc.translatePath(PROFILE),'%s.png' % str(url.split('/')[-1]))
            qrIMG = pyqrcode.create(url)
            qrIMG.png(imagefile, scale=10)
            qr = QRCode( "script-loguploader-main.xml" , CWD, "DefaultSkin", image=imagefile, text=message+added_txt)
            qr.doModal()
            del qr
            xbmcvfs.delete(imagefile)
        else:
            dialog = xbmcgui.Dialog()
            confirm = dialog.ok(ADDONNAME, message)
            
def logupload_new():
    LOGPATH = xbmc.translatePath('special://logpath')
    

    
    LOGFILE = os.path.join(LOGPATH, 'kodi.log')
    path1=xbmc.translatePath('special://home/addons/script.module.requests/lib')
    sys.path.append( path1)
    path1=xbmc.translatePath('special://home/addons/script.module.urllib3/lib')
    sys.path.append( path1)
    path1=xbmc.translatePath('special://home/addons/script.module.chardet/lib')
    sys.path.append( path1)
    path1=xbmc.translatePath('special://home/addons/script.module.certifi/lib')
    sys.path.append( path1)
    path1=xbmc.translatePath('special://home/addons/script.module.idna/lib')
    sys.path.append( path1)
    path1=xbmc.translatePath('special://home/addons/script.module.futures/lib')
    sys.path.append( path1)
    import requests
    files = {
    'file': (LOGFILE, open(LOGFILE, 'rb')),
    }

    response = requests.post('https://file.io/', files=files).json()
    lk=response['link']
    showResult_new("Post this url or scan QRcode for your Log\n[COLOR lightgreen]"+lk+'[/COLOR]' ,url=lk)
 
class Main:
    def __init__(self):
        self.dp = xbmcgui . DialogProgress ( )
        self.dp.create(Addon.getLocalizedString(32072),Addon.getLocalizedString(32151), '','')
        self.dp.update(0, Addon.getLocalizedString(32072),Addon.getLocalizedString(32151), '' )
        self.getSettings()
        if not xbmcvfs.exists(PROFILE):
            xbmcvfs.mkdirs(PROFILE)
        files = self.getFiles()
        for item in files:
  
            filetype = item[0]
            if filetype == 'log':
                error = Addon.getLocalizedString(32153)
                name = "logfile"
            elif filetype == 'oldlog':
                error = Addon.getLocalizedString(32154)
                name = "old log"
            elif filetype == 'crashlog':
                error = Addon.getLocalizedString(32155)
                name = "crashlog"
            self.dp.update(0,Addon.getLocalizedString(32072),Addon.getLocalizedString(32156), '' )
            succes, data = self.readLog(item[1])
            if succes:
                self.dp.update(0, Addon.getLocalizedString(32072),Addon.getLocalizedString(32157), '' )
                content = self.cleanLog(data)
                dialog = xbmcgui.Dialog()
                confirm = dialog.yesno(ADDONNAME, "%s  %s %s http://paste.kodi.tv/?" % (Addon.getLocalizedString(32158),name,Addon.getLocalizedString(32159)),nolabel=Addon.getLocalizedString(32272), yeslabel=Addon.getLocalizedString(32273))
                if confirm:
                    succes, data = self.postLog(content)
                    if succes:
                        self.showResult("Post this url or scan QRcode for your %s, together with a problem description, on the Kodi forum: %s" % (name, data), data)
                    else:
                        self.showResult('%s[CR]%s' % (error, data))
                else:
                    lv = LogView( "script-loguploader-view.xml" , CWD, "DefaultSkin", name=name, content=content)
                    lv.doModal()
                    del lv
            else:
                self.showResult('%s[CR]%s' % (error, data))

    def getSettings(self):
        self.oldlog = False
        self.crashlog = False

    def getFiles(self):
        logfiles = []
        logfiles.append(['log', LOGFILE])
        if self.oldlog:
            if xbmcvfs.exists(OLDLOG):
                logfiles.append(['oldlog', OLDLOG])
            else:
                self.showResult("No old log file found")
        if self.crashlog:
            crashlog_path = ''
            items = []
            if xbmc.getCondVisibility('system.platform.osx'):
                crashlog_path = os.path.join(os.path.expanduser('~'), 'Library/Logs/DiagnosticReports/')
                filematch = 'Kodi'
            elif xbmc.getCondVisibility('system.platform.ios'):
                crashlog_path = '/var/mobile/Library/Logs/CrashReporter/'
                filematch = 'Kodi'
            elif xbmc.getCondVisibility('system.platform.linux'):
                crashlog_path = os.path.expanduser('~') # not 100% accurate (crashlogs can be created in the dir kodi was started from as well)
                filematch = 'kodi_crashlog'
            elif xbmc.getCondVisibility('system.platform.windows'):
                self.showResult("Windows crashlogs are not supported, please disable this option in the addon settings")
            elif xbmc.getCondVisibility('system.platform.android'):
                self.showResult("Android crashlogs are not supported, please disable this option in the addon settings")
            if crashlog_path and os.path.isdir(crashlog_path):
                lastcrash = None
                dirs, files = xbmcvfs.listdir(crashlog_path)
                for item in files:
                    if filematch in item and os.path.isfile(os.path.join(crashlog_path, item)):
                        items.append(os.path.join(crashlog_path, item))
                        items.sort(key=lambda f: os.path.getmtime(f))
                        lastcrash = items[-1]
                if lastcrash:
                    logfiles.append(['crashlog', lastcrash])
            if len(items) == 0:
                self.showResult("No crashlog file found")
        return logfiles

    def readLog(self, path):
        try:
            lf = xbmcvfs.File(path)
            sz = lf.size()
            
            content = lf.read()
            lf.close()
            if content:
                return True, content
            else:
                log('file is empty')
                return False, "The file is empty"
        except:
            log('unable to read file')
            return False, "Failed to read the file"

    def cleanLog(self, content):
        for pattern, repl in REPLACES:
            content = re.sub(pattern, repl, content)
            return content

    def postLog(self, data):
        path1=xbmc.translatePath('special://home/addons/script.module.requests/lib')
        sys.path.append( path1)
        path1=xbmc.translatePath('special://home/addons/script.module.urllib3/lib')
        sys.path.append( path1)
        path1=xbmc.translatePath('special://home/addons/script.module.chardet/lib')
        sys.path.append( path1)
        path1=xbmc.translatePath('special://home/addons/script.module.certifi/lib')
        sys.path.append( path1)
        path1=xbmc.translatePath('special://home/addons/script.module.idna/lib')
        sys.path.append( path1)
        path1=xbmc.translatePath('special://home/addons/script.module.futures/lib')
        sys.path.append( path1)
        import requests
        self.session = requests.Session()
        UserAgent = '%s: %s' % (ADDONID, ADDONVERSION)
        if 1:#try:
            try:
                n_data=data.encode('utf-8')
            except:
                n_data=data
            n_data=n_data.replace(CWD,'').replace(PROFILE,'')
            start=False
            if 'initialize done' in n_data:
                nn_data=[]
                for item in n_data.split('\n'):
                    if 'initialize done' in item:
                        start=True
                    if start:
                        nn_data.append(item)
            else:
                nn_data=n_data.split('\n')

            local_log=xbmc.translatePath(os.path.join(PROFILE, 'kodi_log.log'))
            self.dp.update(0, Addon.getLocalizedString(32072),'building file', '' )
            file = open(local_log, 'w') 
            file.write('\n'.join(nn_data))
            file.close()

            files = {
                'file': ('kodi_log.log', open(local_log, 'rb')),
            }
            
        
            #it = upload_in_chunks(local_log, 10,dp)
            
            #response = requests.post("https://api.anonfile.com/upload",data=IterableToFileAdapter(it)).json()
            response = requests.post("https://api.anonfile.com/upload",files=files).json()
            
            self.dp.close()
            
            #response = requests.post('https://api.anonfile.com/upload', files=files)
            #response = self.session.post(URL + 'documents', data='\n'.join(nn_data), headers={'User-Agent': UserAgent})
            return True, response['data']['file']['url']['short']
            if 'key' in response.json():
                result = URL + response.json()['key']
                return True, result
            elif 'message' in response.json():
                log('upload failed, paste may be too large')
                return False, response.json()['message']
            else:
                log.warning('error: %s' % response.text)
                return False, "Error posting the logfile."
        #except Exception as e:
        #    log('unable to retrieve the paste url')
        #    return False, "Failed to retrieve the paste url: "+str(e)

    def showResult(self, message, url=None):
        if url:
            copy2clip(url)
            platform = sys.platform
            added_txt=''
            if platform == 'win32':
                added_txt='\n[COLOR lightblue][I]link was copied to clipboard[/I][/COLOR]'
            imagefile = os.path.join(xbmc.translatePath(PROFILE),'%s.png' % str(url.split('/')[-1]))
            qrIMG = pyqrcode.create(url)
            qrIMG.png(imagefile, scale=10)
            qr = QRCode( "script-loguploader-main.xml" , CWD, "DefaultSkin", image=imagefile, text=message+added_txt)
            qr.doModal()
            del qr
            xbmcvfs.delete(imagefile)
        else:
            dialog = xbmcgui.Dialog()
            confirm = dialog.ok(ADDONNAME, message)
def start():
    Main()

