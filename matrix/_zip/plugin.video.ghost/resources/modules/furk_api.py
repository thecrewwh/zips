#thanks to Tiki from the Fen addon.
import sys
import xbmcaddon,xbmc
import  json
import time, datetime
import logging
from resources.modules import log
from resources.modules import fen_cache
from  resources.modules.client import get_html
addon_id=sys.argv[0].replace('plugin://','').replace('/','')
__addon__ = xbmcaddon.Addon(id=addon_id)
_cache = fen_cache.FenCache()
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    xbmc_tranlate_path=xbmc.translatePath
else:
    import xbmcvfs
    xbmc_tranlate_path=xbmcvfs.translatePath
def remove_accents(obj):
    import unicodedata
    try:
        obj = u'%s' % obj
        obj = ''.join(c for c in unicodedata.normalize('NFD', obj) if unicodedata.category(c) != 'Mn')
    except:
        pass
    return obj
def to_utf8(obj):
    try:
        import copy
        if isinstance(obj, unicode):
            obj = obj.encode('utf-8', 'ignore')
        elif isinstance(obj, dict):
            obj = copy.deepcopy(obj)
            for key, val in obj.items():
                obj[key] = to_utf8(val)
        elif obj is not None and hasattr(obj, "__iter__"):
            obj = obj.__class__([to_utf8(x) for x in obj])
        else: pass
    except: pass
    return obj
class FurkAPI:
    def __init__(self):
        self.base_link = 'https://www.furk.net'
        self.login_link = "/api/login/login?login=%s&pwd=%s"
        self.file_get_video_link = "/api/file/get?api_key=%s&type=video"
        self.file_get_audio_link = "/api/file/get?api_key=%s&type=audio"
        self.file_link_link = "/api/file/link?api_key=%s&id=%s"
        self.file_unlink_link = "/api/file/unlink?api_key=%s&id=%s"
        self.file_protect_link = "/api/file/protect?api_key=%s&id=%s&is_protected=%s"
        self.add_uncached_link = "/api/dl/add?api_key=%s&info_hash=%s"
        self.active_dl_link = "/api/dl/get?api_key=%s&dl_status=active"
        self.failed_dl_link = "/api/dl/get?api_key=%s&dl_status=failed"
        self.remove_dl_link = "/api/dl/unlink?api_key=%s&id=%s"
        self.account_info_link = "/api/account/info?api_key=%s"
        self.search_link = "/api/plugins/metasearch?api_key=%s&q=%s&cached=all" \
                                "&match=%s&moderated=%s%s&sort=relevance&type=video&offset=0&limit=200"
        self.search_direct_link = "/api/plugins/metasearch?api_key=%s&q=%s&cached=all" \
                                "&sort=cached&type=video&offset=0&limit=200"
        self.tfile_link = "/api/file/get?api_key=%s&t_files=1&id=%s"
        self.user_name = __addon__.getSetting('furk_login')
        self.user_pass = __addon__.getSetting('furk_password')
        self.timeout = 12.0

    def get_api(self):
        if 1:#try:
            api_key = __addon__.getSetting('furk_api_key')
            if not api_key:
                if not self.user_name or not self.user_pass:
                    return
                else:
                    link = (self.base_link + self.login_link % (self.user_name, self.user_pass))
                    p = get_html(link, timeout=self.timeout).json()
                    
                    if p['status'] == 'ok':
                        api_key = p['api_key']
                        __addon__.setSetting('furk_api_key', api_key)
                    else:
                        pass
            return api_key
        

    def search(self, query):
        if 1:#try:
            api_key = self.get_api()
            log.warning(api_key)
            if not api_key: return
            if '@files' in query:
                search_in = ''
                mod_level = 'no'
            else:
                search_in = '&attrs=name'
                mod_level = __addon__.getSetting('furk.mod.level').lower()
            link = (self.base_link + self.search_link \
                % (api_key, query, 'extended', mod_level, search_in))
            cache_name = "fen_FURK_SEARCH_%s" % link
            cache = _cache.get(cache_name)
            if cache:
                files = cache
            else:
                p = self._get(link)
                if p['status'] != 'ok':
                    return
                files = p['files']
                _cache.set(cache_name, files,
                    expiration=datetime.timedelta(hours=2))
            return files
        #except: return

    def direct_search(self, query):
        try:
            api_key = self.get_api()
            if not api_key: return
            link = (self.base_link + self.search_direct_link % (api_key, query))
            cache_name = "fen_FURK_SEARCH_DIRECT_%s" % link
            cache = _cache.get(cache_name)
            if cache:
                files = cache
            else:
                p = self._get(link)
                if p['status'] != 'ok':
                    return
                files = p['files']
                _cache.set(cache_name, files,
                    expiration=datetime.timedelta(hours=2))
            return files
        except: return

    def t_files(self, file_id):
        try:
            cache = _cache.get("fen_%s_%s" % ('FURK_T_FILE', file_id))
            if cache:
                t_files = cache
            else:
                api_key = self.get_api()
                link = (self.base_link + self.tfile_link % (api_key, file_id))
                p = self._get(link)
                if p['status'] != 'ok' or p['found_files'] != '1': return
                t_files = p['files']
                t_files = (t_files[0])['t_files']
                _cache.set("fen_%s_%s" % ('FURK_T_FILE', file_id), t_files,
                    expiration=datetime.timedelta(hours=2))
            return t_files
        except: return

    def file_get_video(self):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.file_get_video_link % (api_key))
            p = self._get(link)
            files = p['files']
            return files
        except: return

    def file_get_audio(self):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.file_get_audio_link % (api_key))
            p = self._get(link)
            files = p['files']
            return files
        except: return

    def file_get_active(self):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.active_dl_link % (api_key))
            p = self._get(link)
            files = p['torrents']
            return files
        except: return

    def file_get_failed(self):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.failed_dl_link % (api_key))
            p = self._get(link)
            files = p['torrents']
            return files
        except: return

    def file_link(self, item_id):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.file_link_link % (api_key, item_id))
            return self._get(link)
        except: return

    def file_unlink(self, item_id):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.file_unlink_link % (api_key, item_id))
            return self._get(link)
        except: return

    def download_unlink(self, item_id):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.remove_dl_link % (api_key, item_id))
            return self._get(link)
        except: return

    def file_protect(self, item_id, is_protected):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.file_protect_link % (api_key, item_id, is_protected))
            return self._get(link)
        except: return

    def add_uncached(self, item_id):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.add_uncached_link % (api_key, item_id))
            return self._get(link)
        except: return

    def account_info(self):
        try:
            api_key = self.get_api()
            link = (self.base_link + self.account_info_link % (api_key))
            return self._get(link)
        except: return

    def _get(self, link):
        p_org = get_html(link, timeout=self.timeout)
        p = to_utf8(remove_accents(p_org.text()))
        return (p_org.json())

def clear_media_results_database():
    import xbmc
    try: from sqlite3 import dbapi2 as database
    except ImportError: from pysqlite2 import dbapi2 as database
    profile_dir = xbmc_tranlate_path(__addon__.getAddonInfo('profile'))
    try: fen_cache_file = xbmc_tranlate_path("%s/fen_cache.db" % profile_dir).decode('utf-8')
    except: fen_cache_file = xbmc_tranlate_path("%s/fen_cache.db" % profile_dir)
    dbcon = database.connect(fen_cache_file)
    dbcur = dbcon.cursor()
    try:
        dbcur.execute("DELETE FROM fencache WHERE id LIKE 'fen_FURK_SEARCH_%'")
        dbcon.commit()
        dbcon.close()
        return 'success'
    except: return 'failed'
