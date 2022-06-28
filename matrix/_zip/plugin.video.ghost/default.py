# -*- coding: utf-8 -*-
import xbmcgui,xbmcaddon,time,base64
import _strptime,xbmcvfs
__addon__ = xbmcaddon.Addon()
Addon = xbmcaddon.Addon()
#if Addon.getSetting("debug")=='true' and Addon.getSetting("check_time")=='true':
    #xbmcgui.Dialog().ok('Start','Start')

start_time_start=time.time()
time_data=[]
import xbmcaddon,os,xbmc,urllib,re,xbmcplugin,sys,logging
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if Addon.getSetting("full_db")=='true':
    dp_full = xbmcgui . DialogProgress ( )
    if KODI_VERSION>18:
        dp_full.create('Please wait','Got your input...')
    else:
        dp_full.create('Please wait','Got your input...', '','')
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Got your input...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Got your input...', '' )
__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
from resources.modules import log
if KODI_VERSION<=18:
    xbmc_tranlate_path=xbmc.translatePath
else:
    import xbmcvfs,urllib,urllib.parse
    xbmc_tranlate_path=xbmcvfs.translatePath
__cwd__ = xbmc_tranlate_path(__addon__.getAddonInfo('path'))
addon_name=str(__addon__.getAddonInfo('name'))
addon_id=__addon__.getAddonInfo('id')
log.warning('Addon name:'+addon_name)
from os import listdir
import string
from os.path import isfile, join
import random
import threading,json
global sort_by_episode,break_jump,silent,clicked,selected_index,clicked_id,po_watching,l_full_stats,all_w_global,all_hased
global all_other_sources,once_fast_play,close_on_error,all_s_in,close_sources_now,global_result,stop_window,wait_for_subs,done1,done1_1
global tvdb_results,aa_results
global avg_f,stop_cpu,cores_use,all_other_sources_uni,infoDialog_counter_close
global play_status,break_window
global play_status_rd_ext,break_window_rd
global all_results_imdb
all_results_imdb=[]
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 0.1...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 0.1...', '' )
from resources.modules import public
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 0.2...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 0.2...', '' )
global all_jen_links
global from_seek
sort_by_episode=False
from_seek=False
all_jen_links=[]

play_status_rd_ext=''
break_window_rd=False
break_window=False
play_status=''
infoDialog_counter_close=False
all_other_sources_uni={}
aa_results={}
avg_f=''
stop_cpu=False
cores_use=''

tvdb_results=[]
done1=0
done1_1=0
wait_for_subs=''
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 1...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 1...', '' )
stop_window=False
global_result=global_result="4K: [COLOR yellow]%s[/COLOR] 1080: [COLOR khaki]%s[/COLOR] 720: [COLOR gold]%s[/COLOR] 480: [COLOR silver]%s[/COLOR] %s: [COLOR burlywood]%s[/COLOR]"%('0','0','0','0',Addon.getLocalizedString(32078),'0')
once_fast_play=0
close_on_error=0
all_other_sources={}
all_hased=[]

if KODI_VERSION<=18:#kodi18
    if Addon.getSetting('debug')=='false':
        reload (sys )#line:61
        sys .setdefaultencoding ('utf8')#line:62
else:#kodi19
    import importlib
    importlib.reload (sys )#line:61
all_w_global={}
l_full_stats=''
po_watching=''
clicked_id=''
selected_index=-1
clicked=False
silent=False
break_jump=0
global list_index,str_next,sources_searching
global susb_data_next
susb_data_next={}
sources_searching=False
str_next=''
list_index=999
all_s_in=({},0,'','','')
close_sources_now=0
addonPath = xbmc_tranlate_path(Addon.getAddonInfo("path"))
user_dataDir = xbmc_tranlate_path(Addon.getAddonInfo("profile"))
if not os.path.exists(user_dataDir):
     os.makedirs(user_dataDir)
lang=xbmc.getLanguage(0)
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 2...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 2...', '' )
addNolink=public.addNolink
addDir3=public.addDir3
addLink=public.addLink
lang=public.lang
pre_mode=public.pre_mode
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time+999)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 3...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 3...', '' )
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
from  resources.modules import cache
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

global playing_text
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 4...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 4...', '' )
playing_text=''
from  resources.modules.client import get_html


if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 66...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 66...', '' )
if KODI_VERSION<=18:
    que=urllib.quote_plus
    url_encode=urllib.urlencode
else:
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus
if KODI_VERSION<=18:
    from urlparse import urlparse
    urp=urlparse
else:
    import urllib.parse as urlparse
    urp=urlparse.urlparse
if KODI_VERSION>18:
    def trd_alive(thread):
        return thread.is_alive()
    class Thread (threading.Thread):
       def __init__(self, target, *args):
        super().__init__(target=target, args=args)
        
       def run(self, *args):
          try:
            self._target(*self._args)
          except Exception as e:
              log.error(e)
          return 0
else:
    def trd_alive(thread):
        return thread.isAlive()
    class Thread(threading.Thread):
        def __init__(self, target, *args):
           
            self._target = target
            self._args = args
            
            
            threading.Thread.__init__(self)
            
        def run(self):
            
            self._target(*self._args)


base_header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',

            'Pragma': 'no-cache',
            
           
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            }
   
def clean_name(name,option):

    if option==1:
      return name.replace('%20',' ').replace('%3a',':').replace('%27',"'").replace('  ',' ')
    else:
      return name.replace('%20',' ').replace('%3a',':').replace('%27'," ").replace('  ',' ')
def res_q(quality):
    f_q='480'
    if '2160' in quality:
      f_q='2160'
    elif '1080' in quality:
      f_q='1080'
    elif '720' in quality:
      f_q='720'
    elif '480' in quality:
      f_q='480'
    elif 'hd' in quality.lower() or 'hq' in quality.lower():
      f_q='720'
    elif '360' in quality or 'sd' in quality.lower():
      f_q='360'
    elif '240' in quality:
      f_q='240'
    
    return f_q
if Addon.getSetting("theme")=='0':
    art_folder='artwork'
    
elif Addon.getSetting("theme")=='1':
    art_folder='artwork_keshav'
elif Addon.getSetting("theme")=='2':
    art_folder='artwork_shinobi'
elif Addon.getSetting("theme")=='3':
    art_folder='artwork_sonic'
elif Addon.getSetting("theme")=='4':
    art_folder='artwork_bob'
BASE_LOGO=os.path.join(addonPath, 'resources', art_folder+'/')
file = open(os.path.join(BASE_LOGO, 'fanart.json'), 'r') 
fans= file.read()
file.close()
fanarts=json.loads(fans)
all_fanarts={}
for items in fanarts:
    if 'http' in fanarts[items]:
        all_fanarts[items]=fanarts[items]
    else:
        all_fanarts[items]=(os.path.join(BASE_LOGO, fanarts[items]))
    

ACTION_PREVIOUS_MENU 			=  10	## ESC action
ACTION_NAV_BACK 				=  92	## Backspace action
ACTION_MOVE_LEFT				=   1	## Left arrow key
ACTION_MOVE_RIGHT 				=   2	## Right arrow key
ACTION_MOVE_UP 					=   3	## Up arrow key
ACTION_MOVE_DOWN 				=   4	## Down arrow key
ACTION_MOUSE_WHEEL_UP 			= 104	## Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN			= 105	## Mouse wheel down
ACTION_MOVE_MOUSE 				= 107	## Down arrow key
ACTION_SELECT_ITEM				=   7	## Number Pad Enter
ACTION_BACKSPACE				= 110	## ?
ACTION_MOUSE_LEFT_CLICK 		= 100
ACTION_MOUSE_LONG_CLICK 		= 108

ACTION_PLAYER_STOP = 13
ACTION_BACK          = 92
ACTION_NAV_BACK =  92## Backspace action
ACTION_PARENT_DIR    = 9
ACTION_PREVIOUS_MENU = 10
ACTION_CONTEXT_MENU  = 117
ACTION_C_KEY         = 122

ACTION_LEFT  = 1
ACTION_RIGHT = 2
ACTION_UP    = 3
ACTION_DOWN  = 4
domain_s='https://'
COLOR1         = 'gold'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'

use_debrid=Addon.getSetting('debrid_use')=='true'
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 5...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 5...', '' )
def MySubs(title='',list=[],f_list=[]):
    from  resources.modules import pyxbmct

    class MySubs(pyxbmct.AddonDialogWindow):
        
        def __init__(self, title='',list=[],f_list=[]):
        
            super(MySubs, self).__init__(title)
            self.list_o=list
            self.title=title
            try:
                self.start_time= xbmc.Player().getTime()
            except:
                self.start_time=0
            wd=int(Addon.getSetting("subs_width"))
            hd=int(Addon.getSetting("subs_hight"))
            px=int(Addon.getSetting("subs_px"))
            py=int(Addon.getSetting("subs_py"))
            self.full_list=f_list
            self.setGeometry(wd, hd, 9, 1,pos_x=px, pos_y=py)
            self.time_c=0
            
            self.set_info_controls()
            self.set_active_controls()
            self.set_navigation()
            
            # Connect a key action (Backspace) to close the window.
            self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
            Thread(target=self.background_task).start()
        def background_task(self):
            global list_index
            max=int(Addon.getSetting("subs_window"))+self.start_time
            self.t=self.start_time
            
            
            self.t2=self.start_time
            once=0
            while(self.t2<max):
              if Addon.getSetting("auto_subtitles")=='true' and xbmc.Player().isPlaying() and once==0:
                once=1
                self.label_info.setLabel('Downloading')
                result=download_subs(self.list_o,0)
                if result=='ok':
                    self.label_info.setLabel('Ready')
                else:
                    self.label_info.setLabel('Error: '+str(result))
              self.label.setLabel(str(int(max-self.t2)))
              self.time_c=self.t2
              
             
              try:
                self.t2= xbmc.Player().getTime()
              except:
                self.t2=self.t
              self.t+=1
              xbmc.sleep(1000)
            list_index=999
            self.close()
        def set_info_controls(self):
          
          
             # Label
            self.label = pyxbmct.Label(str(int(self.time_c)))
            self.placeControl(self.label,  4, 0, 3, 1)
            
            self.label_info = pyxbmct.Label('Waiting for your selection')
            self.placeControl(self.label_info,  0, 0, 1, 1)
             
        def click_list(self):
            global list_index
            list_index=self.list.getSelectedPosition()
            self.t=self.start_time
            self.label_info.setLabel('Downloading')
            result=download_subs(self.list_o,list_index)
            if result=='ok':
                    self.label_info.setLabel('Ready')
            else:
                self.label_info.setLabel('Error: '+str(result))
            self.t=self.start_time
           
            #self.close()
        def click_c(self):
            global list_index
            
            list_index=888
            current_list_item=''
            self.close()
        def set_active_controls(self):
         
          
            # List
            
            self.list = pyxbmct.List()
            self.placeControl(self.list, 1, 0, 7, 1)
            # Add items to the list
            items = self.list_o
            n_items=[]
            log.warning('len(n_items)')
            log.warning(len(n_items))
            for pre,it,index_in,lan in items:
              log.warning(pre)
              if pre==0:
                 n_items.append('[COLOR lightgreen] [%s] [/COLOR]'%lan+it)
              else:
                n_items.append('[COLOR yellow]'+str(pre)+'%[/COLOR]'+'[COLOR lightgreen] [%s] [/COLOR]'%lan+it)
              
            self.list.addItems(n_items)
            # Connect the list to a function to display which list item is selected.
            self.connect(self.list, self.click_list)
            
            # Connect key and mouse events for list navigation feedback.
            
         
            
            self.button = pyxbmct.Button('Close')
            self.placeControl(self.button, 8, 0)
            # Connect control to close the window.
            self.connect(self.button, self.click_c)

        def set_navigation(self):
            # Set navigation between controls
            
            self.list.controlDown(self.button)
            self.list.controlRight(self.button)
            self.list.controlLeft(self.button)
            self.button.controlUp(self.list)
            self.button.controlDown(self.list)
            # Set initial focus
            self.setFocus(self.list)

        def slider_update(self):
            # Update slider value label when the slider nib moves
            try:
                if self.getFocus() == self.slider:
                    self.slider_value.setLabel('{:.1F}'.format(self.slider.getPercent()))
            except (RuntimeError, SystemError):
                pass

        def radio_update(self):
            # Update radiobutton caption on toggle
            if self.radiobutton.isSelected():
                self.radiobutton.setLabel('On')
            else:
                self.radiobutton.setLabel('Off')

        def list_update(self):
            # Update list_item label when navigating through the list.
            try:
                if self.getFocus() == self.list:
                    self.list_item_label.setLabel(self.list.getListItem(self.list.getSelectedPosition()).getLabel())
                else:
                    self.list_item_label.setLabel('')
            except (RuntimeError, SystemError):
                pass

        def setAnimation(self, control):
            # Set fade animation for all add-on window controls
           
            
            control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=100',),
                                    ('WindowClose', 'effect=fade start=100 end=0 time=100',)])
    window = MySubs(title,list,f_list)
    window.doModal()

    del window

def get_trailer_f(id,tv_movie):
    import random
    try:
        html_t='99'
        log.warning('Get Trailer')
        if tv_movie=='movie':
          url_t='http://api.themoviedb.org/3/movie/%s/videos?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en'%id
        else:
          url_t='http://api.themoviedb.org/3/tv/%s/videos?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en'%id
        html_t=get_html(url_t).json()
        if len(html_t['results'])==0:
            if tv_movie=='movie':
              url_t='http://api.themoviedb.org/3/movie/%s/videos?api_key=fb981e5ab89415bba616409d5eb5f05e'%id
            else:
              url_t='http://api.themoviedb.org/3/tv/%s/videos?api_key=fb981e5ab89415bba616409d5eb5f05e'%id
            html_t=get_html(url_t).json()
        else:
            log.warning(html_t)
        if len(html_t['results'])>0:
            vid_num=random.randint(0,len(html_t['results'])-1)
        else:
          return 0
        video_id=(html_t['results'][vid_num]['key'])
        #from pytube import YouTube
        #playback_url = YouTube(domain_s+'www.youtube.com/watch?v='+video_id).streams.first().download()
        playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
        return playback_url
        from resources.modules.youtube_ext import get_youtube5
       
        
        if video_id!=None and 'error_code' not in video_id:
          try:
            return get_youtube5(video_id).replace(' ','%20')
          except Exception as e:
            log.warning(e)
            return ''
        else:
            return ''
        return playback_url
    except Exception as e:
        import linecache
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        xbmc.executebuiltin((u'Notification(%s,%s)' % (addon_name, 'Line:'+str(lineno)+' E:'+str(e))).encode('utf-8'))
        log.warning('ERROR IN Trailer :'+str(lineno))
        log.warning('inline:'+line)
        log.warning(e)
        log.warning(html_t)
        log.warning('BAD Trailer play')
        return ''
def monitor_play():
    global stoped_play_once,all_s_in,once_fast_play
    log.warning('In monitor Play')
    once=0
    while(1):
        
        if all_s_in[3]!=4:
            
            if not xbmc.Player().isPlaying():
                if once==0:
                    xbmc.executebuiltin("Dialog.Open(busydialog)")
                    log.warning('Stop super')
                    xbmc.executebuiltin((u'Notification(%s,%s)' % (addon_name, 'Waiting for sources'.decode('utf8'))).encode('utf-8'))
                    dp = xbmcgui . DialogProgress ( )
                    if KODI_VERSION>18:
                        dp.create('Please wait','Searching...')
                    else:
                        dp.create('Please wait','Searching...', '','')
                    if KODI_VERSION>18:
                        dp.update(0, 'Please wait'+'\n'+'Searching...'+'\n'+ '' )
                    else:
                        dp.update(0, 'Please wait','Searching...', '' )
                    once=1
                if KODI_VERSION>18:
                    dp.update(all_s_in[1], 'Please wait'+'\n'+all_s_in[2]+'\n'+ all_s_in[4] )
                else:
                    dp.update(all_s_in[1], 'Please wait',all_s_in[2], all_s_in[4] )
                if dp.iscanceled():
                 stop_window=True
                 
                
                once_fast_play=0;
                stoped_play_once=1
                
       
        else:
            break
        xbmc.sleep(100)
    if once==1:
    
        dp.close()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
class player_window(xbmcgui.WindowXMLDialog):
    def __new__(cls, addonID,id,tv_movie,season,episode):
        
        
        FILENAME='play_window.xml'
        
        return super(player_window, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
        

    def __init__(self, addonID,id,tv_movie,season,episode):
        super(player_window, self).__init__()
        self.tv_movie=tv_movie
        self.id=id
        self.poster=1
        self.label=5
        self.close_now=False
        self.playbutton=5003
    def onAction(self, action):
        
        
        actionId = action.getId()

        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            self.close_now=True
            return self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK]:
            self.close_now=True
            return self.close()
    def get_img_ch(self,tv_movie,id):
        url='https://api.themoviedb.org/3/%s/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&include_image_language=ru,null&append_to_response=images,external_ids'%(self.tv_movie,self.id,lang)
       
        html=get_html(url).json()
        return html
    def get_img(self):
        self.html=cache.get(self.get_img_ch, 999,self.tv_movie,self.id,table='pages')
        
        fan=domain_s+'image.tmdb.org/t/p/original/'+self.html['backdrop_path']
       
       
        self.getControl(self.poster).setImage(fan)
        
        try:
          tvdb_id=str(self.html['external_ids']['tvdb_id'])
        except:
         tvdb_id=''
        log.warning('tvdb::'+tvdb_id)
        all_n_fan=[]
        all_banner=[]
        try:
            
            time_to_save=int(Addon.getSetting("save_time"))
            full_art= cache.get(get_more_meta, time_to_save, self.id,self.tv_movie,tvdb_id, table='pages') 
            
            
            if self.tv_movie=='tv':
                logo=full_art['hdtvlogo']
                if len(logo)>0:
                   
                    all_logo=[]
                    for itt in logo:
                       if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    self.getControl(5002).setImage(all_logo[0])
                
                
                for itt in full_art['showbackground']:
                   if itt['lang']=='en':
                    all_n_fan.append(itt['url'])
                for itt in full_art['tvbanner']:
                   if itt['lang']=='en':
                    all_banner.append(itt['url'])
            else:
                logo=full_art['hdmovielogo']
                if len(logo)>0:
                    all_logo=[]
                    for itt in logo:
                      if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    self.getControl(5002).setImage(all_logo[0])
                
                
                for itt in full_art['moviebackground']:
                   if itt['lang']=='en':
                    all_n_fan.append(itt['url'])
                for itt in full_art['moviebanner']:
                   if itt['lang']=='en':
                    all_banner.append(itt['url'])
        except Exception as e:
            log.warning('Fanart Err:'+str(e))
    def onInit(self):
        global play_status,play_status_rd_ext,break_window
        
        thread=[]
        thread.append(Thread(self.get_img))
        thread[len(thread)-1].setName('background_task')
        
        for td in thread:
            td.start()
            
        
        timeout=0
        start_time=time.time()
        while timeout<2000:
            timeout+=1
            if self.close_now:
                break
            elapsed_time = time.time() - start_time
            try:
               ext=play_status_rd_ext.play_status_rd
            except :
               ext=''
            self.getControl(self.label).setLabel('Please wait'+': '+time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+', '+play_status+ext)
            
            #self.getControl(self.playbutton).setVisible(True)
            
            if xbmc.Player().isPlaying():
                    
                try:
                    vidtime = xbmc.Player().getTime()
                    if vidtime>0:
                        break
                except:
                    pass
           
                
            if break_window:
                break
            xbmc.sleep(100)
        
        return self.close()
class sources_search2(xbmcgui.WindowXMLDialog):
    
    def __new__(cls, addonID,id,tv_movie,type,season,episode):
        
        if Addon.getSetting("eye_candy_style")=='1':
            FILENAME='sources_s3.xml'
        elif Addon.getSetting("eye_candy_style")=='0':
            FILENAME='sources_s2.xml'
        return super(sources_search2, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
        

    def __init__(self, addonID,id,tv_movie,type,season,episode):
        super(sources_search2, self).__init__()
        
        if tv_movie=='movie':
            fav_search_f=Addon.getSetting("fav_search_f")
            fav_servers_en=Addon.getSetting("fav_servers_en")
            fav_servers=Addon.getSetting("fav_servers")
           
            google_server= Addon.getSetting("google_server")
            rapid_server=Addon.getSetting("rapid_server")
            direct_server=Addon.getSetting("direct_server")
            heb_server=Addon.getSetting("heb_server")
        else:
            fav_search_f=Addon.getSetting("fav_search_f_tv")
            fav_servers_en=Addon.getSetting("fav_servers_en_tv")
            fav_servers=Addon.getSetting("fav_servers_tv")
            google_server= Addon.getSetting("google_server_tv")
            rapid_server=Addon.getSetting("rapid_server_tv")
            direct_server=Addon.getSetting("direct_server_tv")
            heb_server=Addon.getSetting("heb_server_tv")
        
        if  fav_search_f=='true' and fav_servers_en=='true' and (len(fav_servers)>0 or heb_server=='true' or google_server=='true' or rapid_server=='true' or direct_server=='true'):
            self.fav_status='true'
        else:
            self.fav_status='false'
        self.full=0
        self.season=season
        self.episode=episode
        self.onint=False
        self.poster=1
        self.timer_close=0
        self.changed_poster=2
        self.all_ids=[]
        self.close_tsk=0
        self.type=type
        self.titlein=4
        self.titlein2=5
        self.txt_movie=6
        self.genere=7
        self.progress=8
        self.labelpre=9
        self.labelResult=10
        self.timelabel=11
        self.recomlabel=13
        self.labelstatus=14
        xbmc.Player().stop()
        self.id=id
        self.st_init=0
        self.tv_movie=tv_movie
        thread=[]
        thread.append(Thread(self.background_task))
        thread[len(thread)-1].setName('background_task')
        thread.append(Thread(self.get_similer))
        thread[len(thread)-1].setName('get_similer')
        for td in thread:
            td.start()
        #Thread(target=self.background_task).start()
        
        #Thread(target=self.get_similer).start()
    def get_similer(self):
        global all_s_in,global_result,stop_window,once_fast_play,close_sources_now
        while  self.st_init==0:
            xbmc.sleep(100)
        log.warning('Start Similar')
        start_time=time.time()
        counter_close=0
        tick=0
        tick_global=0
        pre_state=0
        while(1):
                if once_fast_play==1:
                    log.warning('cloging on one clisk')
                    self.close()
                    
                if self.timer_close==1 :
                    
                    counter_close+=1
                    self.getControl(self.labelstatus).setLabel('Closing Please Wait'+' '+all_s_in[2])
                   
                try:
                        
                        if pre_state==1 and all_s_in[3]==2:
                            log.warning('reset time')
                            #start_time=time.time()
                        pre_state=all_s_in[3]
                        self.getControl(self.labelpre).setLabel(str(all_s_in[1])+'% '+str(all_s_in[3])+'/4')
                        if 1:#'Playing' in global_result:
                            self.getControl(self.labelResult).setLabel(global_result)
                            
                        else:
                            self.getControl(self.labelResult).setLabel(global_result)
                        self.getControl(self.progress).setPercent(all_s_in[1])
                        all_t=[]
                        for thread in threading.enumerate():
                            if ('background_task' in thread.getName()) or ('get_similer' in thread.getName()) or ('MainThread' in thread.getName()) or ('sources_s' in thread.getName()):
                                continue
                            
                            if (trd_alive(thread)):
                                all_t.append( thread.getName())
                        if len(all_t)>0:
                            if len(all_t)>10:
                                tt=' Remaining:'+str(len(all_t))
                            else:
                                tt=','.join(all_t)
                            self.getControl(self.labelstatus).setLabel(tt)
                        self.getControl(self.labelstatus).setLabel(all_s_in[2])
                        elapsed_time = time.time() - start_time
                        self.getControl(self.timelabel).setLabel(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
                        
                        if self.tv_movie=='movie':
                            src_ena=Addon.getSetting("fav_search_time_en")
                        else:
                            src_ena=Addon.getSetting("fav_search_time_en_tv")
                        if self.fav_status=='true' and src_ena=='true':
                           if self.tv_movie=='movie':
                              max_time=int(Addon.getSetting("fav_search_time"))
                           else:
                             max_time=int(Addon.getSetting("fav_search_time_tv"))
                        else:
                           max_time=int(Addon.getSetting("time_s"))
                        if elapsed_time>max_time:
                            self.onClick(3001)
                        if self.close_tsk==1:
                            break
                 
                except Exception as e:
                    log.warning('Error In Skin:'+str(e))
               
                counter_now=False
                if Addon.getSetting("video_in_s_wait")=='true' and ((Addon.getSetting("video_in_sources")=='true' and self.tv_movie=='movie') or (Addon.getSetting("video_in_sources_tv")=='true' and self.tv_movie=='tv')):
                       if not xbmc.Player().isPlaying() and counter_close>30:
                            counter_now=True
                elif counter_close>30:
                        counter_now=True
                
                if all_s_in[3]==4 or counter_now or close_on_error==1 or close_sources_now==1:
                 
                    
                    if Addon.getSetting("video_in_s_wait")=='true' and ((Addon.getSetting("video_in_sources")=='true' and self.tv_movie=='movie') or (Addon.getSetting("video_in_sources_tv")=='true' and self.tv_movie=='tv')):
                      
                        log.warning('Closing:'+str(xbmc.Player().isPlaying()))
                        if Addon.getSetting("eye_candy_style")=='1':
                            self.getControl(3003).setVisible(True)
                            self.getControl(3004).setVisible(True)
                            self.getControl(5002).setVisible(False)
                        elif Addon.getSetting("eye_candy_style")=='0':
                            self.getControl(7).setVisible(False)
                        self.getControl(10).setVisible(False)
                        self.getControl(8).setVisible(False)
                        self.getControl(9).setVisible(False)
                        self.getControl(14).setVisible(False)
                        self.getControl(11).setVisible(False)
                        
                        
                        
                        xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
                        self.getControl(self.labelstatus).setLabel('Wating for the trailer to End')
                        while(xbmc.Player().isPlaying()):
                            xbmc.sleep(100)
                    log.warning('once_fast_play22: '+str(once_fast_play))
                    if once_fast_play==0 and close_sources_now==0:
                        xbmc.Player().stop()
                    self.close_tsk=1
                    stop_window=True
                    self.close()
                    break
                xbmc.sleep(500)
        return 0
    def get_review(self,nm):
        import random
        
        
        x=get_html('https://api.themoviedb.org/3/%s/%s/reviews?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en&page=1'%(self.tv_movie,self.id),headers=base_header).json()
        all_rev=[]
        
        for items in x['results']:

            all_rev.append('[B][I]'+items['author']+'[/B][/I]\n'+items['content'])

        if len(all_rev)>0:
                #self.getControl(6).setWidth(1800)
                self.getControl(66).setText('\n'.join(all_rev))
        else:
            self.getControl(6).setWidth(1800)
            self.getControl(self.txt_movie).setText(self.html['overview'])
        return random.choice(all_rev)
    
    def background_task(self):
       global close_on_error
       
       xbmc.Player().stop()
       if self.type=='find_similar':
           
            url=domain_s+'api.themoviedb.org/3/%s/%s/recommendations?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(self.tv_movie,self.id.replace('\n',''),lang)
            
            self.html=get_html(url).json()

            all_data_int=[]
            self.all_ids=[]
            self.all_ids_done=0
            for items in self.html['results']:
                
               
                all_data_int.append(items['id'])
            random.shuffle(all_data_int)
            self.id=all_data_int[0]
       if self.type=='find_similar' and ((Addon.getSetting("video_in_sources")=='true' and self.tv_movie=='movie') or (Addon.getSetting("video_in_sources_tv")=='true' and self.tv_movie=='tv')):
            
            link_m=get_trailer_f(self.id,self.tv_movie)
            
            if link_m!='':
                try:
                    xbmc.Player().play(link_m, windowed=True)
                except:
                    pass
        
       url='https://api.themoviedb.org/3/%s/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&include_image_language=ru,null&append_to_response=images,external_ids'%(self.tv_movie,self.id,lang)
       
       self.html=get_html(url).json()
       if Addon.getSetting("eye_candy_style")=='1' and ((Addon.getSetting("video_in_sources")=='false' and self.tv_movie=='movie') or (Addon.getSetting("video_in_sources_tv")=='false' and self.tv_movie=='tv')):
           if self.tv_movie=='movie':
            cast_url='https://api.themoviedb.org/3/%s/%s/credits?api_key=fb981e5ab89415bba616409d5eb5f05e'%(self.tv_movie,self.id)
           else:
            cast_url='https://api.themoviedb.org/3/tv/%s/season/%s/episode/%s/credits?api_key=fb981e5ab89415bba616409d5eb5f05e'%(self.id,self.season,self.episode)
           cast=get_html(cast_url).json()
           if 'cast' in cast:
              
               
               all_c=[]
               all_n=[]
               all_c_o=[]
               for items in cast['cast']:
                    if 'profile_path' in items:
                        if items['profile_path']!=None:
                            all_c.append('https://image.tmdb.org/t/p/original/'+items['profile_path'])
                            all_c_o.append('https://image.tmdb.org/t/p/original/'+items['profile_path'])
                            all_n.append(items['name']+'\n[B][I]'+items['character']+'[/I][/B]')
               
               if self.tv_movie=='tv':
                random.shuffle(all_c)
               if len(all_c)>0:
                self.getControl(6002).setImage(all_c[0])
                
               
                self.getControl(6006).setLabel(all_n[all_c_o.index(all_c[0])])
               if len(all_c)>1:
                self.getControl(6003).setImage(all_c[1])
                self.getControl(6007).setLabel(all_n[all_c_o.index(all_c[1])])
               if len(all_c)>2:
                self.getControl(6004).setImage(all_c[2])
                self.getControl(6008).setLabel(all_n[all_c_o.index(all_c[2])])
               if len(all_c)>3:
                self.getControl(6005).setImage(all_c[3])
                self.getControl(6009).setLabel(all_n[all_c_o.index(all_c[3])])
       try:
        tvdb_id=str(self.html['external_ids']['tvdb_id'])
       except:
        tvdb_id=''
       log.warning('tvdb::'+tvdb_id)
       all_n_fan=[]
       all_banner=[]
       try:
            time_to_save=int(Addon.getSetting("save_time"))
            full_art= cache.get(get_more_meta, time_to_save, self.id,self.tv_movie,tvdb_id, table='pages') 
            
            
            if self.tv_movie=='tv':
                logo=full_art['hdtvlogo']
                if len(logo)>0:
                   
                    all_logo=[]
                    for itt in logo:
                       if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    self.getControl(5002).setImage(all_logo[0])
                
                
                for itt in full_art['showbackground']:
                   if itt['lang']=='en':
                    all_n_fan.append(itt['url'])
                for itt in full_art['tvbanner']:
                   if itt['lang']=='en':
                    all_banner.append(itt['url'])
            else:
                logo=full_art['hdmovielogo']
                if len(logo)>0:
                    all_logo=[]
                    for itt in logo:
                      if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    self.getControl(5002).setImage(all_logo[0])
                
                
                for itt in full_art['moviebackground']:
                   if itt['lang']=='en':
                    all_n_fan.append(itt['url'])
                for itt in full_art['moviebanner']:
                   if itt['lang']=='en':
                    all_banner.append(itt['url'])
       except Exception as e:
            log.warning('Fanart Err:'+str(e))
            
       
       while  self.st_init==0:
            xbmc.sleep(100)
       
       fan=domain_s+'image.tmdb.org/t/p/original/'+self.html['backdrop_path']
       log.warning('Fan:'+fan)
       if Addon.getSetting("fanart_scraping")=='true':
            self.getControl(self.poster).setImage(fan)
       if len(all_n_fan)>0 and ((Addon.getSetting("video_in_sources")=='false' and self.tv_movie=='movie') or (Addon.getSetting("video_in_sources_tv")=='false' and self.tv_movie=='tv')):
        random.shuffle(all_n_fan)
        fan2=all_n_fan[0]
        #self.getControl(6002).setImage(fan2)
        if len(all_n_fan)>1:
            fan2=all_n_fan[1]
            #self.getControl(6003).setImage(fan2)
       if Addon.getSetting("eye_candy_style")=='1':
           if len(all_banner)>0:
            random.shuffle(all_banner)
            banner=all_banner[0]
            self.getControl(3003).setVisible(False)
            self.getControl(3003).setImage(banner)
            banner2=banner
            if len(all_banner)>1:
                banner2=all_banner[1]
            self.getControl(3004).setVisible(False)
            self.getControl(3004).setImage(banner2)
        
       if Addon.getSetting("eye_candy_style")=='0':
           log.warning('get55')
           self.getControl(self.txt_movie).setText(self.html['overview'])
           if self.tv_movie=='movie':
               thread=[]
               thread.append(Thread(self.get_review,self.html['original_title']))
                    
               thread[0].start()
           else:
                self.getControl(6).setWidth(1800)
           log.warning('get66')
           all_img=[]
           for items in (self.html['images']['backdrops']):
                    all_img.append(domain_s+'image.tmdb.org/t/p/original/'+items['file_path'])
                    self.getControl(self.changed_poster).setImage(domain_s+'image.tmdb.org/t/p/original/'+items['file_path'])
           random.shuffle(all_img)
           log.warning('get77')
           genres_list=[]
           genere=''
           if 'genres' in self.html:
                for g in self.html['genres']:
                      genres_list.append(g['name'])
                
                try:genere = u' / '.join(genres_list)
                except:genere=''
       
        
        
           log.warning('get11')
           if 'title' in self.html:
            title_n=self.html['title']
           else:
            title_n=self.html['name']
           self.getControl(self.titlein).setLabel('[B]'+title_n+'[/B]')
           if 'tagline' in self.html:
            tag=self.html['tagline']
           else:
            tag=self.html['status']
           log.warning('get22')
           self.getControl(self.titlein2).setLabel('[I]'+tag+'[/I]')
            
           self.getControl(self.genere).setLabel(genere)
           log.warning('get33')
           self.getControl(self.txt_movie).setText(self.html['overview'])
           if self.type=='find_similar':
            self.getControl(self.recomlabel).setLabel('[B][I]Recommended for next time..[/I][/B]')
           log.warning('get44')
           while(1):
                log.warning(all_img+all_n_fan)
                for items in all_img+all_n_fan:
                   
                    self.getControl(self.changed_poster).setImage(items)
                    xbmc.sleep(1500)
                if self.close_tsk==1 or close_on_error==1:
                    break
                xbmc.sleep(100)
            
       return 0
    def onInit(self):
        self.st_init=1
        
        
        self.setFocus(self.getControl(3002))
        if self.type!='find_similar' and ((Addon.getSetting("video_in_sources")=='true' and self.tv_movie=='movie') or (Addon.getSetting("video_in_sources_tv")=='true' and self.tv_movie=='tv')):
            log.warning('Play Trailer')
            
            link_m=get_trailer_f(self.id,self.tv_movie)
            log.warning(link_m)
            if link_m!='':
                try:
                    xbmc.Player().play(link_m, windowed=True)
                except:
                    pass
            
            
        
        #self.getControl(self.title).setLabel(self.html['original_title'])
        
        
       
       
       
    def onAction(self, action):
        global stop_window,once_fast_play
        
        actionId = action.getId()

        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            self.params = 888
            xbmc.sleep(100)
            stop_window=True
            #self.close_tsk=1
            self.timer_close=1
            if once_fast_play==0:
                xbmc.Player().stop()
            #return self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK]:
            self.params = 888
            xbmc.sleep(100)
            stop_window=True
            #self.close_tsk=1
            self.timer_close=1
            if once_fast_play==0:
                xbmc.Player().stop()
            #return self.close()

    
    def onClick(self, controlId):
        global stop_window,once_fast_play
        stop_window=True
        #self.close_tsk=1
        self.timer_close=1
        if once_fast_play==0:
            logging.warning('stop5')
            #xbmc.Player().stop()
        #self.close()
        
    
    def onFocus(self, controlId):
        pass 
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 6...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 6...', '' )
def TrkBox_help(title, msg,img2="https://ia802503.us.archive.org/28/items/icon_20220511/icon.png"):
    class TextBoxes1(xbmcgui.WindowXMLDialog):
        def onInit(self):
            
            self.title      = 101
            self.msg        = 102
            self.scrollbar  = 103
            self.okbutton   = 201
            
            self.imagecontrol=202
            self.sync   = 203
            self.y=0
            self.showdialog()
            self.params=False
            
        def showdialog(self):
            import random
            self.getControl(self.title).setLabel(title)
            self.getControl(self.msg).setText(msg)
            self.getControl(self.imagecontrol).setImage(img2)
            self.setFocusId(self.sync)
            
            xbmc.executebuiltin("Dialog.Close(busydialog)")
        def onClick(self, controlId):
            if (controlId == self.okbutton):
               
                self.close()
                
            if (controlId == self.sync):
                self.params=True
                self.close()
        def onAction(self, action):
            if   action == ACTION_PREVIOUS_MENU: 
               
                self.close()
            elif action == ACTION_NAV_BACK: 
                    
                    self.close()
            
            
    tb = TextBoxes1( "Trktbox.xml" , Addon.getAddonInfo('path'), 'DefaultSkin', title=title, msg=msg)
    tb.doModal()
    pr=tb.params
    del tb
    return pr
def stop_play():
    
    if KODI_VERSION>17:
        return 'forceexit'
    else:
        return 'return'
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 7...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 7...', '' )
def contact(title='',msg=""):
	class MyWindow(xbmcgui.WindowXMLDialog):
		def __init__(self, *args, **kwargs):
			self.title = THEME3 % kwargs["title"]
			self.image = kwargs["image"]
			self.fanart = kwargs["fanart"]
			self.msg = THEME2 % kwargs["msg"]

		def onInit(self):
			self.fanartimage = 101
			self.titlebox = 102
			self.imagecontrol = 103
			self.textbox = 104
			self.scrollcontrol = 105
			self.button = 199
			self.showdialog()

		def showdialog(self):
			self.getControl(self.imagecontrol).setImage(self.image)
			self.getControl(self.fanartimage).setImage(self.fanart)
			self.getControl(self.fanartimage).setColorDiffuse('9FFFFFFF')
			self.getControl(self.textbox).setText(self.msg)
			self.getControl(self.titlebox).setLabel(self.title)
            
	
		
            
			self.setFocusId(self.button)
			
		def onAction(self,action):
			if   action == ACTION_PREVIOUS_MENU: self.close()
			elif action == ACTION_NAV_BACK: self.close()

	cw = MyWindow( "Contact.xml" , Addon.getAddonInfo('path'), 'DefaultSkin', title=title, fanart=' ', image='https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg', msg=msg)
	cw.doModal()
	del cw
def get_html_result(url):
    
    headers = {
        
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    html=get_html(url,headers=headers).json()
    
    return html
class Chose_ep(xbmcgui.WindowXMLDialog):

    def __new__(cls, addonID, heb_name,name, id,season,episode,dates,original_title,dp):
        FILENAME='chose_ep.xml'
        return super(Chose_ep, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
        

    def __init__(self, addonID,heb_name,name, id,season,episode,dates,original_title,dp):
        super(Chose_ep, self).__init__()
        
        self.labelcontrol1=1020
        self.labelcontrol2=1021
        self.imagecontrol=101
        self.bimagecontrol=5001
        self.txtcontrol=2
        self.season=season
        self.original_title=original_title
        self.id=id
        self.episode=episode
        self.heb_name=heb_name
        self.name=name
        self.dates=dates
        self.imagess=[]
        self.plotss=[]
        self.labelss=[]
        self.labelss1=[]
        self.dp=dp
        self.return_fanart=''
        self.return_plot=''
    def onInit(self):
        self.getControl(self.txtcontrol).setText("משיג מידע")
        self.getControl(self.bimagecontrol).setImage('https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg')
        url='https://api.themoviedb.org/3/tv/%s/season/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(self.id,self.season,lang)
        if KODI_VERSION>18:#kodi18
        
            self.dp.update(0, 'Series Traker'+'\n'+ 'Loading'+'\n'+ 'Get Html 1' )
        else:
            self.dp.update(0, 'Series Traker', 'Loading', 'Get Html 1' )
        html=cache.get(get_html_result,24,url, table='posters')
        self.getControl(self.txtcontrol).setText("Loading Episodes")
        try:
            maste_image='https://'+'image.tmdb.org/t/p/original/'+html['poster_path']
        except:
            maste_image=''
        if 'episodes' not in html:
            items={}
            items['name']=''
        else:
           for items in html['episodes']:
            if 'name' not in items or items['name']==None:
                items['name']=''
        if 'overview' not in html:
                html={}
                
                from resources.modules.tvdb import TVDB

                t = TVDB()
               
                url=domain_s+'api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en&append_to_response=external_ids'%id
               
                html=get_html(url).json()
                if 'first_air_date' in html:
                 show_original_year=html['first_air_date'].split("-")[0]
                else:
                 show_original_year=0
              
                tvdb_id=str(html['external_ids']['tvdb_id'])
               
               
                if tvdb_id=='None':
                 log.warning('Tryning None')
                 try:
                    tvdb_id_pre=t.getShow( original_title)
                    for itt in tvdb_id_pre['data']:
                        if itt['seriesName'].lower()==original_title.lower():
                            tvdb_id=str(itt['id'])
                    show=t.getShow_id(tvdb_id)
                 except:
                    show={'data':[]}
                    pass
                
                
                else:
                  show=t.getShow_id(tvdb_id)
                
                show_data=t.getShowData_id(tvdb_id)
                log.warning(json.dumps(show_data))
                html['overview']=show_data['data']['overview']
                html['name']=show_data['data']['seriesName']
                html['episodes']=[]
                maste_image='https://www.thetvdb.com/banners/'+show_data['data']['fanart']
                self.getControl(self.bimagecontrol).setImage(maste_image)
                match=[]
                all_episodes_tmdb=[]
                all_episodes=[]
                for item_tvdb in show['data']:
                    if item_tvdb['filename']!='':
                        img='https://www.thetvdb.com/banners/'+item_tvdb['filename']
                    else:
                        img=maste_image
                    match.append(('(T) '+item_tvdb['episodeName'],item_tvdb['airedEpisodeNumber'],item_tvdb['firstAired'],item_tvdb['overview'],item_tvdb['airedSeason'],img))
                all_season=[]
                all_season_tvdb_data=[]
                season_ep_count={}
                for ep_name,ep_num,aired,overview,s_number,image in match:
                   season_ep_count[s_number]=ep_num
                for ep_name,ep_num,aired,overview,s_number,image in match:
     
                     if str(s_number)==str(self.season):
                         if ep_num not in all_episodes:
                           
                           all_episodes.append(str(ep_num))
                           
                           all_season_tvdb_data.append({"name":ep_name,"episode_number":ep_num,"air_date":aired,"overview":overview,"season_number":s_number,"still_path":image,"poster_path":image})
   
                for items_a in all_episodes:
                     if items_a not in all_episodes_tmdb:
                       html['episodes'].append(all_season_tvdb_data[all_episodes.index(items_a)])
        master_plot=html['overview']
        
        master_name=html['name']
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        if KODI_VERSION>18:#kodi18
            self.dp.update(0, 'Series Traker'+'\n'+ 'Loading'+'\n'+  'DB' )
        else:
            self.dp.update(0, 'Series Traker', 'Loading',  'DB' )
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' AND type='%s' AND season='%s' AND episode = '%s'"%(self.original_title.replace("'","%27"),'tv',self.season,str(int(self.episode)+1)))
     
        match = dbcur.fetchone()
        color_next='white'
        if match!=None:
           color_next='magenta'
        
        dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' AND type='%s' AND season='%s' AND episode = '%s'"%(self.original_title.replace("'","%27"),'tv',self.season,str(int(self.episode))))
     
        match = dbcur.fetchone()
        color_current='white'
        
        if match!=None:
           color_current='magenta'
           
           
        dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' AND type='%s' AND season='%s' AND episode = '%s'"%(self.original_title.replace("'","%27"),'tv',self.season,str(int(self.episode)-1)))
     
        match = dbcur.fetchone()
        dbcur.close()
        dbcon.close()
        color_prev='white'
        if match!=None:
           color_prev='magenta'
           
        height=1100
        self.getControl(5001).setHeight(height)
            
        self.list = self.getControl(3000)
        self.list.setHeight(height)

        newY = 360 - (height/2)

        self.getControl(5000).setPosition(self.getControl(5000).getX(), 0)

        self.params    = None
        
        self.paramList = []
        
        all_d=json.loads(unque(self.dates))
        
        if len(all_d)<2:
            all_d=['','','']
      
        self.nextseason=False
        next_season_json={}
        if KODI_VERSION<=18:#kodi18
            self.dp.update(0, 'Series Traker', 'Loading', 'Get Html 2' )
        else:
            self.dp.update(0, 'Series Traker'+'\n'+ 'Loading'+'\n'+  'Get Html 2' )
        if all_d[2]==0:
            ur='http://api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en&append_to_response=external_ids'%self.id
            next_season_json=get_html(ur).json()
            
            if int(next_season_json['number_of_seasons'])>int(season):
                
                
                url='https://api.themoviedb.org/3/tv/%s/season/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(self.id,str(int(self.season)+1),lang)
  
                html2=cache.get(get_html_data,24,url, table='posters')
                for items in html2['episodes']:
                    if 'name' not in items or items['name']==None:
                        items['name']=''
                
                if 'episodes' in html2 and len(html2['episodes'])>0:
                    self.nextseason=True
        log.warning(self.nextseason)
        log.warning(all_d)
        if self.nextseason:
            #next ep
            
            
            if 1:#len(html2['episodes'])>int(self.episode):
                items=html2['episodes'][0]
                title='[COLOR %s]'%color_next+items['name']+'[/COLOR]'
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                self.imagess.append(image)
                title=title+ Addon.getLocalizedString(32002)+str(1)
                self.labelss.append(title)
                liz   = xbmcgui.ListItem(title)
                
                liz.setProperty('title_type', '[COLOR magenta]'+Addon.getLocalizedString(32006)+'[/COLOR]'+html2['episodes'][0]['air_date'])
                self.labelss1.append('[COLOR magenta]'+Addon.getLocalizedString(32006)+'[/COLOR]'+html2['episodes'][0]['air_date'])
                liz.setProperty('image', image)
                liz.setProperty('description',plot)
                self.plotss.append(plot)
                

                
                self.list.addItem(liz)
            else:
                liz   = xbmcgui.ListItem(Addon.getLocalizedString(32002)+str(int(self.episode)+1))
                liz.setProperty('title_type', Addon.getLocalizedString(32001)+str(all_d[2]))
                self.labelss1.append(Addon.getLocalizedString(32001)+str(all_d[2]))
                
                liz.setProperty('image', '')
                liz.setProperty('description','')
                self.plotss.append('')
                
                
                self.list.addItem(liz)
            #current ep
            if len(html['episodes'])>(int(self.episode)-1):
                items=html['episodes'][int(self.episode)-1]
                title='[COLOR %s]'%color_current+items['name']+'[/COLOR]'
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                self.imagess.append(image)
                title=title+ Addon.getLocalizedString(32002)+str(int(self.episode))
                    
            else:
                title=Addon.getLocalizedString(32002)+self.episode
                plot=''
                image=maste_image
                

            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32003)+all_d[1])
            self.labelss1.append(Addon.getLocalizedString(32003)+all_d[1])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
            
            self.list.addItem(liz)
            
            #prev ep
            if len(html['episodes'])>(int(self.episode)-2):
                items=html['episodes'][int(self.episode)-2]
                title='[COLOR %s]'%color_prev+items['name']+'[/COLOR]'
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                self.imagess.append(image)
                title=title+ Addon.getLocalizedString(32002)+str(int(self.episode)-1)
                self.labelss.append(title)
            else:
                title=Addon.getLocalizedString(32002)+str(int(self.episode)-1)
                plot=''
                image=maste_image
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32008)+all_d[0])
            self.labelss1.append(Addon.getLocalizedString(32008)+all_d[0])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
          

            
            self.list.addItem(liz)
                
            #episodes
            
            title=master_name
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type',Addon.getLocalizedString(32004))
            self.labelss1.append(Addon.getLocalizedString(32004))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            #season ep
            
            title=self.heb_name
            title=title.replace('%20',' ')
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32005))
            self.labelss1.append(Addon.getLocalizedString(32005))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            
        elif all_d[0]==0:
            #next ep
            if len(html['episodes'])>int(self.episode):
                items=html['episodes'][int(self.episode)]
                
                title='[COLOR %s]'%color_next+items['name']+'[/COLOR]'
                
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                self.imagess.append(image)
                title=title+ '- Episode '+str(int(self.episode)+1)
                self.labelss.append(title)
                liz   = xbmcgui.ListItem(title)
                liz.setProperty('title_type',Addon.getLocalizedString(32001)+all_d[2])
                self.labelss1.append(Addon.getLocalizedString(32001)+all_d[2])
                
                liz.setProperty('image', image)
                liz.setProperty('description',plot)
                self.plotss.append(plot)
                

                
                self.list.addItem(liz)
            else:
                liz   = xbmcgui.ListItem(Addon.getLocalizedString(32002)+str(int(self.episode)+1))
                liz.setProperty('title_type', Addon.getLocalizedString(32001)+all_d[2])
                self.labelss1.append(Addon.getLocalizedString(32001)+all_d[2])
                
                liz.setProperty('image', '')
                liz.setProperty('description','')
                self.plotss.append('')
                

                
                self.list.addItem(liz)
            #current ep
            items=html['episodes'][int(self.episode)-1]
            title='[COLOR %s]'%color_current+items['name']+'[/COLOR]'
            plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
            image=maste_image
            if items['still_path']!=None:
                if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                else:
                    image=items['still_path']
            self.imagess.append(image)
            title=title+ Addon.getLocalizedString(32002)+self.episode
            self.labelss.append(title)
     
                
            
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32003)+all_d[1])
            self.labelss1.append(Addon.getLocalizedString(32003)+all_d[1])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
            

            self.list.addItem(liz)
            

            
            #episodes
            
            title=master_name
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32004))
            self.labelss1.append(Addon.getLocalizedString(32004))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            
            #season ep
            
            title=self.heb_name
            title.replace('%20',' ')
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32005))
            self.labelss1.append(Addon.getLocalizedString(32005))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            #choise=['Play next episode - '+all_d[2],'Play current episode - '+all_d[1],'Open season episodes','Open season selection']
        elif all_d[2]==0:
            
            
            #current ep
            items=html['episodes'][int(self.episode)-1]
            title='[COLOR %s]'%color_current+items['name']+'[/COLOR]'
            plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
            image=maste_image
            if items['still_path']!=None:
                if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                else:
                    image=items['still_path']
            self.imagess.append(image)
            title=title+ Addon.getLocalizedString(32002)+self.episode
                
            
                
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32003)+all_d[1])
            self.labelss1.append(Addon.getLocalizedString(32003)+all_d[1])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
            
            self.list.addItem(liz)
            
            #prev ep
            items=html['episodes'][int(self.episode)-2]
            title='[COLOR %s]'%color_prev+items['name']+'[/COLOR]'
            plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
            image=maste_image
            if items['still_path']!=None:
                if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                else:
                    image=items['still_path']
            self.imagess.append(image)
            title=title+ Addon.getLocalizedString(32002)+str(int(self.episode)-1)
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32008)+all_d[0])
            self.labelss1.append( Addon.getLocalizedString(32008)+all_d[0])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
          

            
            self.list.addItem(liz)
            
            
            #episodes
            
            title=master_name
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32004))
            self.labelss1.append(Addon.getLocalizedString(32004))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            #season ep
            
            title=self.heb_name
            title.replace('%20',' ')
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32005))
            self.labelss1.append(Addon.getLocalizedString(32005))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)
 

            self.list.addItem(liz)
            #choise=['Play current episode - '+all_d[1],'Play previous episode - '+all_d[0],'Open season episodes','Open season selection']
        else:
            #next ep
            if len(html['episodes'])>int(self.episode):
                
                
                items=html['episodes'][int(self.episode)]
                title='[COLOR %s]'%color_next+items['name']+'[/COLOR]'
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                
                self.imagess.append(image)
                title=title+ Addon.getLocalizedString(32002)+str(int(self.episode)+1)
                self.labelss.append(title)
                liz   = xbmcgui.ListItem(title)
                if 'magenta' not in all_d[2]:
                
                    liz.setProperty('title_type', Addon.getLocalizedString(32006)+all_d[2])
                    self.labelss1.append(Addon.getLocalizedString(32006)+all_d[2])
                else:
                    liz.setProperty('title_type', '[COLOR magenta]'+Addon.getLocalizedString(32006)+'[/COLOR]'+all_d[2])
                    self.labelss1.append('[COLOR magenta]'+Addon.getLocalizedString(32006)+'[/COLOR]'+all_d[2])
                liz.setProperty('image', image)
                liz.setProperty('description',plot)
                self.plotss.append(plot)
                

                
                self.list.addItem(liz)
            else:
                liz   = xbmcgui.ListItem(Addon.getLocalizedString(32002)+str(int(self.episode)+1))
                liz.setProperty('title_type', Addon.getLocalizedString(32001)+all_d[2])
                self.labelss1.append(Addon.getLocalizedString(32001)+all_d[2])
                
                liz.setProperty('image', '')
                liz.setProperty('description','')
                self.plotss.append('')
                
                
                self.list.addItem(liz)
            #current ep
            if len(html['episodes'])>(int(self.episode)-1):
                items=html['episodes'][int(self.episode)-1]
                title='[COLOR %s]'%color_current+items['name']+'[/COLOR]'
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                self.imagess.append(image)
                title=title+ Addon.getLocalizedString(32002)+str(int(self.episode))
                    
            else:
                title=Addon.getLocalizedString(32002)+self.episode
                plot=''
                image=maste_image
                

            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32003)+all_d[1])
            self.labelss1.append(Addon.getLocalizedString(32003)+all_d[1])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
            
            self.list.addItem(liz)
            
            #prev ep
            if len(html['episodes'])>(int(self.episode)-2):
                items=html['episodes'][int(self.episode)-2]
                title='[COLOR %s]'%color_prev+items['name']+'[/COLOR]'
                plot='[COLOR khaki]'+items['overview']+'[/COLOR]'
                image=maste_image
                if items['still_path']!=None:
                    if 'https' not in items['still_path']:
                        image='https://'+'image.tmdb.org/t/p/original/'+items['still_path']
                    else:
                        image=items['still_path']
                self.imagess.append(image)
                title=title+ Addon.getLocalizedString(32002)+str(int(self.episode)-1)
                self.labelss.append(title)
            else:
                title=Addon.getLocalizedString(32002)+str(int(self.episode)-1)
                plot=''
                image=maste_image
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32008)+all_d[0])
            self.labelss1.append(Addon.getLocalizedString(32008)+all_d[0])
            liz.setProperty('image', image)
            liz.setProperty('description',plot)
            self.plotss.append(plot)
          

            
            self.list.addItem(liz)
                
            #episodes
            
            title=master_name
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type',Addon.getLocalizedString(32004))
            self.labelss1.append(Addon.getLocalizedString(32004))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            #season ep
            
            title=self.heb_name
            title=title.replace('%20',' ')
            self.labelss.append(title)
            liz   = xbmcgui.ListItem(title)
            liz.setProperty('title_type', Addon.getLocalizedString(32005))
            self.labelss1.append(Addon.getLocalizedString(32005))
            liz.setProperty('image', maste_image)
            self.imagess.append(maste_image)
            liz.setProperty('description',master_plot)
            self.plotss.append(master_plot)

            self.list.addItem(liz)
            

           

        if KODI_VERSION>18:#kodi18
            self.dp.update(0, 'Series Traker'+'\n'+ 'Loading'+'\n'+  'Final' )
        else:
            self.dp.update(0, 'Series Traker', 'Loading',  'Final' )
        self.setFocus(self.list)
        self.getControl(self.imagecontrol).setImage(self.imagess[0])
        self.getControl(self.bimagecontrol).setImage(maste_image)
        self.getControl(self.txtcontrol).setText(self.plotss[0])
        
        self.getControl(self.labelcontrol1).setLabel (self.labelss1[0])
        self.getControl(self.labelcontrol2).setLabel (self.labelss[0])
           
    def onAction(self, action):  
        actionId = action.getId()

        try:
            self.getControl(self.imagecontrol).setImage(self.imagess[self.list.getSelectedPosition()])
            self.getControl(self.txtcontrol).setText(self.plotss[self.list.getSelectedPosition()])
            self.getControl(self.labelcontrol1).setLabel (self.labelss1[self.list.getSelectedPosition()])
            self.getControl(self.labelcontrol2).setLabel (self.labelss[self.list.getSelectedPosition()])
        except:
            pass
        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            self.params = -1
            xbmc.sleep(100)
            return self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK]:
            self.params = -1
            return self.close()


    def onClick(self, controlId):
        
        if controlId != 3001:
        
            index = self.list.getSelectedItem().getProperty ('title_type')        
            
            self.return_fanart=self.list.getSelectedItem().getProperty ('image')  
            self.return_plot=self.list.getSelectedItem().getProperty ('description')  
            #self.getControl(self.txtcontrol).setText(self.plotss[index])
            try:    self.params = index
            except: self.params = None

        self.close()
        

    def onFocus(self, controlId):
        pass
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 8...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 8...', '' )
def selection_time(title,choose_time):
    from  resources.modules import pyxbmct
    class selection_time(pyxbmct.AddonDialogWindow):
        
        def __init__(self, title='',item=''):
           
            super(selection_time, self).__init__(title)
            self.item=[item,Addon.getLocalizedString(32009)]
            self.setGeometry(350, 150,1, 1,pos_x=700, pos_y=200)
            self.list_index=-1

            
            
            self.set_active_controls()
            self.set_navigation()
            # Connect a key action (Backspace) to close the window.
            self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
           

        
        def get_selection(self):
            """ get final selection """
            return self.list_index
        def click_list(self):
           
            self.list_index=self.list.getSelectedPosition()
           
            self.close()
        
        def set_active_controls(self):
         
          
            # List
            self.list = pyxbmct.List()
            self.placeControl(self.list, 0,0,  rowspan=2, columnspan=1)
            # Add items to the list
            
           
            self.list.addItems(self.item)
            
            # Connect the list to a function to display which list item is selected.
            self.connect(self.list, self.click_list)
            
           

        def set_navigation(self):
            
            self.setFocus(self.list)

        

        

        def setAnimation(self, control):
            # Set fade animation for all add-on window controls
            control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=50',),
                                    ('WindowClose', 'effect=fade start=100 end=0 time=50',)])
    window = selection_time(title,choose_time)
    window.doModal()
    selection = window.get_selection()
    del window
    return selection
class ContextMenu_new4(xbmcgui.WindowXMLDialog):
    
    def __new__(cls, addonID, menu,icon,fan,txt,results,po_watching,l_full_stats,tv_movie,id,tvdb_id,season,episode,show_original_year,original_title):
        FILENAME='contextMenu_new4.xml'
        
        
        return super(ContextMenu_new4, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
    def clean_title(self,title, broken=None):
        title = title.lower()
        # title = tools.deaccentString(title)
        #title = tools.strip_non_ascii_and_unprintable(title)

        if broken == 1:
            apostrophe_replacement = ''
        elif broken == 2:
            apostrophe_replacement = ' s'
        else:
            apostrophe_replacement = 's'
        title = title.replace("\\'s", apostrophe_replacement)
        title = title.replace("'s", apostrophe_replacement)
        title = title.replace("&#039;s", apostrophe_replacement)
        title = title.replace(" 039 s", apostrophe_replacement)

        title = re.sub(r'\:|\\|\/|\,|\!|\?|\(|\)|\'|\"|\\|\[|\]|\-|\_|\.', ' ', title)
        title = re.sub(r'\s+', ' ', title)
        title = re.sub(r'\&', 'and', title)

        return title.strip()
    def  getInfo(self,release_title):
        info = {}
        release_title = self.clean_title(release_title)
        info['encoding']=[]
        info['audio']=[]
        info['channels']=[]
        info['source']=[]
        info['language']=[]
            
        #info.video
        if any(i in release_title for i in ['x264', 'x 264', 'h264', 'h 264', 'avc']):
            info['encoding'].append('AVC')
        if any(i in release_title for i in ['x265', 'x 265', 'h265', 'h 265', 'hevc']):
            info['encoding'].append('HEVC')
        if any(i in release_title for i in ['xvid']):
            info['encoding'].append('XVID')
        if any(i in release_title for i in ['divx']):
            info['encoding'].append('DIVX')
        if any(i in release_title for i in ['mp4']):
            info['encoding'].append('MP4')
        if any(i in release_title for i in ['wmv']):
            info['encoding'].append('WMV')
        if any(i in release_title for i in ['mpeg']):
            info['encoding'].append('MPEG')
        if any(i in release_title for i in ['remux', 'bdremux']):
            info['encoding'].append('REMUX')
        if any(i in release_title for i in [' hdr ', 'hdr10', 'hdr 10']):
            info['encoding'].append('HDR')
        if any(i in release_title for i in [' sdr ']):
            info['encoding'].append('SDR')
        
        #info.audio
        if any(i in release_title for i in ['aac']):
            info['audio'].append('AAC')
        if any(i in release_title for i in ['dts']):
            info['audio'].append('DTS')
        if any(i in release_title for i in ['hd ma' , 'hdma']):
            info['audio'].append('HD-MA')
        if any(i in release_title for i in ['atmos']):
            info['audio'].append('ATMOS')
        if any(i in release_title for i in ['truehd', 'true hd']):
            info['audio'].append('TRUEHD')
        if any(i in release_title for i in ['ddp', 'dd+', 'eac3']):
            info['audio'].append('DD+')
        if any(i in release_title for i in [' dd ', 'dd2', 'dd5', 'dd7', ' ac3']):
            info['audio'].append('DD')
        if any(i in release_title for i in ['mp3']):
            info['audio'].append('MP3')
        if any(i in release_title for i in [' wma']):
            info['audio'].append('WMA')
        
        #info.channels
        if any(i in release_title for i in ['2 0 ', '2 0ch', '2ch']):
            info['channels'].append('2.0')
        if any(i in release_title for i in ['5 1 ', '5 1ch', '6ch']):
            info['channels'].append('5.1')
        if any(i in release_title for i in ['7 1 ', '7 1ch', '8ch']):
            info['channels'].append('7.1')
        
        #info.source 
        # no point at all with WEBRip vs WEB-DL cuz it's always labeled wrong with TV Shows 
        # WEB = WEB-DL in terms of size and quality
        if any(i in release_title for i in ['bluray' , 'blu ray' , 'bdrip', 'bd rip', 'brrip', 'br rip']):
            info['source'].append('BLURAY')
        if any(i in release_title for i in [' web ' , 'webrip' , 'webdl', 'web rip', 'web dl']):
            info['source'].append('WEB')
        if any(i in release_title for i in ['hdrip', 'hd rip']):
            info['source'].append('HDRIP')
        if any(i in release_title for i in ['dvdrip', 'dvd rip']):
            info['source'].append('DVDRIP')
        if any(i in release_title for i in ['hdtv']):
            info['source'].append('HDTV')
        if any(i in release_title for i in ['pdtv']):
            info['source'].append('PDTV')
        if any(i in release_title for i in [' cam ', 'camrip', 'hdcam', 'hd cam', ' ts ', 'hd ts', 'hdts', 'telesync', ' tc ', 'hd tc', 'hdtc', 'telecine', 'xbet']):
            info['source'].append('CAM')
        if any(i in release_title for i in ['dvdscr', ' scr ', 'screener']):
            info['source'].append('SCR')
        if any(i in release_title for i in ['korsub', ' kor ', ' hc']):
            info['source'].append('HC')
        if any(i in release_title for i in ['blurred']):
            info['source'].append('BLUR')
        if any(i in release_title for i in [' 3d']):
            info['source'].append('3D')
        all_lang=['en','eng','english','rus','russian','fr','french','TrueFrench','ita','italian','italiano','castellano','spanish','swedish','dk','danish','german','nordic','exyu','chs','hindi','polish','mandarin','kor','korean','koraen','multi']
        all_lang_des=['English','English','English','Russian','Russian','French','French','French','Italiano','Italiano','Italiano','Castellano','Spanish','Swedish','Danish','Danish','German','Nordic','ExYu','Chinese','Hindi','Polish','Mandarin','Korean','Korean','Korean','Multi']
        index=0

        for itt in all_lang:
            if ' '+itt+' ' in release_title.lower():
                if all_lang_des[index] not in info['language']:
                    info['language'].append(all_lang_des[index])
            index+=1
            
        fixed_info={}
        for key in info:
            if len(info[key])>0:
                fixed_info[key]=info[key]
                
        return fixed_info
    def __init__(self, addonID, menu,icon,fan,txt,results,po_watching,l_full_stats,tv_movie,id,tvdb_id,season,episode,show_original_year,original_title):
        
        super(ContextMenu_new4, self).__init__()
        self.clicked=False
        self.id=id
        self.menu=menu
        self.original_title=original_title
        self.show_original_year=show_original_year
        self.episode=episode
        self.season=season
        self.results=results
        if len(episode)==1:
          self.episode_n="0"+episode
        else:
           self.episode_n=episode
        if len(season)==1:
          self.season_n="0"+season
        else:
          self.season_n=season
      
        
        self.tv_movie=tv_movie
        self.tvdb_id=tvdb_id
        self.done_extra_fanart=False
        
        thread=[]
        thread.append(Thread(self.add_extra_art))
        thread[len(thread)-1].setName('fill_table')
        
        thread[0].start()
        
    def add_extra_art(self):
        
        log.warning('Start Extra')
        
        all_logo,all_n_fan,all_banner,all_clear_art,r_logo,r_art=get_extra_art(self.id,self.tv_movie,self.tvdb_id)
        log.warning(r_logo)
        self.getControl(3).setImage(r_logo)
        self.getControl(4).setImage(r_art)
    def cached_poster(self,idd):
        if self.tv_movie=='tv':
            x='http://api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(idd,lang)
        else:
            x='http://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(idd,lang)
     
        
        
        html=get_html(x).json()
        return html
    def onInit(self):
        
        
        self.list = self.getControl(2)
        
        html=cache.get(self.cached_poster, 999,self.id,table='pages') 
       
       
        if 'poster_path' in html:
            if html['poster_path']!=None:
                self.icon='https://image.tmdb.org/t/p/original/'+html['poster_path']
            else:
                self.icon=' '
            self.getControl(1).setImage(self.icon)
        self.getControl(5).setLabel(self.results)
        count=0
        all_liz_items=[]
        xbmc_list=xbmcgui.ListItem
        for item in self.menu:
                
                if self.clicked:
                    break
                self.getControl(5).setLabel("Please wait %s/%s"%(str(count),len(self.menu)))
                count+=1
                info=self.getInfo(item[4])
                
                add_d=[]
                
                
                counter_page=0
                nxt=0
                
               
                self.getControl(202).setLabel(str(((count*100)/len(self.menu))) + Addon.getLocalizedString(32010))
                count+=1
               
                '''
                info=(PTN.parse(item[0]))
                if 'excess' in info:
                    if len(info['excess'])>0:
                        item[0]='.'.join(info['excess'])
                '''
                golden=False
                if 'Cached ' in item[0]:
                    golden=True
                item[0]=item[0].replace('Cached ','')
                
                title ='[COLOR deepskyblue][B]'+item[0] +'[/B][/COLOR]'
                if len(item[1].strip())<2:
                    item[1]=''
                if len(item[2].strip())<2:
                    item[2]=''
                if len(item[3].strip())<2:
                    item[3]=''
                if len(item[4])<2:
                    item[4]=''
                if len(item[5])<2:
                    item[5]=''
                server=item[1]
                pre_n='[COLOR lime]'+item[2]+'[/COLOR]'
                q=item[3]
                
                if item[5]=='0.0GB':
                    size=''
                else:
                    size='[COLOR yellow]'+item[5]+'[/COLOR]'
                link=item[6]
                if Addon.getSetting("add_colors")=='true':
                    original_title_wd=self.original_title.replace(' ','.')
                    original_title_alt=self.original_title.replace('&','and')
                    heb_name_wd=heb_name.replace(' ','.')
                    item[4]=item[4].replace('-','.').replace('_','.').replace('.',' ')
                    log.warning('original_title:::')
                    log.warning(item[4])
                    log.warning(self.original_title)
                    item[4]=item[4].replace('  ',' ').replace(self.original_title.lower()+' ',self.original_title+' ')
                    item[4]=item[4].replace('S%sE%s'%(self.season_n,self.episode_n),'[COLOR lime]S%sE%s[/COLOR]'%(self.season_n,self.episode_n))
                    item[4]=item[4].replace(self.original_title+' ','[COLOR yellow]'+self.original_title+'[/COLOR]'+' ').replace(original_title_wd+' ','[COLOR yellow]'+self.original_title+'[/COLOR]'+' ')
                    item[4]=item[4].replace(original_title_alt+' ','[COLOR yellow]'+original_title_alt+'[/COLOR]'+' ')
                    item[4]=item[4].replace(self.show_original_year,'[COLOR plum]'+self.show_original_year+'[/COLOR]')
                    #heb
                    #item[4]=item[4].replace(heb_name,'[COLOR yellow]'+heb_name+'[/COLOR]').replace(heb_name_wd,'[COLOR yellow]'+heb_name+'[/COLOR]')
                added_h=''
                
                if 'https://' in item[6]:
                    
                    r=item[6].split('//')[1].split('/')[0]
                    #r=re.compile('//(.+?)/').findall(item[6])
                    if len(r)>0:
                        added_h='['+ r[0].replace('.com','').replace('www.','').capitalize()+'] '
                    
                    
                
                if q=='2160':
                    q='4k'
                if q.lower()=='hd':
                    q='unk'
                all_info=[]
                if len(q)>0:
                    all_info=['[COLOR lightblue]Quality[/COLOR]: [COLOR %s]'%'yellow'+q+'[/COLOR]']
                for key in info:
                    if type(info[key])==list:
                        
                        try:
                            info_key=','.join(info[key])
                        except:
                            info_key=str(info[key])
                    else:
                        info_key=str(info[key])
                    if key=='language':
                        color='pink'
                    else:
                        color='khaki'
                    all_info.append('[COLOR lightblue]'+key+'[/COLOR]: [COLOR %s]'%color+info_key+'[/COLOR]')
                supplay='[COLOR pink][B]'+size+'[/B][/COLOR] , '+','.join(all_info)
                
                
                
                liz   = xbmc_list()
                if 'collection' not in server.lower():
                    ncolor='lime'
                else:
                    ncolor='pink'
                if KODI_VERSION<19:
                    liz.setProperty('title','[COLOR lime]['+server.capitalize() +'][/COLOR] '+added_h +pre_n+item[4].encode('ascii', errors='ignore').decode('ascii', errors='ignore'))
                    liz.setProperty('server', '')#server
                    liz.setProperty('pre',pre_n)
                    if 'https' in item[7]:
                        liz.setProperty('image_collection',item[7])
                        #liz.setProperty('collection','yes')
                    #liz.setProperty('Quality', q)
                    liz.setProperty('supply', supplay)
                    liz.setProperty('size', size)
                else:
                    liz.setProperties({'title':'[COLOR %s]['%ncolor+server.capitalize() +'][/COLOR] '+added_h +pre_n+item[4].encode('ascii', errors='ignore').decode('ascii', errors='ignore'),
                                    'pre':pre_n,
                                    'image_collection':item[7],
                                    #'Quality': q,
                                    'supply': supplay,
                                    'size': size})
                                    
                #liz.setProperty('title','[COLOR lime]['+server.capitalize() +'][/COLOR] '+added_h +pre_n+item[4].encode('ascii', errors='ignore').decode('ascii', errors='ignore'))
                #liz.setProperty('server', '')#server
                #liz.setProperty('pre',pre_n)
                #if 'https' in item[7]:
                #    liz.setProperty('image_collection',item[7])
                #    #liz.setProperty('collection','yes')
                #liz.setProperty('Quality', q)
                #liz.setProperty('supply', supplay)
                #liz.setProperty('size', size)
              
                
                #liz.setProperty('server_v','100')
           
                
                #all_liz_items.append(liz)
                
                pre_pos=self.list.getSelectedPosition()
                self.list.addItem(liz)
                self.list.selectItem(pre_pos)
                self.setFocus(self.list)
                
        self.getControl(5).setLabel(self.results)
        log.warning(' Done Loading')
        
        #self.list.addItems(all_liz_items)

        self.setFocus(self.list)
    def onAction(self, action):  
        global done1_1,selected_index
        actionId = action.getId()
        #logging.warning('actionId:'+str(actionId))
        self.tick=60
        #logging.warning('ACtion:'+ str(actionId))
        
            
        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            logging.warning('Close:5')
            self.params = 888
            selected_index=-1
            
            self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK,ACTION_NAV_BACK]:
            self.params = 888
            selected_index=-1
            self.close()

    
    def onClick(self, controlId):
        global playing_text,done1_1,selected_index
        self.tick=60
        
        if controlId != 3001:
            self.clicked=True
            '''
            self.getControl(3000).setVisible(False)
            self.getControl(102).setVisible(False)
            self.getControl(505).setVisible(False)
            self.getControl(909).setPosition(1310, 40)
            self.getControl(2).setPosition(1310, 100)
            self.getControl(self.imagecontrol).setVisible(False)
            self.getControl(303).setVisible(False)
            self.story_gone=1
            '''
            index = self.list.getSelectedPosition()        
            
            try:    
                self.params = index
                log.warning('Clicked:'+str(controlId)+':'+str(index))
            except:
                self.params = None
            #playing_text=''
            xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
            selected_index=self.params
            self.close()
            #return self.params
        else:
            log.warning('Close:7')
            selected_index=-1
            self.close()
        
    def close_now(self):
        global done1_1
        log.warning('Close:8')
        self.params = 888
        self.done=1
        xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
        xbmc.sleep(1000)
        log.warning('Close now CLosing')
        done1_1=3
        self.close()
    def onFocus(self, controlId):
        pass
class ContextMenu_new2(xbmcgui.WindowXMLDialog):
    
    def __new__(cls, addonID, menu,icon,fan,txt,results,po_watching,l_full_stats,tv_movie,id,tvdb_id,season,episode,show_original_year,original_title):
        FILENAME='contextmenu_new3.xml'
        if Addon.getSetting("sources_window_n")=='1':
            FILENAME='contextmenu_new.xml'
        
        return super(ContextMenu_new2, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
        

    def __init__(self, addonID, menu,icon,fan,txt,results,po_watching,l_full_stats,tv_movie,id,tvdb_id,season,episode,show_original_year,original_title):
        global playing_text,selected_index
        log.warning('Init')
        super(ContextMenu_new2, self).__init__()
        self.menu = menu
        self.original_title=original_title
        self.show_original_year=show_original_year
        self.episode=episode
        self.season=season
        if len(episode)==1:
          self.episode_n="0"+episode
        else:
           self.episode_n=episode
        if len(season)==1:
          self.season_n="0"+season
        else:
          self.season_n=season
      
        self.id=id
        self.tv_movie=tv_movie
        self.tvdb_id=tvdb_id
        self.done_extra_fanart=False
        self.all_n_fan=[]
        self.all_banner=[]
        if Addon.getSetting("sources_window_n")=='1':
            thread=[]
            thread.append(Thread(self.extra_fanart))
            thread[len(thread)-1].setName('fill_table')
            
            thread[0].start()
         
        self.auto_play=0
        selected_index=-1
        self.po_watching=po_watching
        self.l_full_stats=l_full_stats
        self.results=results
        self.params    = 666666
        self.imagecontrol=101
        self.bimagecontrol=5001
        self.txtcontrol=2
        self.tick_label=6001
        self.icon=icon
        self.fan=fan
        self.text=txt
        playing_text=''
        self.tick=60
        self.done=0
        self.story_gone=0
        self.count_p=0
        self.keep_play=''
        self.tick=60
        self.s_t_point=0
        self.start_time=time.time()
        log.warning('dInit')
    def extra_fanart(self):
        
       self.all_n_fan=[]
       self.all_banner=[]
       try:
            time_to_save=int(Addon.getSetting("save_time"))
            full_art= cache.get(get_more_meta, time_to_save, self.id,self.tv_movie,self.tvdb_id, table='pages') 
            
            
            if self.tv_movie=='tv':
                logo=full_art['hdtvlogo']
                if len(logo)>0:
                    all_logo=[]
                    for itt in logo:
                       if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    
                
                
                for itt in full_art['showbackground']:
                   if itt['lang']=='en':
                    self.all_n_fan.append(itt['url'])
                for itt in full_art['tvbanner']:
                   if itt['lang']=='en':
                    self.all_banner.append(itt['url'])
            else:
                logo=full_art['hdmovielogo']
                if len(logo)>0:
                    all_logo=[]
                    for itt in logo:
                       if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    
                
                
                for itt in full_art['moviebackground']:
                   if itt['lang']=='en':
                    self.all_n_fan.append(itt['url'])
                for itt in full_art['moviebanner']:
                   if itt['lang']=='en':
                    self.all_banner.append(itt['url'])
            
            
           
            if len(self.all_banner)>0:
               
                self.getControl(3003).setImage(random.choice(self.all_banner))
            #if len(self.all_n_fan)>0:
                
            #    self.getControl(5001).setImage(random.choice(self.all_n_fan))
       except Exception as e:
            log.warning('Fanart Err:'+str(e))
       self.done_extra_fanart=True
    def background_work(self):
        global playing_text,mag_start_time_new,now_playing_server,done1_1
        tick=0
        tick2=0
        changed=1
        vidtime=0
        while(1):
            
            all_t=[]
            for thread in threading.enumerate():
                if ('tick_time' in thread.getName()) or ('background_task' in thread.getName()) or ('get_similer' in thread.getName()) or ('MainThread' in thread.getName()) or ('sources_s' in thread.getName()):
                    continue
                
                if (trd_alive(thread)):
                    all_t.append( thread.getName())
            self.getControl(606).setLabel(','.join(all_t))
            if  xbmc.getCondVisibility('Window.IsActive(busydialog)'):
                self.getControl(102).setVisible(True)
                if tick2==1:
                    self.getControl(505).setVisible(True)
                    tick2=0
                else:
                    self.getControl(505).setVisible(False)
                    tick2=1
            else:
                self.getControl(102).setVisible(False)
                self.getControl(505).setVisible(False)
            if len(playing_text)>0 or  self.story_gone==1 :
                changed=1
                vidtime=0
                if xbmc.Player().isPlaying():
                    vidtime = xbmc.Player().getTime()
                
                t=time.strftime("%H:%M:%S", time.gmtime(vidtime))
                
                if len(playing_text)==0:
                    playing_text=self.keep_play
                try:
                    self.keep_play=playing_text
                    self.getControl(self.txtcontrol).setText(t+'\n'+playing_text.split('$$$$')[0]+'\n'+now_playing_server.split('$$$$')[0]+'\n'+now_playing_server.split('$$$$')[1])
                    if vidtime == 0:
                        if tick==1:
                            self.getControl(303).setVisible(True)
                            tick=0
                        else:
                            self.getControl(303).setVisible(False)
                            tick=1
                except Exception as e:
                    log.warning('Skin ERR:'+str(e))
                    self.params = 888
                    self.done=1
                    log.warning('Close:4')
                    xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
                    done1_1=3
                    self.close()
                    pass
            
            elif changed==1:
                    changed=0
                
                    self.getControl(303).setVisible(False)
                    self.getControl(self.txtcontrol).setText(self.text)
            
            if self.done==1:
                break
            if xbmc.Player().isPlaying():
                self.tick=60
                self.count_p+=1
                self.st_time=0
                
                vidtime = xbmc.Player().getTime()
                if self.s_t_point==0:
                    
                    
                    if vidtime > 0:
                        self.getControl(3000).setVisible(False)
                        self.getControl(self.imagecontrol).setVisible(False)
                        self.getControl(505).setVisible(False)
                        self.getControl(909).setPosition(1310, 40)
                        self.getControl(2).setPosition(1310, 100)
                        self.s_t_point=1
                        self.getControl(303).setVisible(False)
                        self.story_gone=1
                        log.warning('Change seek Time:'+str(mag_start_time_new))
                        try:
                            if int(float(mag_start_time_new))>0:
                                xbmc.Player().seekTime(int(float(mag_start_time_new)))
                        except:
                            pass
                
                if vidtime > 0:
                    playing_text=''
     
                try:
                    value_d=(vidtime-(int(float(mag_start_time_new)))) 
                except:
                    value_d=vidtime
                play_time=int(Addon.getSetting("play_full_time"))
                if value_d> play_time and self.s_t_point>0:
                    self.params = 888
                    self.done=1
                    log.warning('Close:1')
                    xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
                    done1_1=3
                    self.close()
              
                if self.count_p>(play_time+30) :
                   if Addon.getSetting("play_first")!='true':
                   
                    self.params = 888
                    self.done=1
                    log.warning('Close:3')
                    xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
                    done1_1=3
                    self.close()
            else:
                self.count_p=0
                self.s_t_point=0
                self.getControl(3000).setVisible(True)
         
                #self.getControl(505).setVisible(True)
                self.getControl(self.imagecontrol).setVisible(True)
                self.story_gone=0
                self.getControl(2).setPosition(1310, 700)
                self.getControl(909).setPosition(1310, 10)
            xbmc.sleep(1000)
    def tick_time(self):
        global done1_1
        while(self.tick)>0:
            self.getControl(self.tick_label).setLabel(str(self.tick))
            self.tick-=1
            
            if self.params == 888:
                break
            xbmc.sleep(1000)
        if self.params != 888:
            self.params = 888
            self.done=1
            log.warning('Close:93')
            xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
            done1_1=3
            self.close()
    def clean_title(self,title, broken=None):
        title = title.lower()
        # title = tools.deaccentString(title)
        #title = tools.strip_non_ascii_and_unprintable(title)

        if broken == 1:
            apostrophe_replacement = ''
        elif broken == 2:
            apostrophe_replacement = ' s'
        else:
            apostrophe_replacement = 's'
        title = title.replace("\\'s", apostrophe_replacement)
        title = title.replace("'s", apostrophe_replacement)
        title = title.replace("&#039;s", apostrophe_replacement)
        title = title.replace(" 039 s", apostrophe_replacement)

        title = re.sub(r'\:|\\|\/|\,|\!|\?|\(|\)|\'|\"|\\|\[|\]|\-|\_|\.', ' ', title)
        title = re.sub(r'\s+', ' ', title)
        title = re.sub(r'\&', 'and', title)

        return title.strip()
    def  getInfo(self,release_title):
        info = {}
        release_title = self.clean_title(release_title)
        info['encoding']=[]
        info['audio']=[]
        info['channels']=[]
        info['source']=[]
        info['language']=[]
            
        #info.video
        if any(i in release_title for i in ['x264', 'x 264', 'h264', 'h 264', 'avc']):
            info['encoding'].append('AVC')
        if any(i in release_title for i in ['x265', 'x 265', 'h265', 'h 265', 'hevc']):
            info['encoding'].append('HEVC')
        if any(i in release_title for i in ['xvid']):
            info['encoding'].append('XVID')
        if any(i in release_title for i in ['divx']):
            info['encoding'].append('DIVX')
        if any(i in release_title for i in ['mp4']):
            info['encoding'].append('MP4')
        if any(i in release_title for i in ['wmv']):
            info['encoding'].append('WMV')
        if any(i in release_title for i in ['mpeg']):
            info['encoding'].append('MPEG')
        if any(i in release_title for i in ['remux', 'bdremux']):
            info['encoding'].append('REMUX')
        if any(i in release_title for i in [' hdr ', 'hdr10', 'hdr 10']):
            info['encoding'].append('HDR')
        if any(i in release_title for i in [' sdr ']):
            info['encoding'].append('SDR')
        
        #info.audio
        if any(i in release_title for i in ['aac']):
            info['audio'].append('AAC')
        if any(i in release_title for i in ['dts']):
            info['audio'].append('DTS')
        if any(i in release_title for i in ['hd ma' , 'hdma']):
            info['audio'].append('HD-MA')
        if any(i in release_title for i in ['atmos']):
            info['audio'].append('ATMOS')
        if any(i in release_title for i in ['truehd', 'true hd']):
            info['audio'].append('TRUEHD')
        if any(i in release_title for i in ['ddp', 'dd+', 'eac3']):
            info['audio'].append('DD+')
        if any(i in release_title for i in [' dd ', 'dd2', 'dd5', 'dd7', ' ac3']):
            info['audio'].append('DD')
        if any(i in release_title for i in ['mp3']):
            info['audio'].append('MP3')
        if any(i in release_title for i in [' wma']):
            info['audio'].append('WMA')
        
        #info.channels
        if any(i in release_title for i in ['2 0 ', '2 0ch', '2ch']):
            info['channels'].append('2.0')
        if any(i in release_title for i in ['5 1 ', '5 1ch', '6ch']):
            info['channels'].append('5.1')
        if any(i in release_title for i in ['7 1 ', '7 1ch', '8ch']):
            info['channels'].append('7.1')
        
        #info.source 
        # no point at all with WEBRip vs WEB-DL cuz it's always labeled wrong with TV Shows 
        # WEB = WEB-DL in terms of size and quality
        if any(i in release_title for i in ['bluray' , 'blu ray' , 'bdrip', 'bd rip', 'brrip', 'br rip']):
            info['source'].append('BLURAY')
        if any(i in release_title for i in [' web ' , 'webrip' , 'webdl', 'web rip', 'web dl']):
            info['source'].append('WEB')
        if any(i in release_title for i in ['hdrip', 'hd rip']):
            info['source'].append('HDRIP')
        if any(i in release_title for i in ['dvdrip', 'dvd rip']):
            info['source'].append('DVDRIP')
        if any(i in release_title for i in ['hdtv']):
            info['source'].append('HDTV')
        if any(i in release_title for i in ['pdtv']):
            info['source'].append('PDTV')
        if any(i in release_title for i in [' cam ', 'camrip', 'hdcam', 'hd cam', ' ts ', 'hd ts', 'hdts', 'telesync', ' tc ', 'hd tc', 'hdtc', 'telecine', 'xbet']):
            info['source'].append('CAM')
        if any(i in release_title for i in ['dvdscr', ' scr ', 'screener']):
            info['source'].append('SCR')
        if any(i in release_title for i in ['korsub', ' kor ', ' hc']):
            info['source'].append('HC')
        if any(i in release_title for i in ['blurred']):
            info['source'].append('BLUR')
        if any(i in release_title for i in [' 3d']):
            info['source'].append('3D')
        all_lang=['en','eng','english','rus','russian','fr','french','TrueFrench','ita','italian','italiano','castellano','spanish','swedish','dk','danish','german','nordic','exyu','chs','hindi','polish','mandarin','kor','korean','koraen','multi']
        all_lang_des=['English','English','English','Russian','Russian','French','French','French','Italiano','Italiano','Italiano','Castellano','Spanish','Swedish','Danish','Danish','German','Nordic','ExYu','Chinese','Hindi','Polish','Mandarin','Korean','Korean','Korean','Multi']
        index=0

        for itt in all_lang:
            if ' '+itt+' ' in release_title.lower():
                if all_lang_des[index] not in info['language']:
                    info['language'].append(all_lang_des[index])
            index+=1
            
        fixed_info={}
        for key in info:
            if len(info[key])>0:
                fixed_info[key]=info[key]
                
        return fixed_info



    def fill_table(self,all_his_links):
        log.warning('Start Fill')
        count=0
        self.paramList = []
        all_liz_items=[]
        log.warning('Fil table start')
        
        
        
        try:
            simple_info=Addon.getSetting("simple_info")=='true'
            
            if not simple_info:
                from resources.modules import PTN
            for item in self.menu:
                
                if simple_info:
                    
                    info=self.getInfo(item[4])
                else:
                   try:
                    info=(PTN.parse(item[4].replace('[COLOR red][I]','').replace('[/I][/COLOR]','').replace('[COLOR lightblue][B]','').replace('[COLOR khaki][B]','').replace('[/B][/COLOR]\n','').replace('-','.')))
                   except:
                    info=self.getInfo(item[4])
                add_d=[]
                
                
                counter_page=0
                nxt=0
                for key in info:
                    if type(info[key])==list:
                        
                        try:
                            info_key=','.join(info[key])
                        except:
                            info_key=str(info[key])
                    else:
                        info_key=str(info[key])
                    if key=='language':
                        color='pink'
                    else:
                        color='khaki'
                    nx_line=2
                    if Addon.getSetting("sources_window_n")=='1':
                        nx_line=2
                    nxt+=1
                    
                    
                    
                    if 'Open filtered links' not in item[4] and 'Open rejected ' not in item[4]:
                        if nxt>nx_line:
                            nxt=0
                            item[4]=item[4]+' - [COLOR lightblue]'+key+'[/COLOR]: [COLOR %s]'%color+info_key+'[/COLOR]\n'
                        else:
                            
                            item[4]=item[4]+' - [COLOR lightblue]'+key+'[/COLOR]: [COLOR %s]'%color+info_key+'[/COLOR]'
                    
               
                self.getControl(202).setLabel(str(((count*100)/len(self.menu))) + Addon.getLocalizedString(32010))
                count+=1
                self.paramList.append(item[6])
                '''
                info=(PTN.parse(item[0]))
                if 'excess' in info:
                    if len(info['excess'])>0:
                        item[0]='.'.join(info['excess'])
                '''
                golden=False
                if 'Cached ' in item[0]:
                    golden=True
                item[0]=item[0].replace('Cached ','')
                
                title ='[COLOR deepskyblue][B]'+item[0] +'[/B][/COLOR]'
                if len(item[1].strip())<2:
                    item[1]='--'
                if len(item[2].strip())<2:
                    item[2]=''
                if len(item[3].strip())<2:
                    item[3]='--'
                if len(item[4])<2:
                    item[4]='--'
                if len(item[5])<2:
                    item[5]='--'
                server=item[1]
                pre_n='[COLOR lime]'+item[2]+'[/COLOR]'
                q=item[3]
                
                if item[5]=='0.0GB':
                    size='--'
                else:
                    size='[COLOR yellow]'+item[5]+'[/COLOR]'
                link=item[6]
                if Addon.getSetting("add_colors")=='true':
                    original_title_wd=self.original_title.replace(' ','.')
                    original_title_alt=self.original_title.replace('&','and')
                    heb_name_wd=heb_name.replace(' ','.')
                    item[4]=item[4].replace('-','.').replace('_','.').replace('.',' ')
                    
                    item[4]=item[4].replace('  ',' ').replace(self.original_title.lower()+' ',self.original_title+' ')
                    item[4]=item[4].replace('S%sE%s'%(self.season_n,self.episode_n),'[COLOR lime]S%sE%s[/COLOR]'%(self.season_n,self.episode_n))
                    item[4]=item[4].replace(self.original_title+' ','[COLOR yellow]'+self.original_title+'[/COLOR]'+' ').replace(original_title_wd+' ','[COLOR yellow]'+self.original_title+'[/COLOR]'+' ')
                    item[4]=item[4].replace(original_title_alt+' ','[COLOR yellow]'+original_title_alt+'[/COLOR]'+' ')
                    item[4]=item[4].replace(self.show_original_year,'[COLOR plum]'+self.show_original_year+'[/COLOR]')
                    #heb
                    #item[4]=item[4].replace(heb_name,'[COLOR yellow]'+heb_name+'[/COLOR]').replace(heb_name_wd,'[COLOR yellow]'+heb_name+'[/COLOR]')
                  
                supplay=item[4]
               
                
                if q=='2160':
                    q='4k'
                if q.lower()=='hd':
                    q='unk'
                liz   = xbmcgui.ListItem(title)
                liz.setProperty('server', '')#server
                liz.setProperty('pre',pre_n)
                if 'https' in item[7]:
                    liz.setProperty('image_collection',item[7])
                    liz.setProperty('collection','yes')
                liz.setProperty('Quality', q)
                liz.setProperty('supply', supplay)
                liz.setProperty('size', size)
              
                
                liz.setProperty('server_v','100')
           
                
                all_liz_items.append(liz)
            log.warning(' Done Loading')
            self.getControl(202).setLabel('')
            self.list.addItems(all_liz_items)

            self.setFocus(self.list)
            log.warning('Fil table End')
            #while self.done_extra_fanart!=True:
            #    xbmc.sleep(100)
     
            
        except Exception as e:
            log.warning('Fill error:'+str(e))
            import linecache
            sources_searching=False
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            log.warning('Fill error:'+str(lineno))
            log.warning('inline:'+line)
            log.warning('Error:'+str(e))
            xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'inLine:'+str(lineno))))
            self.close()
           
    def onInit(self):
        log.warning('Start')
        xbmc.Player().stop()
        xbmc.executebuiltin('Dialog.Close(busydialog)')
        #dbcur.execute("SELECT * FROM historylinks")
        #all_his_links_pre = dbcur.fetchall()
        all_his_links=[]
        #for link,status,option in all_his_links_pre:
        #    all_his_links.append(link)
        
        #thread[1].start()
        #thread[2].start()
        line   = 38
        spacer = 20
        delta  = 0 
        log.warning('1')
        nItem = len(self.menu)
        if nItem > 16:
            nItem = 16
            delta = 1
        log.warning('2')
        self.getControl(self.imagecontrol).setImage(self.icon)
        if Addon.getSetting("fanart_sources")=='true':
            self.getControl(self.bimagecontrol).setImage(self.fan)
        log.warning('3')
        if len(playing_text)==0:
            self.getControl(self.txtcontrol).setText(self.text)
        height = (line+spacer) + (nItem*line)
        height=1100
        self.getControl(5001).setHeight(height)
        log.warning('4')
        self.list = self.getControl(3000)
        self.list.setHeight(height)
        log.warning('5')
        newY = 360 - (height/2)

        self.getControl(5000).setPosition(self.getControl(5000).getX(), 0)
        self.getControl(999).setLabel(self.results)
        self.getControl(888).setLabel(self.po_watching)
        log.warning('self.l_full_stats:'+str(self.l_full_stats))
        self.getControl(777).setLabel(self.l_full_stats)
        
        log.warning('Loading')
        thread=[]
        #thread.append(Thread(self.background_work))
        #thread[len(thread)-1].setName('background_task')
        #thread.append(Thread(self.tick_time))
        #thread[len(thread)-1].setName('tick_time')
        log.warning('Fill table')
        
        thread.append(Thread(self.fill_table,all_his_links))
        thread[len(thread)-1].setName('fill_table')
        log.warning('trd s')
        thread[0].start()
        
            
           
    def played(self):
        self.params =7777
    def onAction(self, action):  
        global done1_1,selected_index
        actionId = action.getId()
        #log.warning('actionId:'+str(actionId))
        self.tick=60
        #log.warning('ACtion:'+ str(actionId))
        
            
        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            log.warning('Close:5')
            self.params = 888
            selected_index=-1
            
            self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK,ACTION_NAV_BACK]:
            self.params = 888
            selected_index=-1
            self.close()

    
    def onClick(self, controlId):
        global playing_text,done1_1,selected_index
        self.tick=60
        
        if controlId != 3001:
            '''
            self.getControl(3000).setVisible(False)
            self.getControl(102).setVisible(False)
            self.getControl(505).setVisible(False)
            self.getControl(909).setPosition(1310, 40)
            self.getControl(2).setPosition(1310, 100)
            self.getControl(self.imagecontrol).setVisible(False)
            self.getControl(303).setVisible(False)
            self.story_gone=1
            '''
            index = self.list.getSelectedPosition()        
            
            try:    
                self.params = index
                log.warning('Clicked:'+str(controlId)+':'+str(index))
            except:
                self.params = None
            #playing_text=''
            xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
            selected_index=self.params
            self.close()
            #return self.params
        else:
            log.warning('Close:7')
            selected_index=-1
            self.close()
        
    def close_now(self):
        global done1_1
        log.warning('Close:8')
        self.params = 888
        self.done=1
        xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
        xbmc.sleep(1000)
        log.warning('Close now CLosing')
        done1_1=3
        self.close()
    def onFocus(self, controlId):
        pass
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 9...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 9...', '' )
def show_updates(force=False):
    
    
    #from shutil import copyfile
    version = Addon.getAddonInfo('version')
    ms=False
    if not os.path.exists(os.path.join(user_dataDir, 'version.txt')):
        ms=True
    else:
        file = open(os.path.join(user_dataDir, 'version.txt'), 'r') 
        file_data= file.readlines()
        file.close()
        if version not in file_data:
          ms=True
    if force==True:
        ms=True
    if ms:
        current_folder = os.path.dirname(os.path.realpath(__file__))
        change_log=os.path.join(current_folder,'changelog.txt')
        file = open(change_log, 'r') 
        news= file.read()
        file.close()
        
        
        contact(title=Addon.getLocalizedString(32011)+version ,msg=news)
        file = open(os.path.join(user_dataDir, 'version.txt'), 'w') 
        file.write(version)
        file.close()
        ClearCache()
       
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 10...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 10...', '' )
class fav_mv(xbmcgui.WindowXMLDialog):
    #from resources.modules.tmdb import html_g_movie
    def __new__(cls, addonID,id):
        
        FILENAME='moviefavorite.xml'
        
        return super(fav_mv, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
        

    def __init__(self, addonID,id):
        super(fav_mv, self).__init__()
        self.id=id
        self.all_d={}
        self.closenow=0
        self.str_next=""
        try:
            self.time_c=xbmc.Player().getTotalTime()-xbmc.Player().getTime()
        except:
            self.time_c=30
        
        #Thread(target=self.background_task).start()
        
        #Thread(target=self.get_similer).start()
    def get_str_next(self):
        return self.str_next
    def onInit(self):
        
        from resources.modules.tmdb import html_g_movie
        a=1
        self.setFocus(self.getControl(201))
        x='http://api.themoviedb.org/3/movie/%s/recommendations?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(self.id,lang)
        html=get_html(x).json()
        loc=random.randint(0,len(html['results'])-1)
        self.all_d={}
        self.all_d['title']=html['results'][loc]['title']
        if 'poster_path' in html['results'][loc]:
            if html['results'][loc]['poster_path']!=None:
                self.all_d['icon']='https://image.tmdb.org/t/p/original/'+html['results'][loc]['poster_path']
            else:
                self.all_d['icon']=' '
                
       
        if 'backdrop_path' in html['results'][loc]:
            if html['results'][loc]['backdrop_path']!=None:
                self.all_d['fan']='https://image.tmdb.org/t/p/original/'+html['results'][loc]['backdrop_path']
            else:
                self.all_d['fan']=' '
        self.all_d['original_title']=html['results'][loc]['original_title']
        self.all_d['plot']=html['results'][loc]['overview']
        self.all_d['n_id']=html['results'][loc]['id']
        html_g=html_g_movie
        genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                if i['name'] is not None])
        try:self.all_d['genere'] = u' / '.join([genres_list[x] for x in html['results'][loc]['genre_ids']])
        except:self.all_d['genere']=''
        self.all_d['rating']=str(html['results'][loc]['vote_average'])
        if 'release_date' in html['results'][loc]:
            self.all_d['year']=str(html['results'][loc]['release_date'].split("-")[0])
        else:
            self.all_d['year']='0'
        #self.getControl(101).setImage(self.all_d['icon'])
        self.getControl(103).setImage(self.all_d['fan'])
        self.getControl(102).setLabel('[COLOR blue][B]'+self.all_d['title']+' - '+self.all_d['year']+ ' - '+self.all_d['rating']+'[/B][/COLOR]')
        self.getControl(104).setText(self.all_d['plot'])
        self.getControl(105).setLabel(self.all_d['genere'])
        
        Thread(target=self.background_task).start()
    def onAction(self, action):
        global stop_window,once_fast_play
        
        actionId = action.getId()

        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            
            stop_window=True
            #self.close_tsk=1
            
            
            return self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK]:
           
            stop_window=True
          
            return self.close()
    def background_task(self):
            global list_index
            t=int(self.time_c)*10
            counter_close=0
            self.progressControl = self.getControl(3014)
            e_close=0
            before_end=int(Addon.getSetting("movie_window"))*10
            counter_close2=before_end
            while(t>30):
                try:
                    t=(xbmc.Player().getTotalTime()-xbmc.Player().getTime())*10
                except:
                    pass
                self.label=self.getControl(3015)
                self.label.setLabel(('%s')%str(int(counter_close2)/10))
                self.label=self.getControl(3016)
                self.label.setLabel(('Movie ends in %s')%str(int(t)/10))
                counter_close2-=1
                if counter_close2==0:
                    t=0
                    break
                if t<counter_close2:
                    sh_p=t
                else:
                    sh_p=counter_close2
                self.currentProgressPercent=int((sh_p*100)/before_end)
           
                self.progressControl.setPercent(self.currentProgressPercent)
                xbmc.sleep(100)
                
                if self.closenow==1:
                    break
             
            self.close()

    def onClick(self, controlId):
        
        stop_window=True
        self.closenow=1
        if controlId==201:
            settings=Addon.getSetting
            fav_search_f=settings("fav_search_f_tv")
            fav_servers_en=settings("fav_servers_en_tv")
            fav_servers=settings("fav_servers_tv")
            google_server= settings("google_server_tv")
            rapid_server=settings("rapid_server_tv")
            direct_server=settings("direct_server_tv")
            heb_server=settings("heb_server_tv")
            if  fav_search_f=='true' and fav_servers_en=='true' and (len(fav_servers)>0 or heb_server=='true' or google_server=='true' or rapid_server=='true' or direct_server=='true'):
                
                fav_status='true'
            else:
                fav_status='false'
            xbmc.Player().stop()
            self.str_next='RunPlugin("%s?nextup=true&url=%s&no_subs=0&season=%s&episode=%s&mode=15&original_title=%s&id=%s&dd=%s&show_original_year=%s&fanart=%s&iconimage=%s&name=%s&description=%s")'%(sys.argv[0],'www','%20','%20',que(self.all_d['original_title']),self.all_d['n_id'],' ',self.all_d['year'],que(self.all_d['fan']),que(self.all_d['icon']),que(self.all_d['title']),que(self.all_d['plot']))
            
        
      
        self.close()
        
    
    def onFocus(self, controlId):
        pass 
class UpNext(xbmcgui.WindowXMLDialog):
    item = None
    cancel = False
    watchnow = False
    
    progressStepSize = 0
    currentProgressPercent = 100

    def __init__(self, *args, **kwargs):
        log.warning('INIT UPNEXT')
        global clicked
        from platform import machine
        
        OS_MACHINE = machine()
        self.closenow=0
        clicked=False
        self.action_exitkeys_id = [10, 13]
        log.warning('INIT UPNEXT0')
        self.progressControl = None
        if OS_MACHINE[0:5] == 'armv7':
            xbmcgui.WindowXMLDialog.__init__(self)
        else:
            xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
        log.warning('INIT UPNEXT2')
        
        
   
    def background_task(self):
        global list_index,clicked_id
        t=int(self.time_c)*10
        counter_close=0
        self.progressControl = self.getControl(3014)
        e_close=0
        before_end=int(Addon.getSetting("before_end2"))*10
        global_t=t-before_end
        counter_close2=t-before_end
        #log.warning('counter_close2_t:'+str(t))
        while(t>30):
            self.label=self.getControl(3015)
            #self.label.setLabel(('%s seconds')%str(int(counter_close2)/10))
            self.label.setLabel(str(clicked_id))
            counter_close2-=1
            #log.warning('counter_close2:'+str(counter_close2))
            
            if counter_close2==0:
                t=0
                break
            self.currentProgressPercent=int((counter_close2*100)/global_t)
       
            self.progressControl.setPercent(self.currentProgressPercent)
            xbmc.sleep(100)
            t-=1
            if self.closenow==1:
                break
        if self.closenow==0:
            list_index=self.list.getSelectedPosition()        
        self.close()
    def onInit(self):
        self.time_c=30
        try:
            self.time_c=xbmc.Player().getTotalTime()-xbmc.Player().getTime()
        except:
            self.time_c=30
        
        
            
        self.list = self.getControl(3000)
        self.but = self.getControl(3012)
        self.closebut=self.getControl(3013)
        self.setFocus(self.but)
        if len(self.item['list'])==0:
                self.but.setVisible(False)
                self.setFocus(self.closebut)
        for it in self.item['list']:
         
          
          liz   = xbmcgui.ListItem(it.split('$$$$$$$')[0])
          self.list.addItem(liz)
       
        
        
        log.warning('INIT UPNEXT1')
        Thread(target=self.background_task).start()
        self.setInfo()
        self.prepareProgressControl()

    def setInfo(self):
        log.warning('INIT UPNEXT2')
       
        episodeInfo = str(self.item['season']) + 'x' + str(self.item['episode']) + '.'
        if self.item['rating'] is not None:
            rating = str(round(float(self.item['rating']), 1))
        else:
            rating = None
        
        if self.item is not None:
            self.setProperty(
                'fanart', self.item['art'].get('tvshow.fanart', ''))
            self.setProperty(
                'landscape', self.item['art'].get('tvshow.landscape', ''))
            self.setProperty(
                'clearart', self.item['art'].get('tvshow.clearart', ''))
            self.setProperty(
                'clearlogo', self.item['art'].get('tvshow.clearlogo', ''))
            self.setProperty(
                'poster', self.item['art'].get('tvshow.poster', ''))
            self.setProperty(
                'thumb', self.item['art'].get('thumb', ''))
            self.setProperty(
                'plot', self.item['plot'].replace("\n",'').strip())
            self.setProperty(
                'tvshowtitle', self.item['showtitle'])
            self.setProperty(
                'title', self.item['title'])
            self.setProperty(
                'season', str(self.item['season']))
            self.setProperty(
                'episode', str(self.item['episode']))
            self.setProperty(
                'seasonepisode', episodeInfo)
            self.setProperty(
                'year', str(self.item['firstaired']))
            self.setProperty(
                'rating', rating)
            self.setProperty(
                'playcount', str(self.item['playcount']))

    def prepareProgressControl(self):
        log.warning('INIT UPNEXT3')
        # noinspection PyBroadException
        try:
            self.progressControl = self.getControl(3014)
            if self.progressControl is not None:
                self.progressControl.setPercent(self.currentProgressPercent)
        except Exception:
            pass

    def setItem(self, item):
        self.item = item

    def setProgressStepSize(self, progressStepSize):
        self.progressStepSize = progressStepSize

    def updateProgressControl(self):
        # noinspection PyBroadException
        try:
            self.currentProgressPercent = self.currentProgressPercent - self.progressStepSize
         
            self.progressControl = self.getControl(3014)
           
            if self.progressControl is not None:
                self.progressControl.setPercent(self.currentProgressPercent)
        except Exception:
            pass

    def setCancel(self, cancel):
        self.cancel = cancel

    def isCancel(self):
        return self.cancel

    def setWatchNow(self, watchnow):
        self.watchnow = watchnow

    def isWatchNow(self):
        return self.watchnow

    def onFocus(self, controlId):
        pass

    def doAction(self):
        pass

    def closeDialog(self):
        self.close()

    def onClick(self, control_id):
        global list_index,clicked,clicked_id
        clicked_id=str(control_id)
        
        if control_id == 3012:
            # watch now
            clicked=True
            list_index=0
            self.setWatchNow(True)
            self.closenow=1
            self.close()
            
        elif control_id == 3013:
            # cancel
            clicked=False
            list_index=888
            self.setCancel(True)
            self.closenow=1
            self.close()
        elif control_id == 3000:
            clicked=True
            index = self.list.getSelectedPosition()        
            list_index=index
            self.closenow=1
            self.close()
        pass

    def onAction(self, action):
        
        if action == ACTION_PLAYER_STOP:
            self.closenow=1
            self.close()

def get_params():
        param=[]
        if len(sys.argv)>=2:
          paramstring=sys.argv[2]
          if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param     

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 11...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 11...', '' )
def get_genere(link):
   
   images={}
   html=get_html(link).json()
   aa=[]
   image='https://ia802503.us.archive.org/28/items/icon_20220511/icon.png'
   for data in html['genres']:
     if '/movie' in link:
       new_link='http://api.themoviedb.org/3/genre/%s/movies?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(str(data['id']),lang)
     else:
       new_link='http://api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&sort_by=popularity.desc&with_genres=%s&language=%s&page=1'%(str(data['id']),lang)
     
     
     aa.append(addDir3(data['name'],new_link,14,image,image,data['name']))
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
def read_site_html(url_link):
    
    '''
    req = urllib2.Request(url_link)
    req.add_header('User-agent',__USERAGENT__)# 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    html = urllib2.urlopen(req).read()
    '''
    html=get_html(url_link)
    return html
def tv_show_menu():
    all_d=[]
    import datetime
    now = datetime.datetime.now()
    aa=addDir3(Addon.getLocalizedString(32023),'tv',145,BASE_LOGO+'ghost1.png',all_fanarts['32023'],'History')
	#place your Jen playlist here:
    #dulpicate this line with your address
    aa=addDir3('1Click','https://ia902508.us.archive.org/35/items/tv.shows.theboys/tv.shows.theboys.xml',189,'https://ia902503.us.archive.org/28/items/icon_20220511/icon.png','https://ia902507.us.archive.org/12/items/fanart_202205/fanart.jpg','1Click')
    all_d.append(aa)
    #Popular
    aa=addDir3(Addon.getLocalizedString(32012),'http://api.themoviedb.org/3/tv/popular?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%lang,14,BASE_LOGO+'ghost1.png',all_fanarts['32013'],'TMDB')
    all_d.append(aa)

    aa=addDir3(Addon.getLocalizedString(32013),'https://api.themoviedb.org/3/tv/on_the_air?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%lang,14,BASE_LOGO+'ghost1.png',all_fanarts['32013'],'TMDB')
    all_d.append(aa)
    
    
    aa=addDir3(Addon.getLocalizedString(32014),'https://api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en-US&sort_by=popularity.desc&first_air_date_year='+str(now.year)+'&timezone=America%2FNew_York&include_null_first_air_ates=false&language={0}&page=1'.format(lang),14,BASE_LOGO+'ghost1.png',all_fanarts['32014'],'New Tv shows')
    all_d.append(aa)
    #new episodes
    aa=addDir3(Addon.getLocalizedString(32015),'https://api.tvmaze.com/schedule',20,BASE_LOGO+'ghost1.png',all_fanarts['32015'],'New Episodes')
    all_d.append(aa)
    #Genre
    aa=addDir3(Addon.getLocalizedString(32016),'http://api.themoviedb.org/3/genre/tv/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%lang,18,BASE_LOGO+'ghost1.png',all_fanarts['32016'],'TMDB')
    all_d.append(aa)
    #Years
    aa=addDir3(Addon.getLocalizedString(32017),'tv_years&page=1',14,BASE_LOGO+'ghost1.png',all_fanarts['32017'],'TMDB')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32018),'tv_years&page=1',101,BASE_LOGO+'ghost1.png',all_fanarts['32018'],'TMDB')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32019),'advance_tv',14,BASE_LOGO+'ghost1.png',all_fanarts['32019'],'Advance Search')
    
    all_d.append(aa)
    #Search tv
    aa=addDir3(Addon.getLocalizedString(32020),'http://api.themoviedb.org/3/search/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&query=%s&language={0}&page=1'.format(lang),14,BASE_LOGO+'ghost1.png',all_fanarts['32020'],'TMDB')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32021),'tv',143,BASE_LOGO+'ghost1.png',all_fanarts['32021'],'TMDB')
    all_d.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32023),'tv',145,BASE_LOGO+'ghost1.png',all_fanarts['32023'],'History')
    all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def tv_neworks():
    all_d=[]
    if Addon.getSetting("order_networks")=='0':
        order_by='popularity.desc'
    elif Addon.getSetting("order_networks")=='2':
        order_by='vote_average.desc'
    elif Addon.getSetting("order_networks")=='1':
        order_by='first_air_date.desc'
    aa=addDir3('[COLOR lightblue]Disney+[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=2739&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Disney')
    all_d.append(aa)
    aa=addDir3('[COLOR blue]Apple TV+[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=2552&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Apple')
    all_d.append(aa)
    aa=addDir3('[COLOR red]NetFlix[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=213&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','NetFlix')
    all_d.append(aa)
    aa=addDir3('[COLOR gray]HBO[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=49&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','HBO')
    all_d.append(aa)
    aa=addDir3('[COLOR lightblue]CBS[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=16&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','HBO')
    all_d.append(aa)
    aa=addDir3('[COLOR purple]SyFy[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=77&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','SyFy')
    all_d.append(aa)
    aa=addDir3('[COLOR lightgreen]The CW[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=71&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','The CW')
    all_d.append(aa)
    aa=addDir3('[COLOR silver]ABC[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=2&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','ABC')
    all_d.append(aa)
    aa=addDir3('[COLOR yellow]NBC[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=6&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','NBC')
    all_d.append(aa)
    aa=addDir3('[COLOR gold]AMAZON[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=1024&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','AMAZON')
    all_d.append(aa)
    aa=addDir3('[COLOR green]hulu[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=453&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','hulu')
    all_d.append(aa)
    aa=addDir3('[COLOR red]Showtime[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=67&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','showtime')
    all_d.append(aa)
    aa=addDir3('[COLOR red]BBC One[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=4&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','BBC')
    all_d.append(aa)
    aa=addDir3('[COLOR teal]BBC Two[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=332&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','BBC')
    all_d.append(aa)
    aa=addDir3('[COLOR pink]BBC Three[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=3&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','BBC')
    all_d.append(aa)
    aa=addDir3('[COLOR lightblue]ITV[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks=9&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','BBC')
    all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
def main_menu(time_data):
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+111)
    #show_updates()
    
            
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+222)
    all_d=[]
   
    if Addon.getSetting('movie_world')=='true':
        aa=addDir3(Addon.getLocalizedString(32024),'www',2,BASE_LOGO+'ghost1.png',all_fanarts['32024'],'Movies')
        all_d.append(aa)
    if Addon.getSetting('tv_world')=='true':
        aa=addDir3(Addon.getLocalizedString(32025),'www',3,BASE_LOGO+'ghost1.png',all_fanarts['32025'],'TV')
        all_d.append(aa)
	#place your Jen playlist here:
    #dulpicate this line with your address
    aa=addDir3('Replays','https://ia902509.us.archive.org/2/items/sportsreplays/sportsreplays.xml',189,'https://ia902503.us.archive.org/28/items/icon_20220511/icon.png','https://ia902507.us.archive.org/12/items/fanart_202205/fanart.jpg','Replays')
    all_d.append(aa)
	#place your Jen playlist here:
    #dulpicate this line with your address
    aa=addDir3('Live TV','https://ia902505.us.archive.org/31/items/Entairt/Entairt.xml',189,'https://ia902503.us.archive.org/28/items/icon_20220511/icon.png','https://ia902507.us.archive.org/12/items/fanart_202205/fanart.jpg','Live TV')
    all_d.append(aa)
    if Addon.getSetting('trakt_world')=='true':
        aa=addDir3(Addon.getLocalizedString(32026),'www',21,BASE_LOGO+'ghost1.png',all_fanarts['32026'],'No account needed)')
        all_d.append(aa)
    if Addon.getSetting('trakt')=='true':
        aa=addDir3(Addon.getLocalizedString(32027),'www',114,BASE_LOGO+'ghost1.png',all_fanarts['32027'],'TV')
        all_d.append(aa)
    if Addon.getSetting('search')=='true':
        aa=addDir3(Addon.getLocalizedString(32020),'www',5,BASE_LOGO+'ghost1.png',all_fanarts['32020'],'Search')
        all_d.append(aa)
    if Addon.getSetting('search_history')=='true':
        aa=addDir3(Addon.getLocalizedString(32021),'both',143,BASE_LOGO+'ghost1.png',all_fanarts['32021'],'TMDB')
        all_d.append(aa)
    if Addon.getSetting('last_link_played')=='true':
        aa=addDir3(Addon.getLocalizedString(32022),'www',144,BASE_LOGO+'ghost1.png',all_fanarts['32022'],'Last Played') 
        all_d.append(aa)
    if Addon.getSetting('whats_new')=='true':
        aa=addNolink(Addon.getLocalizedString(32028) , id,149,False,fanart=all_fanarts['32028'], iconimage=BASE_LOGO+'ghost1.png',plot='',dont_place=True)
        all_d.append(aa)
    if Addon.getSetting('settings')=='true':
        aa=addNolink( Addon.getLocalizedString(32029), id,151,False,fanart=all_fanarts['32029'], iconimage=BASE_LOGO+'ghost1.png',plot='',dont_place=True)
        all_d.append(aa)
    if Addon.getSetting('resume_watching')=='true':		
        aa=addDir3(Addon.getLocalizedString(32030),'both',158,BASE_LOGO+'ghost1.png',all_fanarts['32030'],'TMDB')
        all_d.append(aa)
    if Addon.getSetting('debrid_select')=='0':
        if Addon.getSetting('my_rd_history')=='true':
            aa=addDir3(Addon.getLocalizedString(32031),'1',168,BASE_LOGO+'rd_ghost1.png',all_fanarts['32031'],'TMDB')
            all_d.append(aa)
        if Addon.getSetting('rd_Torrents')=='true':
            aa=addDir3(Addon.getLocalizedString(32032),'1',169,BASE_LOGO+'rd_Torrents.png',all_fanarts['32032'],'TMDB')
            all_d.append(aa)
    if Addon.getSetting('actor')=='true':
        aa=addDir3(Addon.getLocalizedString(32033),'www',72,BASE_LOGO+'ghost1.png',all_fanarts['32033'],'Actor')
        all_d.append(aa)
    if Addon.getSetting('scraper_check')=='true':
        aa=addDir3( Addon.getLocalizedString(32034), id,172,BASE_LOGO+'ghost1.png',all_fanarts['32034'],'Test')
    
    if Addon.getSetting('debug')=='true':
        aa=addDir3( 'Unit tests', 'www',181,'https://lh3.googleusercontent.com/proxy/Ia9aOfcgtzofMb0urCAs8NV-4RRhcIVST-Gqx9GI9RLsx7IJe_5jBqjfdsJcOO3QIV3TT-uiF2nKmyYCX0vj5UPR4iW1iHXgZylE8N8wyNgRLw','https://i.ytimg.com/vi/3wLqsRLvV-c/maxresdefault.jpg','Test')
        
        all_d.append(aa)
    found=False
    for i in range(0,10):
        if Addon.getSetting('imdb_user_'+str(i))!='':
            found=True
            break
    if found:
        aa=addDir3(Addon.getLocalizedString(32309),'www',183,BASE_LOGO+'ghost1.png',all_fanarts['32309'],'Imdb')
        all_d.append(aa)
    
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+333)
    if Addon.getSetting("stop_where")=='0':
            xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+444)
    return time_data
def movie_world():
    all_d=[]
	#place your Jen playlist here:
    #dulpicate this line with your address
    aa=addDir3('1Click','https://ia902507.us.archive.org/35/items/1clicknew/1clicknew.xml',189,'https://ia902503.us.archive.org/28/items/icon_20220511/icon.png','https://ia902507.us.archive.org/12/items/fanart_202205/fanart.jpg','1Click')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32295),'http://api.themoviedb.org/3/movie/now_playing?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%lang,14,BASE_LOGO+'ghost1.png',all_fanarts['32295'],'Tmdb')
    all_d.append(aa)
    'Popular Movies'
    aa=addDir3(Addon.getLocalizedString(32036),'http://api.themoviedb.org/3/movie/popular?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%lang,14,BASE_LOGO+'ghost1.png',all_fanarts['32036'],'Tmdb')
    all_d.append(aa)
    'Released Movies'
    aa=addDir3('Released Movies','http://api.themoviedb.org/3/movie/popular?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&with_release_type=4&page=1'%lang,14,BASE_LOGO+'ghost1.png',all_fanarts['32036'],'Tmdb')
    all_d.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32037),'http://api.themoviedb.org/3/search/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&query=3d&language=%s&append_to_response=origin_country&page=1'%lang,14,BASE_LOGO+'ghost1.png',all_fanarts['32037'],'Tmdb')
    all_d.append(aa)
    
    #Genre
    aa=addDir3(Addon.getLocalizedString(32038),'http://api.themoviedb.org/3/genre/movie/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%lang,18,BASE_LOGO+'ghost1.png',all_fanarts['32038'],'Tmdb')
    all_d.append(aa)
    #Years
    aa=addDir3(Addon.getLocalizedString(32039),'movie_years&page=1',14,BASE_LOGO+'ghost1.png',all_fanarts['32039'],'Tmdb')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32040),'movie_years&page=1',112,BASE_LOGO+'ghost1.png',all_fanarts['32040'],'Tmdb')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32041),'advance_movie',14,BASE_LOGO+'ghost1.png',all_fanarts['32041'],'Advance Search')
    all_d.append(aa)
    #Search movie
    aa=addDir3(Addon.getLocalizedString(32042),'http://api.themoviedb.org/3/search/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&query=%s&language={0}&append_to_response=origin_country&page=1'.format(lang),14,BASE_LOGO+'ghost1.png',all_fanarts['32042'],'Tmdb')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32043),'movie',143,BASE_LOGO+'ghost1.png',all_fanarts['32043'],'TMDB')
    all_d.append(aa)

    aa=addDir3(Addon.getLocalizedString(32044),'movie',145,BASE_LOGO+'ghost1.png',all_fanarts['32044'],'History')
    
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32045),'0',174,BASE_LOGO+'ghost1.png',all_fanarts['32045'],'classic')
    
    all_d.append(aa)
    
    #place your Jen playlist here:
    #dulpicate this line with your address
    #aa=addDir3('Name', 'Your Jen Address',189,'Iconimage','fanart','Description',search_db='Your Search db Address')
    #all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))

def movie_prodiction():
    all_d=[]
    if Addon.getSetting("order_networks")=='0':
        order_by='popularity.desc'
    elif Addon.getSetting("order_networks")=='2':
        order_by='vote_average.desc'
    elif Addon.getSetting("order_networks")=='1':
        order_by='first_air_date.desc'
    
    
    aa=addDir3('[COLOR red]Marvel[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=7505&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Marvel')
    all_d.append(aa)
    aa=addDir3('[COLOR lightblue]DC Studios[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=9993&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','DC Studios')
    all_d.append(aa)
    aa=addDir3('[COLOR lightgreen]Lucasfilm[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=1&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Lucasfilm')
    all_d.append(aa)
    aa=addDir3('[COLOR yellow]Warner Bros.[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=174&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','SyFy')
    all_d.append(aa)
    aa=addDir3('[COLOR blue]Walt Disney Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=2&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Walt Disney Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR skyblue]Pixar[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=3&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Pixar')
    all_d.append(aa)
    aa=addDir3('[COLOR deepskyblue]Paramount[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=4&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Paramount')
    all_d.append(aa)
    aa=addDir3('[COLOR burlywood]Columbia Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=5&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Columbia Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR powderblue]DreamWorks[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=7&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','DreamWorks')
    all_d.append(aa)
    aa=addDir3('[COLOR lightsaltegray]Miramax[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=14&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Miramax')
    all_d.append(aa)
    aa=addDir3('[COLOR gold]20th Century Fox[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=25&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','20th Century Fox')
    all_d.append(aa)
    aa=addDir3('[COLOR bisque]Sony Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=34&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Sony Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR navy]Lions Gate Films[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=35&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Lions Gate Films')
    all_d.append(aa)
    aa=addDir3('[COLOR beige]Orion Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=41&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Orion Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR yellow]MGM[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=21&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','MGM')
    all_d.append(aa)
    aa=addDir3('[COLOR gray]New Line Cinema[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=12&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','New Line Cinema')
    all_d.append(aa)
    aa=addDir3('[COLOR darkblue]Gracie Films[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=18&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Gracie Films')
    all_d.append(aa)
    aa=addDir3('[COLOR goldenrod]Imagine Entertainment[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies=23&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','https://ia802507.us.archive.org/12/items/fanart_202205/fanart.jpg','Imagine Entertainment')
    all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def adjusted_datetime(string=False, dt=False):
    from datetime import datetime, timedelta
    d = datetime.utcnow() + timedelta(hours=int(72))
    if dt: return d
    d = datetime.date(d)
    if string:
        try: d = d.strftime('%Y-%m-%d')
        except ValueError: d = d.strftime('%Y-%m-%d')
    else: return d
def main_trakt():
   all_d=[]
   aa=addDir3(Addon.getLocalizedString(32048),'movie?limit=40&page=1',116,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Lists')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32049),'tv?limit=40&page=1',116,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Lists')
   all_d.append(aa)
   import datetime
   current_date = adjusted_datetime()
   start = (current_date - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
   finish = 14
        
   aa=addDir3(Addon.getLocalizedString(32050),'calendars/my/shows/%s/%s?limit=40&page=1'%(start,finish),117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Lists')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32051),'users/me/watched/shows?extended=full&limit=40&page=1',115,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Progress')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32052),'sync/watchlist/episodes?extended=full&limit=40&page=1',115,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Episodes')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32053),'users/me/watchlist/episodes?extended=full&limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Series')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32054),'users/me/collection/shows?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','TV')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32055),'users/me/watchlist/shows?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Shows')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32056),'recommendations/shows?limit=40&ignore_collected=true&page=1',166,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
   all_d.append(aa)
   
   aa=addDir3(Addon.getLocalizedString(32057),'users/me/watchlist/movies?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32058),'recommendations/movies?limit=40&ignore_collected=true&page=1',166,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
   all_d.append(aa)
   
   aa=addDir3(Addon.getLocalizedString(32059),'users/me/watched/movies?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Watched')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32060),'users/me/watched/shows?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Watched shows')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32061),'users/me/collection/movies?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','collection')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32062),'users/likes/lists?limit=40&page=1',118,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Liked lists')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32063),'sync/playback/movies?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Liked lists')
   all_d.append(aa)
   
   aa=addDir3(Addon.getLocalizedString(32064),'sync/playback/episodes?limit=40&page=1',164,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Liked lists')
   all_d.append(aa)
   
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))

def check_cached(magnet,rd):
    
    
    check=False
    if Addon.getSetting('debrid_select')=='0':
        try:
        
            hash = str(re.findall(r'btih:(.*?)&', magnet)[0].lower())
            hashCheck = rd.checkHash(hash)
            if hash in hashCheck:
                    if 'rd' in hashCheck[hash]:
                        if len(hashCheck[hash]['rd'])>0:
                          if  '.mkv' in str(hashCheck[hash]['rd']) or '.avi' in str(hashCheck[hash]['rd'])  or '.mp4' in str(hashCheck[hash]['rd']) :
                            check=True
        except:
            log.warning(magnet)
            pass
        return check
    elif Addon.getSetting('debrid_select')=='1':
        hash = [str(re.findall(r'btih:(.*?)&', magnet)[0].lower())]
        hashCheck=rd.hash_check(hash)
        if hashCheck['transcoded'][0]==True:
            check=True
        return check
    else:
        hash = [str(re.findall(r'btih:(.*?)&', magnet)[0].lower())]
        hashCheck=rd.check_hash(hash)['data']
        
        if hashCheck['magnets'][0]['instant']==True:
            check=True
        return check
def get_po_watching(original_title,show_original_year,tv_movie):
    global po_watching,full_stats
    from resources.modules.general import call_trakt
    try:
        if tv_movie=='movie':
            log.warning('Starting po')
            user_watching=call_trakt('movies/%s/watching'%(clean_name(original_title,1).lower().replace(' ','-').replace(':','').replace("'","")+'-'+show_original_year),with_auth=False)
            stats=call_trakt('movies/%s/stats'%(clean_name(original_title,1).lower().replace(' ','-')+'-'+show_original_year),with_auth=False)
            log.warning('End po')
            log.warning(stats)
            log.warning(user_watching)
        else:
            user_watching=call_trakt('shows/%s/watching'%(clean_name(original_title,1).lower().replace(' ','-').replace("'","").replace(':','')),with_auth=False)
            stats=call_trakt('shows/%s/stats'%(clean_name(original_title,1).lower().replace(' ','-')+'-'+show_original_year),with_auth=False)
            
        po_watching=(Addon.getLocalizedString(32065)%tv_movie.replace('tv',Addon.getLocalizedString(32066))+'[COLOR lightblue]'+str(len(user_watching))+'[/COLOR]')
        full_stats=Addon.getLocalizedString(32067)+str(stats['watchers'])+Addon.getLocalizedString(32068)+str(stats['plays'])+Addon.getLocalizedString(32069)+str(stats['votes'])+'[/COLOR]'
        
        
    
    except Exception as e:
        log.warning('Po watching err:'+str(e))
        po_watching=''
        full_stats=''
    return po_watching,full_stats
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 11...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 11...', '' )
def check_mass_hash(all_mag,items,rd,pr,ad,statistics,tv_movie,season_n,episode_n,page_no,start_time,dp):
            global all_hased,all_s_in
            #hashCheck = rd.checkHash(all_mag[items])
            log.warning('page_no check:'+str(page_no))
            try:
                count_hash=0
                elapsed_time = time.time() - start_time
                if Addon.getSetting('debrid_select')=='0':
                   #log.warning(json.dumps(all_mag[items]))
                   if not silent:
                        if KODI_VERSION>18:#kodi18
                            dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+'Sending:'+',Page:'+str(page_no))
                        else:
                            dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070),'Sending:'+',Page:'+str(page_no))
               
                   try:
                    hashCheck = rd.checkHash(all_mag[items])
                   except:
                    time.sleep(0.3)
                    hashCheck = rd.checkHash(all_mag[items])
                   
                   if not silent:
                        if KODI_VERSION>18:#kodi18
                            dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+'Got it:'+',Page:'+str(page_no))
                        else:
                            dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070),'Got it:'+',Page:'+str(page_no))
                elif Addon.getSetting('debrid_select')=='1':
                    hashCheck=pr.hash_check(all_mag[items])['transcoded']
                else:
                    hashCheck=ad.check_hash(all_mag[items])['data']['magnets']
                    
               
                
                z=0
                log.warning('hashCheck:')
                log.warning(hashCheck)
                all_rej=[]
                if isinstance(hashCheck, dict) or isinstance(hashCheck, list):
                 for hash in hashCheck:
                    
                    statistics['c_hash']+=1
                    if hash in all_hased:
                        continue
                    if not silent:
                        all_s_in=({},int((z*100.0)/(len(hashCheck))),'Page:'+str(page_no),2,name)
                        z+=1
                        if not silent:
                            if KODI_VERSION>18:#kodi18
                                dp.update(int(((count_hash* 100.0)/(len(hashCheck))) ), Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+ str(count_hash)+'/'+str(len(hashCheck))+',Page:'+str(page_no))
                            else:
                                dp.update(int(((count_hash* 100.0)/(len(hashCheck))) ), Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070), str(count_hash)+'/'+str(len(hashCheck))+',Page:'+str(page_no))
                            if dp.iscanceled():
                                                
                                                break
                    if Addon.getSetting('debrid_select')=='0':
                        ok=False
                        try:
                            if 'rd' in hashCheck[hash]:
                                ok=True
                        except Exception as e: 
                            log.warning(hash)
                            log.warning('Found error:'+str(e))
                            xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'In RD55 %s:'%str(e))))
                            ok=False
                     
                        if ok:
                          
                           if not silent:
                            if KODI_VERSION>18:#kodi18
                                dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+ 'OK')
                            else:
                                dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070), 'OK')
                                if dp.iscanceled():
                                                
                                                break
                           if len(hashCheck[hash]['rd'])>0:
                                
                                if not silent:
                                    if KODI_VERSION>18:#kodi18
                                        dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+ 'OK1')
                                        
                                    else:
                                        dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070), 'OK1')
                                    if dp.iscanceled():
                                                
                                                break
                                found_c_h=False
                                if tv_movie=='tv' and len(hashCheck[hash]['rd'])>1:
                                    if not silent:
                                        if KODI_VERSION>18:#kodi18
                                            dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+ 'OK2')
                                        else:
                                            dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070),'OK2')
                                        if dp.iscanceled():
                                                
                                                break
                                    for storage_variant in hashCheck[hash]['rd']:
                                        if hash in all_hased:
                                            continue
                                        if not silent:
                                            if KODI_VERSION>18:#kodi18
                                                dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+ 'OK3')
                                            else:
                                                dp.update(0, Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070), 'OK3')
                                            if dp.iscanceled():
                                                
                                                break
                                        key_list = storage_variant.keys()
                                        if found_c_h:
                                            break
                                        
                                        for items_t in hashCheck[hash]['rd']:
                                           if found_c_h:
                                              break
                                           for itt in items_t:
                                            if itt in all_rej:
                                                continue
                                            test_name=items_t[itt]['filename'].lower() 
                                            
                                            
                                            if not silent:
                                                if KODI_VERSION>18:#kodi18
                                                    dp.update(int(((count_hash* 100.0)/(len(key_list))) ), Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32070)+'\n'+ itt)
                                                else:
                                                    dp.update(int(((count_hash* 100.0)/(len(key_list))) ), Addon.getLocalizedString(32070)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32070), itt)
                                                if dp.iscanceled():
                                                    break
                                                
                                            if itt in key_list :
                                                    if ('s%se%s.'%(season_n,episode_n) in test_name or 's%se%s '%(season_n,episode_n) in test_name or 'ep '+episode_n in test_name):
                                                        found_c_h=True
                                                        
                                                        break
                                            else:
                                                all_rej.append(itt)
                                            
                                else:
                                    found_c_h=True
                                    
                                if found_c_h and ('.mkv' in str(hashCheck[hash]['rd']) or '.avi' in str(hashCheck[hash]['rd'])  or '.mp4' in str(hashCheck[hash]['rd'])  or '.m4v' in str(hashCheck[hash]['rd'])):
                                    all_hased.append(hash)
                                
                           else:
                              
                              statistics['non_rd']+=1
                        
                    elif Addon.getSetting('debrid_select')=='1':
                        if hash==True:
                            all_hased.append(all_mag[items][count_hash])
                        count_hash+=1
                    else:
                        
                        if 'instant' in hash:
                         if hash['instant']==True:
                           all_hased.append(hash['hash'])
                 
                else:
                    try:
                        regex='<title>(.+?)</title>'
                        m=re.compile(regex).findall(hashCheck)
                        added_t=''
                        if 'realdebrid' in hashCheck.lower():
                            added_t='Realdebrid'
                        xbmcgui.Dialog().ok('Error',added_t+m[0])
                    except:
                        xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'In RD88 Not dict')))
                    
                   
                    
                log.warning('doeeeen check page:'+str(page_no))
            except Exception as e:
                    import linecache
                    sources_searching=False
                    exc_type, exc_obj, tb = sys.exc_info()
                    f = tb.tb_frame
                    lineno = tb.tb_lineno
                    filename = f.f_code.co_filename
                    linecache.checkcache(filename)
                    line = linecache.getline(filename, lineno, f.f_globals)
                    log.warning('ERROR IN Check Cached IN:'+str(lineno))
                    log.warning('inline:'+line)
                    log.warning('Error:'+str(e))
                    xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'inLine:'+str(lineno))))
                    
                    
                    pass

def load_resolveurl_libs():
    path=xbmc_tranlate_path('special://home/addons/script.module.resolveurl/lib')
    sys.path.append( path)
    path=xbmc_tranlate_path('special://home/addons/script.module.six/lib')
    sys.path.append( path)
    path=xbmc_tranlate_path('special://home/addons/script.module.kodi-six/libs')
    sys.path.append( path)
    path1=xbmc_tranlate_path('special://home/addons/script.module.requests/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.urllib3/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.chardet/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.certifi/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.idna/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.futures/lib')
    sys.path.append( path1)

def get_other_scrapers(imdb,original_title,show_original_year,season,episode,tv_movie,dp,silent,start_time):
    #openscrapers
    load_resolveurl_libs()
        
    import resolveurl
    hostDict = resolveurl.relevant_resolvers(order_matters=True)
    hostDict = [i.domains for i in hostDict if not '*' in i.domains]
    hostDict = [i for i in reduce(lambda x, y: x+y, hostDict)] # domains already in lower case
    hostDict = [x for y, x in enumerate(hostDict) if x not in hostDict[:y]]
   
    hostprDict = ['1fichier.com', 'filefactory.com', 'filefreak.com', 'multiup.org', 'nitroflare.com', 'oboom.com', 'rapidgator.net', 'rg.to', 'turbobit.net',
                                        'uploaded.net', 'uploaded.to', 'uploadgig.com', 'ul.to', 'uploadrocket.net']
    result_universal=[]
    all_sources=[]
    all_sources_crew=[]
    all_sources_fen=[]
    if Addon.getSetting('openscrapers')=='true':
        #path=xbmc_tranlate_path('special://home/addons/script.module.openscrapers\lib')
        #sys.path.append( path)
        from openscrapers import sources
        sourceDict=sources()

        threads=[]

            
        
        
        count_others=0
        elapsed_time = time.time() - start_time
        for i in sourceDict:
            call=i[1]
            if not silent:
                elapsed_time = time.time() - start_time
                if KODI_VERSION>18:
                    dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait','Open Scrapers: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ i[0] )
                else:
                    dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait','Open Scrapers: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), i[0] )
            count_others+=1
            try:
                if tv_movie=='movie':
                    url = call.movie(imdb, original_title, show_original_year, original_title, show_original_year)
                    
                else:
                    url = call.tvshow(imdb, '', original_title, original_title, original_title, show_original_year)
                    url = call.episode(url, imdb, '', original_title, show_original_year, season, episode)
                #sources = call.sources(url, hostDict, hostprDict)
                all_sources.append((i[0],i[1],url, hostDict, hostprDict))
                
            except:
                pass
        sys.path.remove(path2)
        
    #universal
    if Addon.getSetting('universal')=='true':
      
        path3=xbmc_tranlate_path('special://home/addons/script.module.universalscrapers/lib')
        sys.path.append( path3)
        
        
        from universalscrapers import relevant_scrapers
        sourceDict=relevant_scrapers()
        
        count_others=0
        for scraper in sourceDict:
            
                if not silent:
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait'+'\n'+'Universal Scrapers: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+scraper.name )
                    else:
                        dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait','Universal Scrapers: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),scraper.name )
                count_others+=1
                result_universal.append((scraper.name ,scraper))
                #result=scraper().scrape_movie( original_title, show_original_year, imdb, debrid=use_debrid)
                
        sys.path.remove(path3)
    if Addon.getSetting('the_crew')=='true':
        import pkgutil
        path4=xbmc_tranlate_path('special://home/addons/script.module.simplejson/lib')
        sys.path.append( path4)
        path4=xbmc_tranlate_path('special://home/addons/script.module.thecrew/lib')
        sys.path.append( path4)
        
        __addon__ = xbmcaddon.Addon('script.module.thecrew')
        __cwd__ = xbmc_tranlate_path(__addon__.getAddonInfo('path'))
        sources_path=os.path.join(__cwd__,'lib','resources','lib','sources','sources')
        sources_path2=os.path.join(__cwd__,'lib','resources','lib','sources')
        log.warning('sources_path:'+sources_path)
        
        __all__ = [x[1] for x in os.walk(os.path.dirname(sources_path))][0]
        log.warning(__all__)
        sourceDict = []
        for i in __all__:
            
            for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(os.path.dirname(sources_path), i)]):
                log.warning(module_name)
                if is_pkg:
                    continue

                try:
                    module = loader.find_module(module_name).load_module(module_name)
                    sourceDict.append((module_name, module.s0urce()))
                except:
                    pass
                    
        

            
        
        
        count_others=0
        elapsed_time = time.time() - start_time
    
        for i in sourceDict:
            
            call=i[1]
            if not silent:
                elapsed_time = time.time() - start_time
                if KODI_VERSION>18:
                    dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait'+'\n'+'The Crew: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ i[0] )
                else:
                    dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait','The Crew: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), i[0] )
            count_others+=1
            try:
                if tv_movie=='movie':
                    url = call.movie(imdb, original_title, show_original_year, original_title, show_original_year)
                    
                else:
                    url = call.tvshow(imdb, '', original_title, original_title, original_title, show_original_year)
                    url = call.episode(url, imdb, '', original_title, show_original_year, season, episode)
                
                all_sources_crew.append((i[0],i[1],url, hostDict, hostprDict))
                
            except:
                pass
    if Addon.getSetting('fen')=='true':
        #path=xbmc_tranlate_path('special://home/addons/script.module.openscrapers\lib')
        #sys.path.append( path)
        path2=xbmc_tranlate_path('special://home/addons/script.module.fenomscrapers/lib')
        sys.path.append( path2)
        from fenomscrapers import sources
        sourceDict=sources()
        log.warning('ALL FEN scraping')
        log.warning(sourceDict)
        
        threads=[]

            
        
        
        count_others=0
        elapsed_time = time.time() - start_time
        for i in sourceDict:
            call=i[1]
            if not silent:
                elapsed_time = time.time() - start_time
                if KODI_VERSION>18:
                    dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait'+'\n'+'Fen: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ i[0] )
                else:
                    dp.update(int(((count_others* 100.0)/(len(sourceDict))) ), 'Please wait','Fen: '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), i[0] )
            count_others+=1
            try:
                if tv_movie=='movie':
                    
                    url = call.movie(imdb, original_title, original_title, show_original_year)
                    
                else:
                    url = call.tvshow(imdb, '', original_title, original_title, original_title, show_original_year)
                    url = call.episode(url, imdb, '', original_title, show_original_year, season, episode)
                #sources = call.sources(url, hostDict, hostprDict)
                all_sources_fen.append((i[0],i[1],url, hostDict, hostprDict))
                
            except Exception as e:
                log.warning('Error fen:'+str(e))
                pass
        sys.path.remove(path2)
      
    return all_sources,result_universal,all_sources_crew,all_sources_fen
def get_uni(name,scraper,original_title, show_original_year, imdb,tv_movie,tvdb, season, episode):
    global all_other_sources_uni
    if tv_movie=='movie':
        result=scraper().scrape_movie( original_title, show_original_year, imdb, debrid=use_debrid)
    else:
        result=scraper().scrape_episode( original_title, show_original_year, show_original_year, season, episode, imdb, tvdb, debrid=use_debrid)
    if result:
        all_other_sources_uni[name]=result
    return all_other_sources_uni
        
def scrape_fen_scrapers(name,call,url,hostDict, hostprDict,tv_movie):
        global all_other_sources
        if not use_debrid:
            hostprDict=[]
        sources=[]
        try:
            sources = call.sources(url, hostDict)
        except:
            pass
       
        if sources:
            all_other_sources[name]=sources
        return all_other_sources
def scrape_other_scrapers(name,call,url,hostDict, hostprDict,tv_movie):
        global all_other_sources
        if not use_debrid:
            hostprDict=[]
        sources=[]
        try:
            sources = call.sources(url, hostDict, hostprDict)
        except:
            pass
       
        if sources:
            all_other_sources[name]=sources
        return all_other_sources


def get_all_files(source_dir):
    onlyfiles = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
    return onlyfiles
def c_get_sources(name,data,original_title,id,season,episode,show_original_year,heb_name,test_mode=False,selected_scrapers='',tvdb_id='',server_test=False):
   global all_other_sources,all_s_in,global_result,stop_window,once_fast_play,all_other_sources_uni
   global silent,sources_searching,po_watching,full_stats,all_hased
   
   dp=[]
   if not silent:
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create(Addon.getLocalizedString(32072),Addon.getLocalizedString(32073)+'\n'+ ''+'\n'+'')
        else:
            dp.create(Addon.getLocalizedString(32072),Addon.getLocalizedString(32073), '','')
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+'\n'+Addon.getLocalizedString(32073)+'\n'+ '' )
        else:
            dp.update(0, Addon.getLocalizedString(32072),Addon.getLocalizedString(32073), '' )
   from resources.modules import real_debrid
   from resources.modules import premiumize
   from resources.modules import all_debrid
   stop_window=False
   try:
    tmdbKey='fb981e5ab89415bba616409d5eb5f05e'
    
    if season!=None and season!="%20":
          tv_movie='tv'
    else:
          tv_movie='movie'
    log.warning('silent:'+str(silent))
    
    
    all_s_in=({},0,'','','')
    full_stats=''
    po_watching=''
    dd=[]
    dd.append((name,data,original_title,id,season,episode,show_original_year,heb_name,test_mode,selected_scrapers,tvdb_id))
    log.warning('dd search')
    log.warning(dd)
    
    sources_searching=True
    all_ok=[]
    rd=[]
    pr=[]
    ad=[]
    if use_debrid:
        if Addon.getSetting('debrid_select')=='0':
           rd = real_debrid.RealDebrid()
        elif Addon.getSetting('debrid_select')=='1':
            pr= premiumize.Premiumize()
        else:
            ad=all_debrid.AllDebrid()
    
    if Addon.getSetting("fancy_scrape")=='true' and server_test==False:
        if not silent:
            
            selected_option=Addon.getSetting("video_type_in_s")
            thread=[]
            thread.append(Thread(start_window2,id,tv_movie,heb_name,selected_option,season,episode))
            thread[len(thread)-1].setName('sources_s2')
            thread[0].start()
    
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    source_dir = os.path.join(addonPath, 'resources', 'sources')
    
    
    sys.path.append( source_dir)
    log.warning(source_dir)
    #onlyfiles = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
    
    onlyfiles=cache.get(get_all_files, 999,source_dir,table='pages')
    start_time = time.time()
    
    if Addon.getSetting('openscrapers')=='true' or Addon.getSetting('universal')=='true' or Addon.getSetting('the_crew')=='true' or Addon.getSetting('fen')=='true':
        if tv_movie=='tv':
          
           url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
        else:
           
           url2='http://api.themoviedb.org/3/movie/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
        try:
            
            imdb_id=get_html(url2,timeout=10).json()['external_ids']['imdb_id']
        except:
            imdb_id=" "
    if len(episode)==1:
      episode_n="0"+episode
    else:
       episode_n=episode
    if len(season)==1:
      season_n="0"+season
    else:
      season_n=season
    all_sources=[]
    thread=[]
    server_check={}
    num_live=0
    added=''
    if tv_movie=='tv':
        added='_tv'
    
    z=0
    import pkgutil
    
    for loader, items, is_pkg in pkgutil.walk_packages([source_dir]):
       if is_pkg: 
            continue
        
       try:
            module = loader.find_module(items).load_module(items)
       except Exception as e:
           log.warning('Fault module:'+items)
           log.warning(e)
           
           continue
       items=items+'.py'
       
       test_scr=Addon.getSetting(items.replace('.py','')+added)
       all_s_in=({},int((z*100.0)/(len(onlyfiles))),items,1,'')
       if items=='furk.py':
            test_scr=Addon.getSetting('provider.furk')
       if items=='easynews.py':
            test_scr=Addon.getSetting('provider.easy')
       if selected_scrapers!='All' and len(selected_scrapers)>0:
            
            if items.replace('.py','')==selected_scrapers:
            
                test_scr='true'
            else:
                test_scr='false'
            
       if test_scr=='false':
          continue
       if  items.endswith('.py') and 'init' not in items:
        if not silent:
            if KODI_VERSION>18:
                dp.update(0, Addon.getLocalizedString(32072)+'\n'+Addon.getLocalizedString(32074)+'\n'+ items.replace('.py','') )
            else:
                dp.update(0, Addon.getLocalizedString(32072),Addon.getLocalizedString(32074), items.replace('.py','') )
        try:
            impmodule = __import__(items.replace('.py',''))
           
            
            
            impmodule.stop_all=0
            impmodule.global_var=[]
            if not use_debrid:
                if 'non_rd' not in impmodule.type  and use_debrid==False:
                    continue
            
            
            thread.append(Thread(impmodule.get_links,tv_movie,original_title,season_n,episode_n,season,episode,show_original_year,id))
            thread[len(thread)-1].setName(items.replace('.py',''))
            server_check[items.replace('.py','')]={}
            all_sources.append((items,impmodule))
        except Exception as e:
            xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'In source:'+str(items)+', '+str(e))))
            log.warning('In source:'+str(items)+', '+str(e))
            continue
        #thread[len(thread)-1].start()
        if not silent:
            elapsed_time = time.time() - start_time
            if KODI_VERSION>18:#kodi18
                dp.update(int(((num_live* 100.0)/(len(onlyfiles))) ), 'Please wait'+'\n'+'Starting '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ items.replace('.py','') )
            else:
                dp.update(int(((num_live* 100.0)/(len(onlyfiles))) ), 'Please wait','Starting '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), items.replace('.py','') )
            num_live+=1
            
        z+=1
    result=[]
    result_universal=[]
    all_sources_crew=[]
    all_sources_fen=[]
    if Addon.getSetting('openscrapers')=='true' or Addon.getSetting('universal')=='true' or Addon.getSetting('the_crew')=='true' or Addon.getSetting('fen')=='true':
       try:
        result,result_universal,all_sources_crew,all_sources_fen=get_other_scrapers(imdb_id,original_title,show_original_year,season,episode,tv_movie,dp,silent,start_time)
       except:
        pass
    all_other_sources={}
    all_other_sources_uni={}
    
    count_others=0
    z=0
    for name,call,url,hostDict, hostprDict in result:
        all_s_in=({},int((z*100.0)/(len(result))),'Op:'+name,1,'')
        if not silent:
            elapsed_time = time.time() - start_time
            if KODI_VERSION>18:#kodi18
                dp.update(int(((count_others* 100.0)/(len(result))) ), 'Please wait'+'\n'+'Open Scrapers '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ name )
            else:
                dp.update(int(((count_others* 100.0)/(len(result))) ), 'Please wait','Open Scrapers '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), name )
        thread.append(Thread(scrape_other_scrapers,'op-'+name,call,url,hostDict, hostprDict,tv_movie))
        thread[len(thread)-1].setName('OP:'+name)
        server_check['OP:'+name]={}
        count_others+=1
        z+=1
        
    count_others=0
    z=0
    for name,call,url,hostDict, hostprDict in all_sources_fen:
        all_s_in=({},int((z*100.0)/(len(all_sources_fen))),'Fn:'+name,1,'')
        if not silent:
            elapsed_time = time.time() - start_time
            if KODI_VERSION>18:#kodi18
                dp.update(int(((count_others* 100.0)/(len(all_sources_fen))) ), 'Please wait'+'\n'+'Fen '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ name )
            else:
                dp.update(int(((count_others* 100.0)/(len(all_sources_fen))) ), 'Please wait','Fen '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), name )
        thread.append(Thread(scrape_fen_scrapers,'FN-'+name,call,url,hostDict, hostprDict,tv_movie))
        thread[len(thread)-1].setName('FN:'+name)
        server_check['FN:'+name]={}
        count_others+=1
        z+=1
        
        
    count_others=0
    z=0
    for name,call,url,hostDict, hostprDict in all_sources_crew:
        all_s_in=({},int((z*100.0)/(len(all_sources_crew))),'CR:'+name,1,'')
        if not silent:
            elapsed_time = time.time() - start_time
            if KODI_VERSION>18:#kodi18
                dp.update(int(((count_others* 100.0)/(len(all_sources_crew))) ), 'Please wait'+'\n'+'The Crew '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ name )
            else:
                dp.update(int(((count_others* 100.0)/(len(all_sources_crew))) ), 'Please wait','The Crew '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), name )
        thread.append(Thread(scrape_other_scrapers,'cr-'+name,call,url,hostDict, hostprDict,tv_movie))
        thread[len(thread)-1].setName('CR:'+name)
        server_check['CR:'+name]={}
        count_others+=1
        z+=1
        
    count_others=0
    
    
    for name,scraper in result_universal:
        all_s_in=({},int((z*100.0)/(len(result_universal))),'UN:'+name,1,'')
        if not silent:
            elapsed_time = time.time() - start_time
            if KODI_VERSION>18:#kodi18
                dp.update(int(((count_others* 100.0)/(len(result_universal))) ), 'Please wait'+'\n'+'Universal Scrapers '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ name )
                
            else:
               dp.update(int(((count_others* 100.0)/(len(result_universal))) ), 'Please wait','Universal Scrapers '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), name ) 
        
        
        thread.append(Thread(get_uni,'un-'+name,scraper,original_title, show_original_year, imdb_id,tv_movie,tvdb_id, season, episode))
        thread[len(thread)-1].setName('UN:'+name)
        server_check['UN:'+name]={}
        count_others+=1
        z+=1
        
    #for tr in thread:
    #    tr.start()
    if Addon.getSetting('po_watch')=='true':
        thread.append(Thread(get_po_watching,original_title,show_original_year,tv_movie))
        thread[len(thread)-1].setName('Po.watching')
        #thread[len(thread)-1].start()
    for td in thread:
        td.start()
    server_check['Po.watching']={}
    tt={}
    for i in range (0,(len(thread)+50)): 
      tt[i]="red"
    max_table=[2160,1080,720,9999]
    min_table=[2160,1080,720,0]
    if tv_movie=='movie':
        se='one_click'
        mq="max_quality"
        minq="min_quality"
    else:
        se='one_click_tv'
        mq="max_quality_tv"
        minq="min_quality_tv"
    one_click=Addon.getSetting(se)=='true'
    log.warning('Addon.getSetting(mq):'+str(Addon.getSetting(mq)))
    try:
        max_q=max_table[int(Addon.getSetting(mq))]
        
    except:
        max_q=int(Addon.getSetting(mq))
        
    try:
        min_q=min_table[int(Addon.getSetting(minq))]
    except:
        min_q=int(Addon.getSetting(minq))
    once=0
    all_lks=[]
    max_time=int(Addon.getSetting("time_s"))
    if test_mode:
        max_time=999999
    stop_all=0
    all_lk_in=[]
    thread2=[]
    counter_for_test=0
    all_mag={}
    all_mag[0]=[]
    page_index2=0
    statistics={}
    statistics['magnet']=0
    statistics['non_magnet']=0
    statistics['unique']=0
    statistics['d_unique']=0
    statistics['c_hash']=0
    statistics['rd']=0
    statistics['non_rd']=0
    statistics['check_this']=0
    hash_index={}
    filter_lang=Addon.getSetting("filter_non_e")=='true'
    #from resources.modules import PTN
    all_s_in=({},100,'',1,'')
    total_pre=0
    total_n=1
    f_result={}
    if len(thread)>0:
      while 1:
        num_live=0
         
          
         
        elapsed_time = time.time() - start_time
        
            
         
              
        num_live=0
        string_dp=''
        string_dp2=''
        still_alive=0
        count_2160=0
        count_1080=0
        count_720=0
        count_480=0
        count_rest=0
        count_alive=0
        all_alive={}
        
        for yy in range(0,len(thread)):
            all_alive[thread[yy].name]=thread[yy].is_alive()
            
            #log.warning(thread[yy].name+' Alive: '+str(thread[yy].is_alive()))
            if not thread[yy].is_alive():
              num_live=num_live+1
              tt[yy]="lightgreen"
              
              #log.warning('Dead:'+thread[yy].name)
              #string_dp2=string_dp2+',[COLOR red]O:'+thread[yy].name+'[/COLOR]'
            else:
              server_check[thread[yy].name]['done_time']= time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
              
              if string_dp2=='':
                string_dp2=thread[yy].name
              else:
                count_alive+=1
                string_dp2=string_dp2+','+thread[yy].name
              still_alive=1
              tt[yy]="red"
        f_result={}
        
        for name_scrape in all_other_sources_uni.keys():
            all_links_others=[]
            for ittm_other in all_other_sources_uni[name_scrape]:
                if 'debridonly' in ittm_other:
                  if ittm_other['debridonly']==True and use_debrid==False:
                        continue
                added_txt=''
                if tv_movie=='tv':
                    added_txt='.S%sE%s.'%(season_n,episode_n)
                try:
                
                    nm_others=ittm_other['name']+added_txt
                except:
                    nm_others=original_title+added_txt
                
                src_others=ittm_other['scraper']
                lk_others=ittm_other['url']
                
                size_others='0'
                res_others='480'
                if 'quality' in ittm_other:
                    div=1
                    if ' MB' in ittm_other['quality']:
                        div=1024
                    
                    q1=ittm_other['quality'].replace('MB','').replace('GB','').replace('KB','').strip()
                    if ' ' in q1:
                        size_others=str(q1.split(' ')[1])
                    try:
                        size_others=float(size_others)/div
                    except:
                        pass
                    
                    if ' ' in q1:
                        res_others=res_q(q1.split(' ')[0])
                    res_others=res_others.replace('SD','480')
                if 'magnet' not in lk_others:
                      if ittm_other['direct']==True:
                        lk_others='Direct_link$$$resolvedirect'+lk_others
                      else:
                        lk_others='Direct_link$$$resolveurl'+lk_others
                    
                res_others=res_q(ittm_other['quality'])
                all_links_others.append((nm_others+', '+src_others,lk_others,str(size_others),res_others))
            f_result[name_scrape]={}
            f_result[name_scrape]['links']=all_links_others
        for name_scrape in all_other_sources.keys():
                all_links_others=[]
                for ittm_other in all_other_sources[name_scrape]:
                    if ittm_other['debridonly']==True and use_debrid==False:
                        continue
                    added_txt=''
                    if tv_movie=='tv':
                        added_txt='.S%sE%s.'%(season_n,episode_n)
                    try:
                    
                        nm_others=ittm_other['name']+added_txt
                    except:
                        nm_others=original_title+added_txt
                    
                    src_others=ittm_other['source']
                    lk_others=ittm_other['url']
                    size_others='0'
                    if 'size' in ittm_other:
                        size_others=str(ittm_other['size'])
                    elif 'info' in ittm_other:
                        size_others=str(ittm_other['info'])
                        if '|' in size_others:
                            size_others=(size_others.split('|')[0])
                            
                    size_others=size_others.replace('GB','').replace('MB','').replace('KB','').strip()
                    if 'magnet' not in lk_others:
                      if ittm_other['direct']==True:
                        lk_others='Direct_link$$$resolvedirect'+lk_others
                      else:
                        lk_others='Direct_link$$$resolveurl'+lk_others
                    
                    res_others=res_q(ittm_other['quality'])
                    all_links_others.append((nm_others+', '+src_others,lk_others,str(size_others),res_others))
                f_result[name_scrape]={}
                f_result[name_scrape]['links']=all_links_others
                
                


        for name1,items in all_sources:
            f_result[name1]={}
            f_result[name1]['links']=items.global_var
        living=[]
        for items in all_alive:
             if all_alive[items]:
               living.append(items)
              
        if count_alive>10:
            
            string_dp2=Addon.getLocalizedString(32075)+str(count_alive)+' - '+random.choice (living)
        count_found=0
        
        for data in f_result:
            #log.warning(f_result)
            if len (f_result[data]['links'])>0:
                   count_found+=1
                   
            if 'links' in f_result[data] and len (f_result[data]['links'])>0:
                 
                for links_in in f_result[data]['links']:
                    
                     
                     
                     name1,links,server,res=links_in
                     if links==None:
                        continue
                     new_res=0
                     if '2160' in res:
                       count_2160+=1
                       new_res=2160
                     if '1080' in res:
                       count_1080+=1
                       new_res=1080
                     elif '720' in res:
                       count_720+=1
                       new_res=720
                     elif '480' in res:
                       count_480+=1
                       new_res=480
                     else:
                       count_rest+=1
                     try:
                        res_c=int(res)
                     except:
                        res_c=480
                     
                     if not (data=='sez.py' or data=='soup.py' or data=='furk.py' or data=='easynews.py' or 'storage.googleapis.com'  in links or 'drive.google.com'  in links):
                            if 0:
                             if 'magnet' in links and use_debrid:
                                statistics['magnet']+=1
                                try:
                                    #hash = str(re.findall(r'btih:(.*?)&', link)[0].lower())
                                    hash=links.split('btih:')[1]
                                    if '&' in hash:
                                        hash=hash.split('&')[0]
                                except:
                                    try:
                                        hash =links.split('btih:')[1]
                                    except:
                                        continue
                                if hash.lower() in all_lk_in:
                                    
                                    continue
                                if 0:
                                    all_lk_in.append(hash.lower())
                                    all_mag[page_index2].append(hash.lower())
                                    counter_for_test+=1
                                    hash_index[hash.lower()]=links
                                    if counter_for_test>148:
                                        
                                        
                                        counter_for_test=0
                                        thread2.append(Thread(check_mass_hash,all_mag,page_index2,rd,pr,ad,statistics,tv_movie,season_n,episode_n,page_index2))
                                        
                                        thread2[len(thread2)-1].setName('Page '+str(page_index2))
                                        thread2[len(thread2)-1].start()
                                        page_index2+=1
                                        all_mag[page_index2]=[]
                     if not silent and (once==0) and int(res_c)>=min_q and int(res_c)<=max_q and links not in all_lks and one_click:
                        check_one_click=True
                        if KODI_VERSION>18:
                            dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32076)+'\n'+str(res_c)+','+ name1)
                        else:
                            dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32076),str(res_c)+','+ name1)
                        if check_rejected(name1,show_original_year,season,episode,original_title,tv_movie,heb_name,filter_lang,one_click=True):
                            check_one_click=False
                        
                        continue_next=check_forbiden(name)
                
                        if continue_next:
                            check_one_click=False
                    
                        if check_one_click:
                            
                            all_lks.append(links)
                            run_lk=False
                            if data=='sez.py' or data=='soup.py' or data=='furk.py' or data=='easynews.py' or 'storage.googleapis.com'  in links or 'drive.google.com'  in links:
                                run_lk=True
                            else:
                                if KODI_VERSION>18:
                                    dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Checking hash'+'\n'+str(res_c)+','+ name1)
                                else:
                                    dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Checking hash',str(res_c)+','+ name1)
                                if Addon.getSetting('debrid_select')=='0':
                                    run_lk=check_cached(links,rd)
                                elif  Addon.getSetting('debrid_select')=='1':
                                    run_lk=check_cached(links,pr)
                                else:
                                    run_lk=check_cached(links,ad)
                            
                            if run_lk:
                                log.warning('name1 passed:'+name1+',original_title:'+original_title)
                                heb_name=name1
                                o_name=name1
                                once=1
                                stop_all=1
                                dp.close()
                                silent=True
                                log.warning('Playing Auto Now:'+str(once))
                                if 1:#not xbmc.Player().isPlaying():
                                    dd=[]
                                    dd.append((name1,data,original_title,id,season,episode,show_original_year))
                                    if KODI_VERSION>18:
                                        dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32077)+'\n'+str(res_c)+','+ name1)
                                    else:
                                        dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32077),str(res_c)+','+ name1)
                                    for name1,items in all_sources:
                                        items.stop_all=1
                                    for threads in thread:
            
                                        if threads.is_alive():
                                             
                                             
                                             try:
                                                thread._Thread__stop()
                                             except:
                                                pass
                                    if not silent:
                                        dp.close()
                                    log.warning('Playing fast click2')
                                    xbmc.Player().stop()
                                    once_fast_play=1
                                    xbmc.executebuiltin((u'Notification(%s,%s)' % ('Playing', 'Source:'+str(data))))
                                    play_link(o_name,links,' ',' ',description,data,original_title,id,season,episode,show_original_year,json.dumps(dd),heb_name,nextup='true',tvdb_id=tvdb_id)
                                    
                                        
                                   
                                break
                            
                all_s_in=(f_result,int(((num_live* 100.0)/(len(thread))) ),string_dp2.replace(Addon.getLocalizedString(32075),''),2,string_dp)
            
                
                
                total=count_1080+count_720+count_480+count_rest
                
                string_dp="4K: [COLOR yellow]%s[/COLOR] 1080: [COLOR khaki]%s[/COLOR] 720: [COLOR gold]%s[/COLOR] 480: [COLOR silver]%s[/COLOR] %s: [COLOR burlywood]%s[/COLOR]  T: [COLOR darksalmon]%s[/COLOR] "%(count_2160,count_1080,count_720,count_480,Addon.getLocalizedString(32078),count_rest,total)
                all_s_in=(f_result,int(((num_live* 100.0)/(len(thread))) ),string_dp2.replace('Remaining sources: ',''),2,string_dp)
                  
                     
                  
            if stop_all==1:
                break
            total_n=count_1080+count_720+count_480+count_rest
            if not silent and total_n>=total_pre:
                    total_pre=total_n
                    
        if not silent:
                    global_result="4K: [COLOR yellow]%s[/COLOR] 1080: [COLOR khaki]%s[/COLOR] 720: [COLOR gold]%s[/COLOR] 480: [COLOR silver]%s[/COLOR] %s: [COLOR burlywood]%s[/COLOR]"%(count_2160,count_1080,count_720,count_480,Addon.getLocalizedString(32078),count_rest)
                    if KODI_VERSION>18:
                        dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+string_dp+'\n'+ string_dp2)
                    else:
                        dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),string_dp, string_dp2)
                  
            
        if not silent:
            check=dp.iscanceled()
        else:
            check=False
        
        if check or still_alive==0 or elapsed_time>max_time or stop_all==1 or stop_window:
          
          log.warning('Stop scrape')

          
          for name1,items in all_sources:
                items.stop_all=1
          num_live2=0
          for threads in thread:
            all_s_in=(f_result,int(((num_live2* 100.0)/(len(thread))) ),Addon.getLocalizedString(32079),2,'Stoping '+threads.name)
            
            elapsed_time = time.time() - start_time
            if not silent:
                if KODI_VERSION>18:
                    dp.update(int(((num_live2* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Closing'+'\n'+ threads.name)
                else:
                    dp.update(int(((num_live2* 100.0)/(len(thread))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Closing', threads.name)
            if threads.is_alive():
                 
                 
                 try:
                    thread._Thread__stop()
                 except:
                    pass
            num_live2+=1
           
          break
        xbmc.sleep(100)
    all_lk2=[]
    
    
    all_q={}
    all_names={}
    page_index=0
    all_mag={}
    all_mag[0]=[]
    counter_hash=0
    '''
    for items in all_hased:
            
                
            all_ok.append(hash_index[items.lower()])
    '''
    
    
    if once==0 or not silent:
        
        all_unique=[]
        
        for name_f in f_result:
          count_all_links=0
          try:
            server_check[name_f.replace('.py','')]['links_count']=str(len(f_result[name_f]['links']))
          except:
            pass
          for name,link,server,quality in f_result[name_f]['links']:
            count_all_links+=1
            if link==None:
                continue
            if 'magnet' in link and use_debrid:
                statistics['magnet']+=1
                try:
                    #hash = str(re.findall(r'btih:(.*?)&', link)[0].lower())
                    hash=link.split('btih:')[1]
                    if '&' in hash:
                        hash=hash.split('&')[0]
                except:
                    try:
                        hash =link.split('btih:')[1]
                    except:
                        continue
                if hash.lower() in all_lk_in:
                    statistics['d_unique']+=1
                    continue
                    
                
                statistics['unique']+=1
                all_lk_in.append(hash.lower())
                all_unique.append((name,link,server,quality))
            else:
                statistics['non_magnet']+=1
                if Addon.getSetting('torrents')=='true' and use_debrid==False:
                    all_ok.append(link)
                    continue
                if 'Direct_link$$$' not in link and name_f!='sez.py' and name_f!='soup.py' and name_f!='furk.py' and name_f!='easynews.py' and 'storage.googleapis.com' not in link and 'drive.google.com' not in link:
                   log.warning('Not magnet:'+link +',server:'+server+',source:'+name_f)
                else:
                   if ' 3d' not in original_title.lower():
                    all_ok.append(link)
            
       
        all_s_in=({},0,'Check Hash',2,'')
        z=0
        if Addon.getSetting('debrid_select')=='0':
             max_items=150
        else:
             max_items=100
        for name,link,server,quality in all_unique:
                        
                        all_s_in=({},int((z*100.0)/(len(all_unique))),'Check Hash',2,name)
                        z+=1
                        if not silent:
                            if KODI_VERSION>18:
                                dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32072)+'\n'+ 'Collecting:'+name)
                            else:
                                dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32072), 'Collecting:'+name)
                        if link not in all_lk2 and link not in all_ok:
                            all_lk2.append(link)
                            
                            c_name=clean_marks(name).replace('and','').replace('.&.','').replace(' & ','').replace(' and ','').replace('_','.').replace('%3A','.').replace('%3a','.').replace(':','').replace('-','.').replace('[','(').replace(']',')').replace('  ','.').replace(' ','.').replace('....','.').replace('...','.').replace('..','.').replace("'",'').strip().lower()
                            if 'season' in c_name and tv_movie=='tv':
              
                              if 'season.%s.'%season not in c_name.lower() and 'season.%s$$$'%season not in (c_name.lower()+'$$$') and 'season.%s$$$'%season_n not in (c_name.lower()+'$$$') and 'season.%s.'%season_n not in c_name.lower() and 'season %s'%season_n not in c_name and 'season %s '%season not in c_name:
                                
                                continue
                              else:
                                  log.warning(name)
                            if 'magnet' in link:
                                try:
                                    #hash = str(re.findall(r'btih:(.*?)&', link)[0].lower())
                                    hash=link.split('btih:')[1]
                                    if '&' in hash:
                                        hash=hash.split('&')[0]
                                except:
                                    hash =link.split('btih:')[1]
                                #log.warning(link)
                                #log.warning(hash)
                                statistics['check_this']+=1
                                all_mag[page_index].append(hash.lower())
                                hash_index[hash.lower()]=link
                                all_names[hash.lower()]=name
                                all_q[hash.lower()]=quality.lower().replace('hd','720')
                                counter_hash+=1
                                if counter_hash>max_items:
                                    page_index+=1
                                    all_mag[page_index]=[]
                                    counter_hash=0
                
        all_hased=[]
                
        for thread in threading.enumerate():
              all_s_in=({},0,'Closing threads:'+thread.getName(),2,name)
              if (trd_alive(thread)):
                 alive=1
                 try:
                    thread._Thread__stop()
                 except:
                    pass
        thread=[]
        page_no=0
        for items in all_mag:
                    
                if len(all_mag[items])>0 :
                    all_s_in=({},0,'Checking Hash page:'+str(items),2,'')
                    check_mass_hash(all_mag,items,rd,pr,ad,statistics,tv_movie,season_n,episode_n,page_no,start_time,dp)
                    #thread.append(Thread(check_mass_hash,all_mag,items,rd,pr,ad,statistics,tv_movie,season_n,episode_n,page_no,start_time,dp))
                    #thread[len(thread)-1].setName('Page '+str(page_no))
                    #thread[len(thread)-1].start()
                    #thread[len(thread)-1].join()
                    page_no+=1

                                        
        if len(thread)>0:
          while 1:
            num_live=0
             
              
             
            elapsed_time = time.time() - start_time
            
                
             
                  
            num_live=0
            
      
            still_alive=0
            all_alive=[]
            for yy in range(0,len(thread)):
                
                
                #log.warning(thread[yy].name+' Alive: '+str(thread[yy].is_alive()))
                if not thread[yy].is_alive():
                  num_live=num_live+1
                 
                  
                  
                  #string_dp2=string_dp2+',[COLOR red]O:'+thread[yy].name+'[/COLOR]'
                else:
                  all_alive.append(thread[yy].name)
                  still_alive=1
                  
            elapsed_time = time.time() - start_time
            if not silent:
                if KODI_VERSION>18:
                    dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32080)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32080)+'\n'+ ','.join(all_alive))
                else:
                    dp.update(int(((num_live* 100.0)/(len(thread))) ), Addon.getLocalizedString(32080)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32080), ','.join(all_alive))
            if still_alive==0:
                break

        for items in all_hased:
            
            all_s_in=({},0,'All Hashed:',2,name)
            all_ok.append(hash_index[items.lower()])
    while(1):
        still_alive=0
        for yy in range(0,len(thread2)):
           
            if not thread2[yy].is_alive():
              num_live=num_live+1
              
            else:
                still_alive=1
        if still_alive==0:
            break
        xbmc.sleep(100)
    if not silent:
        dp.close()
        
    sources_searching=False
    l_po_watching=po_watching
    l_full_stats=full_stats
   
    return f_result,all_ok,once,tv_movie,l_po_watching,l_full_stats,statistics,server_check
   
   except Exception as e:
    import linecache
    sources_searching=False
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    log.warning('ERROR IN Scraping IN:'+str(lineno))
    log.warning('inline:'+line)
    log.warning('Error:'+str(e))
    xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'inLine:'+str(lineno))))
    try:
        dp.close()
    except:
        pass
    sys.exit()
    pass
   
def get_title(title):
    text3=None
    text =title.strip()
    text2= re.search('(.*?)(dvdrip|xvid| cd[0-9]|dvdscr|brrip|divx|[\{\(\[]?[0-9]{4}).*',text)
    if text2:
        text =text2.group(1)
        text3= re.search('(.*?)\(.*\)(.*)',text)
    if text3:
        text =text3.group(1)
    log.warning('text:'+text)
    return text.replace("."," ").strip()
def clean_marks(title):
    regex='\[(.+?)\]'
    m=re.compile(regex).findall(title)
    
    for items in m:
        title=title.replace('[%s]'%items,'')
    regex='[0-9]{1,2}x[0-9]*'
    m=re.compile(regex).findall(title)
    if len(m)>0:
        title=title.replace(m[0],'').strip()
    return title
def get_all_trakt_resume(tv_movie):
            
            all_w={}
            try:
                if tv_movie=='movie':
                    from resources.modules.general import call_trakt
                    result=call_trakt('sync/playback/movies')
                    
                    for items in result:
                        
                  
                        
                        t_id=str(items['movie']['ids']['tmdb'])   
                        
                        if 'progress' in items:
                            progress=items['progress']
                        
                            all_w[t_id]={}
                            all_w[t_id]['precentage']=str(progress)
                            
                            
                            
                else:
                    from resources.modules.general import call_trakt
                    result=call_trakt('sync/playback/episodes')
                    
                    for items in result:
                        t_id=str(items['show']['ids']['tmdb'])
                        season_t=str(items['episode']['season'])
                        episode_t=str(items['episode']['number'])
                        
                        
                        
                        if 'progress' in items:
                            progress=items['progress']
                            
                            all_w[t_id]={}
                            all_w[t_id]['season']=season_t
                            all_w[t_id]['episode']=episode_t
                            all_w[t_id]['precentage']=str(progress)
                            
                        
                
                all_tv_w={}
                all_movie_w=[]
                if tv_movie=='tv':
                   i = (call_trakt('/users/me/watched/shows?extended=full'))
                   
                   for ids in i:
                     
                     all_tv_w[str(ids['show']['ids']['tmdb'])]=[]
                     for seasons in ids['seasons']:
                     
                      for ep in seasons['episodes']:
                       
                        all_tv_w[str(ids['show']['ids']['tmdb'])].append(str(seasons['number'])+'x'+str(ep['number']))
                
                else:
                   
                        i = (call_trakt('/users/me/watched/movies'))
                       
                        for ids in i:
                          all_movie_w.append(str(ids['movie']['ids']['tmdb']))
            except:
                pass
            return all_w,all_tv_w,all_movie_w
def get_trakt_resume(tv_movie,id,season,episode):
            global all_w_global
            all_w={}
            if tv_movie=='movie':
                from resources.modules.general import call_trakt
                result=call_trakt('sync/playback/movies')
                
                for items in result:
                    progress=None
              
                    
                    t_id=items['movie']['ids']['tmdb']    
                    if id==str(t_id):
                        if 'progress' in items:
                            progress=items['progress']
                        all_w={}
                        all_w[id]={}
                        all_w[id]['precentage']=str(progress)
                        all_w=json.dumps(all_w)
                        log.warning('Found progress')
                        log.warning(all_w)
                        break
            else:
                from resources.modules.general import call_trakt
                result=call_trakt('sync/playback/episodes')
      
                for items in result:
                    t_id=items['show']['ids']['tmdb']
                    season_t=items['episode']['season']
                    episode_t=items['episode']['number']
                    
                    
                    if id==str(t_id) and season==str(season_t) and episode==str(episode_t):
                        if 'progress' in items:
                            progress=items['progress']
                        all_w={}
                        all_w[id]={}
                        all_w[id]['precentage']=str(progress)
                        all_w=json.dumps(all_w)
                        break
            all_w_global=all_w
            log.warning('Done progress')
            log.warning(all_w_global)
def clean_title(title, broken=None):
    title = title.lower()
    # title = tools.deaccentString(title)
    
    title = ''.join(char for char in title if char in string.printable)
    title= title.encode('ascii', errors='ignore').decode('ascii', errors='ignore')
    if broken == 1:
        apostrophe_replacement = ''
    elif broken == 2:
        apostrophe_replacement = ' s'
    else:
        apostrophe_replacement = 's'
    title = title.replace("\\'s", apostrophe_replacement)
    title = title.replace("'s", apostrophe_replacement)
    title = title.replace("&#039;s", apostrophe_replacement)
    title = title.replace(" 039 s", apostrophe_replacement)

    title = re.sub(r'\:|\\|\/|\,|\!|\?|\(|\)|\'|\"|\\|\[|\]|\-|\_|\.', ' ', title)
    title = re.sub(r'\s+', ' ', title)
    title = re.sub(r'\&', 'and', title)

    return title.strip()
    
def getInfo(release_title):
    info = []
    
    release_title=clean_title(release_title)
    #release_title=release_title.lower().replace('.',' ')
    
    if any(i in release_title for i in ['x265', 'x 265', 'h265', 'h 265', 'hevc','hdr']):
        info.append('HEVC')

    

    

    if any(i in release_title for i in [' cam ', 'camrip', 'hdcam', 'hd cam', ' ts ', 'hd ts', 'hdts', 'telesync', ' tc ', 'hd tc', 'hdtc', 'telecine', 'xbet']):
        info.append('CAM')
    if any(i in release_title for i in [' 3d']):
        info.append('3D')
        
    return info
def is_hebrew(term):
    import unicodedata
    hebrew=False
    for i in term:
        if KODI_VERSION<=18:
            if 'HEBREW' in unicodedata.name(unicode(i).strip()):
                hebrew=True
                break
        else:
            if 'HEBREW' in (i.strip()):
                hebrew=True
                break

    return hebrew
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 12...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 12...', '' )
def check_rejected(name,show_original_year,season,episode,original_title,tv_movie,heb_name,filter_lang,one_click=False):
       try:
        
        
        rejedcted=False
        
        c_name=clean_marks(name).replace('and','').replace('.&.','').replace(' & ','').replace(' and ','').replace('_','.').replace('%3A','.').replace('%3a','.').replace(':','').replace('-','.').replace('[','(').replace(']',')').replace('  ','.').replace(' ','.').replace('....','.').replace('...','.').replace('..','.').replace("'",'').strip().lower()
        heb_name=heb_name.replace('_','.').replace('%3A','.').replace('%3a','.').replace(':','').replace('-','.').replace('[','(').replace(']',')').replace('  ','.').replace(' ','.').replace('....','.').replace('...','.').replace('..','.').replace("'",'').strip().lower()#mando ok 
        
        '''
        info=(PTN.parse(c_name))
        try:
            info['title'] = re.findall("[a-zA-Z0-9. -_]+",info['title'])[0].encode('utf-8')
        except:
            pass
        try:
            info['title']=info['title'].encode('utf-8')
        except:
            pass
        '''
        original_title=original_title.replace('and','').replace('_','.').replace('%3A','.').replace('%3a','.').replace(':','').replace('-','.').replace('[','(').replace(']',')').replace('  ','.').replace(' ','.').replace('....','.').replace('...','.').replace('..','.').replace("'",'').strip().lower()
     
        original_title_alt=original_title.replace('and','').replace('.&.','').replace(' & ','').replace(' and ','').replace('_','.').replace('%3A','.').replace('%3a','.').replace(':','').replace('-','.').replace('[','(').replace(']',')').replace('  ','.').replace(' ','.').replace('....','.').replace('...','.').replace('..','.').replace("'",'').strip().lower()
        #c_name=c_name.replace('&','').replace('and','')
        if 'stargirl' in original_title.lower():
            original_title=original_title.replace("dcs.",'')
            original_title=original_title.replace("dc%27s.",'')
        reject=False
        if tv_movie=='movie':
            if original_title not in c_name and original_title_alt not in c_name:
                #log.warning('c_name:'+c_name)
                #log.warning('original_title:'+original_title)
                reject=True
        else:
            if len(season)==1:
              season_n="0"+season
            else:
              season_n=season
            if len(episode)==1:
              episode_n="0"+episode
            else:
              episode_n=episode
            #log.warning('original_title:'+original_title)
            #log.warning('original_title_alt:'+original_title_alt)
            #log.warning('c_name:'+c_name)
            if original_title.replace('.','') not in c_name.replace('.','') and original_title_alt.replace('.','') not in c_name.replace('.',''):
                #log.warning('r1')
                reject=True
                
            elif 's%se%s.'%(season_n,episode_n) in c_name or 's%se%s###'%(season_n,episode_n) in c_name+'###'  or 's%se%s###'%(season,episode) in c_name+'###' or 's%se%s.'%(season,episode) in c_name:
                #log.warning('r2')
                reject=False
            elif 'season' in c_name:
              
              if 'season.%s.'%season not in c_name.lower() and 'season.%s$$$'%season not in (c_name.lower()+'$$$') and 'season.%s$$$'%season_n not in (c_name.lower()+'$$$') and 'season.%s.'%season_n not in c_name.lower() and 'season %s'%season_n not in c_name and 'season %s '%season not in c_name:
                #log.warning('r3')
                reject=True
            elif '.s%s.'%season_n in c_name:
                #log.warning('r4')
                reject=False
            else:
                #log.warning('r5')
                reject=True
            
        if ' 3d' in original_title.lower() and '3d' not in name.lower():
             reject=True
        if filter_lang:
            all_lang=['rus','russian','fr','french','TrueFrench','ita','italiano','castellano','spanish','swedish','dk','danish','german','nordic','exyu','chs','hindi','polish','mandarin','kor','korean']
            for itt in all_lang:
                if '.'+itt+'.' in c_name and '.en.' not in c_name and '.eng.' not in c_name and '.english.' not in c_name:
                    reject=True
                    break
        
        
            
           
        return reject
        #info['title']=get_title(name)
        
        
        
        
        reject=False
        if tv_movie=='movie':
            
            
            if 'year' in info:
                if str(info['year'])==str(info['title']):
                  reject=False
                elif str(info['year'])!=show_original_year:
                    
                    reject=True
        else:
            if len(season)==1:
              season_n="0"+season
            else:
              season_n=season
            if len(episode)==1:
              episode_n="0"+episode
            else:
              episode_n=episode
            if 'year' in info:
                if str(info['year'])!=show_original_year:
                    reject=True
            if 'season' in info and 'episode' in info:
                if str(info['season'])!=season or str(info['episode'])!=episode:
                    reject=True
            
            elif 'season' in c_name.lower():
                
                if 'season %s'%season not in c_name.lower().replace('.','') and 'season %s'%season_n not in c_name.lower().replace('.',''):
                    reject=True
            elif ' s%s '%season_n in name.lower().replace('.',' '):
                
                reject=False
            else:
                
                reject=True
            if one_click:
                if 's%se%s'%(season_n,episode_n) not in name.lower():
                    reject=True
        try:
            o_name=clean_name(original_title,1).encode('utf-8').lower().replace('\'','').replace('&','and').replace(':',' ').replace('%3a',' ').replace('view ','').replace('(',' ').replace(')',' ').replace('.',' ').replace('  ',' ').replace('!','').replace('3d','').strip()

            m_name=(info['title'].lower().replace('\'','').replace('&','and').replace(':',' ').replace('%3a',' ').replace('view ','').replace('[I]','').replace('.',' ').replace('(',' ').replace(')',' ').replace('  ',' ').replace('!','')).replace('3d','').strip()
            heb_name=heb_name.lower().replace('\'','').replace('&','and').replace(':',' ').replace('%3a',' ').replace('view ','').replace('[I]','').replace('.',' ').replace('(',' ').replace(')',' ').replace('  ',' ').replace('!','').replace('3d','').strip()
        except:
             return False
        '''
        import difflib

        cases=[(o_name,m_name)] 

        for a,b in cases:     
            log.warning('{} => {}'.format(a,b))  
            for i,s in enumerate(difflib.ndiff(a, b)):
                if s[0]==' ': continue
                elif s[0]=='-':
                    log.warning(u'Delete "{}" from position {}'.format(s[-1],i))
                elif s[0]=='+':
                    log.warning(u'Add "{}" to position {}'.format(s[-1],i))    
        '''
        if ' 3d' in original_title.lower() and '3d' not in name.lower():
             rejedcted=True
        if filter_lang:
            
            if 'language' in info:
                
                if 'English' not in info['language'] and 'english' not in info['language']:
                    
                    reject=True
       
        if o_name != m_name or reject:
            
            rejedcted=True
        
        if heb_name in m_name:#mando ok 
            rejedcted=False
       
        

        return rejedcted
       
       except Exception as e:
        import linecache
        sources_searching=False
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        log.warning('ERROR IN rejedcted IN:'+str(lineno))
        log.warning('inline:'+line)
        log.warning('Error:'+str(e))
       
        return True
def check_forbiden(nm):
    forbidden_words=[' xxx ',' cock ',' lesbian ',' horny ',' ass ',' gay ',' porn ','adulttime','fuck','brazzers','cock',' anal ','mature','pornstar',' sucking ','bigtits','boobs','masturbate',' milf ']
    forbidden_end_with_words=[' xxx',' cock',' lesbian',' horny',' ass',' gay',' porn']

    n_test=nm.lower().replace('.',' ').replace('-',' ').replace('_',' ')
    continue_next=False
    for itt in forbidden_end_with_words:
     
      if n_test.endswith(itt):
        continue_next=True
        break
    
    for itt in forbidden_words:
      
      
      if itt in n_test:
                
                continue_next=True
                break
    return continue_next  
def start_window2(id,tv_movie,name,selected_option,season,episode):

      if selected_option=='0':
        send_type='find_similar'
      else:
        send_type=''
      menu = sources_search2('plugin.video.ghost', id,tv_movie,send_type,season,episode)
      menu.doModal()
     
      del menu
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 13...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 13...', '' )
class infoDialog(xbmcgui.WindowXMLDialog):
    
    def __new__(cls, addonID,msg):
        
        
        FILENAME='Dialog_Notification.xml'
        return super(infoDialog, cls).__new__(cls, FILENAME,Addon.getAddonInfo('path'), 'DefaultSkin')
        

    def __init__(self, addonID,msg):
        super(infoDialog, self).__init__()
        self.msg_txt=msg
        self.counter_close=0
    def onInit(self):
        global infoDialog_counter_close
        self.title = 401
        self.msg = 402
        self.getControl(self.title).setLabel(Addon.getAddonInfo('name'))
        self.getControl(self.msg).setLabel(self.msg_txt)
        while self.counter_close<100:
            xbmc.sleep(60)
            self.counter_close+=1
            if infoDialog_counter_close:
                break
        self.setFocusId(self.getCurrentContainerId())
        self.close()
def show_results(result_string):
    log.warning('result_string:'+result_string)
    menu2 = infoDialog(sys.argv[0], result_string)
    menu2.doModal()
    del menu2
def get_tvdb(id):
    url_media='https://api.themoviedb.org/3/%s/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&include_image_language=ru,null&append_to_response=images,external_ids'%('tv',id,lang)
    time_to_save=int(Addon.getSetting("save_time"))
   
    html_media=get_html(url_media).json()
    try:
      tvdb_id=str(html_media['external_ids']['tvdb_id'])
    except:
      tvdb_id=''
    return tvdb_id
def get_sources(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,heb_name,video_data_exp={},all_w={},use_filter='true',use_rejected='true',tvdb_id=''):
    global silent,selected_index,po_watching,all_w_global,all_s_in,infoDialog_counter_close
    from resources.modules.general import fix_q
    try:
        name=unque(name)
        original_title=unque(original_title)
    except:
        pass
    name=clean_marks(name)
    original_title=clean_marks(original_title)
    
    if original_title=='%20':
        original_title=name
    infoDialog_counter_close=False
    try:
        s=int(season)
        tv_movie='tv'
        
    except:
        tv_movie='movie'
    all_p_data=[]
    
    if tv_movie=='tv':
        tvdb_id= cache.get(get_tvdb,999, id, table='pages') 
    tmdbKey='fb981e5ab89415bba616409d5eb5f05e'
    if name==' ' or original_title==' ':
        if tv_movie=='tv':
          
           url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
           n_type='name'
           o_type='original_name'
        else:
           
           url2='http://api.themoviedb.org/3/movie/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
           n_type='title'
           o_type='original_title'
        x_data=get_html(url2).json()
        name=x_data.get(n_type,' ')
        original_title=x_data.get(o_type,' ')
    
    start_time=time.time()
    if Addon.getSetting("dp")=='true':
     
         dp = xbmcgui.DialogProgress()
         if KODI_VERSION>18:
            dp.create("Collecting", Addon.getLocalizedString(32072)+'\n'+ '')
         else:
            dp.create("Collecting", Addon.getLocalizedString(32072), '')
         
         elapsed_time = time.time() - start_time
         if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32081)+'\n'+ '')
         else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32081), '')
         
    all_p_data.append((name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,video_data_exp,all_w,'false'))
    if Addon.getSetting("trakt_access_token")!=''  and Addon.getSetting("trakt_info")=='true':

        all_w_global={}
        thread=[]
                
        thread.append(Thread(get_trakt_resume,tv_movie,id,season,episode))
            
        
        thread[0].start()
    
    episode=episode.replace('+','%20')
    elapsed_time = time.time() - start_time
    if Addon.getSetting("dp")=='true':
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32081)+'\n'+Addon.getLocalizedString(32073))
        else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32081),Addon.getLocalizedString(32073))
    if 'None' not in id:
        if 'tvdb' in id :
            url2='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=tvdb_id&language=%s'%(id.replace('tvdb',''),lang)
            pre_id=get_html(url2).json()['tv_results']
            
            if len(pre_id)>0:
                id=str(pre_id[0]['id'])
        elif 'imdb' in id:
            url2='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=imdb_id&language=%s'%(id.replace('imdb',''),lang)
            
            if tv_movie=='movie':
                pre_id=get_html(url2).json()['movie_results']
            else:
                pre_id=get_html(url2).json()['tv_results']
            
            if len(pre_id)>0:
                id=str(pre_id[0]['id'])
    
    silent=False
    time_to_save=int(Addon.getSetting("save_time"))
    try:
        c=int(season)
        tv=True
    except:
       tv=False
       season='%20'
    if tv==False:
        se='one_click'
        
    else:
        se='one_click_tv'
    one_click=Addon.getSetting(se)=='true'
    
    original_title=original_title.replace(':','%3A')
    
    elapsed_time = time.time() - start_time
    if Addon.getSetting("dp")=='true':
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32081)+'\n'+ Addon.getLocalizedString(32082))
        else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32081),Addon.getLocalizedString(32082))
    if one_click:
    
        match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= c_get_sources( original_title,data,original_title,id,season,episode,show_original_year,heb_name,False,'',tvdb_id)
    else:
        #match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= c_get_sources( original_title,data,original_title,id,season,episode,show_original_year,heb_name)
        match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= cache.get(c_get_sources, time_to_save, original_title,data,original_title,id,season,episode,show_original_year,heb_name,False,'',tvdb_id,table='pages')
    dd=[]
    dd.append((name,data,original_title,id,season,episode,show_original_year,tvdb_id))
    
    elapsed_time = time.time() - start_time
    if Addon.getSetting("dp")=='true':
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32081)+'\n'+ Addon.getLocalizedString(32083))
        else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32081), Addon.getLocalizedString(32083))
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
    
    dbcur.execute("DELETE FROM nextup")
    code=(base64.b64encode(json.dumps(dd).encode("utf-8"))).decode("utf-8")
    try:
       dbcur.execute("INSERT INTO nextup Values ('%s')"%(code))
    except:
        dbcur.execute("DROP TABLE IF EXISTS nextup;")
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
        dbcur.execute("INSERT INTO nextup Values ('%s')"%(code))
    dbcon.commit()
    
    dbcur.close()
    dbcon.close()
    if Addon.getSetting("dp")=='true':
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32081)+'\n'+ Addon.getLocalizedString(32083))
        else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32081), Addon.getLocalizedString(32083))
    menu=[]
    better_look=Addon.getSetting('better_look')=='true'
    
    links_data={}
    links_data['cached']=0
    links_data['un_cached']=0
    links_data['all']=0
    links_data['duplicated']=0
    
    all_lk=[]
    #from resources.modules import PTN
    max_q_t=[720,1080,2160]
    min_q_t=[0,720,1080,2160]
    
    if tv_movie=='movie':
        added=''
    else:
        added='_tv'
    max_q=max_q_t[int(Addon.getSetting('max_q'+added))]
    min_q=min_q_t[int(Addon.getSetting('min_q'+added))]
    
    disable_3d=Addon.getSetting('3d'+added)=='false'
    disable_hdvc=Addon.getSetting('hdvc'+added)=='false'
    disable_low=Addon.getSetting('low_q'+added)=='false'
    encoding_filter=Addon.getSetting('encoding_filter'+added)=='true'
    #from resources.modules import PTN
    PTN=[]
   
    if once==0:
        all_data=[]
        all_rejected=[]
        all_filted=[]
        all_filted_rejected=[]
        filter_lang=Addon.getSetting("filter_non_e")=='true'
        al_lk_count=0
        all_dup=0
        all_cached=0
        all_unc=0
        for items in match_a:
            for name,lk,data,quality in match_a[items]['links']:
               all_s_in=({},0,' Check Rejected  ',2,name)
               elapsed_time = time.time() - start_time
               if Addon.getSetting("dp")=='true':
                if KODI_VERSION>18:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32084)+'\n'+ name)
                else:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32084), name)
               
               continue_next=False
               
               try:
                   int_q=int(quality)
                   if int_q<min_q or int_q>max_q:
                    continue_next=True
               except:
                   if min_q>0:
                      continue_next=True
                   pass
               
               if encoding_filter:
                   data_name=getInfo(name)
                 
                   if 'CAM' in data_name and disable_low:
                     continue_next=True
                   if 'HEVC' in data_name and disable_hdvc:
                     continue_next=True
                   if '3D' in data_name and disable_3d:
                     continue_next=True
               
              
               al_lk_count+=1
               
               reverse_lookup = {x:i for i, x in enumerate(all_lk)}
               test = reverse_lookup.get(lk, -1)
               
               if test!=-1:
                    all_dup+=1
                    continue
               
               
               
               all_lk.append(lk)
               
               if lk in all_ok:
                
                all_cached+=1
                
                if check_rejected(name,show_original_year,season,episode,original_title,tv_movie,heb_name,filter_lang):
                    if 0:
                        log.warning(clean_name(original_title,1).lower())
                        log.warning(info['title'].lower())
                       
                        if 'year' in info:
                            log.warning(info['year'])
                            log.warning(show_original_year)
                    if continue_next:
                        all_filted_rejected.append(('[COLOR pink][I]'+name+'[/I][/COLOR]',lk,data,fix_q(quality),quality,items.replace('magnet_','').replace('.py',''),))
                        continue
                    
                    all_rejected.append(('[COLOR pink][I]'+name+'[/I][/COLOR]',lk,data,fix_q(quality),quality,items.replace('magnet_','').replace('.py',''),))
                else:
                    if continue_next:
                        all_filted.append((name,lk,data,fix_q(quality),quality,items.replace('magnet_','').replace('.py',''),))
                        continue
                    all_data.append((name,lk,data,fix_q(quality),quality,items.replace('magnet_','').replace('.py',''),))
               else:
                all_unc+=1
        links_data['cached']=all_cached
        links_data['all']=al_lk_count
        links_data['duplicated']=all_dup
        links_data['un_cached']=all_unc
        if len(all_data)==0:
            xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), Addon.getLocalizedString(32085))))
            infoDialog_counter_close=True
            #xbmcgui.Dialog().ok('Error','No results found try looking at the rejected or increasing the scrape time')
        if use_filter=='false':
            all_data=all_filted
        
        if use_rejected=='false':
            all_rejected=sorted(all_rejected, key=lambda x: x[3], reverse=False)
            all_data=all_rejected
            all_rejected=[]
        all_data=sorted(all_data, key=lambda x: x[3], reverse=False)
        
        
        
        all_fav=[]
        
        if tv_movie=='tv':
            all_fav=Addon.getSetting('fav_tv').split(',')
        else:
            all_fav=Addon.getSetting('fav_movie').split(',')
        all_2160_fav=[]
        all_1080_fav=[]
        all_720_fav=[]
        all_rest_fav=[]
        
            
        all_2160=[]
        all_1080=[]
        all_720=[]
        all_rest=[]
        z=0
        all_rejected_orginged=[]
        for name,lk,data,fix,quality,source in all_rejected:
            all_s_in=({},int((z*100.0)/(len(all_rejected))),'Ordering links',2,name)
            z+=1
            if source in all_fav:
                in_2160=all_2160_fav
                in_1080=all_1080_fav
                in_720=all_720_fav
                in_rest=all_rest_fav
                
            else:
                in_2160=all_2160
                in_1080=all_1080
                in_720=all_720
                in_rest=all_rest
                
            elapsed_time = time.time() - start_time
            
            try:
                data_f=float(data)
            except:
                data_f=0
            if Addon.getSetting("dp")=='true':
                if KODI_VERSION>18:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32084)+'\n'+ name)
                else:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32084), name)
            if fix==1:
                in_2160.append((name,lk,data_f,fix,quality,source))
            elif fix==2:
                in_1080.append((name,lk,(data_f),fix,quality,source))
            elif fix==3:
                in_720.append((name,lk,(data_f),fix,quality,source))
            else:
                in_rest.append((name,lk,(data_f),fix,quality,source))
        
        all_2160=sorted(all_2160, key=lambda x: x[2], reverse=True)
        all_1080=sorted(all_1080, key=lambda x: x[2], reverse=True)
        all_720=sorted(all_720, key=lambda x: x[2], reverse=True)
        all_rest=sorted(all_rest, key=lambda x: x[2], reverse=True)
        
        all_2160_fav=sorted(all_2160_fav, key=lambda x: x[2], reverse=True)
        all_1080_fav=sorted(all_1080_fav, key=lambda x: x[2], reverse=True)
        all_720_fav=sorted(all_720_fav, key=lambda x: x[2], reverse=True)
        all_rest_fav=sorted(all_rest_fav, key=lambda x: x[2], reverse=True)
        
        all_rejected_orginged=all_2160_fav+all_1080_fav+all_720_fav+all_rest_fav+all_2160+all_1080+all_720+all_rest
        all_2160_fav=[]
        all_1080_fav=[]
        all_720_fav=[]
        all_rest_fav=[]
        
            
        all_2160=[]
        all_1080=[]
        all_720=[]
        all_rest=[]
        z=0
        for name,lk,data,fix,quality,source in all_data:
            all_s_in=({},int((z*100.0)/(len(all_data))),'Ordering links',2,name)
            z+=1
            if source in all_fav:
                in_2160=all_2160_fav
                in_1080=all_1080_fav
                in_720=all_720_fav
                in_rest=all_rest_fav
                
            else:
                in_2160=all_2160
                in_1080=all_1080
                in_720=all_720
                in_rest=all_rest
                
            elapsed_time = time.time() - start_time
            
            try:
                data_f=float(data)
            except:
                data_f=0
            if Addon.getSetting("dp")=='true':
                if KODI_VERSION>18:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32084)+'\n'+ name)
                else:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32084), name)
            if fix==1:
                in_2160.append((name,lk,data_f,fix,quality,source))
            elif fix==2:
                in_1080.append((name,lk,(data_f),fix,quality,source))
            elif fix==3:
                in_720.append((name,lk,(data_f),fix,quality,source))
            else:
                in_rest.append((name,lk,(data_f),fix,quality,source))
        
        all_2160=sorted(all_2160, key=lambda x: x[2], reverse=True)
        all_1080=sorted(all_1080, key=lambda x: x[2], reverse=True)
        all_720=sorted(all_720, key=lambda x: x[2], reverse=True)
        all_rest=sorted(all_rest, key=lambda x: x[2], reverse=True)
        
        all_2160_fav=sorted(all_2160_fav, key=lambda x: x[2], reverse=True)
        all_1080_fav=sorted(all_1080_fav, key=lambda x: x[2], reverse=True)
        all_720_fav=sorted(all_720_fav, key=lambda x: x[2], reverse=True)
        all_rest_fav=sorted(all_rest_fav, key=lambda x: x[2], reverse=True)
        
        all_data=all_2160_fav+all_1080_fav+all_720_fav+all_rest_fav+all_2160+all_1080+all_720+all_rest+all_rejected_orginged
        all_dd=[]
        choise=[]
        id_col=''
        all_f_sources=[]
        if Addon.getSetting("show_collection")=='true':
          if tv_movie=='movie':
            url_col='https://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(id,lang)
            
            x=get_html(url_col).json()
            
            if 'belongs_to_collection' in x:
              if x['belongs_to_collection']!=None:
                if x['belongs_to_collection']['poster_path']==None:
                    x['belongs_to_collection']['poster_path']=''
                if x['belongs_to_collection']['backdrop_path']==None:
                    x['belongs_to_collection']['backdrop_path']=''
                
                all_f_sources.append('open_collection')

                nmm=x['belongs_to_collection']['name']
                menu.append(['', 'Open collection','','','',nmm,'Open collection','https://image.tmdb.org/t/p/original'+x['belongs_to_collection']['poster_path']])
                all_dd.append(('open_collection', 'open_collection', iconimage,fanart,description,data,x['belongs_to_collection']['id'],season,episode,original_title,show_original_year,json.dumps(dd)))
                id_col=x['belongs_to_collection']['id']
        all_c_name=[]
        
        all_s_in=( {},100 ,'',4,'')
        
        for name,lk,data,fix,quality,source in all_data:
                elapsed_time = time.time() - start_time
                if Addon.getSetting("dp")=='true':
                    if KODI_VERSION>18:
                        dp.update(0,Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32084)+'\n'+ name)
                    else:
                        dp.update(0,Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32084),name)
                color='white'
                if '2160' in quality or '4k' in quality.lower():
                    color='yellow'
                elif '1080' in quality:
                    color='lightblue'
                elif '720' in quality:
                    color='lightgreen'
                if '5.1' in name or '5 1' in name:
                    sound='-[COLOR khaki]5.1[/COLOR]-'
                elif '7.1' in name  or '7 1' in name:
                    sound='-[COLOR khaki]7.1[/COLOR]-'
                else:
                    sound=''
                data=str(round(float(data), 2))
                try:
                    nm='[COLOR lightblue][B]'+name+'[/B][/COLOR]\n'#mando ok 
                except:
                  try:
                    nm='[COLOR lightblue][B]'+name+'[/B][/COLOR]\n'
                  except:
                    nm=name
                
                continue_next=check_forbiden(name)
                
                if continue_next:
                    continue
                menu.append([source, source,sound,quality,nm,data+'GB',lk,''])
                all_c_name.append(name)
                all_f_sources.append(source)
                all_dd.append((name, lk, iconimage,fanart,nm+description,data,id,season,episode,original_title,show_original_year,json.dumps(dd)))
                choise.append(('[COLOR %s]%s-[/COLOR]%s[COLOR bisque][I]%s[/I][/COLOR]-%s'%(color,quality,sound,data+'GB',source,)))
                if not better_look:
                    addLink('[COLOR %s]%s-[/COLOR]%s[COLOR bisque][I]%s[/I][/COLOR]-%s'%(color,quality,sound,data+'GB',source,), lk,6,False, iconimage,fanart,nm+description,data=data,tmdb=id,season=season,episode=episode,original_title=original_title,year=show_original_year,dd=json.dumps(dd))
        elapsed_time = time.time() - start_time
        if Addon.getSetting("dp")=='true':
            if KODI_VERSION>18:
                dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32086)+'\n'+ '')
            else:
                dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32086), '')
        if tv_movie=='movie':
            se='one_click'
            
        else:
            se='one_click_tv'
        if use_filter=='true' and len(all_filted)>0:
            menu.append(['', '','','','[COLOR red][I][B]--%s (%s)--[/I][/B][/COLOR]'%(Addon.getLocalizedString(32087),str(len(all_filted))),'','open_filtered',''])
            all_dd.append(('open_filtered', 'open_filtered', iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,json.dumps(dd)))
        if 0:#use_rejected=='true' and len(all_rejected)>0:
            menu.append(['', '','','','[COLOR red][I][B]--%s (%s)--[/I][/B][/COLOR]'%(Addon.getLocalizedString(32088),str(len(all_rejected))),'','open_rejected',''])
            all_dd.append(('open_rejected', 'open_rejected', iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,json.dumps(dd)))
            
        
            
        result_string=Addon.getLocalizedString(32089)+str(statistics['magnet'])+Addon.getLocalizedString(32090)+str(statistics['d_unique'])+Addon.getLocalizedString(32091)+str(links_data['cached'])+'[/COLOR]'
        if Addon.getSetting("sources_window_n")=='1':
            thread=[]
                    
            thread.append(Thread(show_results,result_string))
                
            
            thread[0].start()
        
        
                
        one_click=Addon.getSetting(se)=='true'
        if Addon.getSetting("video_in_s_wait")=='true':
            while xbmc.Player().isPlaying():
                if Addon.getSetting("dp")=='true':
                    if KODI_VERSION>18:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32086)+'\n'+ 'waiting for video')
                    else:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32086), 'waiting for video')
                xbmc.sleep(100)
        if len(menu)==0:
            xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), Addon.getLocalizedString(32085))))
        if (one_click or better_look) and len(menu)>0:
            if Addon.getSetting("dp")=='true':
                if KODI_VERSION>18:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32086)+'\n'+ 'Opening menu')
                else:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32086),'Opening menu')
                
            if better_look:
                if Addon.getSetting("sources_window_n")=='2': 
                    menu2 = ContextMenu_new4(sys.argv[0], menu,iconimage,fanart,description,str(result_string),po_watching,l_full_stats,tv_movie,id,tvdb_id,season,episode,show_original_year,original_title)
                else:
                    menu2 = ContextMenu_new2(sys.argv[0], menu,iconimage,fanart,description,str(result_string),po_watching,l_full_stats,tv_movie,id,tvdb_id,season,episode,show_original_year,original_title)
                
                menu2.doModal()
                del menu2
                log.warning('Close NOWWWW')
                infoDialog_counter_close=True
                
                ret=selected_index
               
                #
            else:
                ret = xbmcgui.Dialog().select("Choose link", choise)
            if Addon.getSetting("dp")=='true':
                dp.close()
            log.warning(ret)
            
            if ret!=-1:
                name,url,iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,dd=all_dd[ret]
                #xbmc.executebuiltin("Dialog.Open(busydialog)")
                log.warning(name)
                try:
                    f_name=all_c_name[ret]
                except:
                    f_name=name
               
                
                if name=='open_filtered':
                    name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,video_data_exp,all_w,use_filter=all_p_data[0]
                    str_next='RunPlugin("%s?name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&data=%s&original_title=%s&id=%s&season=%s&episode=%s&show_original_year=%s&video_data_exp=%s&all_w=%s&use_filter=false&mode=15&heb_name=%s&tmdbid=%s")'%(sys.argv[0],que(name),'www',iconimage,fanart,que(description),data,que(original_title),id,season,episode,show_original_year,que(video_data_exp),que(all_w),heb_name,tmdbid)
                    #xbmc.executebuiltin("Dialog.Close(busydialog)")
                    if KODI_VERSION<=18:
                        xbmc.executebuiltin(str_next.encode('utf-8'))
                    else:
                        xbmc.executebuiltin(str_next)
                    
                    return 0
                if name=='open_rejected':
                    name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,video_data_exp,all_w,use_filter=all_p_data[0]
                    str_next='RunPlugin("%s?name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&data=%s&original_title=%s&id=%s&season=%s&episode=%s&show_original_year=%s&video_data_exp=%s&all_w=%s&use_rejected=false&mode=15&heb_name=%s&tmdbid=%s")'%(sys.argv[0],que(name),'www',iconimage,fanart,que(description),data,que(original_title),id,season,episode,show_original_year,que(video_data_exp),que(all_w),heb_name,tmdbid)
                    #xbmc.executebuiltin("Dialog.Close(busydialog)")
                 
                    if KODI_VERSION<=18:
                        xbmc.executebuiltin(str_next.encode('utf-8'))
                    else:
                        xbmc.executebuiltin(str_next)
                    
                    return 0
                if name=='open_collection':
                    name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,video_data_exp,all_w,use_filter=all_p_data[0]
                    str_next='Container.update("%s?name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&data=%s&original_title=%s&id=%s&season=%s&episode=%s&show_original_year=%s&video_data_exp=%s&all_w=%s&use_rejected=false&mode=179&heb_name=%s&tmdbid=%s")'%(sys.argv[0],que(name),'www',iconimage,fanart,que(description),data,que(original_title),id_col,season,episode,show_original_year,que(video_data_exp),que(all_w),heb_name,tmdbid)
                    #xbmc.executebuiltin("Dialog.Close(busydialog)")
                  
                    if KODI_VERSION<=18:
                        xbmc.executebuiltin(str_next.encode('utf-8'))
                    else:
                        xbmc.executebuiltin(str_next)
                    s=stop_play()
                    if s=='forceexit':
                        sys.exit(1)
                    else:
                        return 0
                xbmc.executebuiltin("ActivateWindow(10138)")
               
                try:
                    f_source=all_f_sources[ret]
                except:
                    s=stop_play()
                    if s=='forceexit':
                        sys.exit(1)
                    else:
                        return 0
                play_link(f_name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dd,heb_name,nextup='true',video_data_exp=video_data_exp,all_dd=all_dd,start_index=ret,all_w=all_w,source=f_source,tvdb_id=tvdb_id)
                xbmc.executebuiltin("Dialog.Close(busydialog)")
            else:
                
                s=stop_play()
                if s=='forceexit':
                    sys.exit(1)
                else:
                    return 0

def ClearCache():
  
    log.warning('Clear')
    cache.clear(['cookies', 'pages','posters','last_view'])
    xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'),  Addon.getLocalizedString(32092))))
def post_trk(id,season,episode,progress=False,len_progress='',type_progress='',tvdb_id=''):
    
    from resources.modules.general import post_trakt
    if (len(id)>1 and id!='%20') or len(tvdb_id)>1:
         if season!=None and season!="%20":
           '''
           log.warning('tv')
           log.warning(imdb_id)
           url_pre='http://thetvdb.com/api/GetSeriesByRemoteID.php?imdbid=%s&language=en'%imdb_id.replace('tt','')
           html2=get_html(url_pre).content()
           pre_tvdb = str(html2).split('<seriesid>')
           if len(pre_tvdb) > 1:
                tvdb = str(pre_tvdb[1]).split('</seriesid>')
           log.warning(tvdb)
           '''
           season_t, episode_t = int('%01d' % int(season)), int('%01d' % int(episode))
           if progress:
            ur='https://api.themoviedb.org/3/tv/%s/season/%s/episode/%s?api_key=fb981e5ab89415bba616409d5eb5f05e'%(id,season,episode)
            yy=get_html(ur).json()
            f_id=''
            if 'id' in yy:
                f_id=yy['id']
            ddata={"progress": int(len_progress), "episode": {"ids": {"tmdb": f_id,'tvdb':tvdb_id}}}

            i = (post_trakt('/scrobble/'+type_progress, data=ddata))
           else:
               i = (post_trakt('/sync/history', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id,'tvdb':tvdb_id}}]}))
           log.warning('TRK')
           log.warning(i)
         else:
           if progress:
               i = (post_trakt('/scrobble/'+type_progress,data= {'movie': {'ids': {'tmdb': id}}, 'progress': int(len_progress)}))
           else:
                i = (post_trakt('/sync/history',data= {"movies": [{"ids": {"tmdb": id}}]}))
         log.warning('Watched Resoponce:')
         log.warning(i)
def jump_seek(name,id,season,episode,jump_time,precentage,subs,tvdb_id):
    global break_jump,str_next,break_window
    global from_seek
    time_to_save_trk=int(Addon.getSetting("time_to_save"))
    log.warning('Waiting for jump')
    log.warning(xbmc.Player().isPlaying())
    timeout=0
    break_jump=1
    done=0
    time_to_window=int(Addon.getSetting("window"))
    time_left=999999
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
       
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
    dbcon.commit()
    dbcur.execute("SELECT * FROM playback")
    match = dbcur.fetchall()
    dbcur.close()
    dbcon.close()
    all_d_nm=[]
    place_subs=True
    for nm,tm,se,ep,pl,to,fr in match:
        all_d_nm.append(nm+'$$$'+tm+'$$$'+se+'$$$'+ep)
    while timeout<200:
        timeout+=1
        if break_jump==0:
            break
        if xbmc.Player().isPlaying():
            break
        xbmc.sleep(100)
    mark_once=0
    counter_stop=0
   
    while xbmc.Player().isPlaying():
        
        if break_jump==0:
            break
        try:
        
            vidtime = xbmc.Player().getTime()
        except Exception as e:
            vidtime=0
            pass
        #log.warning('Waiting for Vid2:'+str(vidtime))
        
        if vidtime>0.2:
            if subs and place_subs:
                place_subs=False
                subtitlesUrl=subs
                log.warning('Place subtitle:'+subtitlesUrl)
                xbmc.Player().setSubtitles(subtitlesUrl)
            if precentage:
                
                g_item_total_time=xbmc.Player().getTotalTime()
                
                jump_time=((float(jump_time)*g_item_total_time)/100)
                
                precentage=False
            if round(float(jump_time))>round(float(vidtime)):
                
                log.warning('jumping ahead:')
                log.warning(jump_time)
                xbmc.Player().seekTime(int(float(jump_time)))
                jump_time=0
                
                
            
            try:
               g_timer=xbmc.Player().getTime()
               if done==0:
                
                
                g_item_total_time=xbmc.Player().getTotalTime()
                time_left=xbmc.Player().getTotalTime()-xbmc.Player().getTime()
                avg=(g_timer*100)/g_item_total_time
                if mark_once==0:
                    mark_once=1
                    count=0
                    while (count<10):
                        try:
                            post_trk(id,season,episode,progress=True,len_progress=int(avg),type_progress='start',tvdb_id=tvdb_id)
                            break
                        except:
                            pass
                        count+=1
                        time.sleep(1)
                        
                
                if ((avg>time_to_save_trk) and (g_item_total_time>100)):
                    log.warning('Got precentage')
                    count=0
                    while (count<10):
                        try:
                            post_trk(id,season,episode,tvdb_id=tvdb_id)
                            
                            break
                        except:
                            pass
                        count+=1
                        time.sleep(1)
                    done=1
            except Exception as e:
                log.warning('Takt Err:'+str(e))
                pass
            
        xbmc.sleep(100)
    log.warning('Saving')
    log.warning(xbmc.Player().isPlaying())
    log.warning(name+'$$$'+id+'$$$'+season+'$$$'+episode)
    break_window=True
    log.warning(g_timer)
    
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    if name+'$$$'+id+'$$$'+season+'$$$'+episode not in all_d_nm and g_timer>10 and g_item_total_time>300:
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("INSERT INTO playback Values ('%s','%s','%s','%s','%s','%s','%s')"%(name.replace("'","%27"),id,season,episode,str(g_timer),str(g_item_total_time),''))
        dbcon.commit()
    else:
        dbcur.execute("UPDATE playback SET playtime='%s',total='%s' WHERE tmdb = '%s' and season='%s' and episode='%s'"%(str(g_timer),str(g_item_total_time),id,season,episode))
        dbcon.commit()
    post_trk(id,season,episode,progress=True,len_progress=int(avg),type_progress='pause',tvdb_id=tvdb_id)
    dbcur.close()
    dbcon.close()
    log.warning('Waiting for Vid3:'+str(xbmc.Player().isPlaying()))
    log.warning('from_seek22:'+str(from_seek))
    if not from_seek:
        log.warning('from_seek22 Refresh:'+str(from_seek))
        cache.clear(['last_view'])
        xbmc.executebuiltin('Container.Refresh')
def load_test_data(title,icon,fanart,plot,s_title,season,episode,list):
    test_episode = {"episodeid": 0, "tvshowid": 0, "title": title, "art": {}}
    test_episode["art"]["tvshow.poster"] = icon
    test_episode["art"]["thumb"] = icon
    test_episode["art"]["tvshow.fanart"] = fanart
    test_episode["art"]["tvshow.landscape"] =fanart
    test_episode["art"]["tvshow.clearart"] = fanart
    test_episode["art"]["tvshow.clearlogo"] = icon
    test_episode["plot"] = plot
    test_episode["showtitle"] =s_title+' S%sE%s'%(season,episode)
    test_episode["playcount"] = 1
    test_episode["season"] =int( season)
    test_episode["episode"] = int(episode)
    test_episode["seasonepisode"] = "%sx%s"%(season,episode)
    test_episode["rating"] = None
    test_episode["firstaired"] = ""
    test_episode["list"]=list
    test_episode["fanart"]=fanart
    return test_episode
def calculate_progress_steps(period):
                    return (100.0 / int(period)) / 10
def get_next_jen_link(url,episode):
    
    next_episode=int(episode)+1
    match_a={}
    match_a['Jen']={}
    match_a['Jen']['links']=[]
    all_ok=[]
    if '.json' in url:
        log.warning('populate_json_playlist')
        links,title=populate_json_playlist(url,'','','',get_episode_link=True,next_episode=next_episode)
        log.warning('Done_populate_json_playlist::')
        if not links:
            return match_a,all_ok
        if isinstance(url, list):
            for itt in links:
                match_a['Jen']['links'].append((title,itt,'Jen','unk'))
                all_ok.append(itt)
        else:
            match_a['Jen']['links'].append((title,links,'Jen','unk'))
            all_ok.append(links)
    else:
        
        
        x=get_html(url,headers=base_header).content()
        
        regex='<item>(.+?)</item>'
        m=re.compile(regex,re.DOTALL).findall(x)
        
            
        for items in m:
            regex='<imdb>(.+?)</imdb>'
            imdb_id=re.compile(regex).findall(items)
            if len(imdb_id)==0:
                imdb_id=''
            else:
                imdb_id=imdb_id[0]
            regex='<title>(.+?)</title>'
            title=re.compile(regex).findall(items)
            if len(title)==0:
                regex='<name>(.+?)</name>'
                title=re.compile(regex).findall(items)
                if len(title)==0:
                    title=''
                else:
                    title=title[0]
            else:
                title=title[0]
            regex='<year>(.+?)</year>'
            year=re.compile(regex).findall(items)
            if len(year)==0:
                year=''
            else:
                year=year[0]
            regex='<season>(.+?)</season>'
            season=re.compile(regex).findall(items)
            if len(season)==0:
                season=' '
            else:
                season=season[0]
            regex='<episode>(.+?)</episode>'
            episode=re.compile(regex).findall(items)
            if len(episode)==0:
                episode=' '
            else:
                episode=episode[0]
            if episode!=str(next_episode):
                continue
            regex='<sublink>(.+?)</sublink>'
            links=re.compile(regex).findall(items)
            f_link_arr=[]
            
            for itt in links:
                if '(' in itt:
                    itt=itt.split('(')[0]
                f_link_arr.append('Direct_link$$$resolveurl'+itt)
                uri = urp(itt)
                host=(uri.netloc)

                match_a['Jen']['links'].append((title,'Direct_link$$$resolveurl'+itt,host,'unk'))
                all_ok.append('Direct_link$$$resolveurl'+itt)
                
            regex='<link>(.+?)</link>'
            links=re.compile(regex).findall(items)
            for itt in links:
                if '(' in itt:
                    itt=itt.split('(')[0]
                f_link_arr.append('Direct_link$$$resolveurl'+itt)
                uri = urp(itt)
                host=(uri.netloc)
                match_a['Jen']['links'].append(('Jen','Direct_link$$$resolveurl'+itt,host,'unk'))
                all_ok.append('Direct_link$$$resolveurl'+itt)
            if len(f_link_arr)>1:
                f_link='$$$$'.join(f_link_arr)
            elif len(f_link_arr)>0:
                f_link=f_link_arr[0]
            else:
                continue
            
            regex='<thumbnail>(.+?)</thumbnail>'
            icon=re.compile(regex).findall(items)
            if len(icon)==0:
                icon=iconimage
            else:
                icon=icon[0]
            regex='<fanart>(.+?)</fanart>'
            fanart=re.compile(regex).findall(items)
            if len(fanart)==0:
                fanart=o_fanart
            else:
                fanart=fanart[0]
    return match_a,all_ok
def search_next(dd,tv_movie,id,heb_name,playlist):
   global silent,list_index,str_next,break_jump,sources_searching,clicked,break_window,break_window_rd

   from resources.modules.general import fix_q
   try:
    
    if len(str(id))==0:
        return 0
    if str(id)=='%20':
        return 0
    
    list_index=999
    count_timeout_sources=0
    while sources_searching:
        xbmc.sleep(100)
        count_timeout_sources+=1
        if count_timeout_sources>600:
            log.warning('Timeout Search Sources')
            return 0
    log.warning('Done Sources Searching')
    if tv_movie=='tv':
        str_next=''
        silent=True
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
        dbcur.execute("SELECT * FROM nextup")
        match = dbcur.fetchall()
        dbcur.close()
        dbcon.close()
        
        for dd in match:
            dd_a=dd
        
        
        name,data,original_title,id,season,episode,show_original_year,tvdb_id=json.loads(base64.b64decode(dd_a[0]))[0]
        if 'Jen_link' in tvdb_id:
            log.warning(episode)
            log.warning(tvdb_id)
            match_a,all_ok=get_next_jen_link(tvdb_id.replace('Jen_link',''),episode)
            if len(match_a)==0:
               tvdb_id=''
            logging.warning('match_a::')
            logging.warning(match_a)
        
        episode=str(int(episode)+1)
        
        from resources.modules.tmdb import get_episode_data
     
        name_n,plot_n,image_n,season,episode=get_episode_data(id,season,str(int(episode)),o_name=original_title)
        
        time_to_save=int(Addon.getSetting("save_time"))
        
            
        if 'Jen_link' not in tvdb_id:
            match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= cache.get(c_get_sources, time_to_save,str(original_title),str(data),str(original_title),str(id),str(season),str(episode),str(show_original_year),str(heb_name),False,'',tvdb_id ,table='pages')
        #susb_data_next=check_next_last_tv_subs('green',original_title,heb_name,season,episode,show_original_year,id)
        susb_data_next=[]
        logging.warning('Subs nextep:')

        logging.warning('Sources Ready:'+str(len(match_a)))
        dd=[]
        dd.append((original_title,data,original_title,id,season,episode,show_original_year))
        all_data=[]
        all_rejected=[]
        
        filter_lang=Addon.getSetting("filter_non_e")=='true'
        #from resources.modules import PTN
        if 'Jen_link' not in tvdb_id:
            for items in match_a:
                for name,lk,data,quality in match_a[items]['links']:
                   if lk in all_ok:
                        #info=(PTN.parse(clean_marks(name)))
                        
                 
                        
                        if check_rejected(name,show_original_year,season,episode,original_title,tv_movie,heb_name,filter_lang):
                            all_rejected.append(('[COLOR pink][I]'+name+'[/I][/COLOR]',lk,data,fix_q(quality),'[COLOR red][I]Reject'+quality+'[/I][/COLOR]',items.replace('magnet_','').replace('.py',''),))
                        else:
                            all_data.append((name,lk,data,fix_q(quality),quality,items.replace('magnet_','').replace('.py',''),))
        else:
            for items in match_a:
                for name,lk,data,quality in match_a[items]['links']:
                    all_data.append((name,lk,data,fix_q(quality),quality,items.replace('magnet_','').replace('.py',''),))
        log.warning('Sources Ready after filter:'+str(len(all_data)))
        log.warning('Sources Ready Rest filter:'+str(len(all_rejected)))
        all_data=sorted(all_data, key=lambda x: x[3], reverse=False)
        all_2160_fav=[]
        all_1080_fav=[]
        all_720_fav=[]
        all_rest_fav=[]
        
        all_2160=[]
        all_1080=[]
        all_720=[]
        all_rest=[]
        
        all_fav=[]
        
        if tv_movie=='tv':
            all_fav=Addon.getSetting('fav_tv').split(',')
        else:
            all_fav=Addon.getSetting('fav_movie').split(',')
        log.warning('all_fav:')
        log.warning(all_fav)
        for name,lk,data,fix,quality,source in all_data:
            try:
                quality=int(quality)
            except:
                quality=720
            try:
                data=float(data)
            except:
                data=0
            if source in all_fav:
                in_2160=all_2160_fav
                in_1080=all_1080_fav
                in_720=all_720_fav
                in_rest=all_rest_fav
                
            else:
                in_2160=all_2160
                in_1080=all_1080
                in_720=all_720
                in_rest=all_rest
            if source in all_fav:
                log.warning('Fav source:'+source)
            if fix==1:
                in_2160.append((name,lk,data,fix,int(quality),source))
            elif fix==2:
                in_1080.append((name,lk,data,fix,int(quality),source))
            elif fix==3:
                in_720.append((name,lk,data,fix,int(quality),source))
            else:
                in_rest.append((name,lk,data,fix,int(quality),source))
        
        all_2160=sorted(all_2160, key=lambda x: x[2], reverse=True)
        all_1080=sorted(all_1080, key=lambda x: x[2], reverse=True)
        all_720=sorted(all_720, key=lambda x: x[2], reverse=True)
        all_rest=sorted(all_rest, key=lambda x: x[2], reverse=True)
        
        all_2160_fav=sorted(all_2160_fav, key=lambda x: x[2], reverse=True)
        all_1080_fav=sorted(all_1080_fav, key=lambda x: x[2], reverse=True)
        all_720_fav=sorted(all_720_fav, key=lambda x: x[2], reverse=True)
        all_rest_fav=sorted(all_rest_fav, key=lambda x: x[2], reverse=True)
        
        all_data=all_2160_fav+all_1080_fav+all_720_fav+all_rest_fav+all_2160+all_1080+all_720+all_rest
        
        
        list=[]
        all_dd=[]
        all_names=[]
        for name,lk,data,fix,quality,source in all_data:
                quality=str(quality)
                all_dd.append((name,lk,' ',' ',' ',data,id,season,episode,original_title,show_original_year,dd))
                color='white'
                if '2160' in quality or '4k' in quality.lower():
                    color='yellow'
                elif '1080' in quality:
                    color='lightblue'
                elif '720' in quality:
                    color='lightgreen'
                if '[COLOR pink]' in name:
                    color='pink'
                if '5.1' in name:
                    sound='-[COLOR khaki]5.1[/COLOR]-'
                elif '7.1' in name:
                    sound='-[COLOR khaki]7.1[/COLOR]-'
                else:
                    sound=''
                all_names.append(name)
                try:
                    list.append('[COLOR %s]%s-[/COLOR]%s[COLOR bisque][I]%s[/I][/COLOR]-%s'%(color,quality,sound,str(data)+'GB',source,)+'$$$$$$$'+lk)
                except:
                    pass
    time_to_save_trk=int(Addon.getSetting("time_to_save"))
    log.warning('Waiting for jump')
    log.warning(xbmc.Player().isPlaying())
    timeout=0
    break_jump=1
    done=0
    if tv_movie=='tv':
      time_to_window=int(Addon.getSetting("window"))
    else:
        time_to_window=int(Addon.getSetting("movie_window"))
    time_left=999999
    while timeout<200:
        timeout+=1
        if break_jump==0:
            break
        if xbmc.Player().isPlaying():
            break
        xbmc.sleep(100)
    play_next=False
    count_ok=0
    if tv_movie=='tv':
        from resources.modules.tmdb import get_episode_data
        log.warning('Getting next episode')
        name_n,plot_n,image_n,season,episode=get_episode_data(id,season,str(int(episode)),o_name=original_title,yjump=True)
        log.warning('Got it')
        log.warning('season %s, episode %s'%(season,episode))
        
        log.warning('Ep Start')
        ep=load_test_data(name_n,image_n,image_n,plot_n,name_n,season,episode,list)
        log.warning('Ep done')
        
        if original_title  in susb_data_next:
           
            if susb_data_next[original_title]==False:
            
                try:
                    ep['showtitle']='[COLOR red] %s [/COLOR]'%Addon.getLocalizedString(32310)+ep['showtitle']
                except:
                    pass
 
        
        
        if  len(list)==0:
                    return '0'
        log.warning('Find fast_link')
        log.warning(list)
        fast_link=list[0].split('$$$$$$$')[1]
        
                
        
        dd=[]
        dd.append((name,data,original_title,id,season,episode,show_original_year,tvdb_id))

        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup_all_d')
        dbcur.execute("DELETE FROM nextup")
        dbcur.execute("DELETE FROM nextup_all_d")
        dbcur.execute("INSERT INTO nextup Values ('%s')"%(base64.b64encode(json.dumps(dd).encode("utf-8")).decode("utf-8")))
        a=str((all_dd))
        b=base64.b64encode(a.encode("utf-8")).decode("utf-8") 
        dbcur.execute("INSERT INTO nextup_all_d Values ('%s')"%(b))
        dbcon.commit()
        
        dbcur.close()
        dbcon.close()
        log.warning('Nextup episode:'+episode)
        break_window=False
        break_window_rd=False
        break_window_tor=False
        break_window_torrest=False
        str_next='%s?nextup=true&has_alldd=%s&url=%s&no_subs=0&season=%s&episode=%s&mode=6&original_title=%s&id=%s&dd=%s&data=%s&fanart=%s&iconimage=%s&name=%s&description=%s&get_sources_nextup=true'%(sys.argv[0],'true',que(fast_link),season,episode,original_title,id,dd,data,ep["fanart"],iconimage,all_names[0],plot_n)
        #xbmc.executebuiltin(str_next.encode('utf-8'))
        
        
        listItem=xbmcgui.ListItem(all_names[0]+'.S%sE%s'%(season,episode),path=str_next)
        listItem.setInfo('video', {'Title': all_names[0]})
              
    once_pl=True
    while xbmc.Player().isPlaying():
        if break_jump==0:
            break
        try:
        
            vidtime = xbmc.Player().getTime()
        except Exception as e:
            vidtime=0
            pass
        #log.warning('Waiting for Vid2:'+str(vidtime))
        
        if vidtime>10:
            try:
                if tv_movie=='tv' and once_pl:
                    playlist.add(url=str_next, listitem=listItem)
                    once_pl=False
                g_timer=xbmc.Player().getTime()
                g_item_total_time=xbmc.Player().getTotalTime()
                if xbmc.Player().getTotalTime()>10 and xbmc.Player().getTime()>10:
                
                    time_left=xbmc.Player().getTotalTime()-xbmc.Player().getTime()
                
            except Exception as e:
                log.warning('Takt Err:'+str(e))
                pass
            if (time_left<time_to_window) :
                count_ok+=1
            else:
                count_ok=0
            log.warning('error counter:'+str(count_ok))
            if count_ok>10 :
              log.warning('Ready to play next')
              play_next=True
              break
        xbmc.sleep(100)
    if break_jump==0:
            return 0
    
    if play_next:
     
      if tv_movie=='tv':
        from resources.modules.tmdb import get_episode_data
        log.warning('Getting next episode')
        name_n,plot_n,image_n,season,episode=get_episode_data(id,season,str(int(episode)),o_name=original_title,yjump=True)
        log.warning('Got it')
        log.warning('season %s, episode %s'%(season,episode))
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        next_up_page = UpNext("script-ghost-upnext.xml",Addon.getAddonInfo('path'), "DefaultSkin", "1080i")
        
        ep=load_test_data(name_n,image_n,image_n,plot_n,name_n,season,episode,list)
        
        
        if original_title  in susb_data_next:
           
            if susb_data_next[original_title]==False:
            
                try:
                    ep['showtitle']='[COLOR red] %s [/COLOR]'%Addon.getLocalizedString(32310)+ep['showtitle']
                except:
                    pass
 
        next_up_page.setItem(ep)

        next_up_page.setProgressStepSize(calculate_progress_steps(30))
        next_up_page.doModal()
        del next_up_page
        log.warning('clicked:'+str(clicked))
        if (Addon.getSetting('play_nextup_wait')=='false' and clicked==False) or len(list)==0:
                    return '0'
        if list_index!=999 and list_index!=888:
            xbmc.Player().stop()
            xbmc.sleep(2)
            log.warning('Stoped')
            if len(list)==0:
                xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0], Addon.getLocalizedString(32085))))
                sys.exit()
            else:
                log.warning(list_index)
                log.warning('Link to play...:'+list[list_index])
                fast_link=list[list_index].split('$$$$$$$')[1]
        
                log.warning('Link to play:'+fast_link)
        else:
            return '0'
        dd=[]
        dd.append((name,data,original_title,id,season,episode,show_original_year,tvdb_id))

        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup_all_d')
        dbcur.execute("DELETE FROM nextup")
        dbcur.execute("DELETE FROM nextup_all_d")
        dbcur.execute("INSERT INTO nextup Values ('%s')"%(base64.b64encode(json.dumps(dd).encode("utf-8")).decode("utf-8")))
        a=str((all_dd))
        b=base64.b64encode(a.encode("utf-8")).decode("utf-8") 
        dbcur.execute("INSERT INTO nextup_all_d Values ('%s')"%(b))
        dbcon.commit()
        
        dbcur.close()
        dbcon.close()
        log.warning('Nextup episode:'+episode)
        break_window=False
        break_window_rd=False
        str_next='RunPlugin("%s?nextup=true&has_alldd=%s&url=%s&no_subs=0&season=%s&episode=%s&mode=6&original_title=%s&id=%s&dd=%s&data=%s&fanart=%s&iconimage=%s&name=%s&description=%s&get_sources_nextup=true")'%(sys.argv[0],'true',que(fast_link),season,episode,original_title,id,dd,data,ep["fanart"],iconimage,all_names[list_index],plot_n)
        xbmc.executebuiltin(str_next)
      else:
      
        window = fav_mv(sys.argv[0],id)
        window.doModal()
        str_next=window.get_str_next()
        del window
        if str_next!="":
            xbmc.executebuiltin(str_next)
    #playlist.clear()
    log.warning('Next Episode Done')
   except Exception as e:
    import linecache
    sources_searching=False
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    log.warning('ERROR IN Play IN:'+str(lineno))
    log.warning('inline:'+line)
    log.warning('Error:'+str(e))
    xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'PlayinLine:'+str(lineno))))
   
    pass
def simple_play(name,url):
        from resources.modules import real_debrid
        rd = real_debrid.RealDebrid()
        if 'Direct$$$$' in url:
            url=url.replace('Direct$$$$','')
            
            info=rd.torrentInfo(url)
            all_nm=[]
            all_lk=[]
            all_t=[]
            for items in info['links']:
                all_lk.append(items)
            count=0
            for items in info['files']:
               
                if (len(all_lk)-1)<count:
                    break
                all_t.append((items['path'].replace('/',''),all_lk[count]))
                count+=1
                
            
            all_t=sorted(all_t, key=lambda x: x[0], reverse=False)
            for nm,lk in all_t:
                all_nm.append(nm)
            
            if len(all_nm)==1:
                name,link=all_t[0]
            else:
                ret = xbmcgui.Dialog().select("Choose", all_nm)
                if ret!=-1:
                    name,link=all_t[ret]
            
                    
                else:
                
                    s=stop_play()
                    if s=='forceexit':
                        sys.exit(1)
                    else:
                        return 0
                    
            
            
            link=rd.unrestrict_link(link)
        elif '[' in url:
            all_ur=json.loads(url)
            all_nam=[]
            for items in all_ur:
                items_s=items.split('/')
                
                all_nam.append(items_s[len(items_s)-1])
            if len(all_nam)==1:
                link=unque(all_ur[0])
                name=all_nam[0]
            else:
                ret = xbmcgui.Dialog().select("Choose", all_nam)
                if ret!=-1:
                    link=all_ur[ret]
                    try:
                        link=unque(link)
                    except:
                        pass
                    name=all_nam[ret]
                else:
                
                    s=stop_play()
                    if s=='forceexit':
                        sys.exit(1)
                    else:
                        return 0
        if link==None:
            xbmcgui.Dialog().ok('Error','[COLOR aqua][I] Item was removed from RD [/I][/COLOR]')
            s=stop_play()
            if s=='forceexit':
                sys.exit(1)
            else:
                return 0
                
        listItem = xbmcgui.ListItem(name, path=link) 
        
      
        listItem.setInfo(type='Video', infoLabels={'title':name}) 
        ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
def resolve_3d(url):
    
    y,cook=get_html(url,headers=base_header,get_cookies=True).json()
  
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Accept': 'video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5',
                'Accept-Language': 'en-US,en;q=0.5',
                
                'Connection': 'keep-alive',
                'Referer': url.replace('www.3donlinefilms.com','www.documentarymania.org'),
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
    }
    headers['cookie']=url_encode(cook)
    f_lk='http://www.documentarymania.org/video.php'
    head=url_encode(headers)
    f_lk=f_lk+"|"+head
    return f_lk

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 14...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 14...', '' )
def get_google_subs(url):
    path1=xbmc_tranlate_path('special://home/addons/script.module.requests/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.urllib3/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.chardet/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.certifi/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.idna/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.futures/lib')
    sys.path.append( path1)
    from resources.modules.xmlsub import xml2srt
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5',
            'Accept-Language': 'en-US,en;q=0.5',
           
            'Connection': 'keep-alive',
            
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
    
    x=get_html(url.strip(),headers=headers).content()
    
    regex='"ttsurl","(.+?)"'
    m=re.compile(regex).findall(x)
    if len(m)==0:
        return False
        
    url=m[0].decode('unicode_escape')+'&ts=%s&type=track&lang=iw&format=1&kind='%(str(time.time()*100))
    
    x=get_html(url,headers=headers).content()
    if len(x)<10:
        url=m[0].decode('unicode_escape')+'&ts=%s&type=track&lang=en&format=1&kind='%(str(time.time()*100))
    
        x=get_html(url,headers=headers).content()
    xml2srt(x,os.path.join(user_dataDir, 'sub.srt'))

    return os.path.join(user_dataDir, 'sub.srt')
def resolve_link_others(nm,url):
    f_link=''
    if 'FN-' in nm:
        nm=nm.replace('FN-','')
        path=xbmc_tranlate_path('special://home/addons/script.module.fenomscrapers/lib')
        sys.path.append( path)
        
        try:
            from fenomscrapers import sources
            sourceDict=sources()
       
           

                
           
            all_sources=[]
            
            found=False
            for i in sourceDict:
                call=i[1]
                
                if i[0]==nm:
                    
                    f_link=call.resolve(url)
                   
                    found=True
                    break
            if found:
                return f_link
        except Exception as e:
            log.warning('error resolve:'+str(e))
            return f_link
    if 'op-' in nm:
        nm=nm.replace('op-','')
        path=xbmc_tranlate_path('special://home/addons/script.module.openscrapers/lib')
        sys.path.append( path)
        
        try:
            from openscrapers import sources
            sourceDict=sources()

           

                
           
            all_sources=[]
            
            found=False
            for i in sourceDict:
                call=i[1]
                if i[0]==nm:
                    f_link=call.resolve(url)
                    found=True
                    break
            if found:
                return f_link
        except:
            return f_link
    log.warning('1')
    path=xbmc_tranlate_path('special://home/addons/script.module.universalscrapers/lib')
    sys.path.append( path)
    path1=xbmc_tranlate_path('special://home/addons/script.module.requests/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.urllib3/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.chardet/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.certifi/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.idna/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.futures/lib')
    sys.path.append( path1)
    log.warning('2')
    if 'un-' in nm:
        try:
            nm=nm.replace('un-','')
            from universalscrapers import relevant_scrapers
            sourceDict=relevant_scrapers()
            log.warning('3')
            all_sources=[]
            f_link=''
            
            for scraper in sourceDict:
                log.warning(scraper.name)
                log.warning(nm)
                if scraper.name==nm:
                    log.warning('Resolving')
                    f_link=scraper().resolve( url)
                    log.warning(f_link)
                    break
            return f_link
        except:
            return f_link
    if 'cr-' in nm:
       nm=nm.replace('cr-','')
       try:
        import pkgutil
        path4=xbmc_tranlate_path('special://home/addons/script.module.simplejson/lib')
        sys.path.append( path4)
        path4=xbmc_tranlate_path('special://home/addons/script.module.thecrew/lib')
        sys.path.append( path4)
        
        __addon__ = xbmcaddon.Addon('script.module.thecrew')
        __cwd__ = xbmc_tranlate_path(__addon__.getAddonInfo('path'))
        sources_path=os.path.join(__cwd__,'lib','resources','lib','sources','sources')
        sources_path2=os.path.join(__cwd__,'lib','resources','lib','sources')
        log.warning('sources_path:'+sources_path)
        
        __all__ = [x[1] for x in os.walk(os.path.dirname(sources_path))][0]
        log.warning(__all__)
        sourceDict = []
        for i in __all__:
            
            for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(os.path.dirname(sources_path), i)]):
                log.warning(module_name)
                log.warning(nm)
                if is_pkg:
                    continue

                try:
                    module = loader.find_module(module_name).load_module(module_name)
                    sourceDict.append((module_name, module.s0urce()))
                    if nm==module_name:
                        log.warning('Resolving:'+module_name+', from:'+nm)
                        f_link=module.s0urce().resolve( url)
                        log.warning(f_link)
                        return f_link
                    
                except Exception as e:
                    log.warning('Error in crew2:'+str(e))
                    pass
                
       except Exception as e:
        log.warning('Error in crew:'+str(e))
        return f_link
        
def getsubs( name, imdb, season, episode,saved_name):
            global done1
            if not Addon.getSetting('subtitles') == 'true': return 'ok'

            log.warning('1')
            

            codePageDict = {'ara': 'cp1256', 'ar': 'cp1256', 'ell': 'cp1253', 'el': 'cp1253', 'heb': 'cp1255', 'he': 'cp1255', 'tur': 'cp1254', 'tr': 'cp1254', 'rus': 'cp1251', 'ru': 'cp1251'}

            quality = ['bluray', 'hdrip', 'brrip', 'bdrip', 'dvdrip', 'webrip', 'hdtv']

            log.warning('2')
            
            log.warning('3')
            '''
            try: subLang = xbmc.Player().getSubtitles()
            except: subLang = ''
            if subLang == langs[0]: raise Exception()
            '''
            if season=='%20':
                season=None
            if episode=='%20':
                episode=None
            #result,f_list=get_sub_result(imdb,season,episode,name,saved_name)
            
            result,f_list=cache.get(get_sub_result,24,imdb,season,episode,name,saved_name, table='pages')
            log.warning('check_pre')
            result=check_pre(saved_name,result,name)
           
            
           
            fixed_list=[]
            log.warning('4')
            if result==0:
                for items in f_list:
                    fixed_list.append((0,items['MovieReleaseName'],items['IDSubtitleFile'],items['SubLanguageID']))
            else:
                for items in result:
                    fixed_list.append((items['pre'],items['MovieReleaseName'],items['IDSubtitleFile'],items['SubLanguageID']))
            
            fixed_list=sorted(fixed_list, key=lambda x: x[0], reverse=True)
            log.warning('5')
            
            if len(fixed_list)==0:
                xbmc.executebuiltin((u'Notification(%s,%s)' % (addon_name, 'No available subs')))
            else:
                log.warning('Show Window')
                window = MySubs('Subtitles - '+name ,fixed_list,f_list)
            log.warning('Done Subs')
            
            done1=2
            '''
            filter = []
            result = [i for i in result if i['SubSumCD'] == '1']

            for lang in langs:
                filter += [i for i in result if i['SubLanguageID'] == lang and any(x in i['MovieReleaseName'].lower() for x in fmt)]
                filter += [i for i in result if i['SubLanguageID'] == lang and any(x in i['MovieReleaseName'].lower() for x in quality)]
                filter += [i for i in result if i['SubLanguageID'] == lang]

            try: lang = xbmc.convertLanguage(filter[0]['SubLanguageID'], xbmc.ISO_639_1)
            except: lang = filter[0]['SubLanguageID']

            content = [filter[0]['IDSubtitleFile'],]
            content = server.DownloadSubtitles(token, content)
            content = base64.b64decode(content['data'][0]['data'])
            content = gzip.GzipFile(fileobj=StringIO.StringIO(content)).read()

            subtitle = xbmc_tranlate_path('special://temp/')
            subtitle = os.path.join(subtitle, 'TemporarySubs.%s.srt' % lang)
            log.warning(subtitle)
            codepage = codePageDict.get(lang, '')
            if codepage and control.setting('subtitles.utf') == 'true':
                try:
                    content_encoded = codecs.decode(content, codepage)
                    content = codecs.encode(content_encoded, 'utf-8')
                except:
                    pass

            file = control.openFile(subtitle, 'w')
            file.write(str(content))
            file.close()

            xbmc.sleep(1000)
            #xbmc.Player().setSubtitles(subtitle)
            '''
def start_subs(name, imdb, season, episode,saved_name):
    global wait_for_subs,done1
    log.warning('wait_for_subs:'+str(wait_for_subs))
    if wait_for_subs==1:
        return 'ok'
    
    wait_for_subs=1
    exit_counter=0
    get_sub_now=0
    play_time=1
    if Addon.getSetting("new_window_type2")=='3':
        play_time=int(Addon.getSetting("play_full_time"))+1
    if done1_1==3:
        play_time=1
    while(1):
        
        if done1_1==3:
            
            play_time=1
            
        if xbmc.Player().isPlaying():
           xbmc.sleep(1000)
           vidtime = xbmc.Player().getTime()
                        
                        
           if vidtime > play_time :
                
                log.warning('Vidtime OK:'+str(vidtime))
                get_sub_now=1
                break
        if exit_counter>600:
                break
        exit_counter+=1
        xbmc.sleep(100)
    wait_for_subs=0
    log.warning('Vidtime OK:'+str(get_sub_now))
    if get_sub_now>0:
        #getsubs( 'Rampage', 'tt2231461', None, None,'Rampage.2018.720p.BluRay.x264-SPARKS')
       
        if season=='%20':
            season=None
        if episode=='%20':
            episode=None
        
        #xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
        getsubs( name, imdb, season, episode,saved_name)
        xbmc.executebuiltin( "XBMC.Action(Fullscreen)" )
        
    return 'OK'
def get_sub_result(imdb,season,episode,name,saved_name):
    log.warning('In 1')
    #result=get_sub_server(imdb,season,episode)
    da=[]
    da.append((imdb,season,episode))
    log.warning('Subtitles Search result')
    log.warning(da)
    if season=='%20':
        season=None
    if episode=='%20':
        episode=None
    
    result=cache.get(get_sub_server,24,imdb,season,episode, table='pages')
    
    log.warning('In 2')
    f_list=result
    #result=check_pre(saved_name,result,name)
    log.warning('In 4')
    return result,f_list
def get_sub_server(imdb,season,episode):
    log.warning('In 4')
    if KODI_VERSION<=18:#kodi18
        import xmlrpclib
        xmlserver=xmlrpclib.Server
    else:
        import xmlrpc.client as xc
        xmlserver=xc.Server
    langs = []
    langDict = {'Afrikaans': 'afr', 'Albanian': 'alb', 'Arabic': 'ara', 'Armenian': 'arm', 'Basque': 'baq', 'Bengali': 'ben', 'Bosnian': 'bos', 'Breton': 'bre', 'Bulgarian': 'bul', 'Burmese': 'bur', 'Catalan': 'cat', 'Chinese': 'chi', 'Croatian': 'hrv', 'Czech': 'cze', 'Danish': 'dan', 'Dutch': 'dut', 'English': 'eng', 'Esperanto': 'epo', 'Estonian': 'est', 'Finnish': 'fin', 'French': 'fre', 'Galician': 'glg', 'Georgian': 'geo', 'German': 'ger', 'Greek': 'ell', 'Hebrew': 'heb', 'Hindi': 'hin', 'Hungarian': 'hun', 'Icelandic': 'ice', 'Indonesian': 'ind', 'Italian': 'ita', 'Japanese': 'jpn', 'Kazakh': 'kaz', 'Khmer': 'khm', 'Korean': 'kor', 'Latvian': 'lav', 'Lithuanian': 'lit', 'Luxembourgish': 'ltz', 'Macedonian': 'mac', 'Malay': 'may', 'Malayalam': 'mal', 'Manipuri': 'mni', 'Mongolian': 'mon', 'Montenegrin': 'mne', 'Norwegian': 'nor', 'Occitan': 'oci', 'Persian': 'per', 'Polish': 'pol', 'Portuguese': 'por,pob', 'Portuguese(Brazil)': 'pob,por', 'Romanian': 'rum', 'Russian': 'rus', 'Serbian': 'scc', 'Sinhalese': 'sin', 'Slovak': 'slo', 'Slovenian': 'slv', 'Spanish': 'spa', 'Swahili': 'swa', 'Swedish': 'swe', 'Syriac': 'syr', 'Tagalog': 'tgl', 'Tamil': 'tam', 'Telugu': 'tel', 'Thai': 'tha', 'Turkish': 'tur', 'Ukrainian': 'ukr', 'Urdu': 'urd'}
    
    try:
        try: langs = langDict[Addon.getSetting('subtitles.lang.1')].split(',')
        except: langs.append(langDict[Addon.getSetting('subtitles.lang.1')])
    except: pass
    try:
        try: langs = langs + langDict[Addon.getSetting('subtitles.lang.2')].split(',')
        except: langs.append(langDict[Addon.getSetting('subtitles.lang.2')])
    except: pass
            
    server = xmlserver('http://api.opensubtitles.org/xml-rpc')
    log.warning('4')
    __scriptname__ = "XBMC Subtitles Unofficial"
    __version__='2.5.1'
    token = server.LogIn('', '', 'en', "%s_v%s" %(__scriptname__.replace(" ","_"),__version__))['token']

    sublanguageid = ','.join(langs) ; imdbid = re.sub('[^0-9]', '', imdb)
    log.warning('5')
    if not (season == None or episode == None):
        result = server.SearchSubtitles(token, [{'sublanguageid': sublanguageid, 'imdbid': imdbid, 'season': season, 'episode': episode}])
        log.warning(result)
        result=result['data']
    else:
        result = server.SearchSubtitles(token, [{'sublanguageid': sublanguageid, 'imdbid': imdbid}])['data']
       
    log.warning('In 5')
    return result
def check_pre(saved_name,all_subs,original_title):
    try:
       release_names=['bluray','hdtv','dvdrip','bdrip','web-dl']
       #array_original=list(saved_name)
       fixed_name=saved_name.lower().strip().replace("%20",".").replace("_",".").replace(" ",".").replace("-",".").replace(".avi","").replace(".mp4","").replace(".mkv","")
       original_title=original_title.lower().strip().replace("%20",".").replace("_",".").replace(" ",".").replace("-",".").replace(".avi","").replace(".mp4","").replace(".mkv","")
       

       
       if KODI_VERSION<=18:#kodi18
        fixed_name=fixed_name.decode('utf-8','ignore').encode("utf-8").replace(original_title,'')
       else:
        fixed_name=fixed_name.encode("ascii", errors="ignore").decode().replace(original_title,'')
       
       if fixed_name=='':
         return 0
       array_original=fixed_name.split(".")

       array_original=[line.strip().lower() for line in array_original]
       array_original=[(x) for x in array_original if x != '']
       highest=0
       all_subs_new=[]
       for items in all_subs:
           
           #array_subs=list(items)
           fixed_name=items['MovieReleaseName'].lower().strip().replace("%20",".").replace("_",".").replace(" ",".").replace("-",".").replace(".avi","").replace(".mp4","").replace(".mkv","")
           fixed_name=fixed_name.replace(original_title,'')
           array_subs=fixed_name.split(".")
           array_subs=[line.strip().lower() for line in array_subs]
           array_subs=[str(x).lower() for x in array_subs if x != '']
           
     
           for item_2 in release_names:
           
            if item_2 in array_original and item_2 in array_subs:
              array_original.append(item_2)
              array_original.append(item_2)
              array_original.append(item_2)
              array_subs.append(item_2)
              array_subs.append(item_2)
              array_subs.append(item_2)
    
            
           precent=similar(array_original,array_subs)
           
           
           items['pre']=precent
           all_subs_new.append(items)
           
           
           if precent>=highest:
             highest=precent
      
       return all_subs_new
    except Exception as e:
          import linecache
          break_window=True
          exc_type, exc_obj, tb = sys.exc_info()
          f = tb.tb_frame
          lineno = tb.tb_lineno
          filename = f.f_code.co_filename
          linecache.checkcache(filename)
          line = linecache.getline(filename, lineno, f.f_globals)
          
          log.warning('ERROR IN Check pre:'+str(lineno))
          log.warning('inline:'+line)
          log.warning(e)
def similar(w1, w2):
    from difflib import SequenceMatcher
   
    s = SequenceMatcher(None, (w1), (w2))
    
    return int(round(s.ratio()*100))
def download_subs(f_list,index):
    try:
        log.warning(f_list[index][2])
        log.warning(f_list[index][3])
        if KODI_VERSION<=18:#kodi18
            import xmlrpclib
            xmlserver=xmlrpclib.Server
        else:
            import xmlrpc.client as xc
            xmlserver=xc.Server
        try:
            from StringIO import StringIO ## for Python 2
        except ImportError:
            from io import StringIO ## for Python 3
            import io
        import codecs,base64,gzip
        codePageDict = {'ara': 'cp1256', 'ar': 'cp1256', 'ell': 'cp1253', 'el': 'cp1253', 'heb': 'cp1255', 'he': 'cp1255', 'tur': 'cp1254', 'tr': 'cp1254', 'rus': 'cp1251', 'ru': 'cp1251'}
        server = xmlserver('http://api.opensubtitles.org/xml-rpc', verbose=0)
        __scriptname__ = "XBMC Subtitles Unofficial"
        __version__='2.5.1'
        token = server.LogIn('', '', 'en', "%s_v%s" %(__scriptname__.replace(" ","_"),__version__))['token']
        content = [f_list[index][2],]
        content = server.DownloadSubtitles(token, content)
        content = base64.b64decode(content['data'][0]['data'])
        if KODI_VERSION>18:#kodi18
            x=io.BytesIO(content)
        else:
            x=StringIO(content)
        content = gzip.GzipFile(fileobj=x).read()
        try: lang = xbmc.convertLanguage(f_list[index][3], xbmc.ISO_639_1)
        except: lang = f_list[index]['SubLanguageID']
        if KODI_VERSION>18:#kodi18
            content=content.decode()
        
        subtitle = xbmc_tranlate_path('special://temp/')
        subtitle = os.path.join(subtitle, 'TemporarySubs.%s.srt' % lang)

        codepage = codePageDict.get(lang, '')
        if codepage and Addon.getSetting('subtitles.utf') == 'true':
            try:
                content_encoded = codecs.decode(content, codepage)
                content = codecs.encode(content_encoded, 'utf-8')
            except:
                pass
        if KODI_VERSION>18:#kodi18
            with io.open(subtitle, "w", encoding="utf-8") as f:
                f.write(content)
        else:
            file = open(subtitle, 'w')
            file.write(str(content))
            file.close()

        xbmc.sleep(1000)
        xbmc.Player().setSubtitles(subtitle)
        return 'ok'
    except Exception as e:
          import linecache
          break_window=True
          exc_type, exc_obj, tb = sys.exc_info()
          f = tb.tb_frame
          lineno = tb.tb_lineno
          filename = f.f_code.co_filename
          linecache.checkcache(filename)
          line = linecache.getline(filename, lineno, f.f_globals)
          
          log.warning('ERROR IN download_subs:'+str(lineno))
          log.warning('inline:'+line)
          log.warning(e)
          return e
def get_more_meta(id,tv_movie,tvdb_id):
    user = 'cf0ebcc2f7b824bd04cf3a318f15c17d'

    headers = {'api-key': '9f846e7ec1ea94fad5d8a431d1d26b43'}

    headers.update({'client-key': user})
    if tv_movie=='tv':
        m_type='tv'
    else:
        m_type='movies'
    f_id=id
    if tv_movie=='tv':
        f_id=tvdb_id
    art=get_html('http://webservice.fanart.tv/v3/%s/%s'%(m_type,f_id),headers=headers).json()
    
    return art
def resolve_prime(f_url):
   try:
    x=get_html(f_url).content()
    regex='</style>.+?javascript">(.+?)</script>'
    m=re.compile(regex,re.DOTALL).findall(x)[0]
   
    f_url=m.split('\n')[2].strip()
    log.warning(f_url)
    if 'http' not in f_url:
        f_url='https:'+f_url
                    
    log.warning(f_url)
    return f_url
   except Exception as e:
    log.warning('Error primewire:'+str(e))
    return f_url
def solve_vidcloud(f_url):
   try:
    x=get_html(f_url).content()
    regex="file: '(.+?)'"
    match=re.compile(regex,re.DOTALL).findall(x)
    
    return (match[0])
   except Exception as e:
    log.warning('Error vidcloud:'+str(e))
    pass
def get_extra_art(id,tv_movie,tvdb_id):
    time_to_save=int(Addon.getSetting("save_time"))
    try:
            all_logo=[]
            all_banner=[]
            all_n_fan=[]
            all_clear_art=[]
            r_logo=''
            r_art=''
            
            
            full_art= cache.get(get_more_meta, time_to_save, id,tv_movie,tvdb_id, table='pages') 
            
            if tv_movie=='tv':
                logo=full_art['hdtvlogo']
                if len(logo)>0:
                   
                    
                    for itt in logo:
                       if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    r_logo=all_logo[0]
                
                
                for itt in full_art['showbackground']:
                   if itt['lang']=='en':
                    all_n_fan.append(itt['url'])
                for itt in full_art['tvbanner']:
                   if itt['lang']=='en':
                    all_banner.append(itt['url'])
            else:
                logo=full_art['hdmovielogo']
                if len(logo)>0:
                    all_logo=[]
                    for itt in logo:
                      if itt['lang']=='en':
                        all_logo.append(itt['url'])
                    random.shuffle(all_logo)
                    r_logo=all_logo[0]
                
                for itt in full_art['hdmovieclearart']:
                   if itt['lang']=='en':
                    all_clear_art.append(itt['url'])
                random.shuffle(all_clear_art)
                r_art=all_clear_art[0]
                for itt in full_art['moviebackground']:
                   if itt['lang']=='en':
                    all_n_fan.append(itt['url'])
                for itt in full_art['moviebanner']:
                   if itt['lang']=='en':
                    all_banner.append(itt['url'])
    except Exception as e:
        log.warning('Fanart Err:'+str(e))
    return all_logo,all_n_fan,all_banner,all_clear_art,r_logo,r_art
def extract_domain(url, remove_http=True):
    if KODI_VERSION<=18:
        from urlparse import urlparse
    else:
        import urllib.parse as urlparse
    uri = urlparse(url)
    if remove_http:
        domain_name = uri.netloc
    domain_name=domain_name.split('.')[0]
    return domain_name
    
def getHoster( sHosterFileName):
        
        log.warning("from resources.hosters." + sHosterFileName + " import cHoster")
        exec ("from resources.hosters." + sHosterFileName + " import cHoster", globals())
        return cHoster()
def v_staream_solve(f_url):
    
    sHosterFileName=extract_domain(f_url)
    log.warning('sHosterFileName:'+sHosterFileName)
    oHoster=getHoster( sHosterFileName)
    
    oHoster.setUrl(f_url)
    found,aLink = oHoster.getMediaLink()
    return found,aLink
def get_vstram_title(url,original_name):
    name1=original_name
    html2=get_html(url).content()
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
    log.warning(match4)
    log.warning(name1)
    if '1fichier.com' in name1:
        name1=original_name
    return name1.replace("."," ").replace('Watch','').replace('watch','').replace(' mp4','').replace('watch','').replace(' MP4','').replace(' mkv','').replace(' MKV','').replace("_",".")
def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z
def decode_vivo(source):
    log.warning(source)
    new_str=unque(str(source))
    a=''
    for ch in new_str:
        
        char_value=ord(ch)+47
  
        if char_value>126:
            ch=chr(ord(ch)-47)
            
            a=a+ch
        else:
            a=a+chr(char_value)
    return a
def solve_vivo(url_n):
    
    
    x=get_html(url_n,headers=base_header).content()
    regex="source: '(.+?)'"
    m=re.compile(regex).findall(x)
    return True,decode_vivo(m[0])
def solve_streamh(url):
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://streamhoe.online',
    'Connection': 'keep-alive',
    'Referer': url,
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
    }

    data = {
      'r': '',
      'd': 'streamhoe.online'
    }
    x=get_html(url.replace('/v/','/api/source/'),headers=base_header,data=data).json()
    
    return True,x['data'][len(x['data'])-1]['file']
def solve_might(url):
    
    x=get_html(url,headers=base_header).content()
    regex="<script type='text/javascript'>(.+?)</script>"
    m2=re.compile(regex,re.DOTALL).findall(x)
    
    from resources.modules.jsunpack import unpack
    data=unpack(m2[0])
    
    data = re.findall('file:"(.+?)"',data, re.DOTALL)[0]
    
    return True,data
def solve_wootly(url_n):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.wootly.ch',
        'Connection': 'keep-alive',
        'Referer': url_n,
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    x,cook1 = get_html(url_n, headers=headers,get_cookies=True).content()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': url_n,
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    
    x,cook = get_html(url_n.replace('/?v=','/e/'), headers=headers,cookies=cook1,get_cookies=True).content()
    regex='input type="hidden" name="(.+?)" value="(.+?)"'
    m=re.compile(regex).findall(x)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.wootly.ch',
        'Connection': 'keep-alive',
        'Referer': url_n.replace('/?v=','/e/'),
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
      m[0][0]: m[0][1]
    }

    
    cook=merge_two_dicts(cook1, cook)
   
    
    x,cook3 = get_html(url_n.replace('/?v=','/e/'), headers=headers,data=data,cookies=cook,get_cookies=True).content()
   
    regex='var vd="(.+?)".+?tk="(.+?)"'
    m=re.compile(regex).findall(x)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': url_n,
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('t', m[0][1]),
        ('id', m[0][0]),
    )

    y = get_html('https://www.wootly.ch/ajax', headers=headers,cookies=cook, params=params).content()
   
    
    return True,'https:/'+y
def resolve_google(url):
    if Addon.getSetting('debrid_select')=='0' and Addon.getSetting('debrid_use')=='true':
        rd = real_debrid.RealDebrid()
        log.warning('unrestrict:'+url)
        link=rd.unrestrict_link(url.strip())
        #link,q=googledrive_resolve(url)
    else:
        
        
        log.warning('Loaindg libs google here:')
        load_resolveurl_libs()
        
        
        import resolveurl
        link =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
        #log.warning('Resolving google here:'+link)
    return True,link
    try:
        found=False
        if Addon.getSetting('debrid_select')=='0' and Addon.getSetting('debrid_use')=='true':
            rd = real_debrid.RealDebrid()
            log.warning('unrestrict:'+url)
            link=rd.unrestrict_link(url.strip())
            found=True
            #link,q=googledrive_resolve(url)
        else:
            
            #from resources.modules.google_solve import googledrive_resolve
            #link,q=googledrive_resolve(url)
            path=xbmc_tranlate_path('special://home/addons/script.module.resolveurl/lib')
            sys.path.append( path)
            path=xbmc_tranlate_path('special://home/addons/script.module.six/lib')
            sys.path.append( path)
            path=xbmc_tranlate_path('special://home/addons/script.module.kodi-six/libs')
            sys.path.append( path)
            import resolveurl
            link =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
            found=True
    except Exception as e:
        log.warning('Resolve google Fault:'+str(e))
        pass
    return found,link
def resolve_vidsrc(url_n):
    regex='https://vidsrc.xyz/v/(.+?)(?:/|$)'
    in_id_pre=re.compile(regex).findall(url_n)
    
    if len(in_id_pre)>0:
    
        in_id=in_id_pre[0]
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': url_n,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        }

        data = {
          'r': url_n,
          'd': 'www.vidsource.me'
        }

        response = get_html('https://www.vidsource.me/api/source/'+in_id, headers=headers, data=data).json()
        log.warning(response)
        highest_res=0
        f_link=''
        for items in response['data']:
            
            
            res=items['label']
            res1=res.replace('p','')
            if int(res1)>highest_res:
                highest_res=int(res1)
                f_link=items['file']
        return True,f_link
def show_new_window(tv_movie,id,season,episode):
    global break_window,break_window_rd
    menu = player_window('plugin.video.ghost', id,tv_movie,season,episode)
    menu.doModal()

    del menu
    
    break_window=True
    break_window_rd=True
    logging.warning('break_window2:'+str(break_window))
def resolve_youtube(url):
    if url .endswith ('/'):#line:3026
        url =url [:-1 ]#line:3027
    y_id =url .split ('v=')[1 ]#line:3028
    if '&' in y_id:
        y_id=y_id.split('&')[0]
    f_url ='plugin://plugin.video.youtube/play/?video_id='+y_id #line:3029
    return f_url
def resolve_meta(url):
    x=get_html(url,headers=base_header).content()
    regex='data-mcvideourl="(.+?)"'
    return re.compile(regex).findall(x)[0]
def solve_stream4u(url):
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://streamm4u.club',
        'Alt-Used': 'streamm4u.club',
        'Connection': 'keep-alive',
        'Referer': url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers',
    }

    data = {
      'r': '',
      'd': 'streamm4u.club'
    }
    source=url.split('v/')[1]
    response = get_html('https://streamm4u.club/api/source/'+source, headers=headers, data=data).json()
    for items in response['data']:
        link=items['file']
    return link
def solve_m4u(url,name,year):
    url='https://m4ufree.tv/'+url.replace('Solve%20m4u','')
    log.warning(url)
    x,cookies=get_html(url,headers=base_header,get_cookies=True).content()
    log.warning('cookies::')
    log.warning(cookies)
    regex='csrf-token" content="(.+?)"'
    token=re.compile(regex).findall(x)[0]
    regex='class="singlemv.+?data="(.+?)"'
    datas=re.compile(regex).findall(x)
    
    regex='h1 class="tittv center">Watch (.+?)<'
    mtitle=re.compile(regex).findall(x)[0]
    if '(' in mtitle:
        mtitle=mtitle.split('(')[0]
    log.warning('mtitle:'+mtitle)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://m4uhd.tv',
        'Alt-Used': 'm4uhd.tv',
        'Connection': 'keep-alive',
        'Referer': url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers',
        }
    all_links=[]
    names=[]
    for items in datas:
        data = {
          'm4u': items,
          '_token': token
        }
        response = get_html('https://m4ufree.tv/ajax', headers=headers, cookies=cookies, data=data).content()
        log.warning(response)
        regex='iframe src="(.+?)"'
        m=re.compile(regex).findall(response)
        if len(response)>0:
            if 'streamm4u' in m[0]:
                all_links.append(m[0])
                names.append(urp(m[0]).netloc)
    
    url_t='https://api.themoviedb.org/3/search/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en-US&query=%s&page=1&include_adult=false&year=%s'%(mtitle,year)
    log.warning(url_t)
    html_im=get_html(url_t).json()
    id=""
    for items in html_im['results']:
        
            id=str(items['id'])
    log.warning("id::"+id)
    if len(names)==1:
        url=solve_stream4u(all_links[0])
    else:
        ret = xbmcgui.Dialog().select("Choose link", names)
        url=solve_stream4u(all_links[ret])
    '''
    if 'streamm4u' in all_links[ret]:
        url=solve_stream4u(all_links[ret])
    if 'playm4u' in all_links[ret]:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Alt-Used': 'play.playm4u.xyz',
            'Connection': 'keep-alive',
            'Referer': 'https://m4ufree.tv/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'trailers',
        }
        head=url_encode(headers)
        url=all_links[ret].split('?')[0]+"|"+head
    '''
    return 'resolveurlhttps://goplayer.top/watch/7e92259a8825d00ee171a77bb75a1151/tt9376612',id,mtitle
def play_link(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dd,heb_name,prev_name='',has_alldd='false',nextup='false',video_data_exp={},all_dd=[],start_index=0,get_sources_nextup='false',all_w={},source='',tvdb_id=''):
   global play_status,break_window,play_status_rd_ext,break_window_rd
   
   if 'Solve%20m4u' in url:
        url,id,name=solve_m4u(url,name,show_original_year)
   log.warning('heb_name2:'+heb_name)
   log.warning('url:'+url)
   if 'last play link' in description:
        dd=[]
        dd.append((name,data,original_title,id,season,episode,show_original_year,tvdb_id))
        

        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
        
        dbcur.execute("DELETE FROM nextup")
        code=(base64.b64encode(json.dumps(dd).encode("utf-8"))).decode("utf-8")
        try:
           dbcur.execute("INSERT INTO nextup Values ('%s')"%(code))
        except:
            dbcur.execute("DROP TABLE IF EXISTS nextup;")
            dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
            dbcur.execute("INSERT INTO nextup Values ('%s')"%(code))
        dbcon.commit()
   if 'youtu.be' in url:
        url=get_html(url).geturl()
   break_window=False
   break_window_rd=False
   play_status=''
   playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
   playlist.clear()
   log.warning('p_link:'+url)
   if 'www.metacritic.com' in url:
        url=resolve_meta(url)
   if 'tt' in id:
        try:
         url_t='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=imdb_id&language=%s'%(id,lang)
         html_im=get_html(url_t).json()


         if season=='0' or season==' ' or season=='%20' or season=='+':
             if len(html_im['movie_results'])>0:
                id=str(html_im['movie_results'][0]['id'])
                original_title=html_im['movie_results'][0]['original_title']
                name=html_im['movie_results'][0]['title']
                heb_name=name
                description=['movie_results'][0]['overview']
         else:
            if len(html_im['tv_results'])>0:
                id=str(html_im['tv_results'][0]['id'])
                original_title=html_im['tv_results'][0]['original_name']
                name=html_im['tv_results'][0]['name']
                heb_name=name
         
        except Exception as e:
            log.warning('error in getting tmdb:'+str(e))
            pass
   master_addon=False
   if 'Jen_link' in url:
        url=url.replace('Jen_link','')
        urls=url.split('$$$$$')
        url=urls[1]
        db_type='Jen_link'
        if 'Matser_link' in url:
            master_addon=True
            
            url=url.replace('Matser_link','')
            url='Direct_link$$$resolveurl'+decode_nom(url).replace('$$$','$$$$').replace('\n','').replace('\r','').replace('\t','').strip()
            if 'plugin://' in url:
                log.warning('url::::'+url)
                log.warning('Container.update(%s)'%url.replace('Direct_link$$$resolveurl',''))
                xbmc.executebuiltin('Container.update(%s)'%url.replace('Direct_link$$$resolveurl',''))
                s=stop_play()
                if s=='forceexit':
                    sys.exit(1)
                else:
                    return 0
                
            log.warning('Decoded:'+url)
            db_type='Matser_link'
            if season!=None and season!="%20":
              
               url2='http://api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&append_to_response=external_ids'%(id)
               try:
                    ht=get_html(url2,timeout=10).json()
                    original_title=ht['original_name']
               except:
                    pass
                    
            else:
               
               url2='http://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&append_to_response=external_ids'%(id)
               try:
                    ht=get_html(url2,timeout=10).json()
                    original_title=ht['original_title']
               except:
                    pass
        dd=[]
        dd.append((name,data,name,id,season,episode,show_original_year,db_type+urls[0]))
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
        
        dbcur.execute("DELETE FROM nextup")
        code=(base64.b64encode(json.dumps(dd).encode("utf-8"))).decode("utf-8")
        try:
           dbcur.execute("INSERT INTO nextup Values ('%s')"%(code))
        except:
            dbcur.execute("DROP TABLE IF EXISTS nextup;")
            dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup')
            dbcur.execute("INSERT INTO nextup Values ('%s')"%(code))
        dbcon.commit()
        
        dbcur.close()
        dbcon.close()
        log.warning('Saved_DB::')
   if '$$$$' in url:
        
        urls=url.split('$$$$')
        choise=[]
        count=0
        counter2=1
        for ur in urls:
            log.warning('ur:'+ur)
            
            if '(' in ur :
                
                ur_s=ur.split('(')[0]
                #ur_s='Link No. '+str(count)
                ur_p='('+ur.split('(')[1]+' '
            else:
                ur_s=ur
                #ur_s='Link No. '+str(count)
                ur_p=''
            if 'http' not in ur:
                uri ='Debrid (%s)'%str(count)
                count+=1
            else:
                uri = urp(ur_s.replace('Direct_link$$$resolveurl','')).netloc
                uri ='Link No. '+str(counter2)
                counter2+=1
            choise.append('[COLOR khaki]'+ur_p.replace('%20','')+'[/COLOR]'+uri)
            

        ret = xbmcgui.Dialog().select("Choose link", choise)
        if ret!=-1:
            
             if master_addon:
                url='Direct_link$$$resolveurl'+urls[ret]
             else:
                url=urls[ret]
                if '(' in url:
                    url=url.split('(')[0]
        else:
            s=stop_play()
            if s=='forceexit':
                sys.exit(1)
            else:
                return 0
   sub=False
   if master_addon:
        
        if 'www.you'in url and 'list'in url :#line:2751
                pl =xbmc .PlayList (xbmc .PLAYLIST_VIDEO )#line:2745
                pl .clear ()#line:2746
                url =get_all_youtube_items (name ,url.replace('Direct_link$$$resolveurl','') ,pl )#line:2753
                log.warning(url)
        elif 'www.you'in url:
            url=play_youtube(url)
        if 'google' in url  :
            url=url.replace('Direct_link$$$resolveurl','')
            dir_pat = os.path.dirname(os.path.realpath(__file__))
            account_exist=os.path.join(dir_pat,'accounts.db')
            if os.path.exists(account_exist):
                if '='in url :#line:2046
                    urlss =url .split ('=')[-1 ]#line:2047
                else :#line:2049
                   regex ='/d/(.+?)/view'#line:2050
                   m =re .compile (regex ).findall (url )#line:2051
                   if len (m )>0 :#line:2052
                     urlss =m [0 ]#line:2053
                   else :#line:2054
                     regex ='/d/(.+?)/preview'#line:2055
                     m =re .compile (regex ).findall (url )#line:2056
                     urlss =m [0 ]#line:2057
                url,sub=googledrive_resolve_new (urlss )
                log.warning('New google resolve')
                log.warning(url)
                log.warning(sub)
   log.warning('original_title::'+original_title)
   from resources.modules.general import post_trakt
   from resources.modules import real_debrid,premiumize
   from resources.modules import all_debrid
   #meta=get_more_meta(id)
   if has_alldd=='true':
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup_all_d')
        dbcur.execute("SELECT * from nextup_all_d")
        
        
        all_dd_pre = dbcur.fetchone()
        
        dbcur.close()
        dbcon.close()
        if all_dd_pre!=None:
            import ast
            all_dd=ast.literal_eval(base64.b64decode(all_dd_pre[0]).decode('utf-8'))
            log.warning('all_dd:')
            log.warning(all_dd)
            
            
   try:
        s=int(season)
        tv_movie='tv'
        
   except:
        tv_movie='movie'
   if Addon.getSetting('new_play_window')=='true':
        thread=[]

        thread.append(Thread(show_new_window,tv_movie, id, season, episode))

        thread[0].start()
   
   google_solved=False
   try:
    
    log.warning('PLAYRL:'+url)
    log.warning('o_name:'+name)
    direct=False
    if Addon.getLocalizedString(32022) in name:
        o_name=prev_name
        name=prev_name
    else:
        o_name=name
    heb_source=False
    if 'easynews' in url:
        all_lk=json.loads(url)
        stream_url=all_lk['link']
        headers=all_lk['headers']
        auth=(all_lk['cookie'])
        #log.warning(type(all_lk['cookie']))
        #x=get_html(stream_url,cookies=auth,stream=True,get_cookies=True)
        #x_2,x_cookie=x.json()
        #stream_url = down_url + quote('/%s/%s/%s%s/%s%s' % (dl_farm, dl_port, post_hash, ext, post_title, ext))
     
        headers['cookie']=(auth)

        f_lk=stream_url
        head=url_encode(headers)
        url=f_lk+"|"+head
    
    
    if '3donlinefilms' in url:
        url=resolve_3d(url)
    subs=False
    if 'HEBSOURCE$$$' in url:
        url=url.split('HEBSOURCE$$$')[1]
        subs=get_google_subs(url)
        
        heb_source=True
    if 'magnet' not in url:
        direct=True
        nextup='false'
    save_link=None
    if '[' in url and 'http' not in url and 'magnet' not in url:#mando ok
       #from resources.modules.sdarot import MyResolver
       t_path=os.path.dirname(os.path.realpath(__file__))
       save_link=url
       try:
            if Addon.getSetting("full_db")=='true':
            
                if KODI_VERSION>18:
                    dp_full.update(0, 'Please wait'+'\n'+'Level 55...'+'\n'+ '' )
                else:
                    dp_full.update(0, 'Please wait','Level 55...', '' )
            from resources.sources.sdarot import resolve_dns,get_final_video_and_cookie,get_ip_url,get_user_cookie_sratim
           
       except:
            import shutil
            d= os.path.join(t_path,'dns')
            if os.path.exists(d):
                shutil.rmtree(d)
            
            
            shutil.copytree(dns_path, d, False, None)
            
            from resources.sources.sdarot import resolve_dns,get_final_video_and_cookie,get_ip_url,get_user_cookie_sratim

       url_data=json.loads(url.replace('Direct_link$$$','').replace('%20',''))
       log.warning('Doner Test Resolve:')
       url, cookie=get_final_video_and_cookie(url_data[0], url_data[1], url_data[2], False, False)
       nextup='true'
       heb_source=True
    
    if '.xspf' in url:
        nextup='true'
        x=get_html(url).content()
        regex='<location>(.+?)</'
        url=re.compile(regex).findall(x)[0]
    if 'easynews.com' in url or 'storage.googleapis.com' in url or 'drive.google.com' in url or 'Direct_link$$$' in url:
        nextup='true'
    url=url.replace('Direct_link$$$','').replace('resolvedirect','')
    
        
    if 'resolveurl' in url or 'resolveprime' in url:
        
      
        
        start_index=0
        counter_index=0
        url=url.replace('resolveurl','').replace('resolveprime','')
        log.warning('ResolveUrl:')
        if len(all_dd)==0:
            #all_dd.append((name,url,iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,dd))
            load_resolveurl_libs()
            url=url.replace('https://dood.so','https://dood.to')
            log.warning('ResolveUrl1:')
            try:
                import resolveurl
                log.warning('Resolveurl now:'+url)
                oo_url=url
                url =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
                log.warning('ResolveD now:'+str(url))
                if not url:
                    url=oo_url
            except Exception as e:
                log.warning('Resolver error:'+str(e))
        for name,n_url,iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,dd in all_dd:
            if url==n_url.replace('Direct_link$$$','').replace('resolveurl','').replace('resolveprime',''):
                break
            start_index+=1
        log.warning('start_index:'+str(start_index))
        start_time=time.time()
        dp=None
        if Addon.getSetting('new_play_window')=='false':
            dp = xbmcgui.DialogProgress()
            if KODI_VERSION>18:
                dp.create(Addon.getLocalizedString(32085)+'\n'+ Addon.getLocalizedString(32072))
            else:
                dp.create(Addon.getLocalizedString(32085), Addon.getLocalizedString(32072), '')
        elapsed_time = time.time() - start_time
        if Addon.getSetting('new_play_window')=='false':
            if KODI_VERSION>18:
                dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32077)+'\n'+ '')
            else:
                dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32077), '')
        
        for name,url_n,iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,dd in all_dd:
            
            if counter_index>=start_index:
                
                
                if 'resolveprime' in url_n:
                    
                    try:


                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Connection': 'keep-alive',
                            'Upgrade-Insecure-Requests': '1',
                            'Pragma': 'no-cache',
                            'Cache-Control': 'no-cache',
                            'TE': 'Trailers',
                        }
                        log.warning(url_n.replace('Direct_link$$$','').replace('resolveprime','').replace('resolveurl',''))
                        
                        cookies=get_html(url_n.replace('Direct_link$$$','').replace('resolveprime','').replace('resolveurl',''),headers=headers).cookies_get_only()
                        log.warning(cookies)
                        url_n=get_html(url_n.replace('Direct_link$$$','').replace('resolveprime','').replace('resolveurl',''),headers=headers,cookies=cookies).geturl()+'resolveurl'

                        #url_n=get_html(url_n.replace('Direct_link$$$','').replace('resolveprime','').replace('resolveurl',''),headers=base_header).geturl()+'resolveurl'
                        log.warning('New url:='+url_n)
                    except Exception as e:
                        log.warning('Get_html_err:'+str(e))
                        counter_index+=1
                        continue
                url_n=url_n.replace('Direct_link$$$','').replace('resolvedirect','').replace('resolveprime','')
                
                if 'magnet' in url_n:
                    url=url_n
                    direct=False
                    skip=True
                    if Addon.getSetting('torrents')=='true' and use_debrid==False:
                        try:
                            if Addon.getSetting('torrents_s')=='0':
                                url=resolve_torrent(url_n,tv_movie,name,dp)
                            else:
                                url=resolve_torrent_torrest(url_n,tv_movie,name,dp)
                            if url=='stop':
                                
                                break_window=True
                                try:
                                    from resources.modules.torrent_resolve import _process
                                    _process.kill()
                                    
                                except Exception as e:
                                    log.warning('Error kill:'+str(e))
                                    pass
                                try:
                                    from resources.modules.torrest_api import _process
                                    _process.kill()
                                    
                                except Exception as e:
                                    log.warning('Error kill:'+str(e))
                                    pass
                               
                                _path = xbmc_tranlate_path("special://profile/addon_data/%s/cache" % Addon.getAddonInfo('id'))
                              
                                if os.path.exists(_path):
                                    counter=0
                                    while(counter<20):
                                        try:
                                            log.warning('Remove:')
                                            shutil.rmtree(_path)
                                            break
                                        except:
                                            xbmc.sleep(100)
                                            try:
                                                from resources.modules.torrest_api import _process
                                                _process.kill()
                                                
                                            except:
                                                pass
            
                                        counter+=1
                
                            o_name=name
                            if break_window:
                                
                                break
                        except Exception as e:
                            log.warning('Next torrent:'+str(e))
                            continue
                        if Addon.getSetting('new_play_window')=='false':
                            if dp.iscanceled():
                                dp.close()
                                break
                        elif break_window:
                            break
                        if not url:
                            continue
                        
                        log.warning('Play url:'+url)
                        break
                    
                if 'resolveurl' not in url_n:
                    url=url_n
                    break
               
                url_n=url_n.replace('resolveurl','')
                url_n=url_n.replace('Direct_link$$$','').replace('resolveurl','').replace('resolveprime','')
                if 'http' not in url_n:
                    url_n='https:'+url_n
                if Addon.getSetting('new_play_window')=='false':
                    if KODI_VERSION>18:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+str(counter_index)+'/'+str(len(all_dd))+'\n'+ source)
                    else:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),str(counter_index)+'/'+str(len(all_dd)), source)
                play_status=str(counter_index)+'/'+str(len(all_dd))+','+ source
                if Addon.getSetting('new_play_window')=='false':
                    if dp.iscanceled():
                            dp.close()
                            break
                   
                elif break_window:
                            break
                try:
                    log.warning('next_url:'+url_n)
                    if 'direct' in url_n:
                        log.warning('Found direct:'+url_n)
                        url_solved=url_n.replace('$$$direct','')
                    else:
                        if 'vidsrc' in url_n:
                            found,f_url=resolve_vidsrc(url_n.replace('resolveurl',''))
                        elif 'drive.google.com' in url:
                            
                            found,f_url=resolve_google(url_n.replace('resolveurl',''))
                            google_solved=True
                        elif 'wootly.ch' in url_n:
                            
                            found,f_url=solve_wootly(url_n.replace('resolveurl',''))
                        elif 'vivo.sx' in url:
                            log.warning('Original_solve:'+url)
                            
                            found,f_url=solve_vivo(url_n.replace('resolveurl',''))
                        elif 'streamhoe.online' in url:
                            found,f_url=solve_streamh(url_n.replace('resolveurl',''))
                        #elif 'mightyupload.com' in url:
                        #    found,f_url=solve_might(url_n.replace('resolveurl',''))
                        else:
                            log.warning('Vstream_solve:'+url)
                            try:
                                found,f_url=v_staream_solve(url_n)
                            except:
                                found=False
                                f_url=url_n
                        
                        if 'vidcloud.pro' not in url_n:
                            o_name=get_vstram_title(url_n,name)
                       
                        url_solved=f_url
                        if not found:
                            
                            
                            if 'primewire' in url_n:
                                log.warning('Resolving Primwire')
                                f_url=resolve_prime(url_n)
                            else:
                                try:
                                    log.warning('sss')
                                    f_url=resolve_link_others(source,url_n)
                                    log.warning('sss2')
                                except Exception as e:
                                    log.warning('Error in resolving:'+str(e))
                                    f_url=url_n
                            log.warning('URL SOLVEING')
                            
                            log.warning(url_solved)
                            if 'vidcloud9' in url_n:
                                url_solved=solve_vidcloud(url_n)
                            else:
                                
                                load_resolveurl_libs()
                                
                                import resolveurl
                                
                                url_solved =resolveurl .HostedMediaFile (url =url_n ).resolve ()#line:2687
                                if not url_solved:
                                    url_solved=url_n
                            log.warning(url_solved)
                    
                    if url_solved:
                        url=url_solved
                        
                        
                        break
                except Exception as e:
                    log.warning('Error resolve:'+str(e))
                    pass
            counter_index+=1
        if Addon.getSetting('new_play_window')=='false':
            dp.close()
    
    if 'Resolve$$$' in url:
        log.warning(url)
        rd = real_debrid.RealDebrid()
        url=url.replace('Resolve$$$','')
        url=rd.get_link(url)['download']
        
    episode=episode.replace('+',"%20")
    global break_jump,all_w_global
    break_jump=0
  
    tmdbKey = 'fb981e5ab89415bba616409d5eb5f05e'
    if len(episode)==1:
      episode_n="0"+episode
    else:
       episode_n=episode
    if len(season)==1:
      season_n="0"+season
    else:
      season_n=season
    
    
    if tv_movie=='tv':
        url_media='https://api.themoviedb.org/3/%s/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&include_image_language=ru,null&append_to_response=images,external_ids'%(tv_movie,id,lang)
           
        html_media=get_html(url_media).json()
        try:
          tvdb_id=str(html_media['external_ids']['tvdb_id'])
        except:
          tvdb_id=''
    if direct==False and use_debrid:
        if Addon.getSetting('debrid_select')=='0':
           rd = real_debrid.RealDebrid()
           play_status_rd_ext=real_debrid
           break_window_rd=real_debrid.break_window_rd
           if tv_movie=='tv' and 's%se'%season_n not in url.lower():
               
               if get_sources_nextup=='true':
                    try:
                        from sqlite3 import dbapi2 as database
                    except:
                        from pysqlite2 import dbapi2 as database
                    cacheFile=os.path.join(user_dataDir,'database.db')
                    dbcon = database.connect(cacheFile)
                    dbcur = dbcon.cursor()
                    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""data TEXT);" % 'nextup_all_d')
                    dbcur.execute("SELECT * from nextup_all_d")
                    
                    
                    all_dd_pre = dbcur.fetchone()
                    
                    dbcur.close()
                    dbcon.close()
                    if all_dd_pre!=None:
                        import ast
                        all_dd=ast.literal_eval(base64.b64decode(all_dd_pre[0]).decode('utf-8'))
                    start_index=0
                    for name,n_url,iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,dd in all_dd:
                        if url==n_url:
                            break
                        start_index+=1
               if len(all_dd)>0:
                log.warning('LEN ALLDD:'+str(len(all_dd)))
                counter_index=0
                start_time=time.time()
                if Addon.getSetting('new_play_window')=='false':
                    dp = xbmcgui.DialogProgress()
                    if KODI_VERSION>18:
                        dp.create(Addon.getLocalizedString(32085)+'\n'+ Addon.getLocalizedString(32072))
                    else:
                        dp.create(Addon.getLocalizedString(32085), Addon.getLocalizedString(32072), '')
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32077)+'\n'+ '')
                    else:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32077), '')
                else:
                    dp=None
                xxx=0
                for name,url,iconimage,fanart,description,data,id,season,episode,original_title,show_original_year,dd in all_dd:
                    if url=='open_rejected' or url=='open_filtered':
                        continue
                    if counter_index>=start_index:
                        log.warning('Trying22:')
                        log.warning(url)
                        if tv_movie=='tv' and 's%se'%season_n not in url.lower():
                            link=rd.singleMagnetToLink_season(url,tv_movie,season_n,episode_n,dp=dp)
                        else:
                            link=rd.singleMagnetToLink(url)
                        
                        o_name=name
                        log.warning('Trying:'+str(link))
                        if Addon.getSetting('new_play_window')=='false':
                            if KODI_VERSION>18:
                                dp.update(int(((xxx* 100.0)/(len(all_dd)-start_index)) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32077)+'\n'+ str(counter_index)+'/'+str(len(all_dd)-start_index))
                            else:
                                dp.update(int(((xxx* 100.0)/(len(all_dd)-start_index)) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32077), str(counter_index)+'/'+str(len(all_dd)-start_index))
                        play_status=Addon.getLocalizedString(32077)+','+ str(counter_index)+'/'+str(len(all_dd)-start_index)
                        xxx+=1
                        if Addon.getSetting('new_play_window')=='false':
                            if dp.iscanceled():
                                dp.close()
                                break
                        elif break_window:
                                break
                        log.warning(counter_index)
                        log.warning(link)
                        if link!=None:
                            if Addon.getSetting('new_play_window')=='false':
                                dp.close()
                            break
                    
                    counter_index+=1
                    
               else:
                start_time=time.time()
                dp=None
                if Addon.getSetting('new_play_window')=='false':
                    dp = xbmcgui.DialogProgress()
                    if KODI_VERSION>18:
                        dp.create("Collecting", Addon.getLocalizedString(32072))
                    else:
                        dp.create("Collecting", Addon.getLocalizedString(32072), '')
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32094)+'\n'+ '')
                    else:
                        dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32094), '')
                play_status=Addon.getLocalizedString(32094)
                link=rd.singleMagnetToLink_season(url,tv_movie,season_n,episode_n,dp=dp)
           else:
                log.warning('Play mode::one play')
                link=rd.singleMagnetToLink(url)
        elif Addon.getSetting('debrid_select')=='1':
            pr= premiumize.Premiumize()
            link=pr._single_magnet_resolve(url)
        else:
            ad=all_debrid.AllDebrid()
            link=ad.movie_magnet_to_stream(url)
    else:
        link=url
        
        if 'drive.google.com' in url and google_solved==False and 'videoplayback' not in url:
            '''
            path=xbmc_tranlate_path('special://home/addons/script.module.resolveurl/lib')
            sys.path.append( path)
            path=xbmc_tranlate_path('special://home/addons/script.module.six/lib')
            sys.path.append( path)
            import resolveurl
            link =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
            '''
            if master_addon :
                dir_path = os.path.dirname(os.path.realpath(__file__))
                f_dir=os.path.join(dir_path,'accounts.db')
    
                if not os.path.exists(f_dir):
                    load_resolveurl_libs()
                    import resolveurl
                    link =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
            else:
                if Addon.getSetting('debrid_select')=='0' and Addon.getSetting('debrid_use')=='true':
                    rd = real_debrid.RealDebrid()
                    log.warning('unrestrict:'+url)
                    link=rd.unrestrict_link(url.strip())
                    #link,q=googledrive_resolve(url)
                else:
                    
                    
                    log.warning('Loaindg libs google here:')
                    load_resolveurl_libs()
                    
                    
                    import resolveurl
                    link =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
                
                
           
    try:
        c=int(season)
        tv=True
    except:
       tv=False
       season='%20'
    
    
  
    
    video_data={}
    if season!=None and season!="%20":
       video_data['TVshowtitle']=original_title
       video_data['mediatype']='episode'
       url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
    else:
       video_data['mediatype']='movie'
       url2='http://api.themoviedb.org/3/movie/%s?api_key=%s&append_to_response=external_ids'%(id,tmdbKey)
    try:
        log.warning(url2)
        imdb_id=get_html(url2,timeout=10).json()['external_ids']['imdb_id']
    except:
        imdb_id=" "
    if Addon.getSetting("subtitles")=='true' and 'tt' in imdb_id:
        thread=[]
                
        thread.append(Thread(start_subs,original_title, imdb_id, season, episode,o_name))
            
        
        thread[0].start()
    log.warning('imdb_id:'+str(imdb_id))
    if '>>,' in o_name:
        o_name=o_name.split('>>,')[1]
    if Addon.getSetting("clean_video_title")=='true':
        if tv_movie=='tv':
            video_data['title']=original_title+' S%sE%s'%(season_n,episode_n)
        else:
            video_data['title']=original_title+' '+show_original_year
    else:
        video_data['title']=o_name
    video_data['icon']=iconimage
    video_data['original_title']=original_title
    video_data['plot']=description
    video_data['year']=show_original_year
    video_data['season']=season
    video_data['episode']=episode
    video_data['poster']=fanart
    video_data['poster3']=fanart
    video_data['fanart2']=fanart
    video_data['imdb']=imdb_id
    video_data['code']=imdb_id
    video_data['IMDBNumber']=imdb_id
    video_data['imdbnumber']=imdb_id
    video_data['imdb_id']=imdb_id
    video_data['imdb']=imdb_id
    if sub:
        video_data['mpaa']='heb'
    if Addon.getSetting('subtitles_master')=='false' and master_addon:
        video_data['mpaa']='heb'
    
    log.warning('flink:'+str(link)+' Direct:'+str(direct)+' nextup:'+str(nextup))
    log.warning('heb_name2:'+heb_name)
    if link:
        listItem = xbmcgui.ListItem(video_data['title'], path=link) 
        
        if video_data_exp!={}:
            video_data=json.loads(video_data_exp)
            #if video_data['mediatype']=='tvshow':
            #    video_data['mediatype']='episode'
        if Addon.getSetting("clean_video_title")=='true':
            if tv_movie=='tv':
                video_data['title']=original_title+' S%sE%s'%(season_n,episode_n)
            else:
                video_data['title']=original_title+' '+show_original_year
        else:
            video_data['title']=o_name
        #video_data['genre']=imdb_id
        
        if heb_source:#mando ok
            video_data[u'mpaa']=('heb')
        listItem.setInfo(type='Video', infoLabels=video_data)
        all_logo,all_n_fan,all_banner,all_clear_art,r_logo,r_art=get_extra_art(id,tv_movie,tvdb_id)
        log.warning('r_art:'+r_art)
        listItem.setArt({'clearlogo':r_logo,'clearart':r_art,'icon': iconimage, 'thumb': fanart, 'poster': iconimage,'tvshow.poster': iconimage, 'season.poster': iconimage})
        video_streaminfo = {'codec': 'h264'}
        try:
            listItem.setUniqueIDs({ 'imdb': imdb_id, 'tmdb' : id }, "imdb")
        except:
            pass
        #listItem.addStreamInfo('video', video_streaminfo)
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
           
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
        dbcon.commit()
        
        dbcur.execute("SELECT * FROM playback where name='%s' and tmdb='%s' and season='%s' and episode='%s'"%(original_title.replace("'",'%27'),id,season,episode))
        
        match_playtime = dbcur.fetchone()
        log.warning(match_playtime)
        #return 0
        res=False
        if match_playtime!=None:
            name_r,timdb_r,season_r,episode_r,playtime,totaltime,free=match_playtime
            res={}
            res['wflag']=False
            res['resumetime']=playtime
            res['totaltime']=totaltime
        
        jump_time=0
        if Addon.getSetting("trakt_access_token")!=''  and Addon.getSetting("trakt_info")=='true':
           log.warning('Playing all_w_global:')
           log.warning(all_w_global)
           if all_w_global!={}:
                all_w=all_w_global
           falback=False
           try:
            log.warning('Mark start')
            
            log.warning('All_w::')
            log.warning(all_w)
            
            if str(all_w)!='{}':
              j_aa_w=json.loads(all_w)
              if id in j_aa_w:
                res={}
                falback=True
                if 'precentage' in j_aa_w[id]:
                   res['wflag']=False
                   res['resumetime']=j_aa_w[id]['precentage']
                else:
                
                    res['wflag']=False
                    res['resumetime']=j_aa_w[id]['resume']
                    res['totaltime']=j_aa_w[id]['totaltime']
           except Exception as e:
             log.warning('Error in resume2:'+str(e))
             if falback:
                res=False
             pass
        precentage=False
        log.warning('res::'+str(res))
        resume_time=0
        if res and 'precentage' not in all_w:
            
            if float(res['resumetime'])>10 and (100*(float(res['resumetime'])/float(res['totaltime'])))<95:
                choose_time=Addon.getLocalizedString(32095)+time.strftime("%H:%M:%S", time.gmtime(float(res['resumetime'])))
                if break_window:
                    selection=0
                else:
                    selection =selection_time('Menu',choose_time)
                
                #window = selection_time('Menu',choose_time)
                #window.doModal()
                #selection = window.get_selection()
                #del window
                log.warning('selection:'+str(selection))
                if selection!=-1:
                    
                    if selection==1:
                        resume_time=0
                        jump_time=0
                        listItem.setProperty('resumetime', u'0')
                        listItem.setProperty('totaltime', res['totaltime'])
                    else:
                        resume_time=res['resumetime']
                        jump_time=res['resumetime']
                        listItem.setProperty('resumetime', res['resumetime'])
                        listItem.setProperty('totaltime', res['totaltime'])
                else:
                    break_window=True
                    s=stop_play()
                    if s=='forceexit':
                        sys.exit(1)
                    else:
                        return 0
            else:
                jump_time=0
        elif 'precentage'  in all_w:
            if float(res['resumetime'])>1 and float(res['resumetime'])<95:
                precentage=True
                choose_time=Addon.getLocalizedString(32095)+res['resumetime']+'%'
                selection =selection_time('Menu',choose_time)
               
               
                if selection!=-1:
                    
                    if selection==1:
                        resume_time=0
                        jump_time=0
                        
                    else:
                        jump_time=res['resumetime']
                        resume_time=res['resumetime']
                else:
                    s=stop_play()
                    if s=='forceexit':
                        sys.exit(1)
                    else:
                        return 0
            else:
                jump_time=0
        dbcur.close()
        dbcon.close()
        
        ids = json.dumps({u'tmdb': id, u'imdb': imdb_id, u'slug': original_title})
        xbmcgui.Window(10000).setProperty('script.trakt.ids', ids)
        playlist.add(url=link, listitem=listItem)
        
        if nextup=='true':
            log.warning('Playing:'+str(link))
            if 'plugin://' in url:
                log.warning('RunPlugin:'+str(url))
                if KODI_VERSION<19:
                    xbmc.executebuiltin('XBMC.RunPlugin(%s)'%url)
                else:
                    xbmc.executebuiltin('RunPlugin(%s)'%url)
            else:
                ok=xbmc.Player().play(playlist,listitem=listItem,windowed=False)
                ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
        else:
            
            ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        save_url=url
        if season!=None and season!="%20":
           table_name='lastlinktv'
           if save_link:
               save_url=save_link
        else:
           table_name='lastlinkmovie'
        
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%table_name)
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""icon TEXT, ""image TEXT, ""plot TEXT, ""year TEXT, ""original_title TEXT, ""season TEXT, ""episode TEXT, ""id TEXT, ""eng_name TEXT, ""show_original_year TEXT, ""heb_name TEXT , ""isr TEXT, ""type TEXT);" % 'Lastepisode')
        
        dbcon.commit()
        set_update=False
        from time import gmtime, strftime
        date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if table_name=='lastlinktv' and (len(id)>2):
            dbcur.execute("SELECT * FROM %s WHERE id = '%s' "%(table_name,id))
            match = dbcur.fetchone()
            if match!=None:
                dbcur.execute("UPDATE %s SET season='%s',episode='%s',url='%s',fanart='%s',isr='%s' WHERE id = '%s'"%(table_name,season,episode,base64.b64encode(save_url.replace('%20','').encode("utf-8")).decode("utf-8"),fanart,date_time,id))
                dbcon.commit()
                set_update=True
            else:
                dbcur.execute("DELETE FROM %s"%table_name)
              
        else:
            dbcur.execute("DELETE FROM %s"%table_name)
                 
        
        
        log.warning('heb_name::'+heb_name)
        if not set_update:
            dbcur.execute("INSERT INTO %s Values ('f_name','%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s');" %  (table_name,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '))
            dbcon.commit()
            try:
            
                try:
                   if KODI_VERSION<=18:
                        desk=description.replace("'","%27").encode('utf-8')
                   else:
                        desk=description.replace("'","%27")
                except:
                    desk=''
                dbcur.execute("UPDATE %s SET name='%s',url='%s',iconimage='%s',fanart='%s',description='%s',data='%s',season='%s',episode='%s',original_title='%s',saved_name='%s',heb_name='%s',show_original_year='%s',eng_name='%s',isr='%s',prev_name='%s',id='%s' WHERE o_name = 'f_name'"%(table_name,original_title.replace("'","%27"),base64.b64encode(save_url.encode("utf-8")).decode("utf-8") ,iconimage,fanart,desk,str(show_original_year).replace("'","%27"),season,episode,original_title.replace("'","%27"),original_title.replace("'","%27"),heb_name.replace("'","%27"),show_original_year,original_title.replace("'","%27").replace("'","%27"),date_time,original_title.replace("'","%27"),id))
                dbcon.commit()
            except Exception as e:
                log.warning('Error in Saving Last:'+str(e))
                pass
        
        if table_name=='lastlinktv':
            tv_movie='tv'
        else:
            tv_movie='movie'
        dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' and type='%s'"%(original_title.replace("'","%27"),tv_movie))
        match = dbcur.fetchone()
        
        dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' and type='%s'"%(original_title.replace("'","%27").replace(" ","%20"),tv_movie))
        match_space = dbcur.fetchone()
        if match==None and match_space!=None:
            dbcur.execute("UPDATE Lastepisode SET original_title='%s' WHERE original_title = '%s' and type='%s'"%(original_title.replace("'","%27"),original_title.replace("'","%27").replace(" ","%20"),tv_movie))
            dbcon.commit()
            dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' and type='%s'"%(original_title.replace("'","%27"),tv_movie))
            match = dbcur.fetchone()
       
        if match==None:
          try:
            dbcur.execute("INSERT INTO Lastepisode Values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');" %  (heb_name.replace("'","%27"),url.replace("'","%27"),iconimage,fanart,description.replace("'","%27"),show_original_year,original_title.replace("'","%27"),season,episode,id,original_title.replace("'","%27"),show_original_year,heb_name.replace("'","%27"),date_time,tv_movie))
          except:
            try:
                dbcur.execute("INSERT INTO Lastepisode Values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');" %  (heb_name.replace("'","%27"),url.replace("'","%27"),iconimage,fanart,description.replace("'","%27"),show_original_year,original_title.replace("'","%27"),season,episode,id,original_title.replace("'","%27"),show_original_year,heb_name.replace("'","%27"),date_time,tv_movie))
            except:
                
                dbcur.execute("INSERT INTO Lastepisode Values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');" %  (heb_name.replace("'","%27"),url.replace("'","%27"),iconimage,fanart,' ',show_original_year,original_title.replace("'","%27"),season,episode,id,original_title.replace("'","%27"),show_original_year,heb_name.replace("'","%27"),date_time,tv_movie))
          dbcon.commit()
         
        else:
          dbcur.execute("SELECT * FROM Lastepisode WHERE original_title = '%s' and type='%s' and season='%s' and episode='%s'"%(original_title.replace("'","%27"),tv_movie,season,episode))

          match = dbcur.fetchone()
          log.warning('heb_name:'+heb_name)
          if match==None:
            
            
            dbcur.execute("UPDATE Lastepisode SET season='%s',episode='%s',image='%s',heb_name='%s',isr='%s' WHERE original_title = '%s' and type='%s'"%(season,episode,fanart,heb_name.replace("'","%27"),date_time,original_title.replace("'","%27"),tv_movie))
            dbcon.commit()
                
        dbcur.close()
        dbcon.close()
        if id!='%20':
                try:
                    c=int(season)
                    tv=True
                except:
                   tv=False
        
                if season!=None and season!="%20" and tv :
                   '''
                   log.warning('tv')
                   log.warning(imdb_id)
                   url_pre='http://thetvdb.com/api/GetSeriesByRemoteID.php?imdbid=%s&language=en'%imdb_id.replace('tt','')
                   html2=get_html(url_pre).content()
                   pre_tvdb = str(html2).split('<seriesid>')
                   if len(pre_tvdb) > 1:
                        tvdb = str(pre_tvdb[1]).split('</seriesid>')
                   log.warning(tvdb)
                   '''
                   season_t, episode_t = int('%01d' % int(season)), int('%01d' % int(episode))
                   data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id,"tvdb":tvdb_id}}]}
                   if 'tvdb' in id:
                    id=''
                   try:
                       i = (post_trakt('/sync/watchlist', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id,"tvdb":tvdb_id}}]}))
                   except:
                       xbmc.sleep(1000)
                       i = (post_trakt('/sync/watchlist', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id,"tvdb":tvdb_id}}]}))
                   log.warning(data)
                else:
                   
                   i = (post_trakt('/sync/watchlist',data= {"movies": [{"ids": {"tmdb": id}}]}))
                log.warning('Trakt Resoponce:')
                log.warning(i)

        if str(id)!='0' and str(id)!='+':
            thread=[]
            
            thread.append(Thread(jump_seek,original_title,id,season,episode,jump_time,precentage,subs,tvdb_id))
                
            
            thread[0].start()
            try:
                s=int(season)
                tv_movie='tv'
                video_data['mediatype']='episode'
            except:
                tv_movie='movie'
                video_data['mediatype']='movie'
            
                
                
                
            #search_next(dd)
            log.warning('Player Done')
            log.warning('Nextup')
            if (Addon.getSetting("nextup_episode")=='true' and tv_movie=='tv') or (Addon.getSetting("nextup_movie")=='true' and tv_movie=='movie'):
                thread=[]
                    
                thread.append(Thread(search_next,dd,tv_movie,id,heb_name,playlist))
                    
                
                thread[0].start()
        if sub:
            xbmc.Player().setSubtitles(sub)
   except Exception as e:
      import linecache
      break_window=True
      exc_type, exc_obj, tb = sys.exc_info()
      f = tb.tb_frame
      lineno = tb.tb_lineno
      filename = f.f_code.co_filename
      linecache.checkcache(filename)
      line = linecache.getline(filename, lineno, f.f_globals)
      
      log.warning('ERROR IN Playing:'+str(lineno))
      log.warning('inline:'+line)
      log.warning(e)
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'inLine:'+str(lineno)+str(e))))
      try:
        dp.close()
      except:
        
        pass
      s=stop_play()
      if s=='forceexit':
            sys.exit(1)
      else:
            return 0
   
def clear_rd():
    Addon.setSetting('rd.client_id','')
    Addon.setSetting('rd.auth','')
    Addon.setSetting('rd.refresh','')
    Addon.setSetting('rd.secret','')
    xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), (Addon.getLocalizedString(32092)))))
def re_enable_rd():
    from resources.modules import real_debrid
    clear_rd()
    
    rd = real_debrid.RealDebrid()
    log.warning('Enable_Rd')
    rd.auth()
    log.warning('Enable_RdDD')
    xbmc.executebuiltin(u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'OK'))
def clear_pr():
    Addon.setSetting('premiumize.token','')
    
    xbmc.executebuiltin(u'Notification(%s,%s)' % ((Addon.getAddonInfo('name'), (Addon.getLocalizedString(32092)))))
def clear_all_d():
    Addon.setSetting('alldebrid.token','')
    
    xbmc.executebuiltin(u'Notification(%s,%s)' % ((Addon.getAddonInfo('name'), (Addon.getLocalizedString(32092)))))
def re_enable_pr():
    from resources.modules import premiumize
    pr = premiumize.Premiumize()
    pr.auth()
    xbmc.executebuiltin(u'Notification(%s,%s)' % ((Addon.getAddonInfo('name'), ('OK'))))
def re_enable_all_d():
    from resources.modules import all_debrid
    alld = all_debrid.AllDebrid()
    alld.auth()
    xbmc.executebuiltin(u'Notification(%s,%s)' % ((Addon.getAddonInfo('name'), ('OK'))))
def add_remove_trakt(name,original_title,id,season,episode):
    from resources.modules.general import post_trakt
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
        
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    
    if original_title=='add':
        if name=='tv':
         
           season_t, episode_t = int('%01d' % int(season)), int('%01d' % int(episode))
           
           i = (post_trakt('/sync/history', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id}}]}))
        else:
          
           i = (post_trakt('/sync/history',data= {"movies": [{"ids": {"tmdb": id}}]}))
    elif original_title=='remove':
        if name=='tv':
         
           season_t, episode_t = int('%01d' % int(season)), int('%01d' % int(episode))
           
           i = (post_trakt('/sync/history/remove', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id}}]}))
           from resources.modules.general import call_trakt
           result=call_trakt('sync/playback/episodes')
           log.warning(result)
           f_id=None
           for items in result:
                t_id=str(items['show']['ids']['tmdb'])
                season_t=str(items['episode']['season'])
                episode_t=str(items['episode']['number'])
                t_id=str(items['show']['ids']['tmdb'])
                if t_id=='60735':
                    log.warning('found:')
                    log.warning(season_t)
                    log.warning(episode_t)
                    log.warning(season)
                    log.warning(episode)
                if str(id)==t_id and str(season_t)==season and str(episode_t)==episode:
                    log.warning('In')
                    f_id=str(items['id'])
                    break
           if f_id:
            j=call_trakt('sync/playback/'+f_id, is_delete=True)
            log.warning('jj')
           dbcur.execute("DELETE FROM playback where tmdb='%s' and season='%s' and episode='%s';"%(id,season,episode))
           log.warning("DELETE FROM playback where tmdb='%s' and season='%s' and episode='%s';"%(id,season,episode))
        else:
         
           i = (post_trakt('/sync/history/remove',data= {"movies": [{"ids": {"tmdb": id}}]}))
           from resources.modules.general import call_trakt
           result=call_trakt('sync/playback/movies')
           f_id=None
           for items in result:
                t_id=str(items['movie']['ids']['tmdb'])   
                if str(id)==t_id:
                    f_id=str(items['id'])
                    break
           if f_id:
            j=call_trakt('sync/playback/'+f_id, is_delete=True)
            log.warning(j)
           dbcur.execute("DELETE FROM playback where tmdb='%s'"%(id))
    if 'added' in i:
       xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0], Addon.getLocalizedString(32096).encode('utf-8'))))
    elif 'deleted' in i:
       xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0], Addon.getLocalizedString(32097).encode('utf-8'))))
    else:
      xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0], 'Error'.encode('utf-8'))))
    dbcon.commit()
    dbcur.close()
    dbcon.close()
    ClearCache()
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    xbmc.executebuiltin('Container.Refresh')
def calendars():
        import datetime
        datetime_get = (datetime.datetime.utcnow() - datetime.timedelta(hours = 5))
        if KODI_VERSION<=18:
            m = "January|February|March|April|May|June|July|August|September|October|November|December".encode('utf-8').split('|')
        else:
            m = "January|February|March|April|May|June|July|August|September|October|November|December".split('|')
        try: months = [(m[0], 'January'), (m[1], 'February'), (m[2], 'March'), (m[3], 'April'), (m[4], 'May'), (m[5], 'June'), (m[6], 'July'), (m[7], 'August'), (m[8], 'September'), (m[9], 'October'), (m[10], 'November'), (m[11], 'December')]
        except: months = []
        if KODI_VERSION<=18:
            d = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday".encode('utf-8').split('|')
        else:
            d = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday".split('|')
        try: days = [(d[0], 'Monday'), (d[1], 'Tuesday'), (d[2], 'Wednesday'), (d[3], 'Thursday'), (d[4], 'Friday'), (d[5], 'Saturday'), (d[6], 'Sunday')]
        except: days = []
        list=[]
        calendar_link = 'https://api.tvmaze.com/schedule?date=%s'
        for i in range(0, 30):
            if 1:#try:
                name = (datetime_get - datetime.timedelta(days = i))
                if KODI_VERSION<=18:
                    name = ("[B]%s[/B] : %s" % (name.strftime('%A'), name.strftime('%d %B'))).encode('utf-8')
                else:
                    name = ("[B]%s[/B] : %s" % (name.strftime('%A'), name.strftime('%d %B')))
                for m in months: name = name.replace(m[1], m[0])
                for d in days: name = name.replace(d[1], d[0])
                try: name = name.encode('utf-8')
                except: pass

                url = calendar_link % (datetime_get - datetime.timedelta(days = i)).strftime('%Y-%m-%d')

                list.append({'name': name, 'url': url, 'image': 'calendar.png', 'action': 'calendar'})
            #except:
            #    pass
        
        return list
        
def c_get_tv_maze(urls,original_image):
   
   all_d=[]
   for url in urls:
    log.warning(url)
    x=get_html(url,headers=base_header).json()
    
    for items in x:
        season=str(items['season'])
        if items['number']==None:
            episode='1'
        else:
            episode=str(int(items['number']))
        
        if len(episode)==1:
          episode_n="0"+episode
        else:
           episode_n=episode
        if len(season)==1:
          season_n="0"+season
        else:
          season_n=season
        
        id=items['show']['externals']['thetvdb']
        if id==None:
            id=items['show']['externals']['imdb']
            id='imdb'+str(id)
        else:
            id='tvdb'+str(id)
            
        '''
        url2='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=tvdb_id&language=%s'%(imdb_id,lang)
        log.warning(items['show']['externals'])
        html_im=get_html(url2).json()
       
        data=html_im['tv_results']
        if len(data)==0:
            continue
        else:
            data=data[0]
        title=data['name']+' -S%sE%s - '%(season_n,episode_n)
        plot=items['airdate']+'\n'+data['overview']
        if data['poster_path']==None:
            data['poster_path']=''
        if data['backdrop_path']==None:
            data['backdrop_path']=''
        icon='https://image.tmdb.org/t/p/original/'+data['poster_path']
        fan='https://image.tmdb.org/t/p/original/'+data['backdrop_path']
        id=str(data['id'])
        original_name=data['original_name']
        eng_name=original_name
        if 'first_air_date' in data:
           year=str(data['first_air_date'].split("-")[0])
        elif 'release_date' in data:
            year=str(data['release_date'].split("-")[0])
        else:
            year='0'
        '''
        title=items['show']['name']+' -S%sE%s- %s'%(season_n,episode_n,items['name'])
        plot=items['show']['summary']
        if plot==None:
            plot=''
        plot=items['airdate']+'\n'+plot
        icon=' '
        if items['show']['image']==None:
            icon=original_image
        else:
         for it in items['show']['image']:
           icon=items['show']['image'][it]
        fan=icon
       
        original_name=items['show']['name']
        eng_name=items['show']['name']
        if 'premiered' in items:
           year=str(data['premiered'].split("-")[0])
       
        else:
            year='0'
        all_g=[]
        for it in items['show']['genres']:
            all_g.append(it)
        generes=','.join(all_g)
        
        aa=addDir3( title, 'www',15, icon,fan,plot,data=year,generes=generes,original_title=original_name,id=id,season=season,episode=episode,eng_name=eng_name,show_original_year=year,heb_name=original_name)
        all_d.append(aa)
   return all_d
def get_tv_maze(url,original_image):
    urls = [i['url'] for i in calendars()][:5]
    log.warning(urls)
    
    all_d=c_get_tv_maze(urls,original_image)
    
    #time_to_save=int(Addon.getSetting("save_time"))
    #all_d=cache.get(c_get_tv_maze, time_to_save, urls,original_image)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def play_trailer(id,tv_movie,plot):
    

    if tv_movie=='tv':
        url_t='http://api.themoviedb.org/3/tv/%s/videos?api_key=fb981e5ab89415bba616409d5eb5f05e'%id
        log.warning(url_t)
        html_t=get_html(url_t).json()
        if len(html_t['results'])==0:
            xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0], Addon.getLocalizedString(32098))))
            return 
    else:
        url_t='http://api.themoviedb.org/3/movie/%s/videos?api_key=fb981e5ab89415bba616409d5eb5f05e'%id
        log.warning(url_t)
        html_t=get_html(url_t).json()
        if len(html_t['results'])==0:
            xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0], Addon.getLocalizedString(32098))))
            return 
        if 'results' not in html_t:
            
            xbmc.executebuiltin((u'Notification(%s,%s)' % (sys.argv[0],Addon.getLocalizedString(32098))))
            sys.exit()
        
    if len(html_t['results'])>1:
        all_nm=[]
        all_lk=[]
        for items in html_t['results']:
            all_nm.append(items['name']+","+str(items['size']))
            all_lk.append(items['key'])
        
        ret = xbmcgui.Dialog().select("Choose trailer", all_nm)
        if ret!=-1:
            video_id=(all_lk[ret])
        else:
            s=stop_play()
            if s=='forceexit':
                sys.exit(1)
            else:
                return 0
    else:
        video_id=(html_t['results'][0]['key'])
    from resources.modules.youtube_ext import get_youtube5
    playback_url=''
    if video_id!=None:
      if 1:
        log.warning(video_id)
        #playback_url= get_youtube5(video_id).replace(' ','%20')
        log.warning(playback_url)
    
      
      #from pytube import YouTube
      #playback_url = YouTube('https://'+'www.youtube.com/watch?v='+video_id).streams.first().download()
         
       
        
      playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
      item = xbmcgui.ListItem(path=playback_url)

      if plot=='play_now':
        ok=xbmc.Player().play(playback_url,listitem=item,windowed=False)
      else:
      
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
def search_history(url,icon,fan):
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
   
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT,""tv_movie TEXT );" % 'search_string2')
   
    dbcon.commit()
    log.warning('URL:'+url)
    if url=='both':
        dbcur.execute("SELECT * FROM search_string2 where tv_movie='tv'")
    else:
        dbcur.execute("SELECT * FROM search_string2 where tv_movie='%s'"%url)
    match = dbcur.fetchall()
    all=[]
    type_pre='none'
    for qua,type in match:
    
        if type!=type_pre and url=='both':
           aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%type, id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
           all.append(aa)
           type_pre=type
        aa=addDir3(qua,'http://api.themoviedb.org/3/search/{0}?api_key=fb981e5ab89415bba616409d5eb5f05e&query={1}&language={2}&page=1'.format(type,qua,lang),14,BASE_LOGO+'ghost1.png','https://www.york.ac.uk/media/study/courses/postgraduate/centreforlifelonglearning/English-Building-History-banner-bought.jpg','TMDB')
        all.append(aa)
        
    if url=='both':
        dbcur.execute("SELECT * FROM search_string2 where tv_movie='movie'")
        match = dbcur.fetchall()
 
        type_pre='none'
        for qua,type in match:

            if type!=type_pre and url=='both':
               aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%type, id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
               all.append(aa)
               type_pre=type
            aa=addDir3(qua,'http://api.themoviedb.org/3/search/{0}?api_key=fb981e5ab89415bba616409d5eb5f05e&query={1}&language={2}&page=1'.format(type,qua,lang),14,BASE_LOGO+'ghost1.png','https://www.york.ac.uk/media/study/courses/postgraduate/centreforlifelonglearning/English-Building-History-banner-bought.jpg','TMDB')
            all.append(aa)
    dbcur.close()
    dbcon.close()
    aa=addNolink( '[COLOR khaki][I]---Clear %s History---[/I][/COLOR]'%url,url,148,False,fanart=fan, iconimage=icon,plot='Clear %s History'%url,dont_place=True)
    all.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))
def  last_played():
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    table_name='lastlinktv'
    
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%table_name)
    
    table_name='lastlinkmovie'
    
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%table_name)
    
    
    dbcur.execute("SELECT * FROM lastlinktv WHERE o_name='f_name'")

    match_tv = dbcur.fetchone()
    
    dbcur.execute("SELECT * FROM lastlinkmovie WHERE o_name='f_name'")

    match_movie = dbcur.fetchone()
    
    dbcon.commit()
    
    dbcur.close()
    dbcon.close()
    all=[]
    if match_tv!=None:
       aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32099), 'www',27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
       all.append(aa)
       f_name,name,url,iconimage,fanart,description,data,season,episode,original_title,saved_name,heb_name,show_original_year,eng_name,isr,prev_name,id=match_tv
       try:
           if url!=' ':
             if 'http' not  in url:
           
               url=base64.b64decode(url)
             if len(episode)==1:
              episode_n="0"+episode
             else:
               episode_n=episode
             if len(season)==1:
              season_n="0"+season
             else:
              season_n=season
             aa=addLink(original_title+' - S%sE%s'%(season_n,episode_n), url,6,False,iconimage,fanart,description,data=show_original_year,original_title=original_title,season=season,episode=episode,tmdb=id,year=show_original_year,place_control=True)
             all.append(aa)
       except  Exception as e:
         log.warning(e)
         pass
    if match_movie!=None:
       aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32100), 'www',27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
       all.append(aa)
       f_name,name,url,iconimage,fanart,description,data,season,episode,original_title,saved_name,heb_name,show_original_year,eng_name,isr,prev_name,id=match_movie
       try:
           if url!=' ':
             if 'http' not  in url:
           
               url=base64.b64decode(url)
              
             aa=addLink(original_title, url,6,False,iconimage,fanart,description,data=show_original_year,original_title=original_title,season='%20',episode='%20',tmdb=id,year=show_original_year,place_control=True)
             all.append(aa)
       except  Exception as e:
         log.warning(e)
         pass
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))
def c_get_one_trk(color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image):
          global all_data_imdb
          import _strptime
          dd=[]
          
          dd.append((color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image))
         
          data_ep=''
          dates=' '
          fanart=image
          url='https://'+'api.themoviedb.org/3/tv/%s/season/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(id,season,lang)
         
          html=get_html(url).json()
          next=''
          ep=0
          f_episode=0
          catch=0
          counter=0
          if 'episodes' in html:
              for items in html['episodes']:
                if 'air_date' in items:
                   try:
                       datea=items['air_date']+'\n'
                       
                       a=(time.strptime(items['air_date'], '%Y-%m-%d'))
                       b=time.strptime(str(time.strftime('%Y-%m-%d')), '%Y-%m-%d')
                      
                   
                       if a>b:
                         if catch==0:
                           f_episode=counter
                           
                           catch=1
                       counter=counter+1
                       
                   except:
                         ep=0
          else:
             ep=0
          episode_fixed=int(episode)-1
          try:
              try:
                plot=html['episodes'][int(episode_fixed)]['overview']
              except:
                plot=''
          
              ep=len(html['episodes'])
              try:
                  if (html['episodes'][int(episode_fixed)]['still_path'])==None:
                    fanart=image
                  else:
                    fanart='https://'+'image.tmdb.org/t/p/original/'+html['episodes'][int(episode_fixed)]['still_path']
              except:
                fanart=image
              if f_episode==0:
                f_episode=ep
              data_ep='[COLOR aqua]'+Addon.getLocalizedString(32101)+season+Addon.getLocalizedString(32102)+episode+Addon.getLocalizedString(32103) +str(f_episode)  +Addon.getLocalizedString(32104)
              try:
                  if int(episode)>1:
                    
                    prev_ep=time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)-1]['air_date'], '%Y-%m-%d'))) 
                  else:
                    prev_ep=0
              except:
                prev_ep=0

          

                      
              if int(episode)<ep:

                if (int(episode)+1)>=f_episode:
                  color_ep='magenta'
                  next_ep='[COLOR %s]'%color_ep+time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)+1]['air_date'], '%Y-%m-%d'))) +'[/COLOR]'
                else:
                  
                  next_ep=time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)+1]['air_date'], '%Y-%m-%d'))) 
              else:
                next_ep=0
              dates=((prev_ep,time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)]['air_date'], '%Y-%m-%d'))) ,next_ep))
              if int(episode)<int(f_episode):
               color='gold'
              else:
               color='white'
               h2=get_html('https://api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=en-US'%(id)).json()
               last_s_to_air=int(h2['last_episode_to_air']['season_number'])
               last_e_to_air=int(h2['last_episode_to_air']['episode_number'])
              
               if int(season)<last_s_to_air:
      
                 color='lightblue'
            
               if h2['status']=='Ended' or h2['status']=='Canceled':
                color='peru'
               
               
               if h2['next_episode_to_air']!=None:
                 
                 if 'air_date' in h2['next_episode_to_air']:
                  
                  a=(time.strptime(h2['next_episode_to_air']['air_date'], '%Y-%m-%d'))
                  next=time.strftime( "%d-%m-%Y",a)
                  
               else:
                  next=''
                 
          except Exception as e:
              import linecache,sys
              exc_type, exc_obj, tb = sys.exc_info()
              f = tb.tb_frame
              lineno = tb.tb_lineno
              log.warning('Error :'+ heb_name)
              log.warning('Error :'+ str(e) +',line no:'+str(lineno))
              plot=' '
              color='green'
              if f_episode==0:
                f_episode=ep
              data_ep='[COLOR aqua]'+Addon.getLocalizedString(32101)+season+Addon.getLocalizedString(32102)+episode+ Addon.getLocalizedString(32103) +str(f_episode)  +Addon.getLocalizedString(32104)
              dates=' '
              fanart=image
          try:
            f_name=unque(heb_name.encode('utf8'))
     
          except:
            f_name=name
          if (heb_name)=='':
            f_name=name
          if len(heb_name)<2:
            heb_name=name
          if color=='peru':
            add_p='[COLOR peru][B]%s[/B][/COLOR]'%Addon.getLocalizedString(32105)+'\n'
          else:
            add_p=''
          add_n=''
          if color=='white' and url_o=='tv' :
              if next !='':
                add_n='[COLOR tomato][I]'+Addon.getLocalizedString(32106) +next+'[/I][/COLOR]\n'
              else:
                add_n='[COLOR tomato][I]'+Addon.getLocalizedString(32106) +Addon.getLocalizedString(32107)+'[/I][/COLOR]\n'

                next='???'
          
          added_txt=' [COLOR khaki][I]%sx%s[/I][/COLOR] '%(season,episode)
          #all_data_imdb.append((color,f_name+' '+added_txt+' '+next,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx))
          return data_ep,dates,fanart,color,next,color,(f_name+' '+added_txt+' '+next),url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx
def get_one_trk(color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image):
    global all_data_imdb
    
    data_ep,dates,fanart,color,next,color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx=cache.get(c_get_one_trk,999,color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image, table='posters')
    all_data_imdb.append((color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx))
    return data_ep,dates,fanart,color,next
def get_Series_trk_data(url_o,match):
        import _strptime
        
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile_trk = os.path.join(user_dataDir, 'cache_play_trk.db')
        dbcon_trk2 = database.connect(cacheFile_trk)
        dbcur_trk2  = dbcon_trk2.cursor()
        dbcur_trk2.execute("CREATE TABLE IF NOT EXISTS %s ( ""data_ep TEXT, ""dates TEXT, ""fanart TEXT,""color TEXT,""id TEXT,""season TEXT,""episode TEXT, ""next TEXT,""plot TEXT);" % 'AllData4')
        dbcon_trk2.commit()
        dbcur_trk2.execute("DELETE FROM AllData4")

        image=' '
        for item in match:
          next=''
          name,url,icon,image,plot,year,original_title,season,episode,id,eng_name,show_original_year,heb_name,isr,tv_movie=item
          #name,id,season,episode=item
          data_ep=''
          dates=' '
          fanart=image
          url='https://'+'api.themoviedb.org/3/tv/%s/season/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(id,season,lang)
         
          html=get_html(url).json()
          if 'status_message' in html:
            if html['status_message']!='The resource you requested could not be found.':
                xbmc.sleep(10000)
                html=get_html(url).json()
            
          ep=0
          f_episode=0
          catch=0
          counter=0
          if 'episodes' in html:
              for items in html['episodes']:
                if 'air_date' in items:
                   try:
                       datea=items['air_date']+'\n'
                       
                       a=(time.strptime(items['air_date'], '%Y-%m-%d'))
                       b=time.strptime(str(time.strftime('%Y-%m-%d')), '%Y-%m-%d')
                      
                   
                       if a>b:
                         if catch==0:
                           f_episode=counter
                           
                           catch=1
                       counter=counter+1
                       
                   except:
                         ep=0
          else:
             ep=0
          episode_fixed=int(episode)-1
          try:
              try:
                plot=html['episodes'][int(episode_fixed)]['overview']
              except:
                
                if 'episodes' not in html:
                    log.warning(html)
                    
                
                log.warning(episode_fixed)
                
                plot=''
                pass
              
              if 'episodes' not in html:
                  log.warning('Series with no episodes:'+id+','+name)
                  continue
              ep=len(html['episodes'])
              try:
                  if (html['episodes'][int(episode_fixed)]['still_path'])==None:
                    fanart=image
                  else:
                    fanart='https://'+'image.tmdb.org/t/p/original/'+html['episodes'][int(episode_fixed)]['still_path']
              except:
                fanart=image
              if f_episode==0:
                f_episode=ep
              data_ep='[COLOR aqua]'+Addon.getLocalizedString(32101)+season+Addon.getLocalizedString(32102)+episode+ Addon.getLocalizedString(32103) +str(f_episode)  +Addon.getLocalizedString(32108) 
              try:
                  if int(episode)>1:
                    
                    prev_ep=time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)-1]['air_date'], '%Y-%m-%d'))) 
                  else:
                    prev_ep=0
              except:
                prev_ep=0

          

              try:
                  if int(episode)<ep:
                    
                    if (int(episode)+1)>=f_episode:
                      color_ep='magenta'
                      next_ep='[COLOR %s]'%color_ep+time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)+1]['air_date'], '%Y-%m-%d'))) +'[/COLOR]'
                    else:
                      
                      next_ep=time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)+1]['air_date'], '%Y-%m-%d'))) 
                  else:
                    next_ep=0
              except:
                next_ep=0
              try:
                  dates=((prev_ep,time.strftime( "%d-%m-%Y",(time.strptime(html['episodes'][int(episode_fixed)]['air_date'], '%Y-%m-%d'))) ,next_ep))
              except:
                dates=' '
              if int(episode)<int(f_episode):
               color='gold'
              else:
               color='white'
               h2=get_html('https://api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(id,lang)).json()
               last_s_to_air=int(h2['last_episode_to_air']['season_number'])
               last_e_to_air=int(h2['last_episode_to_air']['episode_number'])
              
               if int(season)<last_s_to_air:
        
                 color='lightblue'
               if h2['status']==Addon.getLocalizedString(32109) or h2['status']==Addon.getLocalizedString(32111):
                color='peru'
                
               if h2['next_episode_to_air']!=None:
                 if 'air_date' in h2['next_episode_to_air']:
                    a=(time.strptime(h2['next_episode_to_air']['air_date'], '%Y-%m-%d'))
                    next=time.strftime( "%d-%m-%Y",a)
               else:
                  next=''
          
          except Exception as e:
              import linecache
              exc_type, exc_obj, tb = sys.exc_info()
              f = tb.tb_frame
              lineno = tb.tb_lineno
              filename = f.f_code.co_filename
              linecache.checkcache(filename)
              line = linecache.getline(filename, lineno, f.f_globals)
              
              log.warning('ERROR IN Series Tracker:'+str(lineno))
              log.warning('inline:'+line)
              log.warning(e)
              log.warning('BAD Series Tracker')
              plot=' '
              color='green'
              if f_episode==0:
                f_episode=ep
              data_ep='[COLOR aqua]'+Addon.getLocalizedString(32101)+season+Addon.getLocalizedString(32102)+episode+ Addon.getLocalizedString(32103) +str(f_episode)  +Addon.getLocalizedString(32108)
              dates=' '
              fanart=image
          
          dbcon_trk2.execute("INSERT INTO AllData4 Values ('%s', '%s', '%s', '%s','%s', '%s', '%s','%s','%s');" % (data_ep.replace("'","%27"),json.dumps(dates),fanart.replace("'","%27"),color,id,season,episode,next,plot.replace("'","%27")))
        dbcon_trk2.commit()
        dbcon_trk2.close()
        log.warning('TRD SUCE')
        return 0
def sync_trk(removedb=False,show_msg=True):
    #tv
    from resources.modules.trakt import progress_trakt
    from resources.modules.general import post_trakt
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""icon TEXT, ""image TEXT, ""plot TEXT, ""year TEXT, ""original_title TEXT, ""season TEXT, ""episode TEXT, ""id TEXT, ""eng_name TEXT, ""show_original_year TEXT, ""heb_name TEXT , ""isr TEXT, ""type TEXT);" % 'Lastepisode')
    
    all_tv_prog=progress_trakt('users/me/watched/shows?extended=full',sync=True)
    
    if removedb:
        dbcur.execute("DELETE FROM Lastepisode")
    else:
        dbcur.execute("SELECT  * FROM Lastepisode WHERE  type='tv' ")
   
    match_tv = dbcur.fetchall()
   
    
    new_tv={}
    all_local_mv={}
    new_tv_far={}
    for item in match_tv:
      
      
      name,url,icon,image,plot,year,original_title,season,episode,id,eng_name,show_original_year,heb_name,isr,tv_movie=item
     
      all_local_mv[id]={}
      all_local_mv[id]['icon']=icon
      all_local_mv[id]['fan']=image
      all_local_mv[id]['plot']=plot
      all_local_mv[id]['year']=year
      all_local_mv[id]['original_title']=original_title
      all_local_mv[id]['title']=name
      all_local_mv[id]['season']=season
      all_local_mv[id]['episode']=episode
      all_local_mv[id]['eng_name']=eng_name
      all_local_mv[id]['heb_name']=heb_name
      
      all_local_mv[id]['type']='tv'
     
      if id not in all_tv_prog:
       
        new_tv[id]={}
        new_tv[id]['item']=(all_local_mv[id])
        
        new_tv[id]['change_reason']='New'
       
        new_tv[id]['local']=''
        new_tv[id]['trk']=''
      else:
        if season!=all_tv_prog[id]['season']:
            if id not in new_tv:
                new_tv[id]={}
                new_tv[id]['change_reason']=''
            new_tv[id]['item']=(all_tv_prog[id])
            new_tv[id]['change_reason']=new_tv[id]['change_reason']+'$$$$season'
            
            new_tv[id]['local']=season
            new_tv[id]['trk']=all_tv_prog[id]['season']
        if episode!=all_tv_prog[id]['episode']:
            if id not in new_tv:
                new_tv[id]={}
                new_tv[id]['change_reason']=''
            new_tv[id]['item']=(all_tv_prog[id])
            
            new_tv[id]['change_reason']=new_tv[id]['change_reason']+'$$$$episode'
            new_tv[id]['local']=episode
            new_tv[id]['trk']=all_tv_prog[id]['episode']
    for id in all_tv_prog:
      if id not in all_local_mv:
        new_tv_far[id]={}
        new_tv_far[id]['item']=(all_tv_prog[id])
        new_tv_far[id]['change_reason']='New'

        new_tv_far[id]['local']=''
        new_tv_far[id]['trk']=''
      else:
        if all_tv_prog[id]['season']!=all_local_mv[id]['season']:
            if id not in new_tv_far:
                new_tv_far[id]={}
                new_tv_far[id]['change_reason']=''
            new_tv_far[id]['item']=(all_local_mv[id])
            new_tv_far[id]['change_reason']=new_tv_far[id]['change_reason']+'$$$$season'
            
            new_tv_far[id]['local']=all_local_mv[id]['season']
            new_tv_far[id]['trk']=all_tv_prog[id]['season']
        if all_tv_prog[id]['episode']!=all_local_mv[id]['episode']:
            if id not in new_tv_far:
                new_tv_far[id]={}
                new_tv_far[id]['change_reason']=''
            new_tv_far[id]['item']=(all_local_mv[id])
            
            new_tv_far[id]['change_reason']=new_tv_far[id]['change_reason']+'$$$$episode'
            new_tv_far[id]['local']=all_local_mv[id]['episode']
            new_tv_far[id]['trk']=all_tv_prog[id]['episode']
    not_on_trk=[]
    not_on_local=[]
    for id in new_tv:
        if new_tv[id]['change_reason']=='New':
            not_on_trk.append(clean_name(all_local_mv[id]['original_title'],1)+' S%sE%s'%(all_local_mv[id]['season'],all_local_mv[id]['episode'])+'-'+all_local_mv[id]['year'])
    for id in new_tv_far:
        if new_tv_far[id]['change_reason']=='New':
            not_on_local.append(clean_name(all_tv_prog[id]['original_title'],1)+' S%sE%s'%(all_tv_prog[id]['season'],all_tv_prog[id]['episode'])+'-'+all_tv_prog[id]['year'])
    

            
            
    #movie
    from resources.modules.trakt import get_trk_data
    all_mv_prog=get_trk_data('users/me/watched/movies')
    
    dbcur.execute("SELECT * FROM Lastepisode WHERE  type='movie'")
    match_tv = dbcur.fetchall()


    new_mv={}
    all_local_mv={}
    new_mv_far={}
    for item in match_tv:
      
      
      name,url,icon,image,plot,year,original_title,season,episode,id,eng_name,show_original_year,heb_name,isr,tv_movie=item
     
      all_local_mv[id]={}
      all_local_mv[id]['icon']=icon
      all_local_mv[id]['fan']=image
      all_local_mv[id]['plot']=plot
      all_local_mv[id]['year']=year
      all_local_mv[id]['original_title']=original_title
      all_local_mv[id]['title']=name
      all_local_mv[id]['season']=season
      all_local_mv[id]['episode']=episode
      all_local_mv[id]['eng_name']=eng_name
      all_local_mv[id]['heb_name']=heb_name
      
      all_local_mv[id]['type']='tv'
      if id not in all_mv_prog:
        new_mv[id]={}
        new_mv[id]['item']=(all_local_mv[id])
        
        new_mv[id]['change_reason']='New'
       
        new_mv[id]['local']=''
        new_mv[id]['trk']=''
    for id in all_mv_prog:
      if id not in all_local_mv:
        new_mv_far[id]={}
        new_mv_far[id]['item']=(all_mv_prog[id])
        new_mv_far[id]['change_reason']='New'

        new_mv_far[id]['local']=''
        new_mv_far[id]['trk']=''
    not_on_trk_mv=[]
    not_on_local_mv=[]
    for id in new_mv:
        if new_mv[id]['change_reason']=='New':
            not_on_trk_mv.append(clean_name(all_local_mv[id]['original_title'],1)+'-'+all_local_mv[id]['year'])
    for id in new_mv_far:
        if new_mv_far[id]['change_reason']=='New':
            not_on_local_mv.append(clean_name(all_mv_prog[id]['original_title'],1)+'-'+all_mv_prog[id]['year'])
    msg='[COLOR yellow][I]%s[/I][/COLOR]\n[COLOR lightblue]not found on TRAKT'%Addon.getLocalizedString(32099)+'\n----------------\n'+'\n'.join(not_on_trk)+'[/COLOR]\n\n[COLOR khaki]only on TRAKT not in local db'+'\n----------------\n'+'\n'.join(not_on_local)+'[/COLOR]'
    msg=msg+'\n\n[COLOR yellow][I]%s[/I][/COLOR]\n[COLOR lightblue]not found on TRAKT'%Addon.getLocalizedString(32100)+'\n----------------\n'+'\n'.join(not_on_trk_mv)+'[/COLOR]\n\n[COLOR khaki]only on TRAKT not in local db'+'\n----------------\n'+'\n'.join(not_on_local_mv)+'[/COLOR]'
    if removedb:
        ok=True
    else:
       ok=TrkBox_help('Changes', msg)
    if ok:
        start_time=time.time()
     
        dp = xbmcgui.DialogProgress()
        if KODI_VERSION>18:
            dp.create("Syncing", Addon.getLocalizedString(32072)+'\n'+ '')
        else:
            dp.create("Syncing", Addon.getLocalizedString(32072), '')
        elapsed_time = time.time() - start_time
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+Addon.getLocalizedString(32093)+'\n'+ '')
        else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),Addon.getLocalizedString(32093), '')
        xxx=0
        for id in new_tv_far:
           if new_tv_far[id]['change_reason']=='New':
            name=new_tv_far[id]['item']['title']
            url='www'
            icon=new_tv_far[id]['item']['icon']
            image=new_tv_far[id]['item']['fan']
            plot=new_tv_far[id]['item']['plot']
            year=new_tv_far[id]['item']['year']
            original_title=new_tv_far[id]['item']['original_title']
            season=new_tv_far[id]['item']['season']
            episode=new_tv_far[id]['item']['episode']
            eng_name=new_tv_far[id]['item']['eng_name']
            show_original_year=new_tv_far[id]['item']['year']
            heb_name=new_tv_far[id]['item']['heb_name']
            isr='0'
            tv_movie='tv'
            dbcur.execute("INSERT INTO Lastepisode Values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');" %  (name.replace("'","%27"),url,icon,image,plot.replace("'","%27"),year,original_title.replace("'","%27").replace(" ","%20"),season,episode,id,eng_name.replace("'","%27"),show_original_year,heb_name.replace("'","%27"),isr,tv_movie))
            if KODI_VERSION>18:
                dp.update(int(((xxx* 100.0)/(len(new_tv_far))) ), ' Movies '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Sync DB'+'\n'+ name)
            else:
                dp.update(int(((xxx* 100.0)/(len(new_tv_far))) ), ' Movies '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Sync DB', name)
            xxx+=1
        dbcon.commit()
            
        xxx=0
        for id in new_mv_far:
           
           if new_mv_far[id]['change_reason']=='New':
            name=new_mv_far[id]['item']['title']
            url='www'
            icon=new_mv_far[id]['item']['icon']
            image=new_mv_far[id]['item']['fan']
            plot=new_mv_far[id]['item']['plot']
            year=new_mv_far[id]['item']['year']
            original_title=new_mv_far[id]['item']['original_title']
            season=new_mv_far[id]['item']['season']
            episode=new_mv_far[id]['item']['episode']
            eng_name=new_mv_far[id]['item']['eng_name']
            show_original_year=new_mv_far[id]['item']['year']
            heb_name=new_mv_far[id]['item']['heb_name']
            isr='0'
            tv_movie='movie'
            dbcur.execute("INSERT INTO Lastepisode Values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');" %  (name.replace("'","%27"),url,icon,image,plot.replace("'","%27"),year,original_title.replace("'","%27").replace(" ","%20"),season,episode,id,eng_name.replace("'","%27"),show_original_year,heb_name.replace("'","%27"),isr,tv_movie))
            if KODI_VERSION>18:
                dp.update(int(((xxx* 100.0)/(len(new_mv_far))) ), Addon.getLocalizedString(32099)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Sync DB'+'\n'+ name)
            else:
                dp.update(int(((xxx* 100.0)/(len(new_mv_far))) ), Addon.getLocalizedString(32099)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Sync DB', name)
            xxx+=1
        dbcon.commit()
        xxx=0
        for id in new_mv:
          if new_mv[id]['change_reason']=='New':
            i = (post_trakt('/sync/history',data= {"movies": [{"ids": {"tmdb": id}}]}))
            if KODI_VERSION>18:
                dp.update(int(((xxx* 100.0)/(len(new_mv))) ), Addon.getLocalizedString(32100)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Sync Trakt'+'\n'+ id)
            else:
                dp.update(int(((xxx* 100.0)/(len(new_mv))) ), Addon.getLocalizedString(32100)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Sync Trakt', id)
            xxx+=1
        xxx=0
        for id in new_tv:
          if new_tv[id]['change_reason']=='New':
            
            season=new_tv[id]['item']['season']
            episode=new_tv[id]['item']['episode']
            season_t, episode_t = int('%01d' % int(season)), int('%01d' % int(episode))
            i = (post_trakt('/sync/watchlist', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id}}]}))
            
            
            i = (post_trakt('/sync/history', data={"shows": [{"seasons": [{"episodes": [{"number": episode_t}], "number": season_t}], "ids": {"tmdb": id}}]}))
            if KODI_VERSION>18:
                dp.update(int(((xxx* 100.0)/(len(new_tv))) ), Addon.getLocalizedString(32099)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Sync Trakt'+'\n'+ id)
            else:
                dp.update(int(((xxx* 100.0)/(len(new_tv))) ), Addon.getLocalizedString(32099)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Sync Trakt',id)
            xxx+=1
        if show_msg:
            xbmc.executebuiltin('Container.Refresh')
            xbmcgui.Dialog().ok('Sync','[COLOR aqua][I] %s [/I][/COLOR]'%Addon.getLocalizedString(32112))
    else:
        dbcur.close()
        dbcon.close()
        try:
         dp.close()
        except:
            pass
        sys.exit(1)
    dbcur.close()
    dbcon.close()
    try:
     dp.close()
    except:
        pass
def check_last_tv_subs(original_title,name,season,episode,show_original_year,id):#mando ok
    global susb_data
    from resources.modules import subs
    
    
    
    if len(episode)==1:
          episode_n="0"+episode
    else:
           episode_n=episode
    if len(season)==1:
          season_n="0"+season
    else:
          season_n=season
    
    f_subs=cache.get(subs.get_links,24,'tv',original_title,name,season_n,episode_n,season,episode,show_original_year,id,check_one=True, table='posters')
    log.warning('Subs:')
    log.warning(original_title)
    log.warning(f_subs)
    if len(f_subs)>0:
        susb_data[original_title]=True
    else:
        susb_data[original_title]=False
        
    return susb_data
def c_check_next_last_tv_subs(color,original_title,name,season,episode,show_original_year,id):
       
  
    global susb_data_next
    from resources.modules import subs
    
    
    if color=='lightblue':
        season=str(int(season)+1)
        episode='1'
    if len(episode)==1:
          episode_n="0"+episode
    else:
           episode_n=episode
    if len(season)==1:
          season_n="0"+season
    else:
          season_n=season
    log.warning('Searchig for subs:')
    log.warning(season_n)
    log.warning(episode_n)
    f_subs=subs.get_links('tv',original_title,name,season_n,episode_n,season,episode,show_original_year,id,check_one=True)
   
    if len(f_subs)>0:
        susb_data_next[original_title]=True
    else:
        susb_data_next[original_title]=False
        
    return susb_data_next
def check_next_last_tv_subs(color,original_title,name,season,episode,show_original_year,id):
   global susb_data_next
   #c_check_next_last_tv_subs(color,original_title,name,season,episode,show_original_year,id)
   dd=[]
   dd.append((color,original_title,name,season,episode,show_original_year,id))
   log.warning(dd)
   susb_data_next=cache.get(c_check_next_last_tv_subs,23,color,original_title,name,season,episode,show_original_year,id, table='posters')
   if 0:#try:
  
    
    from resources.modules import subs
    
    
    if color=='lightblue':
        season=str(int(season)+1)
        episode='1'
    if len(episode)==1:
          episode_n="0"+episode
    else:
           episode_n=episode
    if len(season)==1:
          season_n="0"+season
    else:
          season_n=season
    
    f_subs=subs.get_links('tv',original_title,name,season_n,episode_n,season,episode,show_original_year,id,check_one=True)
   
    if len(f_subs)>0:
        susb_data_next[original_title]=True
    else:
        susb_data_next[original_title]=False
        
   return susb_data_next
   #except Exception as e:
   #  log.warning('Error in Subs:'+str(e))#END mando ok
def last_viewed(url_o,isr=' '):
    global all_data_imdb
    all_data_imdb=[]
    all_folders=[]
    all_f_data=[]
    global susb_data,susb_data_next
    import datetime
    all_w_trk={}
    all_tv_w={}
    all_movie_w={}
    
    if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
        all_w_trk,all_tv_w,all_movie_w=get_all_trakt_resume(url_o)
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile_trk = os.path.join(user_dataDir, 'cache_play_trk.db')
    dbcon_trk = database.connect(cacheFile_trk)
    dbcur_trk  = dbcon_trk.cursor()
    dbcur_trk.execute("CREATE TABLE IF NOT EXISTS %s ( ""data_ep TEXT, ""dates TEXT, ""fanart TEXT,""color TEXT,""id TEXT,""season TEXT,""episode TEXT, ""next TEXT,""plot TEXT);" % 'AllData4')
    
    dbcon_trk.commit()
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""icon TEXT, ""image TEXT, ""plot TEXT, ""year TEXT, ""original_title TEXT, ""season TEXT, ""episode TEXT, ""id TEXT, ""eng_name TEXT, ""show_original_year TEXT, ""heb_name TEXT , ""isr TEXT, ""type TEXT);" % 'Lastepisode')
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT,""id TEXT, ""season TEXT, ""episode TEXT);" % 'subs')#mando ok
    
    dbcon.commit()
    
    all_o_data=[]
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%'lastlinktv')
    
    dbcur.execute("SELECT * FROM lastlinktv WHERE o_name='f_name'")

    match = dbcur.fetchone()
    dbcon.commit()
    
    
    
    if match!=None:
       f_name,name,url,iconimage,fanart,description,data,season,episode,original_title,saved_name,heb_name,show_original_year,eng_name,isr,prev_name,id=match
       try:
           if url!=' ':
             if 'http' not  in url:
           
               url=base64.b64decode(url)
             dd=[]
             if url_o!='tv':
                data_ep=show_original_year
                dbcur.execute("SELECT * FROM playback")
                match_playback = dbcur.fetchall()
                all_w={}
                  
                for n,tm,s,e,p,t,f in match_playback:
                        ee=str(tm)
                        all_w[ee]={}
                        all_w[ee]['resume']=str(p)
                        all_w[ee]['totaltime']=str(t)
                
             else:
                dbcur.execute("SELECT * FROM playback where tmdb='%s' and season='%s' "%(id,str(season)))
                match_playback = dbcur.fetchall()
                
                all_w={}
            
                for n,t,s,e,p,t,f in match_playback:
                    ee=str(e)
                    all_w[ee]={}
                    all_w[ee]['resume']=str(p)
                    all_w[ee]['totaltime']=str(t)
             added_res_trakt=''
        
             if (id) in all_w_trk:
                
                if url_o=='tv':
                   
                    if season==all_w_trk[id]['season'] and episode==all_w_trk[id]['episode']:
                        added_res_trakt=all_w_trk[id]['precentage']
                else:
                    added_res_trakt=all_w_trk[id]['precentage']
             #aa=addLink('[I]%s[/I]'%Addon.getLocalizedString(32022), url,6,False,iconimage,fanart,description,data=show_original_year,original_title=original_title,season=season,episode=episode,tmdb=id,year=show_original_year,place_control=True)
             dd.append((name,show_original_year,original_title,id,season,episode,show_original_year))
             log.warning('all_w:')
             log.warning(all_w)
             all_folders.append(('[COLOR %s]'%'salmon'+ heb_name.replace('%27',"'")+' %sx%s[/COLOR]'%(season,episode), url,6, iconimage,added_res_trakt,all_w,heb_name,fanart,'',description+'last play link',original_title,id,season,episode,eng_name,'',show_original_year,'{}',json.dumps(dd)))
             
       except  Exception as e:
         log.warning('Error1:'+str(e))
         pass
    
    
    
    
    
    
    strptime = datetime.datetime.strptime
    start_time=time.time()
    if Addon.getSetting("dp")=='true':
     
         dp = xbmcgui.DialogProgress()
         if KODI_VERSION>18:
            dp.create("Collecting",Addon.getLocalizedString(32072)+'\n'+ '')
         else:
            dp.create("Collecting",Addon.getLocalizedString(32072), '')
         elapsed_time = time.time() - start_time
         if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ Addon.getLocalizedString(32093)+'\n'+  '')
         else:
            dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), Addon.getLocalizedString(32093), '')
    color='white'
    
    if url_o=='tv':
        dbcur.execute("SELECT  * FROM Lastepisode WHERE  type='tv' ")
    else:
       dbcur.execute("SELECT * FROM Lastepisode WHERE  type='movie'")
    match_tv = dbcur.fetchall()
    
    xxx=0
    all_data_imdb=[]
    thread=[]
    
    for item in match_tv:
      name,url,icon,image,plot,year,original_title,season,episode,id,eng_name,show_original_year,heb_name,isr,tv_movie=item
      
      original_title=original_title.encode('ascii', errors='ignore').decode('ascii', errors='ignore')
      
      dates=' '
      next=''
      data_ep=''
      fanart=image
      if Addon.getSetting("dp")=='true' :
        if KODI_VERSION>18:
            dp.update(int(((xxx* 100.0)/(len(match_tv))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ Addon.getLocalizedString(32093)+'\n'+  clean_name(original_title,1))
        else:
            dp.update(int(((xxx* 100.0)/(len(match_tv))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), Addon.getLocalizedString(32093),  clean_name(original_title,1))
      xxx+=1
      done_data=0
      if url_o=='tv' :
          try:
              dbcur_trk.execute("SELECT  * FROM AllData4 WHERE  id='%s' AND season='%s' AND episode='%s'"%(id,season,episode))
               
                  
              match2 = dbcur_trk.fetchone()

            
              if match2!=None:
                data_ep,dates,fanart,color,i,j,k,next,plot=match2
                dates=json.loads(dates)

                if color=='white' :
                    
                    thread.append(Thread(get_one_trk,color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image))
                    thread[len(thread)-1].setName(clean_name(original_title,1))
                    done_data=1
                    #data_ep,dates,fanart,color,next=get_one_trk(color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image)
              else:

                thread.append(Thread(get_one_trk,color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image))
                thread[len(thread)-1].setName(clean_name(original_title,1))
                done_data=1
                #data_ep,dates,fanart,color,next=get_one_trk(color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image)
          except:
            thread.append(Thread(get_one_trk,color,name,url_o,url,icon,fanart,data_ep,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image))
            thread[len(thread)-1].setName(clean_name(original_title,1))
            done_data=1
            #data_ep,dates,fanart,color,next=get_one_trk(color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,image)
      added_txt=''
      if done_data==0:
          try:
            f_name=unque(heb_name.encode('utf8'))
     
          except:
            f_name=name
          if (heb_name)=='':
            f_name=name
          if len(heb_name)<2:
            heb_name=name
          if color=='peru':
            add_p='[COLOR peru][B]%s[/B][/COLOR]'%Addon.getLocalizedString(32105)+'\n'
          else:
            add_p=''
          add_n=''
          if color=='white' and url_o=='tv' :
              if next !='':
                add_n='[COLOR tomato][I]'+Addon.getLocalizedString(32106) +next+'[/I][/COLOR]\n'
              else:
                add_n='[COLOR tomato][I]'+Addon.getLocalizedString(32106) +Addon.getLocalizedString(32107)+'[/I][/COLOR]\n'
                next='???'
          if url_o=='tv' :
            added_txt=' [COLOR khaki][I]%sx%s[/I][/COLOR] '%(season,episode)
          all_data_imdb.append((color,f_name+' '+added_txt+' '+next,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx))
      
    
    for td in thread:
        td.start()

        if Addon.getSetting("dp")=='true':
                elapsed_time = time.time() - start_time
                if KODI_VERSION>18:
                    dp.update(0, ' Starting '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ td.name+'\n'+ " ")
                else:
                    dp.update(0, ' Starting '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), td.name, " ")
        if len(thread)>38:
            xbmc.sleep(10)
        else:
            xbmc.sleep(10)
    while 1:

          still_alive=0
          all_alive=[]
          for yy in range(0,len(thread)):
            
            if  thread[yy].is_alive():
              
              still_alive=1
              all_alive.append(thread[yy].name)
          if still_alive==0:
            break
          if Addon.getSetting("dp")=='true' :
                elapsed_time = time.time() - start_time
                if KODI_VERSION>18:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ ','.join(all_alive)+'\n'+ " ")
                else:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), ','.join(all_alive), " ")
          xbmc.sleep(100)
          if Addon.getSetting("dp")=='true' :
              if dp.iscanceled():
                dp.close()
              
                break
    
    thread=[]
    if url_o=='tv':
        all_subs_db=[]
        if 1:#mando ok
            dbcur.execute("SELECT * FROM subs")
            match = dbcur.fetchall()
            
            for title,id,season,episode in match:
                if len(episode)==1:
                  episode_n="0"+episode
                else:
                   episode_n=episode
                if len(season)==1:
                  season_n="0"+season
                else:
                  season_n=season
                next_ep=str(int(episode_n)+1)
                if len(next_ep)==1:
                  next_ep_n="0"+next_ep
                else:
                  next_ep_n=next_ep
                sub_title=title.replace("%27","'")+'-'+id+'-'+season_n+'-'+episode_n
                all_subs_db.append(sub_title)
        for color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx in all_data_imdb:
            if len(episode)==1:
              episode_n="0"+episode
            else:
               episode_n=episode
            if len(season)==1:
              season_n="0"+season
            else:
              season_n=season
            next_ep=str(int(episode_n)+1)
            if len(next_ep)==1:
              next_ep_n="0"+next_ep
            else:
              next_ep_n=next_ep
            season_c=season#mando ok
            episode_c=episode

            if color=='lightblue':
                season_c=str(int(season)+1)
                
            if len(season_c)==1:
              season_c_n="0"+season_c
            else:
              season_c_n=season_c
     
            sub_title=original_title.replace("%27","'")+'-'+id+'-'+season_n+'-'+episode_n
            sub_title_next=original_title.replace("%27","'")+'-'+id+'-'+season_n+'-'+next_ep_n
            if color=='lightblue':
                        sub_title_next=original_title.replace("%27","'")+'-'+id+'-'+season_c_n+'-'+'01'

            if (color=='gold' or color=='white' or color=='lightblue')  :
                
                
                if sub_title not in all_subs_db:
                    thread.append(Thread(check_last_tv_subs,original_title,heb_name,season,episode,show_original_year,id))
                    thread[len(thread)-1].setName(eng_name+' S%sE%s'%(season,episode))
                if (color=='gold' or color=='lightblue') and sub_title_next not in all_subs_db:
                    #check_next_last_tv_subs(color,original_title,heb_name,season,str(int(episode)+1),show_original_year,id)
                    thread.append(Thread(check_next_last_tv_subs,color,original_title,heb_name,season,str(int(episode)+1),show_original_year,id))
                    season_c=season
                    episode_c=episode
                    if color=='lightblue':
                        season_c=str(int(season)+1)
                        episode_c='1'
                    else:
                        episode_c=str(int(episode_c)+1)
                    thread[len(thread)-1].setName(eng_name+' S%sE%s'%(season_c,episode_c))#End mando ok
                
            
    susb_data={}
    susb_data_next={}
    if url_o=='tv' :
        for td in thread:
            td.start()

            if Addon.getSetting("dp")=='true' :
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(0, ' Starting '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ td.name+'\n'+ " ")
                    else:
                        dp.update(0, ' Starting '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), td.name, " ")
        while 1:

              still_alive=0
              all_alive=[]
              for yy in range(0,len(thread)):
                
                if  thread[yy].is_alive():
                  
                  still_alive=1
                  all_alive.append(thread[yy].name)
              if still_alive==0:
                break
              if Addon.getSetting("dp")=='true' :#mando ok
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(0, ' %s '%Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+ ','.join(all_alive)+'\n'+ " ")
                    else:
                        dp.update(0, ' %s '%Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), ','.join(all_alive), " ")
              xbmc.sleep(100)
              if Addon.getSetting("dp")=='true' :
                  if dp.iscanceled():
                    dp.close()
                  
                    break
    all_data_imdb=sorted(all_data_imdb, key=lambda x: x[19], reverse=False)
    
    level=0
    for color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx in all_data_imdb:
        if url_o=='tv':
            if color=='gold':
                level=1
            elif color=='lightblue':
                level=2
            elif color=='green':
                level=3
            elif color=='white':
                level=4
            elif color=='peru':
                level=5
        else:
            level+=1
        all_o_data.append((color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,level))
    if url_o=='tv':
        order=False
    else:
        order=True
    #if Addon.getSetting("order_latest")=='true':
    
    all_o_data=sorted(all_o_data, key=lambda x: x[20], reverse=order)
    all_gold=[]
    all_folders_temp=[]
    for color,f_name,url,icon,fanart,add_p,data_ep,add_n,plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,dates,xxx,pos in all_o_data:
        if url_o=='tv':
            if len(episode)==1:
              episode_n="0"+episode
            else:
               episode_n=episode
            if len(season)==1:
              season_n="0"+season
            else:
              season_n=season
              
            season_next=str(int(season)+1)#mando ok
            if len(season_next)==1:
              season_next_n="0"+season_next
            else:
              season_next_n=season_next
            next_ep=str(int(episode_n)+1)
            if len(next_ep)==1:
              next_ep_n="0"+next_ep
            else:
              next_ep_n=next_ep
              
            sub_title=original_title.replace("%27","'")+'-'+id+'-'+season_n+'-'+episode_n
            if color=='lightblue':
                sub_title_next=original_title.replace("%27","'")+'-'+id+'-'+season_next_n+'-'+'01'
                
            else:
                sub_title_next=original_title.replace("%27","'")+'-'+id+'-'+season_n+'-'+next_ep_n
            
            if original_title in susb_data_next:
                
                if original_title in susb_data:
                    if susb_data[original_title]==True:
                        
                        dbcur.execute("DELETE  FROM subs WHERE name = '%s' and id= '%s' and season <> '%s' "%(original_title.replace("'","%27"),id,season_n))
                        dbcur.execute("INSERT INTO subs Values ('%s', '%s','%s','%s');" %  (original_title.replace("'","%27"),id,season_n,episode_n))
                        dbcon.commit()
                        f_name='[COLOR lightblue] | [/COLOR]'+f_name
                if susb_data_next[original_title]==True:
                    if color=='lightblue':
                        episode_n='01'
                        next_ep_n='01'
                        
                        season_n=season_next_n
                        
                    else:
                        dbcur.execute("DELETE  FROM subs WHERE name = '%s' and id= '%s' and season <> '%s' "%(original_title.replace("'","%27"),id,season_n))
                    dbcur.execute("INSERT INTO subs Values ('%s', '%s','%s','%s');" %  (original_title.replace("'","%27"),id,season_n,next_ep_n))
                    dbcon.commit()
                    f_name='[COLOR peru] < [/COLOR]'+f_name
                
            elif original_title in susb_data:
                    
                    if susb_data[original_title]==True:
                        dbcur.execute("DELETE  FROM subs WHERE name = '%s' and id= '%s' and season <> '%s'"%(original_title.replace("'","%27"),id,season_n))
                        dbcur.execute("INSERT INTO subs Values ('%s', '%s','%s','%s');" %  (original_title.replace("'","%27"),id,season_n,episode_n))
                        dbcon.commit()
                        f_name='[COLOR lightblue] | [/COLOR]'+f_name
            if sub_title in all_subs_db:
                f_name='[COLOR lightblue] | [/COLOR]'+f_name
            if sub_title_next in all_subs_db:
                f_name=f_name='[COLOR peru] < [/COLOR]'+f_name#End mando ok
        all_d=((dates))
        if color!='white' and len(all_d)>1:
          
            
            
            
            add_n='[COLOR aqua]'+Addon.getLocalizedString(32113)+all_d[1] + '[/COLOR]\n'
        all_f_data.append(('[COLOR %s]'%color+ f_name+'[/COLOR]', url,4, icon,fanart,add_p+data_ep+add_n+plot,year,original_title,id,season,episode,eng_name,show_original_year,heb_name,isr,json.dumps(dates)))
        
        plot=plot.replace('%27',"'")
        if url_o=='tv':
            mode=146
        else:
            mode=15
        dd=[]
        if url_o!='tv':
            data_ep=show_original_year
            dbcur.execute("SELECT * FROM playback")
            match_playback = dbcur.fetchall()
            all_w={}
              
            for n,tm,s,e,p,t,f in match_playback:
                    ee=str(tm)
                    all_w[ee]={}
                    all_w[ee]['resume']=str(p)
                    all_w[ee]['totaltime']=str(t)
            
        else:
            dbcur.execute("SELECT * FROM playback where tmdb='%s' and season='%s' "%(id,str(season)))
            match_playback = dbcur.fetchall()
            
            all_w={}
        
            for n,t,s,e,p,t,f in match_playback:
                ee=str(e)
                all_w[ee]={}
                all_w[ee]['resume']=str(p)
                all_w[ee]['totaltime']=str(t)
        added_res_trakt=''
        
        if (id) in all_w_trk:
            
            if url_o=='tv':
               
                if season==all_w_trk[id]['season'] and episode==all_w_trk[id]['episode']:
                    added_res_trakt=all_w_trk[id]['precentage']
            else:
                added_res_trakt=all_w_trk[id]['precentage']
        watched='no'
        
        if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
            if url_o=='movie':
                if id in all_movie_w:
                    watched='yes'
            else:
                if id in all_tv_w:
                   if season+'x'+episode in all_tv_w[id]:
              
                    watched='yes'
                
        
        dd.append((f_name,show_original_year,original_title,id,season,episode,show_original_year))
        aa=addNolink('[COLOR %s]'%color+ f_name.replace('%27',"'")+'[/COLOR]', url,mode,False, iconimage=icon,all_w_trk=added_res_trakt,all_w=all_w,heb_name=heb_name,fanart=fanart,data=data_ep,plot=add_p+data_ep+add_n+plot.replace('%27',"'"),original_title=original_title,id=id,season=season,episode=episode,eng_name=eng_name,watched=watched,show_original_year=show_original_year,dates=json.dumps(dates),dd=json.dumps(dd),dont_place=True)
        if color=='gold':
            all_gold.append((isr,'[COLOR %s]'%color+ f_name.replace('%27',"'")+'[/COLOR]', url,mode, icon,added_res_trakt,all_w,heb_name,fanart,data_ep,add_p+data_ep+add_n+plot.replace('%27',"'"),original_title,id,season,episode,eng_name,watched,show_original_year,json.dumps(dates),json.dumps(dd)))
        else:
            all_folders_temp.append(('[COLOR %s]'%color+ f_name.replace('%27',"'")+'[/COLOR]', url,mode, icon,added_res_trakt,all_w,heb_name,fanart,data_ep,add_p+data_ep+add_n+plot.replace('%27',"'"),original_title,id,season,episode,eng_name,watched,show_original_year,json.dumps(dates),json.dumps(dd)))
    all_gold=sorted(all_gold, key=lambda x: x[0], reverse=True)
    for isr,nm, url,mode, icon,added_res_trakt,all_w,heb_name,fanart,data_ep,pl,original_title,id,season,episode,eng_name,watched,show_original_year,dates,dd in all_gold:
        all_folders.append((nm, url,mode, icon,added_res_trakt,all_w,heb_name,fanart,data_ep,pl,original_title,id,season,episode,eng_name,watched,show_original_year,dates,dd))
    all_folders=all_folders+all_folders_temp
    dbcur_trk.close()
    dbcon_trk.close()
   
    dbcur.close()
    dbcon.close()
    read_data2=[]
    '''
    if len(all_folders)>0:
        if Addon.getSetting("trakt_access_token")!='' and url_o=='tv':
            aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32114), id,157,False,fanart='https://bestdroidplayer.com/wp-content/uploads/2019/06/trakt-what-is-how-use-on-kodi.png', iconimage=BASE_LOGO+'ghost1.png',plot=' ',dont_place=True)
            all_folders.append(aa)
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_folders,len(all_folders))
    '''
    if url_o=='tv' :
        read_data2.append((url_o,match_tv))
    
    log.warning('ALLDONE TRK')
    if Addon.getSetting("dp")=='true':
        dp.close()

    enc_data=(base64.b64encode(json.dumps(all_f_data).encode("utf-8"))).decode("utf-8") 
    if len(read_data2)>0:
        url_o,match=read_data2[0]
        thread=[]
        thread.append(Thread(get_Series_trk_data,url_o,match))
        import datetime
        strptime = datetime.datetime.strptime
        thread[0].start()    
    return read_data2,enc_data,all_folders,url_o
def history_old(url):
    o_url=url
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    
    
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""icon TEXT, ""image TEXT, ""plot TEXT, ""year TEXT, ""original_title TEXT, ""season TEXT, ""episode TEXT, ""id TEXT, ""eng_name TEXT, ""show_original_year TEXT, ""heb_name TEXT , ""isr TEXT, ""type TEXT);" % 'Lastepisode')
    
    dbcur.execute("SELECT * FROM Lastepisode WHERE type='%s'"%url)

    match = dbcur.fetchall()
    dbcon.commit()
    
    dbcur.close()
    dbcon.close()
    all_d=[]
    
    
    for name,url,icon,fan,plot,year,original_title,season,episode,id,eng_name,show_original_year,heb_name,isr,type in match:
        if o_url=='tv':
            if len(episode)==1:
              episode_n="0"+episode
            else:
               episode_n=episode
            if len(season)==1:
              season_n="0"+season
            else:
              season_n=season
            added='- S%sE%s'%(season_n,episode_n)
        else:
            added=''
        aa=addDir3( name+added, 'history',15, icon,fan,plot,data=year,original_title=original_title,id=id,season=season,episode=episode,eng_name=eng_name,show_original_year=year,heb_name=original_title)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def s_tracker(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dates,heb_name):
    menu=[]
    dp = xbmcgui . DialogProgress ( )
    if KODI_VERSION>18:
        dp.create('Series Traker'+'\n'+ 'Loading'+'\n'+  '','')
    else:
        dp.create('Series Traker','Loading', '','')
    if KODI_VERSION>18:
        dp.update(0, 'Series Traker'+'\n'+ 'Loading'+'\n'+  '' )
    else:
        dp.update(0, 'Series Traker','Loading',  '' )
    menu = Chose_ep(sys.argv[0], original_title,name,id,season,episode,dates,original_title,dp)
    menu.doModal()
    ret = menu.params
    fanart=menu.return_fanart
    description=menu.return_plot
    log.warning('fanart2::'+description)
    next_season=menu.nextseason
    del menu
    dp.close()
    log.warning('ret:'+str(ret))
    if ret!=-1:
        all_d=json.loads(unque(dates))
        log.warning('all_d:'+str(all_d))
        if len(all_d)<2:
            all_d=[1,1,1]
        if all_d[2]==0 or all_d[0]==0:
          if all_d[2]==0:
            prev_index=1
          elif all_d[0]==0:
            prev_index=2
        else:
          prev_index=2
        log.warning('prev_index:'+str(prev_index))
        log.warning(ret)
        if 'next' in ret.lower() and next_season:
              if next_season:
                season=str(int(season)+1)
                episode='1'
        elif 'next' in ret.lower():
          
          episode=str(int(episode)+1)
          from resources.modules.tmdb import get_episode_data
          name,plot,image,season,episode=get_episode_data(id,season,episode)
          o_plot='%s %s %s %s \n'%(Addon.getLocalizedString(32101),season,Addon.getLocalizedString(32102),episode)+plot
        elif 'previous' in ret.lower():
          
          if int(episode)>1:
            
            episode=str(int(episode)-1)
            from resources.modules.tmdb import get_episode_data
            name,plot,image,season,episode=get_episode_data(id,season,episode)
            o_plot='%s %s %s %s \n'%(Addon.getLocalizedString(32101),season,Addon.getLocalizedString(32102),episode)+plot
        elif 'episodes' in ret:
            
            
            xbmc.executebuiltin(('Container.update("%s?name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&data=%s&original_title=%s&id=%s&season=%s&tmdbid=%s&show_original_year=%s&heb_name=%s&isr=%s&mode=19",return)'%(sys.argv[0],que(name),que(url),iconimage,fanart,que(description),show_original_year,que(original_title),id,season,id,show_original_year,que(heb_name),'0')))
            
            return 'ok',[] 
          
        elif 'selection' in ret:
            
            xbmc.executebuiltin(('Container.update("%s?name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&data=%s&original_title=%s&id=%s&season=%s&tmdbid=%s&show_original_year=%s&heb_name=%s&isr=%s&mode=16"),return'%(sys.argv[0],que(name),que(url),iconimage,fanart,que(description),show_original_year,que(original_title),id,season,id,show_original_year,que(heb_name),'0')))
            
            return 'ok',[]
        xbmc.executebuiltin(('RunPlugin("%s?name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&data=%s&original_title=%s&id=%s&season=%s&episode=%s&tmdbid=%s&show_original_year=%s&heb_name=%s&isr=%s&mode=15",return)'%(sys.argv[0],que(name),que(url),iconimage,fanart,que(description),show_original_year,que(original_title),id,season,episode,id,show_original_year,que(heb_name),'0')))
        sys.exit(1)
    else:
        sys.exit(1)
def clear_trakt():
    from resources.modules.general import reset_trakt
    reset_trakt()
def clear_search(url):
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    if url=='both':
        dbcur.execute("DELETE FROM search_string2 ;" )
        
    else:
      dbcur.execute("DELETE FROM search_string2 where tv_movie='%s';" % url)
   
    dbcon.commit()
    dbcur.close()
    dbcon.close()
    xbmc.executebuiltin((u'Notification(%s,%s)' % ('History', 'Cleared')))
    xbmc.executebuiltin('Container.Refresh')
def get_html_data(url):
    
    html=get_html(url).json()
    return html
def was_i():
    
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    addNolink('[COLOR red][I][B]%s[/B][/I][/COLOR]'%Addon.getLocalizedString(32115),'www',162,False,iconimage='https://keepingitclean.ca/images/social/keep-it-clean-social-sharing.jpg',fanart='https://the-clean-show.us.messefrankfurt.com/content/dam/messefrankfurt-usa/the-clean-show/2021/images/kv/Cleanshow%20websideheader_tropfen_2560x1440px_01.jpg')
    dbcur.execute("SELECT * FROM playback")
    dbcon.commit()
    match = dbcur.fetchall()
    if Addon.getSetting("dp")=='true':
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create(Addon.getLocalizedString(32072),Addon.getLocalizedString(32093)+'\n'+  ''+'\n'+ '')
        else:
            dp.create(Addon.getLocalizedString(32072),Addon.getLocalizedString(32093),  '','')
        if KODI_VERSION>18:
            dp.update(0, Addon.getLocalizedString(32115)+'\n'+ Addon.getLocalizedString(32093)+'\n'+  '' )
        else:
            dp.update(0, Addon.getLocalizedString(32115), Addon.getLocalizedString(32093),  '' )
    zzz=0
    tmdbKey='fb981e5ab89415bba616409d5eb5f05e'
    all_d=[]
    for name,tmdb,season,episode,playtime,totaltime,free in match:
      
      if float(totaltime)==0:
        continue
      if (int((float(playtime)*100)/float(totaltime)))<95:
        try:
        
            a=int(tmdb)
            
        except:
            if 'tt' in free:
             url='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=imdb_id&language=%s'%(free,lang)
             html_im=get_html(url).json()
             log.warning(free)
             log.warning(html_im)
             
             if season=='0':
                 if len(html_im['movie_results'])>0:
                    tmdb=str(html_im['movie_results'][0]['id'])
             else:
                if len(html_im['tv_results'])>0:
                    tmdb=str(html_im['tv_results'][0]['id'])
             try:
        
                a=int(tmdb)
                
             except:
                continue
            else:
                continue
        
        if season!='0' and season!='' and season!='%20':
          url_t='http://api.themoviedb.org/3/tv/%s/season/%s/episode/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=external_ids'%(tmdb,season,episode,lang)
          html_t=cache.get(get_html_data,9999,url_t, table='posters')
          if 'status_code' in html_t:
            continue
          if 'still_path' in html_t:
            if html_t['still_path']==None:
                html_t['still_path']=''
          else:
            html_t['still_path']=''
          fan='https://'+'image.tmdb.org/t/p/original/'+html_t['still_path']
          
          plot= '[COLOR yellow] %s '%str(int((float(playtime)*100)/float(totaltime)))+'%[/COLOR]\n'+html_t['overview']
          url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&language=%s&append_to_response=external_ids'%(tmdb,tmdbKey,lang)
          html=cache.get(get_html_data,9999,url2, table='posters')
          if 'poster_path' in html:
              if html['poster_path']==None:
                html['poster_path']=''
          else:
            html['poster_path']=''
          icon='https://'+'image.tmdb.org/t/p/original/'+html['poster_path']
          new_name=html['name']+ ' S%sE%s '%(season,episode)
          url='www'
          if 'air_date' in html_t:
           if html_t['air_date']!=None:
             
             year=str(html_t['air_date'].split("-")[0])
           else:
            year='0'
          else:
            year='0'
          if 'first_air_date' in html:
           if html['first_air_date']!=None:
             
             data=str(html['first_air_date'].split("-")[0])
           else:
            data='0'
          else:
            data='0'
          original_name=html['original_name']
          rating=html['vote_average']
          heb_name=html['name']
          isr='0'
          genres_list=[]
          if 'genres' in html:
            for g in html['genres']:
                  genres_list.append(g['name'])
            
            try:genere = u' / '.join(genres_list)
            except:genere=''
          trailer = "%s?mode=25&url=www&id=%s&tv_movie=%s" % (sys.argv[0],tmdb,'tv')
          
          all_d.append(addDir3(new_name,url,15,icon,fan,plot,data=year,original_title=original_name,id=tmdb,rating=rating,heb_name=heb_name,show_original_year=data,isr=isr,generes=genere,trailer=trailer,season=season,episode=episode,hist='true'))
        
        else:
          url_t='http://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(tmdb,lang)
          
          
          log.warning(url_t)
          html=cache.get(get_html_data,9999,url_t, table='poster')
          if 'status_code' in html:
            continue
          if 'backdrop_path' in html:
              if html['backdrop_path']==None:
                html['backdrop_path']=''
          else:
            html['backdrop_path']=''
          fan='https://'+'image.tmdb.org/t/p/original/'+html['backdrop_path']
          
          plot= '[COLOR yellow] %s '%str(int((float(playtime)*100)/float(totaltime)))+'%[/COLOR]\n'+html['overview']
          if 'poster_path' in html:
              if html['poster_path']==None:
                html['poster_path']=''
          else:
            html['poster_path']=''
          icon='https://'+'image.tmdb.org/t/p/original/'+html['poster_path']
          new_name=html['title']
          url='www'
          if 'release_date' in html:
           if html['release_date']!=None:
             
             year=str(html['release_date'].split("-")[0])
           else:
            year='0'
          else:
            year='0'
          original_title=html['original_title']
          rating=html['vote_average']
          heb_name=html['title']
          isr='0'
          genres_list=[]
          if 'genres' in html:
            for g in html['genres']:
                  genres_list.append(g['name'])
            
            try:genere = u' / '.join(genres_list)
            except:genere=''
          trailer = "%s?mode=25&url=www&id=%s&tv_movie=%s" % (sys.argv[0],tmdb,'tv')
          all_d.append(addDir3(new_name,url,15,icon,fan,plot,episode=' ',season=' ',data=year,original_title=original_title,id=tmdb,rating=rating,heb_name=heb_name,show_original_year=year,isr=isr,generes=genere,trailer=trailer,hist='true'))
        if Addon.getSetting("dp")=='true':
            if KODI_VERSION>18:
                dp.update(int(((zzz* 100.0)/(len(match))) ), Addon.getLocalizedString(32072)+'\n'+ Addon.getLocalizedString(32116)+'\n'+  new_name )
            else:
                dp.update(int(((zzz* 100.0)/(len(match))) ), Addon.getLocalizedString(32072),Addon.getLocalizedString(32116),  new_name )
            zzz+=1
            if dp.iscanceled():
               dp.close()
               break
    if Addon.getSetting("dp")=='true':
        dp.close()
    dbcur.close()
    dbcon.close()
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def remove_was_i(name,id,season,episode):
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("DELETE  FROM playback   where tmdb='%s' and season='%s' and episode='%s'"%(id,str(season).replace('%20','0').replace(' ','0'),str(episode).replace('%20','0').replace(' ','0')))
        log.warning(' Remove DATA')
        log.warning("SELECT * FROM playback where tmdb='%s' and season='%s' and episode='%s'"%(id,str(season).replace('%20','0').replace(' ','0'),str(episode).replace('%20','0').replace(' ','0')))
        dbcon.commit()
        xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), Addon.getLocalizedString(32117).decode('utf8')+name)).encode('utf-8'))
        xbmc.executebuiltin('Container.Refresh')
        dbcur.close()
        dbcon.close()
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 15...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 15...', '' )
def clear_was_i():
    ok=xbmcgui.Dialog().yesno((Addon.getLocalizedString(32118)),(Addon.getLocalizedString(32119)))
    if ok:
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("DELETE FROM playback")
        dbcon.commit()
        dbcur.close()
        dbcon.close()

        xbmc.executebuiltin('Container.Refresh')
def remove_from_trace(name,original_title,id,season,episode):
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    #dbcur.execute("select id from Lastepisode WHERE original_title = '%s'"%(original_title))

    #dbcon.commit()
    #id_new = dbcur.fetchone()[0]
    log.warning('Remove trace')
    if id=='0':
      ok=xbmcgui.Dialog().yesno((Addon.getLocalizedString(32120)),(Addon.getLocalizedString(32121)+name+Addon.getLocalizedString(32122)))
    else:
      ok=xbmcgui.Dialog().yesno((Addon.getLocalizedString(32123)),('Unwatched '+name+" ?"))
    if ok:
      if id=='0':
        
        dbcur.execute("DELETE  FROM Lastepisode WHERE original_title = '%s' or original_title = '%s'"%(original_title.replace(' ','%20').replace("'","%27"),original_title.replace('%20',' ').replace("'","%27")))
        
        dbcon.commit()
      else:
      
        if len(episode)==0:
          episode='%20'
        if len(season)==0:
          season='%20'
        episode=episode.replace(" ","%20")
        season=season.replace(" ","%20")
        #dbcur.execute("DELETE  FROM  AllData WHERE original_title = '%s'  AND season='%s' AND episode = '%s'"%(original_title,season.replace(" ","%20"),episode.replace(" ","%20")))
        dbcur.execute("DELETE  FROM  Lastepisode WHERE id = '%s' "%(id))
        
        dbcon.commit()
      dbcur.close()
      dbcon.close()
      ClearCache()
      xbmc.executebuiltin('Container.Refresh')
      
def trakt_world():
    all=[]
    aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32124), id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
    all.append(aa)
    
    
    
    aa=addDir3(Addon.getLocalizedString(32125),'movies/trending?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32126),'movies/popular?limit=40&page=1$$$noaut',166,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    aa=addDir3(Addon.getLocalizedString(32127),'movies/played/%s?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32128),'movies/watched/%s?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32129),'movies/collected/%s?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32130),'movies/anticipated?limit=40&page=1$$$noaut',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32131),'movies/boxoffice?limit=40&page=1$$$noaut',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Movies')
    all.append(aa)
    
    aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32025), id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
    all.append(aa)
    aa=addDir3(Addon.getLocalizedString(32132),'shows/trending?limit=40&page=1$$$noaut',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32133),'shows/popular?limit=40&page=1$$$noaut',166,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32134),'shows/played/%s?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32135),'shows/collected/%s?limit=40&page=1',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32136),'shows/anticipated?limit=40&page=1$$$noaut',117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    import datetime
    datetime_get = (datetime.datetime.utcnow() - datetime.timedelta(days = 7))

    log.warning(datetime_get.strftime('%Y-%m-%d'))
    f_data=datetime_get.strftime('%Y-%m-%d')
    
    
    aa=addDir3(Addon.getLocalizedString(32307),'shows/updates/%s?limit=40&page=1$$$noaut'%f_data,117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    datetime_get = (datetime.datetime.utcnow() - datetime.timedelta(days = 30))

    log.warning(datetime_get.strftime('%Y-%m-%d'))
    f_data=datetime_get.strftime('%Y-%m-%d')
    
    
    aa=addDir3(Addon.getLocalizedString(32308),'shows/updates/%s?limit=40&page=1$$$noaut'%f_data,117,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32137), id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
    all.append(aa)
    aa=addDir3(Addon.getLocalizedString(32138),'lists/trending',119,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32139),'lists/popular',119,BASE_LOGO+'ghost1.png','https://ia802503.us.archive.org/28/items/icon_20220511/icon.png','Tv')
    all.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))

        
def set_view_type(pre_mode):
    log.warning('saved_mode:'+str(pre_mode))
    window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    preserve_viewid = window.getFocusId()
    log.warning('preserve_viewid:'+str(preserve_viewid))
    view_type=xbmc.getInfoLabel('Container.Viewmode' )
    listlabel = xbmc.getInfoLabel("ListItem.Tag")
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s (""mode TEXT,""name TEXT, ""id TEXT, ""type TEXT, ""free TEXT,""free2 TEXT);"%'views')
    
    #ok=xbmcgui.Dialog().yesno((Addon.getLocalizedString(32140)),(Addon.getLocalizedString(32141)))
    if 1:
        dbcur.execute("SELECT * FROM views  where mode='%s'"%str(pre_mode))

        match = dbcur.fetchall()
       
        if len(match)>0:
            dbcur.execute("UPDATE views SET name='%s',id='%s' where mode='%s'"%(view_type,str(preserve_viewid),str(pre_mode)))
        else:
            dbcur.execute("INSERT INTO views Values ('%s','%s','%s','%s','%s','%s')"%(str(pre_mode),view_type,str(preserve_viewid),' ','global',' '))
        dbcon.commit()
        a= str('Updated to '+(view_type))
        xbmcgui.Dialog().ok('Ok',a)
    else:
        dbcur.execute("DELETE  FROM views  where free='global'")
        view_mode_id='List'
        #xbmc.executebuiltin('Container.SetViewMode(%d)' % view_mode_id)
        all_types=[Addon.getAddonInfo('name')+' default','files', 'movies', 'tvshows', 'episodes']
        ret = xbmcgui.Dialog().select("Choose Type", all_types)
        if ret!=-1:
            selected_view=all_types[ret]
        else:
            selected_view='Defualt'

        
        
        dbcur.execute("SELECT * FROM views")

        match = dbcur.fetchall()
        dbcon.commit()
        all_modes=[]
        for mode,name,id,type,free1,free2 in match:
            all_modes.append(mode)
        
        if pre_mode in all_modes:
            dbcur.execute("UPDATE views SET name='%s',id='%s',type='%s' WHERE mode = '%s'"%(view_type,str(preserve_viewid),selected_view,str(pre_mode)))
        else:
            dbcur.execute("INSERT INTO views Values ('%s','%s','%s','%s','%s','%s')"%(str(pre_mode),view_type,str(preserve_viewid),selected_view,' ',' '))
        dbcon.commit()
        log.warning(Addon.getLocalizedString(32142)+(view_type)+', '+selected_view)
        a= str(Addon.getLocalizedString(32142)+(view_type)+', '+selected_view)
        xbmcgui.Dialog().ok('Ok',a)
   
    dbcur.close()
    dbcon.close()
def rd_history_torrents():
    from resources.modules import real_debrid
    rd = real_debrid.RealDebrid()
    items=rd.list_torrents()
    
    items = [i for i in items if i['status'] == 'downloaded']
    log.warning(json.dumps(items))
    addNolink( '[COLOR blue][I]---%s!---[/I][/COLOR]'%Addon.getLocalizedString(32143), id,27,False,fanart=' ', iconimage=' ',plot=' ')
    
    all=[]
    all_links=[]
    for i in items:
        i['name'] = i['filename']
       
          
          
        aa=addLink(i['name'], 'Direct$$$$'+i['id'],170,False,BASE_LOGO+'rd.png','https://sfilev2.f-static.com/image/users/350976/ftp/my_files/sop-resize-800-36aa0a0160a3eeaaa92d076e1f914735.jpg?sopC=1494244549658','Rd',tmdb=i['id'],place_control=True)
        
        all.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))
def rd_history(url):
    from resources.modules import real_debrid
    o_url=url
    rd = real_debrid.RealDebrid()
    all_hist=rd.get_history(url)
   
    all=[]
    all_data={}
    all_full_data={}
    addNolink( '[COLOR blue][I]---%s!---[/I][/COLOR]'%Addon.getLocalizedString(32143), ' ',27,False,fanart=' ', iconimage=' ',plot=' ')
    
    for items in all_hist:
        
        if items['mimeType']!=None and 'video' in items['mimeType']:
            from resources.modules import PTN
        
            info=(PTN.parse(items['filename']))
            show_original_year='0'
            season='%20'
            episode='%20'
            if 'title' in info:
                original_title=info['title']
            else:
                original_title=items['filename']
            if 'year' in info:
                show_original_year=info['year']
            if 'season' in info:
                season=str(info['season'])
            if 'episode' in info:
                episode=str(info['episode'])
            if season!='%20' and episode!='%20':
                if len(episode)==1:
                  episode_n="0"+episode
                else:
                   episode_n=episode
                if len(season)==1:
                  season_n="0"+season
                else:
                  season_n=season
                nm=original_title+' - S%sE%s'%(season_n,episode_n)
            else:
                nm=original_title
            id=items['id']
            if nm.lower() not in all_data:
                all_data[nm.lower()]=[]
                all_full_data[nm.lower()]=[]
            if items['download'] not in all_data[nm.lower()]:
               all_data[nm.lower()].append(items['download'])
               all_full_data[nm.lower()].append((show_original_year,items['filename'],season,episode,id))
    
    for items in all_full_data:
      if len(items)>2:
       
        nm=items
        season=all_full_data[items][0][2]
        episode=all_full_data[items][0][3]
        show_original_year=all_full_data[items][0][0]
        name=all_full_data[items][0][1]
        id=all_full_data[items][0][4]
        aa=addLink(nm, json.dumps(all_data[items]),170,False,' ',' ',' ',tmdb=id,data=show_original_year,original_title=name,season=season,episode=episode,year=show_original_year,place_control=True)
        all.append(aa)
        
    aa=addDir3('[COLOR aqua][I]%s[/I][/COLOR]'%Addon.getLocalizedString(32144),str(int(o_url)+1),168,BASE_LOGO+'rd.png','https://sfilev2.f-static.com/image/users/350976/ftp/my_files/sop-resize-800-36aa0a0160a3eeaaa92d076e1f914735.jpg?sopC=1494244549658','Rd')
    all.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))

def remove_rd_history(name,id):
    from resources.modules import real_debrid
    ok=xbmcgui.Dialog().yesno(("Remove"),('%s %s %s'%(Addon.getLocalizedString(32146),name,Addon.getLocalizedString(32147))))
    if ok:
        rd = real_debrid.RealDebrid()
        rd.remove_history(id)
        rd.deleteTorrent(id)
        xbmc.executebuiltin('Container.Refresh')
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
def server_test():
    original_title='rampage'
    data='2018'
    id='427641'
    season='%20'
    episode='%20'
    show_original_year='2018'
    f_str=['[B][I]Movies[/I][/B]']
    source_dir = os.path.join(addonPath, 'resources', 'sources')
    sys.path.append( source_dir)
    onlyfiles = [f for f in listdir(source_dir) if (isfile(join(source_dir, f)) and f.endswith('.py'))]
    all_m_sources=[]
    all_t_sources=[]
    for items in onlyfiles:
        if items.endswith('.py') and items!='__init__.py':
            impmodule = __import__(items.replace('.py',''))

            if 'tv' in impmodule.type:
                all_t_sources.append(items.replace('.py',''))
            if 'movie' in impmodule.type:
                all_m_sources.append(items.replace('.py',''))
    all_types=['All']+onlyfiles
    ret = xbmcgui.Dialog().select("Choose Type", all_types)
    if ret!=-1:
        selected_scrapers=all_types[ret].replace('.py','')
    else:
        return 0
    if Addon.getSetting('one_by_one')=='true':
        for items in onlyfiles:
            log.warning('Checking:'+items)
            match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= c_get_sources( original_title,data,original_title,id,season,episode,show_original_year,heb_name,True,items.replace('.py',''),server_test=True)
            log.warning('Done Checking:'+items)
    else:
        match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= c_get_sources( original_title,data,original_title,id,season,episode,show_original_year,heb_name,True,selected_scrapers,server_test=True)


    for items in server_check:
        if items not in all_m_sources:
            continue
        color='red'
        l_count='0'
        if 'links_count' in server_check[items]:
            l_count=server_check[items]['links_count']
            if int(l_count)>0:
                color='lightgreen'
            
       
            
        if 'done_time' in server_check[items]:
            d_time=server_check[items]['done_time']
        else:
            d_time='expired'
        f_str.append('[COLOR %s]'%color + items+': Links:'+l_count+', time:'+d_time+'[/COLOR]')
    all_addLink=[]
    for items in match_a:
            for name,lk,data,quality in match_a[items]['links']:
                aa=addLink(str(quality)+'|'+str(data)+'|'+name, lk,6,False,'','',str(data),place_control=True)
                all_addLink.append(aa)
    f_str.append('[B][I]Tv[/I][/B]')
    original_title='the flash'
    data='2014'
    id='60735'
    season='6'
    episode='1'
    show_original_year='2014'
    match_a,all_ok,once,tv_movie,po_watching,l_full_stats,statistics,server_check= c_get_sources( original_title,data,original_title,id,season,episode,show_original_year,heb_name,True,selected_scrapers,server_test=True)
    for items in server_check:
        if items not in all_t_sources:
            continue
        color='red'
        l_count='0'
        if 'links_count' in server_check[items]:
            l_count=server_check[items]['links_count']
            if int(l_count)>0:
                color='lightgreen'
            
        if 'done_time' in server_check[items]:
            d_time=server_check[items]['done_time']
        else:
            d_time='expired'
        f_str.append('[COLOR %s]'%color + items+': Links:'+l_count+', time:'+d_time+'[/COLOR]')
    for items in match_a:
            for name,lk,data,quality in match_a[items]['links']:
                aa=addLink(str(quality)+'|'+str(data)+'|'+name, lk,6,False,'','',str(data),place_control=True)
                all_addLink.append(aa)
    if ret==0:
        file = open(os.path.join(user_dataDir,'results.txt'), 'w') 
             
        file.write('\n'.join(f_str))
        file.close()
    if len(all_addLink)>0:
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_addLink,len(all_addLink))
    showText('Results', '\n'.join(f_str))
def en_dis_scrapers(name,url):
    source_dir = os.path.join(addonPath, 'resources', 'sources')
    onlyfiles = [f for f in listdir(source_dir) if (isfile(join(source_dir, f)) and f.endswith('.py'))]
    if name=='enable':
        change='true'
    else:
        change='false'
    added=''
    if url=='tv':
        added='_tv'
    for items in onlyfiles:
            
            Addon.setSetting(items.replace('.py','')+added,change)
    Addon.openSettings()
    #xbmc.executebuiltin(u'Notification(%s,%s)' % ('Ok', 'All Done'))
def classic_movies(url):
    
    x=get_html('http://pizzaflix.videoess.com/webservice_v2.php?action=videos&page=%s&NA=US&limit=100&cat=0'%url,headers=base_header).json()
    all=[]
    for items in x['data']:
        if 'poster' in items:
            icn=items['poster']
        else:
            icn='https:'+items['yt_thumb']
        aa=addLink(items['video_title'], 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % items['yt_id'],175,False,icn,'https:'+items['yt_thumb'],items['description'].replace('<br />','\n'),place_control=True)
        all.append(aa)
       
   
    aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]',str(int(url)+1),174,BASE_LOGO+'ghost1.png','https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/next.png','Next page')
    all.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))

def westwern_movies(url):
    
    if url=='0':
        url=''
    x=get_html('https://api.appmaker.pk/youtube/v3/playlistItems?part=snippet,id&fields=nextPageToken,pageInfo(totalResults),items(snippet(title,thumbnails,publishedAt,resourceId(videoId)))&key=AIzaSyArlObJlqCmzWx2i7WRhhrcSrGdjKb9904&playlistId=PLsUSkk8bQcahW45AEvNHoKzZXHigeo_Dd&pageToken=%s&maxResults=200'%url,headers=base_header).json()
    all=[]
    for items in x['items']:
        title=items['snippet']['title']
        link=items['snippet']['resourceId']['videoId']
        e_itt=None
        icn=''
        for itt in items['snippet']['thumbnails']:
            e_itt=itt
        if e_itt:
            icn=items['snippet']['thumbnails'][e_itt]['url']
        fanart=icn
        aa=addLink(title, 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % link,175,False,icn,fanart,title,place_control=True)
        all.append(aa)
       
    if 'nextPageToken' in x:
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]',x['nextPageToken'],176,BASE_LOGO+'ghost1.png','http://copasi.org/images/next.png','Next page')
        all.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))
def cfscrape_version():
    
    try:
        import shutil
        ver_file=os.path.join(__cwd__,'resources','modules','cfscrape','cfscrape','__init__.py')
        my_cfpath=os.path.join(__cwd__,'resources','modules','cfscrape','cfscrape')
        
        extened_cf=os.path.join(__cwd__,'resources','modules','cfscrape')
        cfscrape_path=os.path.join(__cwd__,'resources','modules','cfscrape_temp')
        if not os.path.exists(cfscrape_path):
            os.makedirs(cfscrape_path)
        regex="__version__.+?'(.+?)'"   
        if  os.path.exists(ver_file):
            file = open(ver_file, 'r') 
            file_data= file.read()
            file.close()
                 
            cur_version=re.compile(regex).findall(file_data)[0]
            
        else:
            cur_version='0'
        
        
        base_url='https://raw.githubusercontent.com/VeNoMouS/cloudscraper/master/cloudscraper/'
        base_url='https://github.com/a4k-openproject/script.module.openscrapers/raw/master/lib/openscrapers/modules/cfscrape/'
        x=get_html(base_url+'__init__.py',headers=base_header).content()

        
        web_version=re.compile(regex).findall(x)[0]
        from resources.modules.packaging import version
        from resources.modules.zfile import ZipFile
        if version.parse(cur_version) < version.parse(web_version):
             if  os.path.exists(my_cfpath):
                shutil.rmtree(my_cfpath, ignore_errors=True, onerror=None)
            
             
             r = get_html('https://github.com/a4k-openproject/script.module.openscrapers/archive/master.zip', stream = True)
             cf_file=os.path.join(user_dataDir,'cfscrape.zip')
             with open(cf_file, "wb") as Pypdf:

                for chunk in r.iter_content(chunk_size = 1024):

                    if chunk:

                        Pypdf.write(chunk)
             zf = ZipFile(cf_file)
             for file in zf.infolist():
                zf.extract(member=file, path=cfscrape_path)
             zf.close()
             new_cfscrape_path=os.path.join(__cwd__,'resources','modules','cfscrape_temp','script.module.openscrapers-master','lib','openscrapers','modules','cfscrape')
             
             log.warning('copy')
             log.warning(new_cfscrape_path)
             log.warning(my_cfpath)
             shutil.copytree(new_cfscrape_path,my_cfpath)
             
             shutil.rmtree(cfscrape_path, ignore_errors=True, onerror=None)
            
             xbmc.executebuiltin((u'Notification(%s,%s)' % ('Ok', 'cfscrape Updated to ver '+str(web_version))))
        return 'ok'
    except Exception as e:
        xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'Cannot update cfscrape , '+str(e))))
        return 'False'
        pass
def by_actor(url,icon,fan):
    
    aa=[]
    if url=='www':
        url='1'
        aa.append(addDir3('[COLOR aqua][I]%s[/COLOR][/I]'%Addon.getLocalizedString(32148),'www',74,icon,fan,'[COLOR aqua][I]%s[/COLOR][/I]'%Addon.getLocalizedString(32148)))
    link='https://api.themoviedb.org/3/person/popular?api_key=1180357040a128da71b71716058f6c5c&language=%s&page=%s&sort_by=popularity.desc'%(lang,url)
    headers = {
                                
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Connection': 'keep-alive',
                                'Upgrade-Insecure-Requests': '1',
                            }
    html=get_html(link,headers=headers).json()
    
    
    for items in html['results']:
        icon=None
        fanart=None
        try:
            icon=items['profile_path']
            fanart=items['known_for'][0]['backdrop_path']
        except:
            pass
        if icon==None:
          icon=' '
        else:
          icon='https://'+'image.tmdb.org/t/p/original/'+icon
        if fanart==None:
          fanart=' '
        else:
          fanart='https://'+'image.tmdb.org/t/p/original/'+fanart
        aa.append(addDir3(items['name'],str(items['id']),73,icon,fanart,items['name']))
    aa.append(addDir3('[COLOR aqua][I]%s[/COLOR][/I]'%Addon.getLocalizedString(32145),str(int(url)+1),72,' ',' ','[COLOR aqua][I]%s[/COLOR][/I]'%Addon.getLocalizedString(32145)))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
def actor_m(url,plot):
    log.warning('plot:'+plot)
    if plot=='shows' or plot=='movie':
        if plot=='shows':
            tv_mode='tv'
        else:
            tv_mode='movie'
    else:
        choise=[Addon.getLocalizedString(32099),Addon.getLocalizedString(32124)]
        ret = xbmcgui.Dialog().select(Addon.getLocalizedString(32149), choise)
        if ret!=-1:
            if ret==0:
             tv_mode='tv'
            else:
             tv_mode='movie'
        else:
          sys.exit()

    if tv_mode=='movie':
       link='https://api.themoviedb.org/3/person/%s?api_key=1180357040a128da71b71716058f6c5c&append_to_response=credits&language=%s&sort_by=popularity.desc'%(url,lang)
    else:
       link='https://api.themoviedb.org/3/person/%s/tv_credits?api_key=1180357040a128da71b71716058f6c5c&append_to_response=credits&language=%s&sort_by=popularity.desc'%(url,lang)
   
    headers = {
                                
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Connection': 'keep-alive',
                                'Upgrade-Insecure-Requests': '1',
                            }
    html=get_html(link,headers=headers).json()
    if tv_mode=='movie':
        url_g='https://'+'api.themoviedb.org/3/genre/movie/list?api_key=1180357040a128da71b71716058f6c5c&language=%s'%lang
                 
    else:
       url_g='https://'+'api.themoviedb.org/3/genre/tv/list?api_key=1180357040a128da71b71716058f6c5c&language=%s'%lang
    html_g=get_html(url_g,headers=headers).json()
    if tv_mode=='movie':
      test=html['credits']['cast']
      mode=15
    else:
      test=html['cast']
      mode=16
    aa=[]
    i=[]
    try:
      if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
        from resources.modules.general import call_trakt
        i = (call_trakt('/users/me/watched/movies'))
    except Exception as e:
        
        i=[]
    
    all_movie_w=[]
    for ids in i:
      all_movie_w.append(str(ids['movie']['ids']['tmdb']))
    
    
    for items in test:
        watched='no'
        if str(items['id']) in all_movie_w:
           watched='yes'
        
        
        add_n=items['character']
        log.warning(add_n)
        icon=items['poster_path']
        fanart=items['backdrop_path']
        if icon==None:
          icon=' '
        else:
          icon='https://'+'image.tmdb.org/t/p/original/'+icon
        if fanart==None:
          fanart=' '
        else:
          fanart='https://'+'image.tmdb.org/t/p/original/'+fanart
        
        plot=items['overview']
        if tv_mode=='movie':
          original_title=items['original_title']
        else:
          original_title=items['original_name']
        id=items['id']
        rating=items['vote_average']
        if tv_mode=='movie':
          title=items['title']
        else:
          title=items['name']
        if 'first_air_date' in items:
           if items['first_air_date']==None:
                    year=' '
           else:
                year=str(items['first_air_date'].split("-")[0])
        else:
            if 'release_date' in items:
              if items['release_date']==None:
                    year=' '
              else:
                year=str(items['release_date'].split("-")[0])
            else:
              year=' '
        genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                    if i['name'] is not None])
        genere = u' / '.join([genres_list[x] for x in items['genre_ids']])
        #except:genere=''
        
        video_data={}
        video_data['title']=title+' [COLOR blue](%s)[/COLOR]'%add_n
        #video_data['poster']=fanart
        video_data['plot']=plot
        #video_data['icon']=icon
        video_data['genre']=genere
        video_data['rating']=rating
        video_data['year']=year
        trailer = "plugin://%s?mode=25&id=%s&url=%s" % (addon_id,id,tv_mode)
        aa.append(addDir3(title+' [COLOR blue](%s)[/COLOR]'%add_n,'www',mode,icon,fanart,plot,data=year,original_title=original_title,id=str(id),rating=rating,heb_name=title,show_original_year=year,isr=' ',generes=genere,video_info=video_data,trailer=trailer,watched=watched))
    if tv_mode=='movie':
      test=html['credits']['crew']
      mode=15
    else:
      test=html['crew']
      mode=16
    for items in test:
        watched='no'
        if str(items['id']) in all_movie_w:
           watched='yes'
        add_n=items['department']
        icon=items['poster_path']
        fanart=items['backdrop_path']
        if icon==None:
          icon=' '
        else:
          icon='https://'+'image.tmdb.org/t/p/original/'+icon
        if fanart==None:
          fanart=' '
        else:
          fanart='https://'+'image.tmdb.org/t/p/original/'+fanart
        plot=items['overview']
        if tv_mode=='movie':
          original_title=items['original_title']
        else:
          original_title=items['original_name']
        id=items['id']
        rating=items['vote_average']
        if tv_mode=='movie':
          title=items['title']
        else:
          title=items['name']
        if 'first_air_date' in items:
           if items['first_air_date']==None:
                    year=' '
           else:
                year=str(items['first_air_date'].split("-")[0])
        else:
            if 'release_date' in items:
              if items['release_date']==None:
                    year=' '
              else:
                year=str(items['release_date'].split("-")[0])
            else:
              year=' '
        genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                    if i['name'] is not None])
        genere = u' / '.join([genres_list[x] for x in items['genre_ids']])
        #except:genere=''
        
        video_data={}
        video_data['title']=title+' [COLOR yellow](%s)[/COLOR]'%add_n
        #video_data['poster']=fanart
        video_data['plot']=plot
        #video_data['icon']=icon
        video_data['genre']=genere
        video_data['rating']=rating
        video_data['year']=year
        trailer = "%s?mode=25&id=%s&url=%s" % (sys.argv,id,tv_mode)
        aa.append(addDir3(title+' [COLOR yellow](%s)[/COLOR]'%add_n,'www',mode,icon,fanart,plot,data=year,original_title=original_title,id=str(id),rating=rating,heb_name=title,show_original_year=year,isr=' ',generes=genere,video_info=video_data,trailer=trailer,watched=watched))
        
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_SORT_TITLE)
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_YEAR)

    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_RATING)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
def search_actor():
    
    aa=[]
    search_entered=''
    keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
    keyboard.doModal()
    if keyboard.isConfirmed():
           search_entered = keyboard.getText()
           link='https://api.themoviedb.org/3/search/person?api_key=1180357040a128da71b71716058f6c5c&language=%s&query=%s&page=1&include_adult=false'%(lang,search_entered)
           headers = {
                                
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Connection': 'keep-alive',
                                'Upgrade-Insecure-Requests': '1',
                            }
           html=get_html(link,headers=headers).json()
           for items in html['results']:
                    icon=None
                    fanart=None
                    try:
                        icon=items['profile_path']
                        fanart=items['known_for'][0]['backdrop_path']
                    except:
                        pass
                    if icon==None:
                      icon=' '
                    else:
                      icon='https://'+'image.tmdb.org/t/p/original/'+icon
                    if fanart==None:
                      fanart=' '
                    else:
                      fanart='https://'+'image.tmdb.org/t/p/original/'+fanart
                    aa.append(addDir3(items['name'],str(items['id']),73,icon,fanart,items['name']))
           xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
    else:
        sys.exit(1)
def get_cast(url,id,season,episode):
    
    if url=='movie':
        x='http://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=credits'%(id,lang)
    else:
        x='http://api.themoviedb.org/3/tv/%s/season/%s/episode/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=credits'%(id,season,episode,lang)
    html=get_html(x).json()
   
    aa=[]
    for items in html['credits']['cast']:
        icon=items['profile_path']
        
        if icon==None:
          icon=' '
        else:
          icon='https://'+'image.tmdb.org/t/p/original/'+icon
        fanart=icon
        aa.append(addDir3(items['name']+' [COLOR yellow](%s)[/COLOR]'%items['character'],str(items['id']),73,icon,fanart,items['name']))
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
def get_3d(url):
    
    o_url=url
    x=get_html('https://3donlinefilms.com/results-year.php?search=&genre=&pageNum_Recordset1='+url,headers=base_header)
    
    x=x.content()
    regex='div class="wrap-col"(.+?)/h3></a>'
    m_pre=re.compile(regex,re.DOTALL).findall(x)
    all=[]
    for items in m_pre:
        regex='a href="(.+?)".+?img data-src="(.+?)".+?title="(.+?)"'
        m=re.compile(regex).findall(items)
        for lk,img,nm in m:
            img='https://3donlinefilms.com/'+img
            
            aa=addLink(nm, lk,6,False,img,img,nm,original_title=nm,place_control=True)
            all.append(aa)
    url=str(int(o_url)+1)
    x=get_html('https://3donlinefilms.com/results-year.php?search=&genre=&pageNum_Recordset1='+url,headers=base_header)
    
    x=x.content()
    regex='div class="wrap-col"(.+?)/h3></a>'
    m_pre=re.compile(regex,re.DOTALL).findall(x)
    
    for items in m_pre:
        regex='a href="(.+?)".+?img data-src="(.+?)".+?title="(.+?)"'
        m=re.compile(regex).findall(items)
        for lk,img,nm in m:
            img='https://3donlinefilms.com/'+img
            
            aa=addLink(nm, lk,6,False,img,img,nm,original_title=nm,season='%20',episode='%20',place_control=True)
            all.append(aa)
    regex='class="page gradient">(.+?)<'
    m=re.compile(regex).findall(x)
    last_p='last'
    for itt in m:
        last_p=itt
    
    aa=addDir3('[COLOR aqua][I]%s (%s/%s)[/I][/COLOR]'%(Addon.getLocalizedString(32145),str(int(o_url)+1),last_p),str(int(o_url)+1),178,BASE_LOGO+'ghost1.png','https://filmkijker.files.wordpress.com/2010/05/aimax.jpg','3d')
    all.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))
def tmdb_lists(id):
    from resources.modules.tmdb import html_g_movie
    url='http://api.themoviedb.org/3/list/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(id,lang)
    
    x=get_html(url).json()
    if 'tv' in url:
        html_g=html_g_tv
    else:
        html_g=html_g_movie
    aa=[]
    i=[]
    try:
      if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
        from resources.modules.general import call_trakt
        i = (call_trakt('/users/me/watched/movies'))
    except Exception as e:
        
        i=[]
    
    all_movie_w=[]
    for ids in i:
      all_movie_w.append(str(ids['movie']['ids']['tmdb']))
    for items in x['items']:
        if items['media_type']=='movie':
            new_name=items['title']
            if items['poster_path']==None:
                items['poster_path']=''
            if items['backdrop_path']==None:
                items['backdrop_path']=''
                    
            icon=domain_s+'image.tmdb.org/t/p/original/'+items['poster_path']
            fan=domain_s+'image.tmdb.org/t/p/original/'+items['backdrop_path']
            if 'release_date' in items:
                year=str(items['release_date'].split("-")[0]) 
            else:
                year=''
            original_name=items['original_title']
            
                
            id=str(items['id'])
            rating=items['vote_average']
            isr='0'
            genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                            if i['name'] is not None])
            try:genere = u' / '.join([genres_list[x] for x in items['genre_ids']])
            except:genere=''
            plot=items['overview']
            watched='no'
            if str(items['id']) in all_movie_w:
               watched='yes'
            mode=15
        else:
            new_name=items['name']
            if items['poster_path']==None:
                items['poster_path']=''
            if items['backdrop_path']==None:
                items['backdrop_path']=''
                    
            icon=domain_s+'image.tmdb.org/t/p/original/'+items['poster_path']
            fan=domain_s+'image.tmdb.org/t/p/original/'+items['backdrop_path']
            if 'release_date' in items:
                year=str(items['release_date'].split("-")[0]) 
            else:
                year=''
            original_name=items['original_name']
            
                
            id=str(items['id'])
            rating=items['vote_average']
            isr='0'
            genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                            if i['name'] is not None])
            try:genere = u' / '.join([genres_list[x] for x in items['genre_ids']])
            except:genere=''
            plot=items['overview']
            watched='no'
            
            mode=16
        aa.append(addDir3(new_name,url,mode,icon,fan,plot,data=year,original_title=original_name,id=id,rating=rating,heb_name=new_name,show_original_year=year,isr=isr,generes=genere,watched=watched))
         
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
        
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_YEAR)
def collection_detials(id):
    
    from resources.modules.tmdb import html_g_movie
    url='https://api.themoviedb.org/3/collection/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(id,lang)
    log.warning(url)
    x=get_html(url).json()
    #html_g=cache.get(cache_genered,72,'movie', table='poster')
    if 'tv' in url:
        html_g=html_g_tv
    else:
        html_g=html_g_movie
    aa=[]
    i=[]
    try:
      if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
        from resources.modules.general import call_trakt
        i = (call_trakt('/users/me/watched/movies'))
    except Exception as e:
        
        i=[]
    
    all_movie_w=[]
    for ids in i:
      all_movie_w.append(str(ids['movie']['ids']['tmdb']))
    
    
    
        
           
    for items in x['parts']:
    
        new_name=items['title']
        if items['poster_path']==None:
            items['poster_path']=''
        if items['backdrop_path']==None:
            items['backdrop_path']=''
                
        icon=domain_s+'image.tmdb.org/t/p/original/'+items['poster_path']
        fan=domain_s+'image.tmdb.org/t/p/original/'+items['backdrop_path']
        if 'release_date' in items:
            year=str(items['release_date'].split("-")[0]) 
        else:
            year=''
        original_name=items['original_title']
        
            
        id=str(items['id'])
        rating=items['vote_average']
        isr='0'
        genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                        if i['name'] is not None])
        try:genere = u' / '.join([genres_list[x] for x in items['genre_ids']])
        except:genere=''
        plot=items['overview']
        watched='no'
        if str(items['id']) in all_movie_w:
           watched='yes'
           
        aa.append(addDir3(new_name,url,15,icon,fan,plot,data=year,original_title=original_name,id=id,rating=rating,heb_name=new_name,show_original_year=year,isr=isr,generes=genere,watched=watched))
         
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
        
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_YEAR)
def search_tvdb(search_string):
    global tvdb_results
    from resources.modules.tvdb import TVDB
    
    t = TVDB()
    tvdb_id_pre=t.getShow( search_string)
   
    aa=[]
    for items in tvdb_id_pre['data']:
        
        icon='https://www.thetvdb.com'+str(items['poster'] )
        fanart='https://www.thetvdb.com'+str(items['image'] )
      
        aa.append(addDir3(items['seriesName'],'www',16,icon,fanart,items.get('overview',' '),tmdbid=str(items['id']),id='tvdb'+str(items['id'])))
    tvdb_results=aa
def all_test_menu(iconimage,fanart):
    
    addNolink( 'Thread Test', '1',182,False,fanart=fanart, iconimage=iconimage,plot=' ')
    addNolink( 'Simple Thread Test', '4',182,False,fanart=fanart, iconimage=iconimage,plot=' ')
    addNolink( 'Regex Test', '2',182,False,fanart=fanart, iconimage=iconimage,plot=' ')
    addNolink( 'Download Speed', '3',182,False,fanart=fanart, iconimage=iconimage,plot=' ')
    addNolink( 'Cpu stress', '5',182,False,fanart=fanart, iconimage=iconimage,plot=' ')
    
def simple_url():
    
    x=get_html('https://gowatchseries.tv',headers=base_header).content()
    return x
def regex_test(html):
    
    for itt in range(0,100):
        regex='<div class="resultdivbottonlength">(.+?)<.+?class="hideinfohash">(.+?)<.+?class="hideinfohash">(.+?)<'
        mod=re.compile(regex,re.DOTALL)
        match=mod.findall(html)
    return match
def cpu_usage(dp):
    global avg_f,stop_cpu,cores_use
    all_c=[]
    avg=0
    counter=0
    stop_cpu=False
    while stop_cpu==False:
        for i in range(0,16):
            prec=float(xbmc.getInfoLabel('System.CoreUsage(%s)'%str(i)))
            if prec>0.0:
                all_c.append(str(int(prec))+'%')
            if prec>0:
                avg+=int(prec)
                counter+=1
        if counter==0:
            counter=1
        avg_f=str(int(float(avg/counter)))+'%'
        cores_use=str(len(all_c))+'.Cpu:'+','.join(all_c)
        if KODI_VERSION>18:
            dp.update(0, 'Cpu stress...'+'\n'+avg_f+'\n'+ cores_use )
        else:
            dp.update(0, 'Cpu stress...',avg_f, cores_use )
        avg=0
        counter=0
        all_c=[]
        #xbmc.sleep(10)
def cpu_test():
    global avg_f,stop_cpu,cores_use
    import math
    dp = xbmcgui . DialogProgress ( )
    if KODI_VERSION>18:
        dp.create('Please wait','Cpu stress...'+'\n'+ ''+'\n'+'')
    else:
        dp.create('Please wait','Cpu stress...', '','')
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'Cpu stress...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','Cpu stress...', '' )
    
    thread=[]
    thread.append(Thread(cpu_usage,dp))
    thread[0].start()
    
    stop_now=False
    x=1024*1024
    while True:
        if stop_now:
            break
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                x**x
            
            if dp.iscanceled():
                stop_cpu=True
                dp.close()
                stop_now=True
                break
        
        x**x
    dp.close()
    stop_cpu=True
def downloadFile() :
  
  url='http://speedtest-safe.bezeqint.net/big500.zip'
  directory=user_dataDir
  localFilename = url.split('/')[-1]
  f_name=os.path.join(directory,localFilename)
  if os.path.exists(f_name):
    os.remove(f_name)
    
  dp = xbmcgui . DialogProgress ( )
  if KODI_VERSION>18:
    dp.create('Please wait','Download speed...'+'\n'+ ''+'\n'+'')
  else:
    dp.create('Please wait','Download speed...', '','')
  if KODI_VERSION>18:
    dp.update(0, 'Please wait'+'\n'+'Download speed..1'+'\n'+ '' )
  else:
    dp.update(0, 'Please wait','Download speed..1', '' )

  with open(directory + '/' + localFilename, 'wb') as f:
    start = time.clock()
    r = get_html(url, stream=True)
    total_length =int( r.headers.get('content-length'))
    log.warning(total_length)
    dl = 0
    if total_length is None: # no content length header
      f.write(r.content())
    else:
      for chunk in r.iter_content(1024):
        dl += len(chunk)
        f.write(chunk)
        done = int(50 * dl / total_length)
        if KODI_VERSION>18:
            dp.update(0, 'Please wait'+'\n'+'Download speed..1'+'\n'+ "\r[%s%s] %s Mbps" % ('=' * done, ' ' * (50-done), round((dl//(time.clock() - start))/(1024*1024),2)))
        else:
            dp.update(0, 'Please wait','Download speed..1', "\r[%s%s] %s Mbps" % ('=' * done, ' ' * (50-done), round((dl//(time.clock() - start))/(1024*1024),2)))
        
        if dp.iscanceled():
            dp.close()
            
                        
  dp.close()
  if os.path.exists(f_name):
     os.remove(f_name)
  return 0
def run_system_test(url):
    
    if url=='3':
        downloadFile()
        return 0
    if url=='5':
        cpu_test()
        return 0
    if url=='2':
    
        html=get_html('https://idope.se/torrent-list/matrix/',headers=base_header).content()
    if 1:#url=='1' or url=='4':
        source_dir = os.path.join(addonPath, 'resources', 'sources')
    
        sys.path.append( source_dir)
        impmodule = __import__('gow')
        
        impmodule.stop_all=0
        impmodule.global_var=[]
        
        
        
        
        
        measure=[1,2,4,8,16,32,64,128,256]
        
        results={}
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create('Please wait','Testing Threads...'+'\n'+ '')
        else:
            dp.create('Please wait','Testing Threads...', '','')
        if KODI_VERSION>18:
            dp.update(0, 'Please wait'+'\n'+'Testing Threads..1'+'\n'+ '' )
        else:
            dp.update(0, 'Please wait','Testing Threads..1', '' )
        
        if url=='2':
                r_string=[]
                for items in measure:
                
                    start_time=time.time()
                    for i in range(1,items+1):
                        regex_test(html)
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(0, 'Please wait'+'\n'+'Testing Threads..'+str(items)+'\n'+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                    else:
                        dp.update(0, 'Please wait','Testing Threads..'+str(items), time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                    
                    r_string.append(str(items)+' - '+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        else:
        
            r_string=[]
            for items in measure:
                thread=[]
                start_time=time.time()
                elapsed_time = time.time() - start_time
                if KODI_VERSION>18:
                    dp.update(0, 'Please wait'+'\n'+'Testing Threads..'+str(items)+'\n'+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                else:
                    dp.update(0, 'Please wait','Testing Threads..'+str(items), time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                for i in range(1,items+1):
                   if url=='4':
                    thread.append(Thread(simple_url))
                   elif url=='1':
                    thread.append(Thread(impmodule.get_links,'movie','rampage','0','0','0','0','2018','427641'))
                   
                for td in thread:
                    td.start()
                while(1):
                    still_alive=0
                    num_live=0
                    for yy in range(0,len(thread)):
                       
                        if not thread[yy].is_alive():
                          num_live=num_live+1
                          
                        else:
                            still_alive=1
                    elapsed_time = time.time() - start_time
                    if KODI_VERSION>18:
                        dp.update(0, 'Please wait, Done: '+str(num_live)+'\n'+'Testing Threads..'+str(items)+'\n'+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                    else:
                        dp.update(0, 'Please wait, Done: '+str(num_live),'Testing Threads..'+str(items), time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                    if still_alive==0:
                        break
                    xbmc.sleep(100)
                elapsed_time = time.time() - start_time
                results[str(items)]=time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                r_string.append(str(items)+' - '+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        dp.close()
        
        
        showText('Times', '\n'.join (r_string))
def imdb_menu(iconimage,fanart):
    user=Addon.getSetting('imdb_user')
    aa=[]
    aa.append(addDir3('My lists','https://www.imdb.com/user/ur%s/lists?sort=mdfd&order=asc',184,iconimage,fanart,' '))
    aa.append(addDir3('My Watched list','https://www.imdb.com/user/ur%s/watchlist?sort=date_added,desc',184,iconimage,fanart,' '))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
def get_users_list(url,user):
    global aa_results
    x=get_html(url).content()
   
    
    
    
    x=str(x)
    log.warning(url)
    if user not in aa_results:
        aa_results[user]={}
        aa_results[user]['links']=[]
    non_empy=True
    if 'This list is not public' in x:
        #xbmcgui.Dialog().ok('Error','This list is not public')
        aa_results[user]['name']='[COLOR red]%s - This list is not public[/COLOR]'%user
        non_empy=False
        return []
    if non_empy:
        if 'watchlist' in url:
            
            regex='meta property="og\:title" content="(.+?)"'
            m=re.compile(regex).findall(x)
            l_title=''
            if len(m)>0:
                l_title=m[0]
            aa_results[user]['name']=l_title

            regex='WatchlistWidget.+?IMDbReactInitialState.push\((.+?)\);'
            m=re.compile(regex,re.DOTALL).findall(x)[0]
            
            j_m=json.loads(m)
            all_reabon=[]
            for itt in j_m['list']['items']:   
                all_reabon.append(itt['const'])
            headers = {
                'authority': 'www.imdb.com',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'x-requested-with': 'XMLHttpRequest',
                'x-imdb-parent-id': 'null',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': url,
                
                
            }

            params = (
                ('ids', ','.join(all_reabon)),
                ('tracking_tag', ''),
                ('pageId', j_m['list']['id']),
                ('pageType', 'list'),
                ('subpageType', 'watchlist'),
            )

            response = get_html('https://www.imdb.com/title/data', headers=headers, params=params).json()
            

            
            for itt in response:   
                j_m=response[itt]
               
                id='imdb'+itt
                nm=j_m['title']['primary']['title']
                year=0
                year_m=None
                if 'year' in j_m['title']['primary']:
                    year_m=j_m['title']['primary']['year']
                
                if year_m:
                    year=year_m[0]
                img=None
                if 'poster' in j_m['title']:
                    img=j_m['title']['poster']
                if img:
                    img=img['url']
                else:
                    img='https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/imdb.png'
                all_g=[]
                for imm in j_m['title']['metadata']['genres']:
                    all_g.append(imm)
                genere=','.join(all_g)
                plot=j_m['title']['plot']
                mode=15
                if 'series' in j_m['title']['type']:
                    mode=16
                video_data={}
                video_data['title']=nm
                video_data['iconimage']=img
                video_data['fanart']=img
                video_data['plot']=plot
                video_data['year']=year
                video_data['genre']=genere
                video_data['id']=id
                
                aa_results[user]['links'].append(( nm, 'www',mode, img,img,plot,id,year,video_data))
                
            
            return aa_results
        else:
            regex='<title>(.+?)</title'
            m=re.compile(regex).findall(x)
            l_title=''
            if len(m)>0:
                l_title=m[0]
            aa_results[user]['name']=l_title
            
            regex='<a class="list-name" href="(.+?)">(.+?)<.+?<div class="list-meta">(.+?)<'
            m=re.compile(regex,re.DOTALL).findall(x)
            aa=[]
            
            for lk,nm,plot in m:
                plot=plot.replace('|',' ')
                
                
                video_data={}
                video_data['title']=nm
                video_data['iconimage']=iconimage
                video_data['fanart']=fanart
                video_data['plot']=plot
                
                
                aa_results[user]['links'].append((nm,'https://www.imdb.com'+lk,185,iconimage,fanart,plot,'test','0',video_data))
            return aa_results
def get_imdb_lists(url,iconimage,fanart):
    global aa_results
    all_users=[]
    aa_results={}
    thread=[]
    for i in range(0,10):
        user=Addon.getSetting('imdb_user_'+str(i))
        if user!='':
            all_users.append(user)
            aa_results[user]={}
            aa_results[user]['links']=[]
            aa_results[user]['name']=''
            thread.append(Thread(get_users_list,url%user,user))
   
    #get_users_list(url%all_users[1],all_users[1])
    for td in thread:
        td.start()
    while(1):
        still_alive=0
        num_live=0
        for yy in range(0,len(thread)):
           
            if not thread[yy].is_alive():
              num_live=num_live+1
              
            else:
                still_alive=1
        if still_alive==0:
            break
        xbmc.sleep(100)
    aa=[]
    log.warning(aa_results)
    for itt in all_users:
      if aa_results[itt]['name']=='':
        aa_results[itt]['name']='-------%s----------'%itt
      
      aa.append(addNolink('[COLOR lightblue][I][B]'+aa_results[itt]['name']+'[/B][/I][/COLOR]' , '0',999,False,fanart=fanart, iconimage=iconimage,plot='',dont_place=True))
      if 'This list is not public' in aa_results[itt]['name']:
        continue
      
      for nm, lk,mode, icon,img,plot,id,year,video_data in aa_results[itt]['links']:
            log.warning('Inserting:'+nm)
            aa.append(addDir3( nm, lk,mode, icon,img,plot,data=year,original_title=nm,id=id,eng_name=nm,show_original_year=year,heb_name=nm))
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
def fill_imdb_list(url):
    x=get_html(url).content()
    regex='ref_=ttls_li_i.+?img alt="(.+?)".+?loadlate="(.+?)".+?data-tconst="(.+?)".+?<span class="lister-item-year text-muted unbold">\((.+?)\)<.+?<span class="genre">(.+?)<.+?<p class="">(.+?)<'
    m=re.compile(regex,re.DOTALL).findall(x)
    all_d=[]
    mode=15
    for nm,img,id,year,genere,plot in m:
        if '-' in year:
            year=year.replace('-','').strip()
            mode=16
        id='imdb'+id
        
        aa=addDir3( nm, 'www',mode, img,img,plot,data=year,generes=genere.replace('\n','').replace('\r','').replace('\t','').strip(),original_title=nm,id=id,eng_name=nm,show_original_year=year,heb_name=nm)
        all_d.append(aa)
    regex='<a class="flat-button lister-page-next next-page" href="(.+?)"'
    m=re.compile(regex).findall(x)
    if len(m)>0:
        aa=(addDir3('[COLOR aqua][I]%s[/COLOR][/I]'%Addon.getLocalizedString(32145),'https://www.imdb.com'+m[0],185,' ',' ','[COLOR aqua][I]%s[/COLOR][/I]'%Addon.getLocalizedString(32145)))
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def download_file_asis(url,dest,name):
    try:
        from urllib2 import urlopen, URLError, HTTPError
    except:
        from urllib.request import urlopen
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    f = urlopen(url, timeout=550)
   

    # Open our local file for writing
    with open(os.path.join(dest,name), "wb") as local_file:
        local_file.write(f.read())
        
def download_file(url,dest):
    try:
        from urllib2 import urlopen, URLError, HTTPError
    except:
        from urllib.request import urlopen
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    f = urlopen(url, timeout=550)
   

    # Open our local file for writing
    with open(os.path.join(dest,'temp_file.zip'), "wb") as local_file:
        local_file.write(f.read())

def update_keys():
    try:
        import gzip
        from datetime import date, timedelta
        yesterday = date.today() - timedelta(days=2)
        dd=yesterday.strftime("%m_%d_%Y")
        #dd=time.strftime("%m_%d_%Y")
        log.warning(dd)
        url='http://files.tmdb.org/p/exports/keyword_ids_%s.json.gz'%dd
        log.warning(url)
        download_file(url,user_dataDir)
        xbmc.sleep(300)
        with gzip.open(os.path.join(user_dataDir,'temp_file.zip'), 'rb') as f:
          file_content = (f.read())
        try:
            file_content=file_content.decode('utf-8')
        except:
            pass
        ff='['+file_content.replace('\n',",")+']'
       
        j_file=json.loads(ff.replace(',]',']'))
        
        all_keys=[]
        all_json_data={}
        for items in j_file:
            #log.warning(items)
            all_keys.append((items['id'],items['name']))
            if items['name'][:1].lower() not in all_json_data:
                all_json_data[items['name'][:1].lower()]=[]
            else:
                all_json_data[items['name'][:1].lower()].append((items['id'],items['name']))
        return all_keys,all_json_data
    except Exception as e:
        import linecache
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        xbmc.executebuiltin((u'Notification(%s,%s)' % (addon_name, 'Line:'+str(lineno)+' E:'+str(e))).encode('utf-8'))
        log.warning('ERROR IN keys :'+str(lineno))
        log.warning('inline:'+line)
        log.warning(e)

        
        return [],{}
    
def get_keywords_ab(icon,fan):
    import string
    a=list(string.ascii_lowercase)
    all_d=[]
   
    all_keys,all_json_data=cache.get(update_keys,72, table='posters')
    
    for items in a:
        
        count=len(all_json_data[items])
        aa=(addDir3('(%s) '%count+items,items,188,icon,fan,items))
        all_d.append(aa)
    aa=(addDir3('Search','search',188,icon,fan,'Search'))
    all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    
def get_keywords(url,icon,fan,dates):
    all_d=[]
    all_keys,all_json_data=cache.get(update_keys,72, table='posters')
    if url=='search':
        search_entered=''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
        keyboard.doModal()
        all_s_result=[]
        if keyboard.isConfirmed() :
               search_entered = que(keyboard.getText().replace("'",""))
               if search_entered=='':
                sys.exit()
               else:
                 for items in all_json_data:
                    for itt in all_json_data[items]:
                        if search_entered in itt[1]:
                            all_s_result.append((itt[0],itt[1]))
                            
        all_s_result=sorted(all_s_result, key=lambda x: x[1], reverse=False)
        for itt in all_s_result:
            aa=(addDir3(itt[1],'https://api.themoviedb.org/3/keyword/%s/movies?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&include_adult=false'%(itt[0],lang),14,icon,fan,itt[1]))
            all_d.append(aa)
    else:
        
        all_j_sort=sorted(all_json_data[url], key=lambda x: x[1], reverse=False)
        if dates==' ' or dates=='%20':
            start=0
            last=100
        else:
            start=int(dates)
            last=100+int(dates)
        
        count=0
        for items in all_j_sort:
            
            count+=1
            if count>=start:
                start+=1
                if start>last:
                    break
                #log.warning('https://api.themoviedb.org/3/movie/%s/keywords?api_key=fb981e5ab89415bba616409d5eb5f05e'%items[0])
                aa=(addDir3(items[1],'https://api.themoviedb.org/3/keyword/%s/movies?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&include_adult=false'%(items[0],lang),14,icon,fan,items[1]))
                all_d.append(aa)
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]',url,188,BASE_LOGO+'ghost1.png','http://copasi.org/images/next.png','Next page',dates=str(start))
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def GetEncodeString(str):
    try:
        import chardet
        str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
    except:
        try:
            str = str.encode("utf-8")
        except:
            pass
    return str
def GET_M3U_LIST(response):

    
    response = response.replace('#AAASTREAM:','#A:')
    response = response.replace('#EXTINF:','#A:')
    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)
    
    li = []
    for params, display_name, url in matches:
        item_data = {"params": params, "display_name": display_name, "url": url}
        li.append(item_data)
    m3u_list = []
    for channel in li:
        item_data = {"display_name": channel["display_name"], "url": channel["url"]}
        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
        for field, value in matches:
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        m3u_list.append(item_data)
    all_chan=[]
    for channel in (m3u_list):
        name = (channel["display_name"])
        url = (channel["url"])
        logo=channel.get("tvg_logo"," ")
        
        url = url.replace('\\n','').replace('\n','').replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
        all_chan.append((name,url,logo))
    return all_chan
def get_all_imdb_items(imdb_scan,link,season,episode,get_movies):
    global all_results_imdb
    url2='https://www.imdb.com/title/%s/'%imdb_scan
    pre_id=get_html(url2).json()
    regex='name="description" content="(.+?)"'
    
    
    url2='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=imdb_id&language=%s'%(imdb_scan,lang)
       
    pre_id=get_html(url2).json()
    tmdb_id=pre_id['movie_results'][0]['id']
    try:
        season=int(season)
        tv_movie='tv'
    except:
        tv_movie='movie'
    if tv_movie=='movie':
        url2='http://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s'%(tmdb_id,lang)
        
      
        all_results_imdb.append(get_movies(url2,return_results=True))
        
def populate_json_playlist(url,iconimage,fanart,search_db,get_episode_link=False,next_episode='0',search=False,mypass=""):
    global all_results_imdb
    not_found=True
    if len(mypass)>0:
        search_entered=''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Password')
        keyboard.doModal()
        if keyboard.isConfirmed() :
               search_entered = (keyboard.getText().replace("'",""))
               key='zWrite'
               mypass=crypt(mypass,key)
               log.warning('Mypass:'+mypass)
               if search_entered!=mypass:
                    xbmcgui.Dialog().ok('Error','Wrong Password')
                    return 0
        else:
            return 0
    try:
        all_imdb_scan=[]
        o_url=url
        log.warning('o_url:'+o_url)
        if "plugin:" in url:
            
            xbmc.executebuiltin(('Container.update("%s")'%url))
            return 0
        headers={
            'User-Agent': "python-requests/3.5",
            'Accept-Encoding': 'UTF-8',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        if ".m3u8" in url:
            x=get_html(url,headers=headers).content()
            all_chan=GET_M3U_LIST(x)
            all_d=[]
            for title,url,icon in all_chan:
                
                aa=addLink(title,url,6,False,icon,icon,' ',original_title=title,place_control=True)
                all_d.append(aa)
                    
        else:
            global from_seek
            from_seek=False
                
            if search:
                
                from_seek=True
                search_entered=''
                keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
                keyboard.doModal()
                if keyboard.isConfirmed() :
                       search_entered = (keyboard.getText().replace("'",""))
                       if search_entered=='':
                        
                            return 0
                dp = xbmcgui . DialogProgress ( )
                if KODI_VERSION>18:
                    dp.create('Please wait','Downloading DB...')
                    dp.update(0, 'Please wait'+'\n'+'Downloading DB...'+'\n'+ '' )
                else:
                    dp.create('Please wait','Downloading DB...', '','')
                    dp.update(0, 'Please wait','Downloading DB...', '' )
                              
                                    
                
                file=os.path.join(user_dataDir,'search.db')
                html=cache.get(download_file_asis,1,search_db,user_dataDir ,'search.db',table='posters')
                if html!=str('ok'):
                    html=cache.get(download_file_asis,0,search_db,user_dataDir,'search.db',table='posters')
                if KODI_VERSION>18:
                    
                    dp.update(0, 'Please wait'+'\n'+'Opening DB...'+'\n'+ '' )
                else:
                    
                    dp.update(0, 'Please wait','Opening DB...', '' )
                all_d=[]
                try:
                    from sqlite3 import dbapi2 as database
                except:
                    from pysqlite2 import dbapi2 as database
                
                dbcon = database.connect(file)
                dbcur = dbcon.cursor()
                
                
                dbcur.execute("SELECT * FROM search where item like '%{0}%'".format(search_entered))
            
                
                        
                match = dbcur.fetchall()
                
                dbcur.close()
                dbcon.close()
                count=0
                x=''
                for y,poster in match:
                    x=x+y
            else:
                
                x=get_html(url,headers=headers).json()
                
        
            
            
            all_d=[]
            added_link='Direct_link$$$resolveurl'
            for items in x['items']:
                icon=items.get("thumbnail",iconimage)
                
                fanart=items.get("fanart",fanart)
                url=items.get("link"," ")
                title=items.get("title"," ")
                type_content=items.get("type"," ")
                imdb=items.get("imdb","")
                season=items.get("season"," ")
                episode=items.get("episode"," ")
                original_title=items.get("tvshowtitle",title)
                plot=items.get("summary"," ")
         
                if season!=' ':
                    tv_movie='tv'
                else:
                    tv_movie='movie'
                trailer=''
                if imdb!='':
                    trailer = "plugin://%s?mode=25&id=%s&url=%s" % (addon_id,imdb,tv_movie)
                
                if isinstance(url, list):
                    
                    f_link_arr=[]
                    for itt in url:
                        f_link_arr.append(added_link+itt)
                    if len(f_link_arr)>1:
                        f_link='$$$$'.join(f_link_arr)
                    elif len(f_link_arr)>0:
                        f_link=f_link_arr[0]
                    else:
                        continue
                else:
                    f_link=added_link+url
                    
            
                
                if get_episode_link:
                    if str(episode)==str(next_episode):
                        log.warning('Found Episode:'+episode)
                        not_found=False
                        return f_link,title
                if type_content== "item":
                    lk='Jen_link'+o_url+'$$$$$'+f_link
                    
                    if 'message' in f_link:
                        aa=addNolink(title, f_link,194,False,fanart=fanart, iconimage=icon,plot=plot,dont_place=True)
                    
                        all_d.append(aa)
                    else:
                        
                        if 0:#'tt' in imdb:
                            all_imdb_scan.append((imdb,lk,season,episode,title))
                        else:
                            aa=addLink(title,lk,6,False,icon,fanart,plot,original_title=title,tmdb=imdb,season=season,episode=episode,trailer=trailer,place_control=True)
                            all_d.append(aa)
                else:
                    if 'message' in f_link:
                        aa=addNolink(title, f_link,194,False,fanart=fanart, iconimage=icon,plot=plot,dont_place=True)
                    
                        all_d.append(aa)
                    else:
                        aa=addDir3(title,url,189,icon,fanart,plot,id=imdb,trailer=trailer)
                        all_d.append(aa)
        
        '''
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create('Please wait','Scaning Items...')
            dp.update(0, 'Please wait'+'\n'+'Scaning Items...'+'\n'+ '' )
        else:
            dp.create('Please wait','Scaning Items...', '','')
            dp.update(0, 'Please wait','Scaning Items...', '' )
        thread=[]
  
        from resources.modules.tmdb import get_movies
        for imdb_scan,link,season,episode,title in all_imdb_scan:
            #get_all_imdb_items(imdb_scan,link,season,episode)
            thread.append(Thread(get_all_imdb_items,imdb_scan,link,season,episode,get_movies))
            thread[len(thread)-1].setName(title)
    
            thread[len(thread)-1].start()
        if len(thread)>0:
            while (1):
                num_live=0
                still_alive=0
                is_alives=[]
                for ites in thread:
                    
                    if trd_alive(ites):
                          num_live+=1
                          is_alives.append(ites.name)
                    else:
                          still_alive=1
                if KODI_VERSION>18:
                    
                    dp.update(int(((num_live* 100.0)/(len(thread))) ), 'Please wait'+'\n'+'Scaning Items..'+str(num_live)+'/'+str(len(thread))+'\n'+ ",".join(is_alives) )
                else:
                    
                    dp.update(int(((num_live* 100.0)/(len(thread))) ), 'Please wait','Scaning Items.'+str(num_live)+'/'+str(len(thread)),  ",".join(is_alives)  )
                
                if still_alive==0 or num_live==0:
                        break
                xbmc.sleep(100)
        dp.close()
        
        log.warning('all_results_imdb:'+str(len(all_results_imdb)))
        
        for itt in all_results_imdb:
            for name,url,mode,icon,fan,plot,year,original_name,id,added_res_trakt,rating,new_name,year,genere,trailer,watched,fav_status,collect_all,all_w in itt:
                aa=addDir3(name,url,mode,icon,fan,plot,data=year,original_title=original_name,id=id,all_w_trk=added_res_trakt,rating=rating,heb_name=new_name,show_original_year=year,generes=genere,trailer=trailer,watched=watched,fav_status=fav_status,collect_all=True,all_w=all_w)
                all_d.append(aa)
        '''
        if len(search_db)>0 and not search:
            aa=addDir3('[COLOR lightblue][B]Search[/B][/COLOR]',o_url,191,icon,fanart,'Search',search_db=search_db)
            all_d.append(aa)
            
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
        if not_found:
            return False,''
    except  Exception as e:
        import linecache
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        
        log.warning('ERROR IN Populate Json :'+str(lineno))
        log.warning('inline:'+line)
        log.warning(e)
   

        return ''
def populate_playlist(url,iconimage,o_fanart,search_db,search=False,mypass=""):
    global from_seek
    from_seek=False
    if len(mypass)>0:
        search_entered=''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Password')
        keyboard.doModal()
        if keyboard.isConfirmed() :
               search_entered = (keyboard.getText().replace("'",""))
               key='zWrite'
               mypass=crypt(mypass,key) 
               if search_entered!=mypass:
                    xbmcgui.Dialog().ok('Error','Wrong Password')
                    return 0
        else:
            return 0
    if search:
        
        from_seek=True
        search_entered=''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
        keyboard.doModal()
        if keyboard.isConfirmed() :
               search_entered = (keyboard.getText().replace("'",""))
               if search_entered=='':
                
                    return 0
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create('Please wait','Downloading DB...')
            dp.update(0, 'Please wait'+'\n'+'Downloading DB...'+'\n'+ '' )
        else:
            dp.create('Please wait','Downloading DB...', '','')
            dp.update(0, 'Please wait','Downloading DB...', '' )
                      
                            
        
        file=os.path.join(user_dataDir,'search.db')
        html=cache.get(download_file_asis,1,search_db,user_dataDir,'search.db', table='posters')
        if html!=str('ok'):
            html=cache.get(download_file_asis,0,search_db,user_dataDir,'search.db', table='posters')
        if KODI_VERSION>18:
            
            dp.update(0, 'Please wait'+'\n'+'Opening DB...'+'\n'+ '' )
        else:
            
            dp.update(0, 'Please wait','Opening DB...', '' )
        all_d=[]
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        
        dbcon = database.connect(file)
        dbcur = dbcon.cursor()
        
        
        dbcur.execute("SELECT * FROM search where item like '%{0}%'".format(search_entered))
    
        
                
        match = dbcur.fetchall()
        
        dbcur.close()
        dbcon.close()
        count=0
        x=''
        for y,poster in match:
            x=x+y
    else:
        log.warning(url)
        x=get_html(url,headers=base_header).content()
        o_url=url
    
    all_d=[]
    all_plugins=[]
    plugin_dir = os.path.join(addonPath, 'resources', 'plugins')
    for f in listdir(plugin_dir):
        if isfile(join(plugin_dir, f)):
            all_plugins.append(f.replace('.py','').replace('tmdb_jen','tmdb').replace('trakt_jen','trakt'))
            
    #all_plugins = [f.replace('.py','') for f in listdir(plugin_dir) if isfile(join(plugin_dir, f))]
    sys.path.append( plugin_dir)
    
    regex='<((?:item|dir|plugin))>(.+?)</(?:item|dir|plugin)>'
    m=re.compile(regex,re.DOTALL).findall(x)
    mode=6
    for type_record,items in m:
        
        if type_record=='item':
            added_link='Direct_link$$$resolveurl'
        else:
            added_link=''
        regex='<imdb>(.+?)</imdb>'
        imdb_id=re.compile(regex).findall(items)
        if len(imdb_id)==0:
            imdb_id=''
        else:
            imdb_id=imdb_id[0]
        
        regex='<title>(.+?)</title>'
        title=re.compile(regex).findall(items)
        if len(title)==0:
            regex='<name>(.+?)</name>'
            title=re.compile(regex).findall(items)
            if len(title)==0:
                title=''
            else:
                title=title[0]
        else:
            title=title[0]
        regex='<year>(.+?)</year>'
        year=re.compile(regex).findall(items)
        if len(year)==0:
            year=''
        else:
            year=year[0]
        regex='<season>(.+?)</season>'
        season=re.compile(regex).findall(items)
        if len(season)==0:
            season=' '
        else:
            season=season[0]
        regex='<episode>(.+?)</episode>'
        episode=re.compile(regex).findall(items)
        if len(episode)==0:
            episode=' '
        else:
            episode=episode[0]
        if season!=' ':
            tv_movie='tv'
        else:
            tv_movie='movie'
        regex='<sublink>(.+?)</sublink>'
        links=re.compile(regex).findall(items)
        f_link_arr=[]
        mode=6
        for itt in links:
            
            f_link_arr.append(added_link+itt)
            if itt=='search':
                mode=15
        regex='<link>(.+?)</link>'
        links=re.compile(regex).findall(items)
        for itt in links:
            if '<sublink>' in itt:
                regex='<sublink>(.+?)</sublink>'
                links=re.compile(regex).findall(items)
                
                
                for itt2 in links:
                    if (added_link+itt) not in f_link_arr and added_link+itt2 not in f_link_arr:
                        f_link_arr.append(added_link+itt2)
                        if itt2=='search':
                            mode=15
            else:
                if (added_link+itt) not in f_link_arr:
                    f_link_arr.append(added_link+itt)
        f_link=False
        if len(f_link_arr)>1:
            f_link='$$$$'.join(f_link_arr)
        elif len(f_link_arr)>0:
            f_link=f_link_arr[0]
        #else:
            
        #    continue
        
        regex='<thumbnail>(.+?)</thumbnail>'
        icon=re.compile(regex).findall(items)
        if len(icon)==0:
            icon=iconimage
        else:
            icon=icon[0]
        regex='<fanart>(.+?)</fanart>'
        fanart=re.compile(regex).findall(items)
        if len(fanart)==0:
            fanart=o_fanart
        else:
            fanart=fanart[0]
        found_cat=False
        regex='<summary>(.+?)</summary>'
        summary=re.compile(regex).findall(items)
        if len(summary)==0:
            plot=" "
        else:
            plot=summary[0]
        trailer=''
        if imdb_id!='':
            trailer = "plugin://%s?mode=25&id=%s&url=%s" % (addon_id,imdb_id,tv_movie)
        for itt in all_plugins:
            
            if '<%s>'%itt in items:
                regex='<%s>(.+?)</%s>'%(itt,itt)
                ur=re.compile(regex).findall(items)[0]
                if itt=='tmdb':
                    itt='tmdb_jen'
                if itt=='trakt':
                    itt='trakt_jen'
                impmodule = __import__(itt.replace('.py',''))
                aa=impmodule.run(ur,lang,icon,fanart,title,title)
                
                all_d.append(aa)
                found_cat=True
                break
                
        if type_record=='dir':
            if not found_cat and f_link:
                if 'message' in f_link:
                    aa=addNolink(title, f_link,194,False,fanart=fanart, iconimage=icon,plot=plot,dont_place=True)
                
                    all_d.append(aa)
                else:
                    aa=addDir3(title,f_link,189,icon,fanart,plot,data=year,original_title=title,trailer=trailer,id=imdb_id)
                    all_d.append(aa)
        else:
            if not f_link:
                
                aa=addNolink(title, 'www',99999,False,fanart=fanart, iconimage=icon,plot=plot,dont_place=True)
                
                all_d.append(aa)
            else:
                if type_record=='item':
                    lk='Jen_link'+url+'$$$$$'+f_link
                else:
                    lk=f_link
                if mode==15:
                
                    aa=addDir3(title,f_link,15,icon,fanart,plot,data=year,original_title=title,trailer=trailer,id=imdb_id)
                    all_d.append(aa)
                else:
                    
                    aa=addLink(title,lk,6,False,icon,fanart,plot,data=year,original_title=title,tmdb=imdb_id,year=year,season=season,episode=episode,trailer=trailer,place_control=True,from_seek=from_seek)
                    all_d.append(aa)
            
    
    if len(search_db)>0 and not search:
        aa=addDir3('[COLOR lightblue][B]Search[/B][/COLOR]',o_url,191,icon,fanart,'Search',search_db=search_db)
        all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    

def play_list(name,url,iconimage,fanart,id,show_original_year,season,episode):
    imdb_id=id
    log.warning('url::'+url)
    if KODI_VERSION<=18:
        from urlparse import urlparse
        urp=urlparse
    else:
        import urllib.parse as urlparse
        urp=urlparse.urlparse
    log.warning('id::'+str(id))
    
    if 'tt' in id:
        
         url_t='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=imdb_id&language=%s'%(id,lang)
         html_im=get_html(url_t).json()
         log.warning('season:::')
         log.warning(html_im)
         log.warning(season)
         if season=='0' or season==' ':
             if len(html_im['movie_results'])>0:
                tmdb=str(html_im['movie_results'][0]['id'])
         else:
            if len(html_im['tv_results'])>0:
                tmdb=str(html_im['tv_results'][0]['id'])
         try:
    
            id=int(tmdb)
            
         except:
            pass
    
    video_data={}
    video_data['title']=name
    video_data['icon']=iconimage
    video_data['original_title']=name
    video_data['plot']=description


    video_data['poster']=fanart
    video_data['poster3']=fanart
    video_data['fanart2']=fanart
    video_data['imdb']=imdb_id
    video_data['code']=imdb_id
    video_data['IMDBNumber']=imdb_id
    video_data['imdbnumber']=imdb_id
    video_data['imdb_id']=imdb_id
    video_data['imdb']=imdb_id
    if season!=None and season!="%20":
       video_data['TVshowtitle']=name
       video_data['mediatype']='episode'
       
    else:
       video_data['mediatype']='movie'
      
    load_resolveurl_libs()
    if '$$$$' in url:
        urls=url.split('$$$$')
        choise=[]
        for ur in urls:
            uri = urp(ur)
            choise.append(uri.netloc)
        ret = xbmcgui.Dialog().select("Choose link", choise)
        url=urls[ret]
    try:
        import resolveurl
    except:
        xbmcgui.Dialog().ok('Error','Need to install Resolveurl')
        return 0
    link =resolveurl .HostedMediaFile (url =url ).resolve ()#line:2687
    if link==False:
        link=url
    if 'plugin://' in link:
        xbmc .executebuiltin ('Container.Update(%s)' %link)#line:2906
    else:
        log.warning('link::'+link)
        listItem = xbmcgui.ListItem( path=link) 
        #listItem.setInfo(type='Video', infoLabels=video_data)
        listItem.setInfo("video", video_data)
        try:
            listItem.setUniqueIDs({ 'imdb': imdb_id, 'tmdb' : '' }, "imdb")
        except:
            pass
            
        listItem.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
def get_jen_files(url,dp,start_time_start):
    global all_jen_links
    url=url.replace(' ','%20')
    log.warning('URL:'+url)
    x=get_html(url,headers=base_header).content()
    regex='<dir>(.+?)</dir>'
    try:
        m=re.compile(regex,re.DOTALL).findall(x)
    except:
        log.warning('Bad url:'+url)
        return 0
    
    for items in m:
        regex='<title>(.+?)</title>'
        title=re.compile(regex).findall(items)
        if len(title)==0:
            regex='<name>(.+?)</name>'
            title=re.compile(regex).findall(items)
            if len(title)==0:
                title=''
            else:
                title=title[0]
        else:
            title=title[0]
        elapsed_time = time.time() - start_time_start
        if KODI_VERSION>18:
            dp.update(0, 'Please wait-'+time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+'Mapping jen...'+'\n'+ title )
        else:
            dp.update(0, 'Please wait-'+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'Mapping jen...', title )
        regex='<link>(.+?)</link>'
        links=re.compile(regex).findall(items)
        for itt in links:
            
            all_jen_links.append(itt)
            
            get_jen_files(itt,dp)
def download_db(url,nm,extract=False,headers={}):
   try:
    file=os.path.join(user_dataDir,nm)
    if os.path.exists(file):
        os.remove(file)
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        from urllib.request import Request, urlopen  # Python 3
    except ImportError:
        from urllib2 import Request, urlopen  # Python 2

    req = Request(url)
    if headers!={}:
        for key in headers:
            req.add_header(key, headers[key])
    response = urlopen(req)
    
    
    CHUNK = 16 * 1024
    file=os.path.join(user_dataDir,nm)
    with open(file, 'wb') as f:
        while True:
            chunk = response.read(CHUNK)
            if not chunk:
                break
            f.write(chunk)
    
    if extract:
        log.warning('Extract:')
        try:
            
            from resources.modules.zfile_18 import ZipFile
        except:
            from zipfile import ZipFile
        xbmc.sleep(500)
        try:
            with contextlib.closing(ZipFile(file , "r")) as z:
                z.extractall(user_dataDir)
        except:
            with ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(user_dataDir)
        log.warning('Done Extract:'+user_dataDir)
    return 'ok'
   except Exception as e:
    xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'),  "בעיה במאסטר")))
    log.warning('ExtractFault:'+str(e))

    return 'Fault'
def search_jen_lists(url):  
    global from_seek
    search_entered=''
    keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
    keyboard.doModal()
    if keyboard.isConfirmed() :
           search_entered = (keyboard.getText().replace("'",""))
           if search_entered=='':
            
                return 0
    dp = xbmcgui . DialogProgress ( )
    if KODI_VERSION>18:
        dp.create('Please wait','Downloading DB...')
        dp.update(0, 'Please wait'+'\n'+'Downloading DB...'+'\n'+ '' )
    else:
        dp.create('Please wait','Downloading DB...', '','')
        dp.update(0, 'Please wait','Downloading DB...', '' )
                  
                        
    
    file=os.path.join(user_dataDir,'search.db')
    html=cache.get(download_db,1,url,'search.db', table='posters')
    if html!=str('ok'):
        html=cache.get(download_db,0,url,'search.db', table='posters')
    if KODI_VERSION>18:
        
        dp.update(0, 'Please wait'+'\n'+'Opening DB...'+'\n'+ '' )
    else:
        
        dp.update(0, 'Please wait','Opening DB...', '' )
    all_d=[]
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    
    dbcon = database.connect(file)
    dbcur = dbcon.cursor()
    

    dbcur.execute("SELECT * FROM search where item like '%{0}%'".format(search_entered))

    
            
    match = dbcur.fetchall()
    
    dbcur.close()
    dbcon.close()
    count=0
    for x,poster in match:
        if KODI_VERSION>18:
        
            dp.update(0, 'Please wait'+'\n'+'Searching DB...'+'\n'+ str(count) )
        else:
            
            dp.update(0, 'Please wait','Searching DB...', str(count) )
        count+=1
        if '<dir>' in x:
            regex='<dir>(.+?)</dir>'
            m=re.compile(regex,re.DOTALL).findall(x)
            
            for items in m:
                
                regex='<title>(.+?)</title>'
                title=re.compile(regex).findall(items)
                if len(title)==0:
                    regex='<name>(.+?)</name>'
                    title=re.compile(regex).findall(items)
                    if len(title)==0:
                        title=''
                    else:
                        title=title[0]
                else:
                    title=title[0]
                log.warning(title)
                
                
                regex='<year>(.+?)</year>'
                year=re.compile(regex).findall(items)
                if len(year)==0:
                    year=''
                else:
                    year=year[0]
                regex='<sublink>(.+?)</sublink>'
                links=re.compile(regex).findall(items)
                f_link_arr=[]
                
                for itt in links:
                    if '(' in itt:
                        itt=itt.split('(')[0]
                    f_link_arr.append(itt)
                
                regex='<link>(.+?)</link>'
                links=re.compile(regex).findall(items)
                for itt in links:
                    if '(' in itt:
                        itt=itt.split('(')[0]
                    f_link_arr.append(itt)
                    
                if len(f_link_arr)>1:
                    f_link='$$$$'.join(f_link_arr)
                elif len(f_link_arr)>0:
                    f_link=f_link_arr[0]
                else:
                    continue
                
                regex='<thumbnail>(.+?)</thumbnail>'
                icon=re.compile(regex).findall(items)
                if len(icon)==0:
                    icon=iconimage
                else:
                    icon=icon[0]
                regex='<fanart>(.+?)</fanart>'
                fanart=re.compile(regex).findall(items)
                if len(fanart)==0:
                    fanart=o_fanart
                else:
                    fanart=fanart[0]
                aa=addDir3(title,f_link,189,icon,fanart,' ',data=year,original_title=title)
                all_d.append(aa)
        if '<item>' in x:
            regex='<item>(.+?)</item>'
            m=re.compile(regex,re.DOTALL).findall(x)
            for items in m:
                regex='<imdb>(.+?)</imdb>'
                imdb_id=re.compile(regex).findall(items)
                if len(imdb_id)==0:
                    imdb_id=''
                else:
                    imdb_id=imdb_id[0]
                regex='<title>(.+?)</title>'
                title=re.compile(regex).findall(items)
                if len(title)==0:
                    regex='<name>(.+?)</name>'
                    title=re.compile(regex).findall(items)
                    if len(title)==0:
                        title=''
                    else:
                        title=title[0]
                else:
                    title=title[0]
                
                regex='<year>(.+?)</year>'
                year=re.compile(regex).findall(items)
                if len(year)==0:
                    year=''
                else:
                    year=year[0]
                regex='<season>(.+?)</season>'
                season=re.compile(regex).findall(items)
                if len(season)==0:
                    season=' '
                else:
                    season=season[0]
                regex='<episode>(.+?)</episode>'
                episode=re.compile(regex).findall(items)
                if len(episode)==0:
                    episode=' '
                else:
                    episode=episode[0]
                
                regex='<sublink>(.+?)</sublink>'
                links=re.compile(regex).findall(items)
                f_link_arr=[]
                
                for itt in links:
                    if '(' in itt:
                        itt=itt.split('(')[0]
                    f_link_arr.append('Direct_link$$$resolveurl'+itt)
                
                regex='<link>(.+?)</link>'
                links=re.compile(regex).findall(items)
                for itt in links:
                    if '(' in itt:
                        itt=itt.split('(')[0]
                    f_link_arr.append('Direct_link$$$resolveurl'+itt)
                
                if len(f_link_arr)>1:
                    f_link='$$$$'.join(f_link_arr)
                elif len(f_link_arr)>0:
                    f_link=f_link_arr[0]
                else:
                    continue
                
                regex='<thumbnail>(.+?)</thumbnail>'
                icon=re.compile(regex).findall(items)
                if len(icon)==0:
                    icon=iconimage
                else:
                    icon=icon[0]
                regex='<fanart>(.+?)</fanart>'
                fanart=re.compile(regex).findall(items)
                if len(fanart)==0:
                    fanart=o_fanart
                else:
                    fanart=fanart[0]
                aa=addLink(title,'Jen_link'+url+'$$$$$'+f_link,6,False,icon,fanart,' ',data=year,original_title=title,tmdb=imdb_id,year=year,season=season,episode=episode,place_control=True,from_seek=True)
                all_d.append(aa)
        if '<plugin>' in x:
            regex='<plugin>(.+?)</plugin>'
            m=re.compile(regex,re.DOTALL).findall(x)
            
            for items in m:
                
                regex='<title>(.+?)</title>'
                title=re.compile(regex).findall(items)
                if len(title)==0:
                    regex='<name>(.+?)</name>'
                    title=re.compile(regex).findall(items)
                    if len(title)==0:
                        title=''
                    else:
                        title=title[0]
                else:
                    title=title[0]
                
                regex='<year>(.+?)</year>'
                year=re.compile(regex).findall(items)
                if len(year)==0:
                    year=''
                else:
                    year=year[0]
                regex='<sublink>(.+?)</sublink>'
                links=re.compile(regex).findall(items)
                f_link_arr=[]
                
                for itt in links:
                    if '(' in itt:
                        itt=itt.split('(')[0]
                    f_link_arr.append(itt)
                
                regex='<link>(.+?)</link>'
                links=re.compile(regex).findall(items)
                for itt in links:
                    if '(' in itt:
                        itt=itt.split('(')[0]
                    f_link_arr.append(itt)
                if len(f_link_arr)>1:
                    f_link='$$$$'.join(f_link_arr)
                elif len(f_link_arr)>0:
                    f_link=f_link_arr[0]
                else:
                    continue
                
                regex='<thumbnail>(.+?)</thumbnail>'
                icon=re.compile(regex).findall(items)
                if len(icon)==0:
                    icon=iconimage
                else:
                    icon=icon[0]
                regex='<fanart>(.+?)</fanart>'
                fanart=re.compile(regex).findall(items)
                if len(fanart)==0:
                    fanart=o_fanart
                else:
                    fanart=fanart[0]
                aa=addLink(title,f_link,6,False,icon,fanart,' ',data=year,original_title=title,year=year,place_control=True,from_seek=True)
                all_d.append(aa)
        
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    dp.close()    
def clean_data(data):
    
    
        
    try:
        a=data.replace ('	','').replace ("\\"," ").replace (': """",',': "" "",').replace (': """"}',': "" ""}').replace (': "",',': " ",').replace (': ""}',': " "}').replace ('""','"').replace ('\n','').replace ('\r','').replace ("OriginalTitle","Originaltitle").replace ('%27',"'")
        a=json.loads(a)
    except:
        log.warning(data.replace ('[',' ').replace (']',' ').replace ('	','').replace ("\\"," ").replace (': """",',': "" "",').replace (': """"}',': "" ""}').replace (': "",',': " ",').replace (': ""}',': " "}').replace ('""','"').replace ('\n','').replace ('\r','').replace ("OriginalTitle","Originaltitle").replace ('%27',"'"))
        a={}
    
    return a
def master_addon(url,iconimage,o_fanart,heb_name,type_search,page,o_plot):
    global sort_by_episode
    o_url=url
    progress_master=Addon.getSetting('progress_master')=='true'
    remove_keys=["heb title","icon","imdb","poster","studios","tmdb"]
    
    try:
        page=int(page)
    except:
        page=0
    if page==0:
        added_index=0
    else:
        added_index=1
    
    if progress_master:
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create('Please wait','Downloading DB...')
            dp.update(0, 'Please wait'+'\n'+'Downloading DB...'+'\n'+ '' )
        else:
            dp.create('Please wait','Downloading DB...', '','')
            dp.update(0, 'Please wait','Downloading DB...', '' )
                  
                        
    
    file=os.path.join(user_dataDir,'master.db')
    refresh_rate=int(Addon.getSetting('refresh_rate'))
    html=cache.get(download_db,refresh_rate,url,'master.db',True, table='posters')
    if html!=str('ok'):
        html=cache.get(download_db,0,url,'master.db',True, table='posters')
    if progress_master:
        if KODI_VERSION>18:
            
            dp.update(0, 'Please wait'+'\n'+'Opening DB...'+'\n'+ '' )
        else:
            
            dp.update(0, 'Please wait','Opening DB...', '' )
    all_d=[]
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    
    file=os.path.join(user_dataDir,'localfile.txt')
    dbcon = database.connect(file)
    dbcur = dbcon.cursor()
    log.warning('type_search:'+type_search)
    
    heb_name=heb_name.replace(' ','')
    if type_search=='latest_movies':
        st_type ='\'%"mediatype": "movie"%\''#line:3423
        dbcur.execute("SELECT * FROM MyTable where type='item' and data like "+st_type )
    elif type_search=='latest_tv':
        st_type ='\'%"mediatype": "tv"%\''#line:3425
        dbcur.execute("SELECT * FROM MyTable where type='item' and data like "+st_type )
    elif type_search=='category_selected':
        if o_plot =='1-2':#line:3194
           dbcur .execute ("SELECT * FROM MyTable WHERE  name LIKE '0%' or name LIKE '1%' or name LIKE '2%' or name LIKE '3%' or name LIKE '4%' or name LIKE '5%' or name LIKE '6%' or name LIKE '7%' or name LIKE '8%' or name LIKE '9%' ")#line:3196
        else :#line:3197
           st_type ='\'%"mediatype": "movie"%\''#line:3423
           dbcur .execute ("SELECT * FROM MyTable WHERE name like '{0}%' and type='item' and data like {1}".format (o_plot,st_type ))#line:3198
    elif type_search=='category_selected_full':
           st_type ='\'%"mediatype": "movie"%\''#line:3423
           dbcur .execute ("SELECT * FROM MyTable WHERE genre like '%{0}%' and type='item' and data like {1}".format (o_plot,st_type ))#line:3198
    elif type_search=='search':
        search_entered=''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
        keyboard.doModal()
        if keyboard.isConfirmed() :
               search_entered = (keyboard.getText().replace("'",""))
               if search_entered=='':
                return 0
        dbcur .execute ("SELECT * FROM MyTable where name like '%{0}%'".format (search_entered ))#line:2995
        
        
    else:
        
        dbcur.execute("SELECT * FROM MyTable where REPLACE(father,' ','')=REPLACE('%s',' ','')"%heb_name)
        
    
            
    match = dbcur.fetchall()

    dbcur.close()
    dbcon.close()
    prev_name=heb_name
    all_data=[]
    count=0
    next_page_en=False
    per_page=int(Addon.getSetting('num_per_page'))
    
    
    sort_by_episode=False
    sort_by_ab=False
    for index,name,link,icon,fanart,plot,data,date,year,genre,father,type in match:
        icon=icon.strip()
        fanart=fanart.strip()
        data = clean_data(data)
        if type_search=='search':
            prev_name=father
            
        if KODI_VERSION<=18:
            name=name.encode('utf-8')
        if type_search=='latest_movies':
            try:
                dateadded=data['dateadded']
                data['plot']=data['dateadded']+'\n'+data['plot']
                plot=data['dateadded']+'\n'+plot
                data['title']=name.replace('%27',"'")
                
            except:
                
                dateadded='2020-01-01 01:01:00'
                pass
            season=' '
            episode=' '
            if 'Season' in data:
                season=data['Season']
            if 'Episode' in data:
                episode=data['Episode']
            original_title=data.get('originaltitle',name)
            
            id=data.get('tmdb',' ')
            if id==' ':
                    id=data.get('imdb',' ')
            for item in remove_keys:
                try:
                    data.pop(item, None)
                except:
                    pass
            try:
                if data['plot']=='':
                    data['plot']=plot
            except:
                pass
            try:
                trailer = "plugin://%s?mode=25&id=%s&url=%s" % (addon_id,id,'movie')
            except:
                trailer = ''
            if not dateadded:
                dateadded='2020-01-01 01:01:00'
            all_data.append((name.replace ('%27',"'"),'Jen_link$$$$Matser_link'+link,icon,fanart,plot.replace ('%27',"'"),id,original_title,year,data,year,season,episode,dateadded,trailer))
        elif type_search=='latest_tv':
            original_title=data.get('originaltitle',name)
            season=' '
            episode=' '
            if 'Season' in data:
                season=data['Season']
            if 'Episode' in data:
                episode=data['Episode']
                
            try:
                dateadded=data['dateadded']
                data['plot']=data['dateadded']+'\n'+data['plot']
                plot=data['dateadded']+'\n'+plot
                data['title']=original_title.replace(' - IMDb','')+' season % episode %s'%(season,episode)
            except:
                dateadded='2020-01-01 01:01:00'
                pass
            
            
            id=data.get('tmdb',' ')
            if id==' ':
                    id=data.get('imdb',' ')
            for item in remove_keys:
                try:
                    data.pop(item, None)
                except:
                    pass
            if not dateadded:
                    dateadded='2020-01-01 01:01:00'
            all_data.append((original_title.replace(' - IMDb','')+' season % episode %s'%(season,episode),'Jen_link$$$$Matser_link'+link,icon,fanart,plot.replace ('%27',"'"),id,original_title,year,data,year,season,episode,dateadded,''))
        
        else:
            if type=='category':
                if 'tvshowtitle' in data:
                    sort_by_ab=True
                
                try:
                    if data['plot']=='':
                            data['plot']=plot
                except:
                    pass
                aa=addDir3(name.replace ('%27',"'"),o_url,193,icon,fanart,plot.replace ('%27',"'"),data=year,video_info=data,id='11',heb_name=prev_name+name,tmdbid='categoty' )
                all_d.append(aa)
            else:
                season=' '
                episode=' '
                
                if 'Season' in data:
                    season=data['Season']
                if 'Episode' in data:
                    episode=data['Episode']
                    try:
                        e=int(episode)
                        sort_by_episode=True
                    except:
                        pass
                        
                    
                log.warning('episode:'+episode)
                try:
                    dateadded=data['dateadded']
                    data['plot']=data['dateadded']+'\n'+data['plot']
                    plot=data['dateadded']+'\n'+plot
                    data['title']=name.replace('%27',"'")
                except:
                    dateadded='2020-01-01 01:01:00'
                    log.warning('Error date:'+str(data))
                    pass
              
                original_title=data.get('originaltitle',name)
                id=data.get('tmdb',' ')
                if id==' ':
                        id=data.get('imdb',' ')
                try:
                    trailer = "plugin://%s?mode=25&id=%s&url=%s" % (addon_id,id,data['mediatype'])
                except:
                    trailer =''
                
                
                #aa=addLink(name.replace ('%27',"'"),'Jen_link$$$$Matser_link'+link,6,False,icon,fanart,plot.replace ('%27',"'"),tmdb=id,original_title=original_title,data=year,video_info=data,year=year,season=season,episode=episode,place_control=True,trailer=trailer)
                #all_d.append(aa)
                for item in remove_keys:
                    try:
                        data.pop(item, None)
                    except:
                        pass
                if not dateadded:
                    dateadded='2020-01-01 01:01:00'
                all_data.append((name.replace ('%27',"'"),'Jen_link$$$$Matser_link'+link,icon,fanart,plot.replace ('%27',"'"),id,original_title,year,data,year,season,episode,dateadded,trailer))
                
             
   
    log.warning('sort_by_ab:'+str(sort_by_ab))
    if len(all_data)>0:#type_search=='latest_movies' or type_search=='latest_tv':
        count=0
        import datetime #line:1601
        import _strptime #line:1602
        if not sort_by_ab:
            
                all_data=sorted(all_data, key=lambda x:  time.strptime(x[12], '%Y-%m-%d %H:%M:%S'), reverse=True)
            
        #all_data.sort(key = lambda x: datetime.strptime(x[12], '%Y-%m-%d %H:%M:%S')) 
        for name,link,icon,fanart,plot,id,original_title,year,data,year,season,episode,dateadded,trailer in all_data:
               
                if count>=((page*per_page)+added_index):
                    aa=addLink(name,link,6,False,icon,fanart,plot,tmdb=id,original_title=original_title,data=year,video_info=data,year=year,season=season,episode=episode,place_control=True,trailer=trailer)
                    all_d.append(aa)
                if count>((page+1)*per_page):
                   
                    next_page_en=True
                    break
                count+=1
        
    if type_search=='' or type_search=='%20':
        aa=addDir3('[B][COLOR burlywood]-סרטים אחרונים- [/COLOR][/B]',o_url,193,iconimage,o_fanart,'סרטים אחרונים',tmdbid='latest_movies' )
        all_d.append(aa)
        aa=addDir3('[B][COLOR burlywood]-פרקים אחרונים- [/COLOR][/B]',o_url,193,iconimage,o_fanart,'פרקים אחרונים',tmdbid='latest_tv' )
        all_d.append(aa)
        aa=addDir3('[B][COLOR burlywood]לפי א-ב[/COLOR][/B]',o_url,194,iconimage,o_fanart,'לפי א-ב' )
        all_d.append(aa)
        aa=addDir3('[B][COLOR burlywood]קטגוריות[/COLOR][/B]',o_url,197,iconimage,o_fanart,'לפי א-ב' )
        all_d.append(aa)
        aa=addDir3('[B][COLOR burlywood]חיפוש[/COLOR][/B]',o_url,193,iconimage,o_fanart,'חיפוש',tmdbid='search' )
        all_d.append(aa)
    elif next_page_en:
        aa=addDir3('[COLOR aqua][I]עמוד הבא[/I][/COLOR]',o_url,193,iconimage,o_fanart,o_plot,tmdbid=type_search,dates=str(page+1),heb_name=prev_name)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    if progress_master:
        dp.close()
    
    if sort_by_episode:
        xbmcplugin .addSortMethod (int (sys .argv [1 ]),xbmcplugin .SORT_METHOD_EPISODE )#line:3759
    if sort_by_ab:
        log.warning('sort_by_ab2')
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_SORT_TITLE)
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_YEAR)

        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_RATING)
def cat_select(iconimage,fanart,url):
    all_cat =['1-2','א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']#line:3176
    all_d=[]
    for itt in all_cat :#line:3177
        all_d .append (addDir3 (itt ,url,193 ,iconimage,fanart,itt,tmdbid='category_selected' ))#line:3178
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def cat_full_select(iconimage,fanart,url):
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'localfile.txt')
    
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    ur ='https://api.themoviedb.org/3/genre/movie/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language=he'#line:3155
    result =get_html (ur ).json ()#line:3156
    all_d=[]
    for item in result ['genres']:#line:3157
        dbcur .execute ("SELECT * FROM MyTable where data like '%{0}%'".format (item ['name']))#line:3159
        match =dbcur .fetchone ()#line:3161
        if match !=None :#line:3162
          
            all_d .append (addDir3 (item ['name'] ,url,193 ,iconimage,fanart,item ['name'],tmdbid='category_selected_full' ))#line:3178
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    dbcur.close()
    dbcon.close()
def c_release_get(idd):
    url='https://api.themoviedb.org/3/movie/%s/release_dates?api_key=fb981e5ab89415bba616409d5eb5f05e'%idd
   
    x=get_html(url).json()
    stop=False
    for items in x['results']:
        
        if stop:
            break
        stop=False
        for oee in items['release_dates']:
            
            if oee['type']>=4:
                return oee['release_date'].split('T')[0]
                stop=True
                break
    return False
    
def check_q(name,url,year,id,check_ok=False):
 
    log.warning("DVD r")
    log.warning(name)
    name=name.replace('%20',' ').replace('%27',"'").replace('%3a',':')
    dp = xbmcgui . DialogProgress ( )
    if KODI_VERSION>18:
        dp.create('Please wait','Cehcking Quality...')
    else:
        dp.create('Please wait','Cehcking Quality...', '','')
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'Cehcking Quality...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','Cehcking Quality...', '' )
        
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    }

    params = (
        ('q', name+' (%s)'%year),
    )
    
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'Sending Quary...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','Sending Quary...', '' )
    response = get_html('https://www.dvdsreleasedates.com/livesearch.php', headers=headers, params=params).content()
    
    regex='<a href=\'(.+?)\'><span class="lsbold">(.+?) \((.+?)\)</span></a>'
    m=re.compile(regex).findall(response)
  
    txt_f=[]
    found=0
    
    unknow=0
    m_Direct=[]
    tet_txt=''
    if len (m)==0:
        if KODI_VERSION>18:
            dp.update(0, 'Please wait'+'\n'+'Sending Second Quary...'+'\n'+ '' )
        else:
            dp.update(0, 'Please wait','Sending Second Quary...', '' )
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.dvdsreleasedates.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.dvdsreleasedates.com/search/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        data = {
          'searchStr': name+' (%s)'%year
        }
        log.warning(data)
        response = get_html('https://www.dvdsreleasedates.com/search/', headers=headers,  data=data,post=True).content()
        regex="<span class='future '>(.+?)<"
        m_Direct=re.compile(regex,re.DOTALL).findall(response)
        for ite in m_Direct:
            
            color='red'
            
            
            txt_f.append(('[COLOR %s]'%color+ite.strip()+'[/COLOR]'))
            tet_txt=ite.strip()
            svn=name
        if len(m_Direct)==0:
            regex="<td class='dvdcell'><a href='(.+?)'><img class='movieimg'.+?title='(.+?)'"
            m=re.compile(regex).findall(response)
            log.warning('m:')
            log.warning(response)
            log.warning(m)
            if len(m)==0:
                unknow=1
            ff=0
            nlk=''
            for lk ,nm in m:
                if KODI_VERSION>18:
                    dp.update(0, 'Please wait'+'\n'+'Checking...'+'\n'+ '' )
                else:
                    dp.update(0, 'Please wait','Checking...', '' )
                
                if 1:#name.lower().strip().decode('utf8') in nm.lower().strip().decode('utf8'):
                    ff=1
                    nlk=lk
                    break
            
            if ff==0:
                m=[]
            else:
                m=[]
                m.append((nlk,nm,year))
    
    
    if len(m_Direct)==0:
        svn=name
        for lk,nm,yr in m:
            if KODI_VERSION>18:
                dp.update(0, 'Please wait'+'\n'+'Checking...'+'\n'+ nm )
            else:
                dp.update(0, 'Please wait','Checking...', nm )
            if 1:#nm.lower()==name.lower() and yr==year:
                x=get_html('https://www.dvdsreleasedates.com'+lk,headers=base_header).content()
                
                regex="<div class='disccellinfo'><b>(.+?)</b>.+?Release Date</span> <span class='(.+?)<"
                       
                m2=re.compile(regex,re.DOTALL).findall(x)
                
                for ty,whda in m2:
                    wh=whda.split('>')[0]
                    da=whda.split('>')[1]
                    
                    if 'future' in wh:
                        color='red'
                    else:
                        color='lightgreen'
                        found=1
                    
                    #txt_f.append(('[COLOR lighblue]'+ty+'[/COLOR] - [COLOR %s][I]'%color+da+'[/COLOR]'))
                    txt_f.append(('[COLOR lightblue]'+ty.strip()+'[/COLOR] - [COLOR %s]'%color+da.strip()+'[/COLOR]'))
                    tet_txt=da.strip()
                    svn=nm
                regex="<span class='future '>(.+?)<"
                m2=re.compile(regex,re.DOTALL).findall(x)
                for ite in m2:
                    
                    color='red'
                    
                    
                    txt_f.append(('[COLOR %s]'%color+ite.strip()+'[/COLOR]'))
                    tet_txt=ite.strip()
                    svn=nm
    dp.close()
    digital_release=c_release_get(id)
    if digital_release:
        txt_f.append(('[COLOR lightgreen]Digital Release At: '+digital_release.strip()+'[/COLOR]'))
        tet_txt=digital_release.strip()
        svn=name
        found=1
    if len(txt_f)==0 :
        unknow=1
    if 1:#check_ok==False:
        if len(txt_f)>0 :
            
            xbmc.executebuiltin('ActivateWindow(%d)' % 10147)
            window = xbmcgui.Window(10147)
            xbmc.sleep(100)
            if found==0:
                add_t=' Not released '+svn
            else:
                add_t=' Released '+svn
            window.getControl(1).setLabel(add_t)
            window.getControl(5).setText('\n'.join(txt_f)+'\n\n')
            #window.close()
        else:
            unknow=1
        if unknow==1:
            xbmc.executebuiltin('ActivateWindow(%d)' % 10147)
            window = xbmcgui.Window(10147)
            xbmc.sleep(100)
            
            window.getControl(1).setLabel(svn)
            window.getControl(5).setText('Unknown'+'\n\n')
            #window.close()
    else:
        logging.warning('found:'+str(found))
        res=False
        if found==1  :
            res=True
        if unknow==1:
            res=True
       
        return res,sub1,tet_txt,unknow



params=get_params()

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 16...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 16...', '' )


selected_scrapers='All'
url=None
name=''
mode=None
iconimage=None
fanart=None
description=None
data=None
original_title=None
read_data2=''
id='0'
dates='0'
season='0'
episode='0'
show_original_year='0'
nextup='true'
dd=''
video_data={}
get_sources_nextup='false'
all_w={}
use_filter='true'
use_rejected='true'
heb_name=''
tmdbid=''
has_alldd='false'
prev_name=''
search_db=''
mypass=""
try:
        url=unque(params["url"])
except:
        pass
try:
        name=unque(params["name"])
except:
        pass
try:
        iconimage=unque(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=unque(params["fanart"])
except:
        pass
try:        
        description=unque(params["description"])
except:
        pass
try:        
        data=(params["data"])
except:
        pass
try:        
        original_title=unque(params["original_title"])
except:
        pass
        
try:        
        id=(params["id"])
except:
        pass
try:        
        season=(params["season"])
except:
        pass
try:        
        episode=(params["episode"])
except:
        pass
try:        
        show_original_year=(params["show_original_year"])
except:
        pass
try:        
        dd=(params["dd"])
except:
        pass
try:        
        nextup=(params["nextup"])
except:
        pass
try:        
        dates=(params["dates"])
except:
        pass
try:        
        video_data=unque(params["video_data"])
except:
        pass
try:        
        get_sources_nextup=(params["get_sources_nextup"])
except:
        pass
        
try:        
        all_w=unque(params["all_w"])
except:
        pass
        
try:        
        use_filter=(params["use_filter"])
except:
        pass
        
try:        
        use_rejected=(params["use_rejected"])
except:
        pass
try:        
        heb_name=unque(params["heb_name"])
except:
        pass
        
try:        
        tmdbid=str(params["tmdbid"])
except:
        pass
try:        
        has_alldd=str(params["has_alldd"])
except:
        pass
prev_name=name
try:        
        prev_name=unque(params["prev_name"])
except:
        pass
try:        
        search_db=unque(params["search_db"])
except:
        pass

try:        
        from_seek=(params["from_seek"])=='True'
except:
        pass
try:
    mypass=unque(params["mypass"])
except:
        pass
log.warning('mode:'+str(mode))
log.warning('url:'+str(url))
log.warning('from_seek:'+str(from_seek))
log.warning(name)
log.warning(original_title)
log.warning(fanart)
log.warning(heb_name)

try:
    url=url.replace(' ','%20')  
except:
    pass

      

#html=cache.get(cfscrape_version,24, table='posters')
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

public.pre_mode=mode

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time+777)
if Addon.getSetting("full_db")=='true':
    
    if KODI_VERSION>18:
        dp_full.update(0, 'Please wait'+'\n'+'Level 17...'+'\n'+ '' )
    else:
        dp_full.update(0, 'Please wait','Level 17...', '' )
    dp_full.close()
if mode==None :
       elapsed_time = time.time() - start_time_start
       time_data.append(elapsed_time+555)
       time_data= main_menu(time_data)
        

elif mode==2:
    movie_world()
elif mode==3:
    tv_show_menu()
elif mode==5:
    
    from resources.modules.tmdb import get_movies
    search_entered=''
    keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
    keyboard.doModal()
    if keyboard.isConfirmed() :
           search_entered = que(keyboard.getText().replace("'",""))
           if search_entered=='':
            sys.exit()
    dp = xbmcgui . DialogProgress ( )
    if KODI_VERSION>18:
        dp.create('Please wait','Searching...')
    else:
        dp.create('Please wait','Searching...', '','')
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'Searching...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','Searching...', '' )
    thread=[]
    
    thread.append(Thread(search_tvdb,search_entered))
   
    thread[0].start()
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'get_movies...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','get_movies...', '' )
    addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32024), id,27,False,fanart=' ', iconimage=' ',plot=' ')
    get_movies('http://api.themoviedb.org/3/search/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&query={0}&language={1}&append_to_response=origin_country&page=1'.format(search_entered,lang),global_s=True)
    
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'Get Tv...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','Get Tv...', '' )
        
    addNolink( '[COLOR blue][I]%s[/I][/COLOR]'%Addon.getLocalizedString(32099), id,27,False,fanart=' ', iconimage=' ',plot=' ')
    get_movies('http://api.themoviedb.org/3/search/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&query={0}&language={1}&page=1'.format(search_entered,lang),global_s=True)
    addNolink( '[COLOR blue][I]TVDB[/I][/COLOR]', id,27,False,fanart=' ', iconimage=' ',plot=' ')
    log.warning('http://api.themoviedb.org/3/search/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&query={0}&language={1}&page=1'.format(search_entered,lang))
    if KODI_VERSION>18:
        dp.update(0, 'Please wait'+'\n'+'Get TvDb...'+'\n'+ '' )
    else:
        dp.update(0, 'Please wait','Get TvDb...', '' )
    while(1):
        num_live=0
        still_alive=0
        if not thread[0].is_alive():
              num_live=num_live+1
              
        else:
                still_alive=1
        if still_alive==0:
            break
        xbmc.sleep(100)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),tvdb_results,len(tvdb_results))
    dp.close()
elif mode==6:

    play_link(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dd,heb_name,prev_name=prev_name,has_alldd=has_alldd,nextup=nextup,video_data_exp=video_data,get_sources_nextup=get_sources_nextup,all_w=all_w,tvdb_id=tmdbid)
elif mode==14:
   
    from resources.modules.tmdb import get_movies
    
    log.warning('url:'+str(url))
    if '/search/tv' in url and 'page=1' in url :
        
        
        if '%' in url:
            search_entered=''
            keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
            keyboard.doModal()
            if keyboard.isConfirmed() :
                   search_entered = que(keyboard.getText().replace("'",""))
                   if search_entered=='':
                    sys.exit()
            
        else:
            
            regex='&query=(.+?)&'
            search_entered=re.compile(regex).findall(url.replace(' ','%20'))[0]
        dp = xbmcgui . DialogProgress ( )
        if KODI_VERSION>18:
            dp.create('Please wait','Searching...')
        else:
            dp.create('Please wait','Searching...', '','')
        if KODI_VERSION>18:
            dp.update(0, 'Please wait'+'\n'+'Searching TMDB...'+'\n'+ '' )
        else:
            dp.update(0, 'Please wait','Searching TMDB...', '' )
            
        thread=[]
        thread.append(Thread(search_tvdb,search_entered))
   
        thread[0].start()
    
        
            
        get_movies('http://api.themoviedb.org/3/search/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&query={0}&language={1}&page=1'.format(search_entered,lang),global_s=True)
        addNolink( '[COLOR blue][I]TVDB[/I][/COLOR]', id,27,False,fanart=' ', iconimage=' ',plot=' ')
        if KODI_VERSION>18:
            dp.update(0, 'Please wait'+'\n'+'Searching TVDB...'+'\n'+ '' )
        else:
            dp.update(0, 'Please wait','Searching TVDB...', '' )
            
        while(1):
            num_live=0
            still_alive=0
            if not thread[0].is_alive():
                  num_live=num_live+1
                  
            else:
                    still_alive=1
            if still_alive==0:
                break
            xbmc.sleep(100)
        if KODI_VERSION>18:
            dp.update(0, 'Please wait'+'\n'+'Placing Results...'+'\n'+ '' )
        else:
            dp.update(0, 'Please wait','Placing Results...', '' )
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),tvdb_results,len(tvdb_results))
        dp.close()
    else:
        get_movies(url.replace(' ','%20'))
elif mode==15:
    #log.warning(name)
    #log.warning(original_title)
    #sys.exit()
    log.warning('Get Sources')
    log.warning(season)
    log.warning(episode)
    get_sources(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,heb_name,video_data_exp=video_data,all_w=all_w,use_filter=use_filter,use_rejected=use_rejected,tvdb_id=tmdbid)
elif mode==16:
    
    if 'tvdb' in id :
        url2='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=tvdb_id&language=%s'%(id.replace('tvdb',''),lang)
        pre_id=get_html(url2).json()['tv_results']
        
        if len(pre_id)>0:
            id=str(pre_id[0]['id'])
    elif 'imdb' in id:
        url2='https://'+'api.themoviedb.org/3/find/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&external_source=imdb_id&language=%s'%(id.replace('imdb',''),lang)
       
        pre_id=get_html(url2).json()['tv_results']
        
        if len(pre_id)>0:
            id=str(pre_id[0]['id'])
    from resources.modules.tmdb import get_seasons
    
    get_seasons(name,url,iconimage,fanart,description,data,original_title,id,heb_name)
elif mode==18:
    get_genere(url)
elif mode==19:
    from resources.modules.tmdb import get_episode
    get_episode(name,url,iconimage,fanart,description,data,original_title,id,season,tmdbid,show_original_year,heb_name)
elif mode==20:
    get_tv_maze(url,iconimage)
elif mode==21:
    trakt_world()
elif mode==25:
    play_trailer(id,url,description)
elif mode==34:
    remove_from_trace(name,original_title,id,season,episode)
elif mode==35:
    
    ClearCache()
elif mode==65:
    add_remove_trakt(name,original_title,id,season,episode)
elif mode==72: 
    by_actor(url,iconimage,fanart)
elif mode==73: 
    actor_m(url,description)
elif mode==74: 
    search_actor()
elif mode==101:
    tv_neworks()
elif mode==112:
    movie_prodiction()

elif mode==114:
    main_trakt()
elif mode==115:
    from resources.modules.trakt import progress_trakt
    progress_trakt(url)
elif mode==116:
    from resources.modules.trakt import get_trakt
    get_trakt(url)
elif mode==117:
    from resources.modules.trakt import get_trk_data
    get_trk_data(url)
elif mode==118:
    from resources.modules.trakt import trakt_liked
    trakt_liked(url,iconimage,fanart)
elif mode==119:
    from resources.modules.trakt import get_simple_trakt
    get_simple_trakt(url)
elif mode==137:
    clear_rd()
elif mode==138:
    re_enable_rd()
elif mode==139:
    clear_pr()
elif mode==140:
    re_enable_pr()
elif mode==141:
    clear_all_d()
elif mode==142:
    re_enable_all_d()
elif mode==143:
    search_history(url,iconimage,fanart)
elif mode==144:
   last_played()
elif mode==145:
   #read_data2,enc_data,all_folders,url_o=last_viewed(url)
   read_data2,enc_data,all_folders,url_o=cache.get(last_viewed,24,url, table='last_view')
   aa=[]
   if len(all_folders)>0:
        
        
        for name, url,mode, icon,added_res_trakt,all_w,heb_name,fanart,data_ep,plot,original_title,id,season,episode,eng_name,watched,show_original_year,dates,dd in all_folders:
            aa.append(addNolink(name, url,mode,False, iconimage=icon,all_w_trk=added_res_trakt,all_w=all_w,heb_name=heb_name,fanart=fanart,data=data_ep,plot=plot,original_title=original_title,id=id,season=season,episode=episode,eng_name=eng_name,watched=watched,show_original_year=show_original_year,dates=dates,dd=dd,dont_place=True))
            
        if Addon.getSetting("trakt_access_token")!='' and url_o=='tv':
            aa.append(addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32114), id,157,False,fanart='https://bestdroidplayer.com/wp-content/uploads/2019/06/trakt-what-is-how-use-on-kodi.png', iconimage=BASE_LOGO+'ghost1.png',plot=' ',dont_place=True))
            
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
elif mode==146:
    log.warning(name)
    log.warning(original_title)
    s_tracker(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dates,heb_name)
elif mode==147:
    clear_trakt()
elif mode==148:
    clear_search(url)
elif mode==149:
    show_updates(force=True)
elif mode==150:
    from resources.modules.trakt import manager
   
    manager(name, url, data)
elif mode==151:
    Addon.openSettings()
elif mode==157:
    ok=xbmcgui.Dialog().yesno("Override",('%s (%s)'%(Addon.getLocalizedString(32150),Addon.getAddonInfo('name'))))
    remove_db=False
    show_msg=True
    if ok:
        remove_db=True
        show_msg=False
    sync_trk(removedb=False,show_msg=show_msg)
    if remove_db:
        show_msg=True
        sync_trk(removedb=True,show_msg=show_msg)
    ClearCache()
    xbmc.executebuiltin('Container.Refresh')
elif mode==158:
    was_i()
elif mode==159:
    remove_was_i(name,id,season,episode)
elif mode==160:
    from resources.modules.trakt import remove_trk_resume
    remove_trk_resume(name,id,season,episode,data)
elif mode==162:
    clear_was_i()
elif mode==163:
    
    #from resources.modules import logupload
    #logupload.start()
    from resources.modules.logupload import logupload_new
    logupload_new()
elif mode==164:
    from resources.modules.trakt import resume_episode_list
    resume_episode_list(url)
elif mode==166:
    from resources.modules.trakt import get_simple_trk_data
    get_simple_trk_data(url)
elif mode==167:
    set_view_type(str(url))
elif mode==168:
    rd_history(url)
elif mode==169:
    rd_history_torrents()
elif mode==170:
    simple_play(name,url)
elif mode==171:
    remove_rd_history(name,id)
elif mode==172:
    server_test()
elif mode==173:
    en_dis_scrapers(name,url)
elif mode==174:
    classic_movies(url)
elif mode==175:
    listItem = xbmcgui.ListItem(name, path=url) 
    listItem.setInfo(type='Video', infoLabels={'title':name})
    ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
elif mode==176:
    westwern_movies(url)
elif mode==177:
    get_cast(url,id,season,episode)
elif mode==178:
    get_3d(url)
elif mode==179:
    collection_detials(id)
elif mode==180:
      try:
        path=xbmc_tranlate_path('special://home/addons/script.module.resolveurl/lib')
        sys.path.append( path)
        path=xbmc_tranlate_path('special://home/addons/script.module.six/lib')
        sys.path.append( path)
        path=xbmc_tranlate_path('special://home/addons/script.module.kodi-six/libs')
        sys.path.append( path)
        import resolveurl
        resolveurl.display_settings()
      except:
        pass
elif mode==181:
    all_test_menu(iconimage,fanart)
elif mode==182:
    run_system_test(url)
elif mode==183:
    imdb_menu(iconimage,fanart)
elif mode==184:
    get_imdb_lists(url,iconimage,fanart)
elif mode==185:
    fill_imdb_list(url)
elif mode==186:
    xbmc.executebuiltin('Addon.OpenSettings(script.module.fenomscrapers)')
elif mode==187:
    get_keywords_ab(iconimage,fanart)
elif mode==188:
    get_keywords(url,iconimage,fanart,dates)
elif mode==189:
    if ".json" in url or ".m3u8" in url:
        populate_json_playlist(url,iconimage,fanart,search_db,mypass=mypass)
    else:
        populate_playlist(url,iconimage,fanart,search_db,mypass=mypass)
elif mode==190:
    play_list(name,url,iconimage,fanart,id,show_original_year,season,episode,mypass=mypass)
elif mode==191:
    populate_playlist(url,iconimage,fanart,search_db,search=True,mypass=mypass)
    #search_jen_lists(search_db)
elif mode==192:
    tmdb_lists(id)
elif mode==193:
    try:
        id=unque(id)
    except:
        pass
    url=url.replace(' ','%20')
    id=id.replace(' ','%20')
    plugin_dir = os.path.join(addonPath, 'resources', 'plugins')
    
    sys.path.append( plugin_dir)
    impmodule = __import__(url.replace('.py',''))
    aa=impmodule.next_level(url,iconimage,fanart,description,name,id)
elif mode==194:
    logging.warning(url)
    furl=re.compile('message\((.+?)\)').findall(url)
    if len(furl)==0:
        x=get_html(url.split('message/')[1]).content()
        showText(name,x)
    else:
        x=get_html(furl[0]).content()
        showText(name,x)
elif mode==195:
    check_q(name,url,show_original_year,id)
elif mode==198:
    from  resources.list_module import m4ufree
    m4ufree.main_list()
elif mode==199:
    from  resources.list_module import m4ufree
    m4ufree.m_list(name,url,iconimage,fanart)
match=[]
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if Addon.getSetting("display_lock")=='true':
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s (""mode TEXT,""name TEXT, ""id TEXT, ""type TEXT, ""free TEXT,""free2 TEXT);"%'views')
    try:
        dbcur.execute("SELECT * FROM views where (mode='%s' or free='global')"%(str(mode)))


                
        match = dbcur.fetchall()
    except:
        match=[]
    dbcur.close()
    dbcon.close()
all_modes={}


type='%s default'%Addon.getAddonInfo('name')
for pre_mode,name,display_id,type,free1,free2 in match:
        all_modes[pre_mode]=display_id

if pre_mode=='global':
    type='%s default'%Addon.getAddonInfo('name')
log.warning('type:'+type)
if type=='files' or type=='movies' or type=='tvshows' or type=='episodes':
    #log.warning('setContent:'+type)
    xbmcplugin.setContent(int(sys.argv[1]), type)
else:
    log.warning('Mode display:'+str(mode))
    if mode==2 or mode==3 or mode==114 or mode==112 or mode==101:
        xbmcplugin.setContent(int(sys.argv[1]), 'files')
    elif mode==16 :
       xbmcplugin.setContent(int(sys.argv[1]), 'seasons')
    elif mode==19 or mode==20 or sort_by_episode:
       xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    else:
        log.warning('Set Type:movies')
        xbmcplugin.setContent(int(sys.argv[1]), 'movies')


elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
str_time_data=[]
for i in time_data:
    str_time_data.append(str(i))
if Addon.getSetting("debug")=='true' and Addon.getSetting("check_time")=='true':

    showText('Times', '\n'.join (str_time_data))
    
xbmcplugin.endOfDirectory(int(sys.argv[1]))
log.warning('pre_mode:'+str(pre_mode))
log.warning(all_modes)
s_mode=str(mode)
if len(all_modes)>0 and s_mode in all_modes:
    xbmc.sleep(100)
    
    log.warning(all_modes[s_mode])

    log.warning('Container.SetViewMode(%d)' % int(all_modes[s_mode]))
    xbmc.executebuiltin('Container.SetViewMode(%d)' % int(all_modes[s_mode]))

log.warning('Done')

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
if mode==None:
    thread=[]
    thread.append(Thread(show_updates))
    thread[len(thread)-1].setName('Show updates')
    thread[0].start()
