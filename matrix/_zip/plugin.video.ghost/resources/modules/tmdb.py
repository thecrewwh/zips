 # -*- coding: utf-8 -*-
from  resources.modules.public import addNolink,addDir3,addLink,lang,user_dataDir

import threading,urllib,os
import re,logging,sys,time
import xbmcaddon,xbmc,xbmcgui
import xbmcplugin,json
Addon = xbmcaddon.Addon()
from resources.modules import cache
from  resources.modules.client import get_html
from resources.modules import log
domain_s='https://'
from  resources.modules.general import fix_q,post_trakt,addon_id
from  resources.modules.general import call_trakt,BASE_LOGO,base_header

KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    que=urllib.quote_plus
else:
    que=urllib.parse.quote_plus
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus

if KODI_VERSION<=18:
    xbmc_tranlate_path=xbmc.translatePath
else:
    import xbmcvfs
    xbmc_tranlate_path=xbmcvfs.translatePath
global all_release_dates
all_release_dates={}
def adv_gen_window(url):
    from  resources.modules import pyxbmct
    class adv_gen_window(pyxbmct.AddonDialogWindow):
        def __init__(self,type):
            super(adv_gen_window, self).__init__(Addon.getLocalizedString(32149))
            wd=int(1250)
            hd=int(700)
            px=int(10)
            py=int(10)
            self.type=type
            self.fromy=''
            self.toy=''
            self.all_clicked=[]
            self.setGeometry(wd, hd, 22, 5,pos_x=px, pos_y=py)
            self.set_info_controls()
            #self.set_active_controls()
            self.set_navigation()
            
            # Connect a key action (Backspace) to close the window..
            self.connect(pyxbmct.ACTION_PREVIOUS_MENU, self.click_c)
            self.connect(pyxbmct.ACTION_NAV_BACK, self.click_c)
            #self.connect(pyxbmct.ACTION_MOUSE_RIGHT_CLICK, self.click_c)
            
        def click_c(self):
            for items in self.all_radio:
                if self.all_radio[items]['button'].isSelected():
                    self.all_clicked.append(str(self.all_radio[items]['id']))
            
            
            self.fromy=self.edit_from.getText()
            self.toy=self.edit_to.getText()
            
            self.close()
        def radio_update(self,radiobutton,id):
            # Update radiobutton caption on toggle

            if radiobutton.isSelected():
                self.all_clicked.append(id)
            else:
                if id in self.all_clicked:
                    self.all_clicked.pop(id)
        def set_info_controls(self):
            # Edit
            edit_label = pyxbmct.Label(Addon.getLocalizedString(32181))
            self.placeControl(edit_label, 0, 0, rowspan=2)
            
            self.edit_from = pyxbmct.Edit('2000')
            self.placeControl(self.edit_from, 0, 1, rowspan=2)
            # Additional properties must be changed after (!) displaying a control.
            self.edit_from.setText('2000')
            
            # Edit
            edit_label = pyxbmct.Label(Addon.getLocalizedString(32182))
            self.placeControl(edit_label, 2, 0, rowspan=2)
            
            self.edit_to = pyxbmct.Edit('2019')
            self.placeControl(self.edit_to, 2, 1, rowspan=2)
            # Additional properties must be changed after (!) displaying a control.
            self.edit_to.setText('2019')
            
            #genere
            edit_label = pyxbmct.Label(Addon.getLocalizedString(32016))
            self.placeControl(edit_label, 0, 3)
            
            url='http://api.themoviedb.org/3/genre/%s/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(self.type,lang)
            x=get_html(url).json()
            self.all_g=[]
            for items in x['genres']:
               
                self.all_g.append((items['name'],items['id']))
            self.all_radio={}
            i=1
            self.all_it=[]
            for name,id in self.all_g:
                # RadioButton
                self.all_it.append(name)
                self.all_radio[name]={}
                self.all_radio[name]['button'] = pyxbmct.RadioButton(name)
                self.all_radio[name]['id']=id
                self.placeControl(self.all_radio[name]['button'], i, 3)
                #self.connect(self.all_radio[name], self.radio_functions[name])
                i+=1
            self.button = pyxbmct.Button('Search')
            self.placeControl(self.button, 21, 4, rowspan=2)
            # Connect control to close the window.
            self.connect(self.button, self.click_c)
        def set_navigation(self):
            self.edit_from.controlUp(self.edit_to)
            self.edit_from.controlDown(self.edit_to)
            
            self.edit_to.controlUp(self.edit_from)
            self.edit_to.controlDown(self.edit_from)
            
            self.edit_to.controlRight(self.all_radio[self.all_g[0][0]]['button'])
            self.edit_to.controlLeft(self.all_radio[self.all_g[0][0]]['button'])
            
            self.edit_from.controlRight(self.all_radio[self.all_g[0][0]]['button'])
            self.edit_from.controlLeft(self.all_radio[self.all_g[0][0]]['button'])
            
            
            
                
            
            for items in self.all_it:
                ind=self.all_it.index(items)
                if ind==0:
                    pre=len(self.all_it)-1
                    next=1
                elif ind==(len(self.all_it)-1):
                    pre=ind-1
                    next=0
                else:
                    pre=ind-1
                    next=ind+1
               
                self.all_radio[items]['button'].controlUp(self.all_radio[self.all_it[pre]]['button'])
                self.all_radio[items]['button'].controlDown(self.all_radio[self.all_it[next]]['button'])
                
                self.all_radio[items]['button'].controlLeft(self.edit_from)
                self.all_radio[items]['button'].controlRight(self.button)
            
            self.setFocus(self.edit_from)
    window = adv_gen_window(url)
    window.doModal()
    all_g=window.all_clicked
    start_y=window.fromy
    end_y=window.toy

    del window
    return all_g,start_y,end_y

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
def get_html_g():
    try:
        url_g='https://api.themoviedb.org/3/genre/tv/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language='+lang
        html_g_tv=get_html(url_g).json()
         
   
        url_g='https://api.themoviedb.org/3/genre/movie/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language='+lang
        html_g_movie=get_html(url_g).json()
    except Exception as e:
        log.warning('Err in HTML_G:'+str(e))
    return html_g_tv,html_g_movie
html_g_tv,html_g_movie=cache.get(get_html_g,72, table='posters')
if KODI_VERSION>18:
    class Thread(threading.Thread):
        def __init__(self, target, *args):
            super().__init__(target=target, args=args)
        def run(self, *args):
         
          self._target(*self._args)
else:
    class Thread(threading.Thread):
        def __init__(self, target, *args):
           
            self._target = target
            self._args = args
            
            
            threading.Thread.__init__(self)
            
        def run(self):
            
            self._target(*self._args)
def get_tmdb_data(new_name_array,html_g,fav_search_f,fav_servers_en,fav_servers,google_server,rapid_server,direct_server,heb_server,url,isr,xxx):
          
          try:
           global all_d
           all_movie_w=[]
           all_w_tv_data={}
           
                   
       #except:
           
           html=get_html(url).json()
           try:
            max_page=html['total_pages']
           except:
               max_page=1
               pass
           try:
            all_res=html['total_results']
           except:
               all_res=1
          
           count=0
           if 'results' in html:
                result_html=html['results']
           else:
               result_html=[html]
           for data in result_html:
           
             count+=1
             if 'vote_average' in data:
               rating=data['vote_average']
             else:
              rating=0
             if 'first_air_date' in data:
               year=str(data['first_air_date'].split("-")[0])
             elif 'release_date' in data:
                year=str(data['release_date'].split("-")[0])
             else:
                year='0'
             try:
                 if data['overview']==None:
                   plot=' '
                 else:
                   plot=data['overview']
             except:
                 plot=""
             if Addon.getSetting("adults")=='true':
                 try:
                     if 'adult' in data:
                        addults=data['adult']
                     else:
                        addults=False
                 except:
                     addults=False
                 if 'erotic ' in plot.lower() or 'sex' in plot.lower() or addults==True :
                    continue
                
             if 'title' not in data:
               
               tv_movie='tv'
               new_name=data['name']
             else:
               tv_movie='movie'
               new_name=data['title']
              
             log.warning(new_name)
             f_subs=[]
             if 'original_title' in data:
               original_name=data['original_title']
               mode=15
               
               id=str(data['id'])
               if Addon.getSetting("check_subs")=='true' or Addon.getSetting("disapear")=='true':
                 import cache
                 from subs import get_links
                 f_subs=cache.get(get_links,9999,'movie',original_name,original_name,'0','0','0','0',year,id,True, table='pages')
               if data['original_language']!='en':
                
                html2=get_html('http://api.themoviedb.org/3/movie/%s?api_key=fb981e5ab89415bba616409d5eb5f05e'%id).json()
                original_name=html2['title']
                
               
             else:
               original_name=data['original_name']
               id=str(data['id'])
               
               mode=16
               
               if data['original_language']!='en':
                
                    html2=get_html('http://api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e'%id).json()
                    if 'name' in html2:
                        original_name=html2['name']
                    #if 'name' in data:
                    #    original_name=data['name']
                   
             if data['poster_path']==None:
              icon=' '
             else:
               icon=data['poster_path']
             if 'backdrop_path' in data:
                 if data['backdrop_path']==None:
                  fan=' '
                 else:
                  fan=data['backdrop_path']
             else:
                fan=html['backdrop_path']
             if plot==None:
               plot=' '
             if 'http' not in fan:
               fan='https://image.tmdb.org/t/p/original/'+fan
             if 'http' not in icon:
               icon='https://image.tmdb.org/t/p/original/'+icon
             genres_list= dict([(i['id'], i['name']) for i in html_g['genres'] \
                    if i['name'] is not None])
             try:genere = u' / '.join([genres_list[x] for x in data['genre_ids']])
             except:genere=''
             
             trailer = "plugin://%s?mode=25&id=%s&url=%s" % (addon_id,id,tv_movie)
             if (new_name+id) not in new_name_array:
              new_name_array.append(new_name+id)
              if Addon.getSetting("check_subs")=='true' or Addon.getSetting("disapear")=='true':
                  if len(f_subs)>0:
                    color='white'
                  else:
                    color='red'
                    
              else:
                 color='white'
              start_time = time.time()
              
              
              
              
              
              
              elapsed_time = time.time() - start_time
              
              
              if  Addon.getSetting("disapear")=='true' and color=='red' and mode!=7:
                a=1
              else:
                color='white'
                
                watched='no'
                if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
                    if id in all_movie_w:
                        watched='yes'
                    if id in all_w_tv_data:
                        watched=all_w_tv_data[id]
                        log.warning('Found watched:'+id)
                        
                if  mode==4 and fav_search_f=='true' and fav_servers_en=='true' and (len(fav_servers)>0 or heb_server=='true' or google_server=='true' or rapid_server=='true' or direct_server=='true'):
                
                    fav_status='true'
                else:
                    fav_status='false'
            
                
                all_d.append(('[COLOR '+color+']'+new_name+'[/COLOR]',url,mode,icon,fan,plot,year,original_name,id,rating,new_name,year,isr,genere,trailer,watched,fav_status,xxx,max_page,all_res))
              
           
           
          except Exception as e:
            import linecache,sys
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            xbmc.executebuiltin((u'Notification(%s,%s)' % (Addon.getAddonInfo('name'), 'No Trailer...Line:'+str(lineno)+' E:'+str(e))))
            log.warning('ERROR IN GET TMDB:'+str(lineno))
            log.warning('inline:'+line)
            log.warning(e)
            
            log.warning('BAD Trailer play')
def get_all_data(first,last,url,link,new_name_array,isr):
    try:
        
        global all_d
        
        all_d=[]
        xxx=0
 
        if '/tv/' in url:
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

   
              
              
        if '/tv/' in url:
             url_g='https://api.themoviedb.org/3/genre/tv/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language='+lang
             
             html_g=html_g_tv
        else:
             url_g='https://api.themoviedb.org/3/genre/movie/list?api_key=fb981e5ab89415bba616409d5eb5f05e&language='+lang
             html_g=html_g_movie
        #html_g=get_html(url_g).json()
 
        if Addon.getSetting("dp")=='true' and (last-first)>1:
                dp = xbmcgui.DialogProgress()
                if KODI_VERSION<19:
                    dp.create(Addon.getLocalizedString(32116), Addon.getLocalizedString(32072), '')
                else:
                    dp.create(Addon.getLocalizedString(32116), Addon.getLocalizedString(32072)+'\n'+'')
                dp.update(0)
        thread=[]
       
        for i in range(first,last):
          
           url=link+'page='+str(i)
          
           
           thread.append(Thread(get_tmdb_data,new_name_array,html_g,fav_search_f,fav_servers_en,fav_servers,google_server,rapid_server,direct_server,heb_server,url,isr,xxx))
           thread[len(thread)-1].setName('Page '+str(i))
           xxx+=1
       

           
          
           
           

                #addDir3('[COLOR '+color+']'+new_name+'[/COLOR]',url,mode,icon,fan,plot,data=year,original_title=original_name,id=id,rating=rating,heb_name=new_name,show_original_year=year,generes=genere,trailer=trailer,watched=watched,fav_status=fav_status)
    except Exception as err:
            import traceback
            from os.path import basename
            exc_info=sys.exc_info()
            e=(traceback.format_exc())
            et=e.split(',')
          
            e=','.join(et).replace('UnboundLocalError: ','')
            home1=xbmc_tranlate_path("special://home/")
            e_al=e.split(home1)
            log.warning(e_al)
            e=e_al[len(e_al)-1].replace(home1,'')
            log.warning('Error TMDB:'+str(e))
    start_time=time.time()
    for td in thread:
        td.start()
        if 1:
            
            while td.is_alive():
                xbmc.sleep(100)
            
        if Addon.getSetting("dp")=='true' and (last-first)>1:
                elapsed_time = time.time() - start_time
                if KODI_VERSION<19:
                    dp.update(0, ' Activating '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),td.name," ")
                else:
                    dp.update(0, ' Activating '+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+td.name+'\n'+" ")
        #xbmc.sleep(255)
        
    while 1:

          still_alive=0
          all_alive=[]
          for yy in range(0,len(thread)):
            
            if  thread[yy].is_alive():
              
              still_alive=1
              all_alive.append(thread[yy].name)
          if still_alive==0:
            break
          if Addon.getSetting("dp")=='true' and (last-first)>1:
                elapsed_time = time.time() - start_time
                if KODI_VERSION<19:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),','.join(all_alive)," ")
                else:
                    dp.update(0, Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time))+'\n'+','.join(all_alive)+'\n'+" ")
          xbmc.sleep(100)
    if Addon.getSetting("dp")=='true' and (last-first)>1:
        dp.close()
    return all_d
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
                            
                        
                
               
            except:
                pass
            return all_w
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
def get_release_date(idd):
    global all_release_dates
    all_in_data=cache.get(c_release_get,24,idd, table='pages')
    if all_in_data:
        all_release_dates[idd]=all_in_data
                
    return all_release_dates
def get_movies(url,local=False,reco=0,global_s=False,return_results=False):
   global all_release_dates
   new_name_array=[]
   isr=0
   all_data_return=[]
   all_years=[]
   import datetime
   all_d=[]
   now = datetime.datetime.now()
   for year in range(now.year,1970,-1):
         all_years.append(str(year))
   if 'advance' in url:
        all_g,start_y,end_y=adv_gen_window(url.split('_')[1])
       
        if len(all_g)==0:
            sys.exit(1)
        typee=url.split('_')[1]
        if typee=='movie':
            url='http://api.themoviedb.org/3/discover/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&primary_release_date.gte=%s-01-01&primary_release_date.lte=%s-12-31&with_genres=%s&page=1'%(typee,lang,start_y,end_y,','.join(all_g))
        else:
            url='http://api.themoviedb.org/3/discover/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&first_air_date.gte=%s-01-01&first_air_date.lte=%s-12-31&with_genres=%s&page=1'%(typee,lang,start_y,end_y,','.join(all_g))
   if url=='movie_years&page=1':
     
      
      if Addon.getSetting("dip_dialog")=='0':
          ret=ret = xbmcgui.Dialog().select("Choose", all_years)
          if ret!=-1:
            
              url='https://api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=%s&with_original_language=en&page=1'%(lang,all_years[ret])
            
          else:
            return 0
      else:
        for items in all_years:
            
            url='https://api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=%s&with_original_language=en&page=1'%(lang,items)
            if 0:
               if  name not in all_n:
                all_n.append(name)
                
                aa=addDir3(items,url,14,'https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/movieyears.png','https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/cal.years.jpg',items,collect_all=True)
                all_d.append(aa)
            else:
                aa=addDir3(items,url,14,'https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/movieyears.png','https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/cal.years.jpg',items,collect_all=True)
                all_d.append(aa)
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
        
        return 0
   if url=='tv_years&page=1' and 'page=1' in url:
      if Addon.getSetting("dip_dialog")=='0':
          ret=ret = xbmcgui.Dialog().select("Choose", all_years)
          if ret!=-1:
            url='https://api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&first_air_date_year=%s&include_null_first_air_dates=false&with_original_language=en&page=1'%(lang,all_years[ret])
           
          else:
            sys.exit()
      else:
        for items in all_years:
            url='https://api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&first_air_date_year=%s&include_null_first_air_dates=false&with_original_language=en&page=1'%(lang,items)
            
            aa=addDir3(items,url,14,'https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/movieyears.png','https://thechains24.com/Ghost-Addon/ghostxmls/xmls1/fanart/movies/cal.years.jpg',items,collect_all=True)
            all_d.append(aa)
   try:
        from sqlite3 import dbapi2 as database
   except:
        from pysqlite2 import dbapi2 as database
   cacheFile=os.path.join(user_dataDir,'database.db')
   dbcon = database.connect(cacheFile)
   dbcur = dbcon.cursor()
   dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
   dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT ,""tv_movie TEXT);" % ('search_string2'))
   
   dbcon.commit()
   dbcur.execute("SELECT * FROM search_string2")
   match = dbcur.fetchall()
   all_s_strings=[]
   for qu,tt in match:
    all_s_strings.append((qu+'$$$'+tt))

   
                 
   if '/search' in url and 'page=1' in url and '%s' in url:
        
        
        
        search_entered =''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
        keyboard.doModal()
        if keyboard.isConfirmed() :
               search_entered = keyboard.getText()
               if search_entered=='':
                sys.exit()
          
               
               url=url%que(search_entered)
               if '/tv?' in url:
                type_in='tv'
               else:
                type_in='movie'
               
              
          
        else:
          
          
          sys.exit()
   if '/search' in url and 'page=1' in url:
       search_entered=url.split('query=')[1]
       search_entered=search_entered.split('&')[0]
       if 'tv' in url:
            tv_movie='tv'
       else:
            tv_movie='movie'
       if search_entered+'$$$'+tv_movie not in all_s_strings:
         dbcur.execute("SELECT * FROM search_string2 where name='%s' and tv_movie='%s'"%(unque(search_entered.replace("'","%27")),tv_movie))
         match = dbcur.fetchall()
         
      
         
         if len(match)==0:
             dbcur.execute("INSERT INTO search_string2 Values ('%s','%s')"%(unque(search_entered.replace("'","%27")),tv_movie))
             dbcon.commit()
   html={}
   html['results']=[]
   regex='page=(.+?)$'
   match=re.compile(regex).findall(url)
   # first=int(match[0])
   # last=int(match[0])+1
   # link=url.split('page=')[0]
   if len(match)==0 or reco==1:
    first=1
    last=2
    link=url.split('page=')[0]
   else:
       link=url.split('page=')[0]
       first=int(match[0])
       s_last=int(Addon.getSetting("num_p"))
       if s_last>10:
         s_last=10
       last=first+int(s_last)


   

   all_w_trk={}
   if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
        if '/movie' in url:
            url_o='movie'
        
            all_w_trk=get_all_trakt_resume(url_o)
   if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
           all_movie_w=[]
           if '/movie' in url:
               try:
                   i = (call_trakt('/users/me/watched/movies'))
                   
                   for ids in i:
                      all_movie_w.append(str(ids['movie']['ids']['tmdb']))
               except Exception as e:
                log.warning(e)
                pass
           
           all_tv_w={}
           all_w_tv_data={}
           if '/tv' in url:
              try:
               i = (call_trakt('/users/me/watched/shows?extended=full'))
               
               for ids in i:
                 aired_episodes=ids['show']['aired_episodes']
                 all_tv_w[str(ids['show']['ids']['tmdb'])]='no'
                 count_episodes=0
                 for seasons in ids['seasons']:
                 
                  for ep in seasons['episodes']:
                   
                    count_episodes+=1
                 
                 
                 if count_episodes>=int(aired_episodes):
                        all_w_tv_data[str(ids['show']['ids']['tmdb'])]='yes'
              except Exception as e:
                log.warning(e)
                pass
   #all_in_data=get_all_data(first,last,url,link,new_name_array,isr)
  
  
   all_in_data=cache.get(get_all_data,24,first,last,url,link,new_name_array,isr, table='pages')

   if '/search' in url:
    all_in_data=sorted(all_in_data, key=lambda x: x[6], reverse=True)
   else:
   
    all_in_data=sorted(all_in_data, key=lambda x: x[17], reverse=False)
   max_page=-1
   
    
   dbcur.execute("SELECT * FROM playback")
   match = dbcur.fetchall()
   all_w={}
      
   for n,tm,s,e,p,t,f in match:
            ee=str(tm)
            all_w[ee]={}
            if '/movie' in url:
                all_w[ee]['resume']=str(p)
                all_w[ee]['totaltime']=str(t)
            else:
                all_w[ee]['resume']=0
                all_w[ee]['totaltime']=100
   if 0:#'/movie' in url:
       all_id_for_test=[]
       for  name,url,mode,icon,fan,plot,year,original_name,id,rating,new_name,year,isr,genere,trailer,watched,fav_status,xxx,max_page,all_res in all_in_data:
            all_id_for_test.append((name,id))
       thread=[]
       all_release_dates={}
       for name,idd in all_id_for_test:
            thread.append(Thread(get_release_date,idd))
            thread[len(thread)-1].setName('Page '+str(i))
       for td in thread:
            td.start()
       while(1):
           

          still_alive=0
          all_alive=[]
          for yy in range(0,len(thread)):
            
            if  trd_alive(thread[yy]):
              
              still_alive=1
              
          if still_alive==0:
            break
       
   for  name,url,mode,icon,fan,plot,year,original_name,id,rating,new_name,year,isr,genere,trailer,watched,fav_status,xxx,max_page,all_res in all_in_data:
            watched='no'
            
            if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
                if id in all_movie_w:
                    watched='yes'
                if id in all_w_tv_data:
                    watched=all_w_tv_data[id]
            added_res_trakt=''
            if (id) in all_w_trk:
            
                
                    added_res_trakt=all_w_trk[id]['precentage']
            add_release=''
            if id in all_release_dates:
                add_release='Release Date: '+all_release_dates[id]+'\n'
            if local:
                addNolink( new_name, id,27,False,fan=fan, iconimage=icon,plot=add_release+plot,year=year,generes=genere,rating=rating,trailer=trailer)
            else:
                
                aa=addDir3(name,url,mode,icon,fan,add_release+'[B][I]'+year+'[/I][/B]\n'+plot,data=year,original_title=original_name,id=id,all_w_trk=added_res_trakt,rating=rating,heb_name=new_name,show_original_year=year,generes=genere,trailer=trailer,watched=watched,fav_status=fav_status,collect_all=True,all_w=all_w)
                all_d.append(aa)
                all_data_return.append((name,url,mode,icon,fan,add_release+'[B][I]'+year+'[/I][/B]\n'+plot,year,original_name,id,added_res_trakt,rating,new_name,year,genere,trailer,watched,fav_status,True,all_w))
   regex='page=(.+?)$'
   match=re.compile(regex).findall(url)
   link=url.split('page=')[0]
   if   max_page==-1 and not return_results:
        if not global_s:
            xbmcgui.Dialog().ok(Addon.getAddonInfo('name'),'[COLOR red][I]%s[/I][/COLOR]'%Addon.getLocalizedString(32183))
            
            sys.exit()
   
   if max_page>int(match[0]):
        if local:
            mode=26
        else:
            mode=14
        aa=addDir3(('[COLOR orange][I]%s %s %s %s (%s %s)[/I][/COLOR]'%(Addon.getLocalizedString(32184),str(int(match[0])+1),Addon.getLocalizedString(32185),str(max_page),str(all_res),Addon.getLocalizedString(32186))),link+'page='+str(int(match[0])+1),mode,BASE_LOGO+'next.png','https://cdn4.iconfinder.com/data/icons/arrows-1-6/48/1-512.png','Results',show_original_year='999',data='999',collect_all=True)
        all_d.append(aa)
     
   if 0:
       xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_YEAR)
       xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_SORT_TITLE)
       

       xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_RATING)
   dbcur.close()
   dbcon.close()
   if return_results:
       
       return all_data_return
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
   
   return new_name_array
   
def get_seasons(name,url,iconimage,fanart,description,data,original_title,id,heb_name):
   all_d=[]
   payload= {
                    "apikey": "0629B785CE550C8D",
                    "userkey": "",
                    "username": ""
   }
   tmdbKey = 'fb981e5ab89415bba616409d5eb5f05e'
   #headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Language': 'he'}
   #r = requests.post(domain_s+'api.thetvdb.com/login', json=payload, headers=headers)
   #r_json = r.json()
   from resources.modules.tvdb import TVDB

   t = TVDB()
   if 'tvdb' not in id:
       url=domain_s+'api.themoviedb.org/3/tv/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=external_ids'%(id,lang)
       log.warning('Season:'+url)
       html=get_html(url).json()
       try:
           if 'first_air_date' in html:
            show_original_year=html['first_air_date'].split("-")[0]
           else:
            show_original_year=0
       except:
        show_original_year=0
       #tmdb data
       #headers['Authorization'] = "Bearer %s" %  str(r_json.get('token'))
       tvdb_id=str(html['external_ids']['tvdb_id'])
   else:
    tvdb_id=id.replace('tvdb','')
    show_data=t.getShowData_id(tvdb_id)
    log.warning('show_data')
    log.warning(show_data)
    html={}
    html['seasons']=[]
    html['overview']=show_data['data']['overview']
    html['original_name']=show_data['data']['seriesName']
    html['original_language']= show_data['data']['language'] 
    html['backdrop_path']= 'https://www.thetvdb.com/banners/'+show_data['data']['fanart'] 
    if 'firstAired' in show_data['data']:
        show_original_year=show_data['data']['firstAired'].split("-")[0]
    else:
        show_original_year=0
   
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
    try:
        show=t.getShow_id(tvdb_id)
    except:
        show={'data':[]}
   if 'error_code' in show:
        show={'data':[]}
   max_season_tvdb=0
   match=[]

   for item_tvdb in show['data']:
        match.append((item_tvdb['episodeName'],item_tvdb['airedEpisodeNumber'],item_tvdb['firstAired'],item_tvdb['airedSeason'],item_tvdb['overview']))
   
  
   #response = get_html('http://thetvdb.com/api/0629B785CE550C8D/series/%s/all/he.xml'%html['external_ids']['tvdb_id'],headers=base_header,timeout=5).content
   #log.warning(json.dumps(response))
   #attr=['Combined_season','FirstAired']
   #regex='<Episode>.+?<EpisodeName>(.+?)</EpisodeName>.+?<EpisodeNumber>(.+?)</EpisodeNumber>.+?<FirstAired>(.+?)</FirstAired>.+?<SeasonNumber>(.+?)</SeasonNumber>'
   #match=re.compile(regex,re.DOTALL).findall(response)
   
   watched_season={}
   if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
      try:
       i = (call_trakt('/users/me/watched/shows?extended=full'))
       
       for ids in i:
         watched_season[str(ids['show']['ids']['tmdb'])]={}
         count_episodes=0
         for seasons in ids['seasons']:
          watched_season[str(ids['show']['ids']['tmdb'])][str(seasons['number'])]=0
          for ep in seasons['episodes']:
           
            watched_season[str(ids['show']['ids']['tmdb'])][str(seasons['number'])]+=1
      except:
        pass
         
         
                            
   
   #seasons_tvdb=parseDOM(response,'Episode', attr)
   all_season=[]
   all_season_tvdb_data=[]
    
   all_season_imdb=[]
   all_season_imdb_data=[]
   count_season=0
   s_number_pre=1
   season_ep_count={}
   for ep_name,ep_num,aired,s_number,overview in match:
     season_ep_count[s_number]=ep_num
   for ep_name,ep_num,aired,s_number,overview in match:
     
     if str(s_number) not in all_season:

       all_season.append(str(s_number))
       all_season_tvdb_data.append({"name":ep_name,"episode_number":ep_num,"air_date":aired,"season_number":s_number,"poster_path":iconimage,'episode_count':season_ep_count[s_number],'overview':overview})
   
   try:
       url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&language=en&append_to_response=external_ids'%(id,tmdbKey)
      
       
       imdb_id=get_html(url2).json()['external_ids']['imdb_id']
       xx=get_html('https://www.imdb.com/title/%s/episodes'%imdb_id).content
       regex='<label for="bySeason">(.+?)</div'
       match_imdb_s_pre=re.compile(regex,re.DOTALL).findall(xx)[0]
       regex='<option.+?value="(.+?)"'
       match_imdb_s=re.compile(regex).findall(match_imdb_s_pre)
       regex_img='<img itemprop="image".+?src="(.+?)"'
       img_imdb_pre=re.compile(regex_img,re.DOTALL).findall(xx)
       if len (img_imdb_pre)>0:
            img_imdb=img_imdb_pre[0]
       else:
            img_imdb=' '
       for s_number in match_imdb_s:
            all_season_imdb.append(str(s_number))
            all_season_imdb_data.append({"name":'0',"episode_number":'0',"air_date":' ',"season_number":s_number,"poster_path":img_imdb,'backdrop_path':img_imdb})
   except:
    pass
   all_season_tmdb=[]
   for data in html['seasons']:
      all_season_tmdb.append(str(data['season_number']))
   for items_a in all_season:
     if items_a not in all_season_tmdb:
       html['seasons'].append(all_season_tvdb_data[all_season.index(items_a)])
       
   for items_a in all_season_imdb:
     if items_a not in all_season_tmdb:
       html['seasons'].append(all_season_imdb_data[all_season_imdb.index(items_a)])
   plot=html['overview']
   original_name=html['original_name']
   if html['original_language']!='en':
    original_name=html['name']
   for data in html['seasons']:
   
     new_name=Addon.getLocalizedString(32101)+str(data['season_number'])
     if data['air_date']!=None:
         year=str(data['air_date'].split("-")[0])
         premired=data['air_date']
     else:
       year=0
       premired=0
     season=str(data['season_number'])
     if data['poster_path']==None:
      icon=iconimage
     else:
       icon=data['poster_path']
     if 'backdrop_path' in data:
         if data['backdrop_path']==None:
          fan=fanart
         else:
          fan=data['backdrop_path']
     else:
        fan=html['backdrop_path']
     ep_number='0'
     if 'episode_count' in data:
        ep_number=data['episode_count']
     
     watched='no'
     if id in watched_season:
       if season in watched_season[id]:
        
        if watched_season[id][season]>=int(ep_number):
            watched='yes'
     
     if plot==None:
       plot=' '
     if fan==None:
       fan=fanart
     if 'http' not in fan:
       fan=domain_s+'image.tmdb.org/t/p/original/'+fan
     if 'http' not in icon:
       icon=domain_s+'image.tmdb.org/t/p/original/'+icon
     
     
     remain=''
      
     
     color='white'
     try:
        if 'air_date' in data:
           
               datea='[COLOR aqua]'+str(time.strptime(data['air_date'], '%Y-%m-%d'))+'[/COLOR]\n'
               
               a=(time.strptime(data['air_date'], '%Y-%m-%d'))
               b=time.strptime(str(time.strftime('%Y-%m-%d')), '%Y-%m-%d')
               
           
               if a>b:
                 color='red'
                 txt_1=' Wait until ... '
               else:
                 txt_1=Addon.getLocalizedString(32187)
                 color='white'
        datea='[COLOR aqua]'+txt_1+time.strftime( "%d-%m-%Y",a) + '[/COLOR]\n'
     except Exception as e:
             log.warning('TVDB error:'+str(e))
             datea=''
             color='red'
     if str(data['season_number'])=='0' or str(data['season_number'])=='-1':
        continue
     aa=addDir3( '[COLOR %s]'%color+new_name+'[/COLOR]',url,19,icon,fan,datea+plot,data=year,original_title=original_title,id=id,season=season,tmdbid=tvdb_id,show_original_year=show_original_year,heb_name=heb_name,ep_number=ep_number,watched_ep=watched,watched=watched,remain=remain,premired=premired)
     all_d.append(aa)
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def get_episode_data(id,season,episode,yjump=True,o_name=' '):
    o_season=season
    o_episode=episode
    url='http://api.themoviedb.org/3/tv/%s/season/%s/episode/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=external_ids'%(id,season,episode,lang)

    html=get_html(url).json()
   
    if yjump:
      
      if 'status_code' in html or ('error_code' in html and html['error_code']==404):
        log.warning('In::')
        url='http://api.themoviedb.org/3/tv/%s/season/%s/episode/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=external_ids'%(id,str(int(season)+1),'1',lang)
        html=get_html(url).json()
        episode='1'
        season=str(int(season)+1)
    if 'name' in html and html['name']!=None:
        name=html['name']
        if 'air_date' in html:
            try:
                from datetime import datetime
                from datetime import date
                from datetime import time
                dateTime1 =datetime.strptime(html['air_date'], "%Y-%m-%d")
                if dateTime1.date() > date.today():
                    color='red'
                else:
                    color='lightblue'
            except:
                color='lightblue'
            name=name + ' [COLOR %s](%s)[/COLOR]'%(color,html['air_date'])
        plot=html['overview']
        if html['still_path']!=None:
          image=domain_s+'image.tmdb.org/t/p/original/'+html['still_path']
        else:
          image=' '
        return name,plot,image,season,episode
    else:
       return o_name,' ',' ',o_season,o_episode
def get_episode(name,url,iconimage,fanart,description,data,original_title,id,season,tvdb_id,show_original_year,heb_name):
   import _strptime
   all_d=[]
   
   url=domain_s+'api.themoviedb.org/3/tv/%s/season/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&append_to_response=external_ids'%(id,season,lang)
   tmdbKey = 'fb981e5ab89415bba616409d5eb5f05e'
   html=get_html(url).json()
   #tmdb data

   if 'episodes'  in html:
      if len(html['episodes'])>0:
       html_en=[]
       if 'name' not in html['episodes'][0] or html['episodes'][0]['name']=='':
         url=domain_s+'api.themoviedb.org/3/tv/%s/season/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=eng'%(id,season)
         html_en=get_html(url).json()
       count=0
       for items in html['episodes']:
            if len(html_en)>0:
                if 'name' not in html_en['episodes'][count] or html_en['episodes'][count]['name']==None:
                    items['name']=''
                elif 'name' not in items or items['name']==None:
                
                    log.warning(html_en['episodes'][count])
                    items['name']=html_en['episodes'][count]['name']
                if 'overview' not in html_en['episodes'][count] or html_en['episodes'][count]['overview']==None:
                    items['overview']=''
                elif 'overview' not in items or items['overview']==None:
                
                    log.warning(html_en['episodes'][count])
                    items['overview']=html_en['episodes'][count]['overview']
                count+=1
   #response = get_html('http://thetvdb.com/api/0629B785CE550C8D/series/%s/all/he.xml'%tmdbid).content
   
   attr=['Combined_season','FirstAired']
   regex='<Episode>.+?<EpisodeName>(.+?)</EpisodeName>.+?<EpisodeNumber>(.+?)</EpisodeNumber>.+?<FirstAired>(.+?)</FirstAired>.+?<Overview>(.+?)</Overview>.+?<SeasonNumber>(.+?)</SeasonNumber>'
   #match=re.compile(regex,re.DOTALL).findall(response)
   match=[]
   from resources.modules.tvdb import TVDB

   t = TVDB()
   try:
    show=t.getShow_id(tvdb_id)
    if 'error_code' in show:
        show={'data':[]}
   except:
    show={'data':[]}
    pass
   log.warning(show)
   max_season_tvdb=0
   match=[]
   for item_tvdb in show['data']:
        if item_tvdb['filename']!='':
            img='https://www.thetvdb.com/banners/'+item_tvdb['filename']
        else:
            img=fanart
        
        ep=item_tvdb['episodeName']
        if not ep:
            ep='Episode '+str(item_tvdb['airedEpisodeNumber'])
        
        
        
        match.append(('(T) '+ep,item_tvdb['airedEpisodeNumber'],item_tvdb['firstAired'],item_tvdb['overview'],item_tvdb['airedSeason'],img))
   
   
   regex_eng='<slug>(.+?)</slug>'
   #match_eng=re.compile(regex_eng).findall(response)
   match_eng=[]
   eng_name=name
   if len (match_eng)>0:
     eng_name=match_eng[0]

   #seasons_tvdb=parseDOM(response,'Episode', attr)

   all_episodes=[]
   all_season_tvdb_data=[]
   
   all_episodes_imdb=[]
   all_episodes_imdb_data=[]
   image2=fanart
   for ep_name,ep_num,aired,overview,s_number,image in match:
     
   
     if str(s_number)==str(season):
         if ep_num not in all_episodes:
           
           all_episodes.append(str(ep_num))
           all_season_tvdb_data.append({"name":ep_name,"episode_number":ep_num,"air_date":aired,"overview":overview,"season_number":s_number,"still_path":image,"poster_path":image})
   
   url2='http://api.themoviedb.org/3/tv/%s?api_key=%s&language=en&append_to_response=external_ids'%(id,tmdbKey)
      
       
    
   try:
       imdb_id=get_html(url2).json()['external_ids']['imdb_id']
       xx=get_html('https://www.imdb.com/title/%s/episodes?season=%s'%(imdb_id,season)).content
       log.warning('https://www.imdb.com/title/%s/episodes?season=%s'%(imdb_id,season))
       regex='div class="image">.+?title="(.+?)"(.+?)meta itemprop="episodeNumber" content="(.+?)".+?<div class="airdate">(.+?)<.+?itemprop="description">(.+?)<'
       match_imdb_s_pre=re.compile(regex,re.DOTALL).findall(xx)
      
       for ep_name,poster,ep_num,air_date,plot in match_imdb_s_pre:
            if 'src="' in poster:
                regex='src="(.+?)"'
                poster=re.compile(regex).findall(poster)[0]
            else:
                poster=' '
            air_date=air_date.replace('\n','').replace(' ','')
            all_episodes_imdb.append(str(ep_num))
            all_episodes_imdb_data.append({"name":'(I) '+ep_name,"episode_number":ep_num,"air_date":air_date,"season_number":season,"poster_path":poster,'still_path':poster,"overview":plot})
   except:
    pass
  
   all_episodes_tmdb=[]
   if 'episodes' not in html:
     html['episodes']=[]
     html['poster_path']=fanart
   else:
      for data in html['episodes']:
          all_episodes_tmdb.append(str(data['episode_number']))
   for items_a in all_episodes:
     if items_a not in all_episodes_tmdb:
       html['episodes'].append(all_season_tvdb_data[all_episodes.index(items_a)])
   for data in html['episodes']:
          all_episodes_tmdb.append(str(data['episode_number']))
   
   for items_a in all_episodes_imdb:
     if items_a not in all_episodes_tmdb:
       html['episodes'].append(all_episodes_imdb_data[all_episodes_imdb.index(items_a)])

   
   
   
       
   original_name=original_title
   if Addon.getSetting("dp")=='true' and (Addon.getSetting("disapear")=='true' or Addon.getSetting("check_subs")=='true'):
            dp = xbmcgui.DialogProgress()
            dp.create(Addon.getLocalizedString(32116), Addon.getLocalizedString(32072), '')
            dp.update(0)
   xxx=0
   start_time = time.time()

   if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
       all_tv_w={}
       if 1:
           i = (call_trakt('/users/me/watched/shows?extended=full'))
           
           for ids in i:
             
             all_tv_w[str(ids['show']['ids']['tmdb'])]=[]
             for seasons in ids['seasons']:
             
              for ep in seasons['episodes']:
               
                all_tv_w[str(ids['show']['ids']['tmdb'])].append(str(seasons['number'])+'x'+str(ep['number']))
          
       #except:
       # pass
   fav_search_f=Addon.getSetting("fav_search_f_tv")
   fav_servers_en=Addon.getSetting("fav_servers_en_tv")
   fav_servers=Addon.getSetting("fav_servers_tv")
   google_server= Addon.getSetting("google_server_tv")
   rapid_server=Addon.getSetting("rapid_server_tv")
   direct_server=Addon.getSetting("direct_server_tv")
   heb_server=Addon.getSetting("heb_server_tv")
   if  fav_search_f=='true' and fav_servers_en=='true' and (len(fav_servers)>0 or heb_server=='true' or google_server=='true' or rapid_server=='true' or direct_server=='true'):

        fav_status='true'
   else:
       fav_status='false'
   from datetime import datetime
   
   try:
        from sqlite3 import dbapi2 as database
   except:
        from pysqlite2 import dbapi2 as database
   cacheFile=os.path.join(user_dataDir,'database.db')
   dbcon = database.connect(cacheFile)
   dbcur = dbcon.cursor()
   dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
   dbcon.commit()
    
   dbcur.execute("SELECT * FROM playback where tmdb='%s' and season='%s' "%(id,str(season)))
   match = dbcur.fetchall()
   
   all_w={}

   for n,t,s,e,p,t,f in match:
        ee=str(e)
        all_w[ee]={}
        all_w[ee]['resume']=str(p)
        all_w[ee]['totaltime']=str(t)
    
   
   count=1
   for data in html['episodes']:
     plot=data['overview']
     ep_name=''
     if 'name' in data and data['name']!=None:
        ep_name=data['name']
     else:
        ep_name='episode '+str(count)
     count+=1
     new_name=str(data['episode_number'])+" . "+ep_name
     air_date=''
     if 'air_date' in data:
       if data['air_date']!=None:
         
         year=str(data['air_date'].split("-")[0])
       else:
         year=0
     else:
       year=0
     
     if data['still_path']!=None:
       if 'https' not in data['still_path']:
         image=domain_s+'image.tmdb.org/t/p/original/'+data['still_path']
       else:
         image=data['still_path']
       
     elif html['poster_path']!=None:
      if 'https' not in html['poster_path']:
       image=domain_s+'image.tmdb.org/t/p/original/'+html['poster_path']
      else:
         image=html['poster_path']
     else:
       image=fanart
     if html['poster_path']!=None:
      if 'https' not in html['poster_path']:
       icon=domain_s+'image.tmdb.org/t/p/original/'+html['poster_path']
      else:
        icon=html['poster_path']
     else:
       icon=iconimage
     #if image2==fanart:
     #  icon=iconimage
      
     #  image=fanart
     color2='white'
     try:
        premired=' '
        if 'air_date' in data:
               premired=data['air_date']
               datea='[COLOR aqua]'+str(time.strptime(data['air_date'], '%Y-%m-%d'))+'[/COLOR]\n'
               
               a=(time.strptime(data['air_date'], '%Y-%m-%d'))
               b=time.strptime(str(time.strftime('%Y-%m-%d')), '%Y-%m-%d')
               
           
               if a>b:
                 color2='red'
               else:
                 
                 color2='white'
        datea='[COLOR gold]'+Addon.getLocalizedString(32187)+time.strftime( "%d-%m-%Y",a) + '[/COLOR]\n'
     except:
             try:
                datea=data['air_date']
             except:
                datea=''
             color2='red'
     f_subs=[]
     
     
     if Addon.getSetting("check_subs")=='true' or Addon.getSetting("disapear")=='true':
         import cache
         from subs import get_links
         f_subs=cache.get(get_links,9999,'tv',original_name,original_name,season,str(data['episode_number']),season,str(data['episode_number']),year,id,True, table='pages')
         
         
     
     

     
     color=color2
     if season!=None and season!="%20":
        tv_movie='tv'
     else:
       tv_movie='movie'
     
     elapsed_time = time.time() - start_time
     if (Addon.getSetting("check_subs")=='true'  or Addon.getSetting("disapear")=='true') and Addon.getSetting("dp")=='true':
        dp.update(int(((xxx* 100.0)/(len(html['episodes']))) ), Addon.getLocalizedString(32072)+ time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),'[COLOR'+color+']'+new_name+'[/COLOR]')
     xxx=xxx+1
     if  Addon.getSetting("disapear")=='true' and color=='red':
        a=1
     else:
     
       watched='no'
       if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_info")=='true':
           if id in all_tv_w:
             if season+'x'+str(data['episode_number']) in all_tv_w[id]:
              watched='yes'
       
       
       aa=addDir3( '[COLOR %s]'%color+new_name+'[/COLOR]', url,15, icon,image,str(datea)+str(plot),data=year,original_title=original_name,id=id,season=season,episode=data['episode_number'],eng_name=eng_name,show_original_year=show_original_year,heb_name=heb_name,watched=watched,fav_status=fav_status,all_w=all_w,premired=premired,tmdbid=tvdb_id)
       all_d.append(aa)
   #dbcur.close()
   #dbcon.close()
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
     #xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_EPISODE)
     #xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_SORT_TITLE)
     
