from resources.modules import public
import logging,xbmcplugin,sys,re,xbmc,json
addDir3=public.addDir3
addLink=public.addLink
from  resources.modules.client import get_html
def run(url,lang,icon,fanart,plot,name):
    if 'page' not in url:
        url=url+'?limit=40&page=1'
    return addDir3(name,url.replace('https://api.trakt.tv/',''),117,icon,fanart,plot)