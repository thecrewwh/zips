import xbmcaddon,xbmc,os
Addon = xbmcaddon.Addon()
def warning(msg):
    msg=str(msg)
    
    if Addon.getSetting('show_debug')=='true':
        import inspect
        callerframerecord = inspect.stack()[1] 
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
       
        xbmc.log('/*'+Addon.getAddonInfo('name')+'*/'+' Line: %s-> '%(str(info.lineno)+','+os.path.basename(info.filename))+msg,level=xbmc.LOGWARNING)
def error(msg):
    msg=str(msg)
    if Addon.getSetting('show_debug')=='true':
        import inspect
        callerframerecord = inspect.stack()[1] 
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        xbmc.log('/*'+Addon.getAddonInfo('name')+'*/'+',Error, Line: %s-> '%(str(info.lineno)+','+os.path.basename(info.filename))+str(msg),level=xbmc.LOGWARNING)