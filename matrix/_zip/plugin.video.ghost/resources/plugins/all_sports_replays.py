"""
    Usage Examples:

    <dir>
    <title>All Sports Replays</title>
    <all_sports_replays>all</all_sports_replays>
    </dir> 
 
    <dir>
    <title>NFL Replays</title>
    <all_sports_replays>leagues/NFL/appSJCjNYAtA6KEfA</all_sports_replays>
    </dir> 

    <dir>
    <title>MLB Replays</title>
    <all_sports_replays>leagues/MLB/app8KZcIqmCP2GfTV</all_sports_replays>
    </dir>

    <dir>
    <title>Fottball Replays</title>
    <all_sports_replays>leagues/FOOTBALL/appGrvFmUpnlMqKE4</all_sports_replays>
    </dir>

    <dir>
    <title>Combat Sports Replays</title>
    <all_sports_replays>leagues/COMBAT_SPORTS/app2clmvReSTvxNTy</all_sports_replays>
    </dir>

    <dir>
    <title>Golf Replays</title>
    <all_sports_replays>leagues/GOLF_REPLAY/app3HVqPpxzqVUaGg</all_sports_replays>
    </dir>

    <dir>
    <title>NHL Replays</title>
    <all_sports_replays>leagues/NHL_REPLAY/app5BBPSzTk4D8ij0</all_sports_replays>
    </dir>

    <dir>
    <title>Motor Sports Replays</title>
    <all_sports_replays>leagues/MOTOR_SPORTS/appxkpEmICFgullUz</all_sports_replays>
    </dir>                    

    --------------------------------------------------------------

"""
from resources.modules import log
from resources.modules import public
import logging,xbmcplugin,sys
addDir3=public.addDir3
addLink=public.addLink
from  resources.modules.client import get_html
def run(url,lang,icon,fanart,plot,name):
    return addDir3(name,'all_sports_replays',193,icon,fanart,plot,id=url)
        
def next_level(url,icon,fanart,plot,name,id):
    import posixpath
    id=id.replace('%2f','/')
    api_key='keybx0HglywRKFmyS'
    if id=="all":
        table_key='appighRQxbaYJz1um'
        table_name = 'sports_replay_main'
        
    else:
        table_name = id.split("/")[-2]
        table_key = id.split("/")[-1]
    
    ur=posixpath.join('https://api.airtable.com/','v0', table_key,table_name)
    
    headers={'Authorization': 'Bearer {0}'.format(api_key)}
    x=get_html(ur,headers=headers,verify=False).json()
    log.warning(ur)
    log.warning(x)
    
    all_d=[]
    for field in x['records']:
        links=[]
        res = field['fields']   
        
        if 'name' not in res:
            continue
        name = res['name']
        name = (name).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
        thumbnail = res['thumbnail']
        fanart = res['fanart']
        if len(thumbnail)<2:
            thumbnail=icon
        if 'link' in res:
            link = 'leagues/'+res['link']      
        
        
            aa=addDir3(name,url,193,thumbnail,fanart,name,id=link) 
        elif 'link1' in res:
            if len(res['link1'])>2:
                links .append( res['link1'])
            if len(res['link2'])>2:
                links .append( res['link2'])
            if len(res['link3'])>2:
                links .append( res['link3'])
            if len(links)==0:
                continue
            if len(links)>1:
                f_link='$$$$'.join(links)
            else:
                f_link=links[0]
            aa=addLink(name,f_link,6,False,thumbnail,fanart,name,original_title=name,place_control=True)
        
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))