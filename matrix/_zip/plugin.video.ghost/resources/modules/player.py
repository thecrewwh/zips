
import xbmc,sys


class SMPlayer(xbmc.Player):
    def __init__(self, syshandle,link='', offset=None,infolabels={}):
        xbmc.Player.__init__(self)
    
    def play_source(self, syshandle,link='', offset=None,infolabels={}):
        item = tools.menuItem(path=link)
    
        item.setInfo(type='video', infoLabels=infolabels)
     
        item.setUniqueIDs(id)
        xbmcplugin.setResolvedUrl.resolvedUrl(syshandle, succeeded=True, listitem=item)
    def run_player(self):
        while self.isPlayingVideo():
            xbmc.sleep(100)
            