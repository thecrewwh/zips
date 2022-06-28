"""
Usage Examples:


    Returns the Tv Channels-

    <dir>
    <title>Tv Channels</title>
    <Airtable>tv_channels</Airtable>
    </dir>

    Tv Channels2 are links that dont require plugins

    <dir>
    <title>Tv Channels2</title>
    <Airtable>channels2</Airtable>
    </dir>

    Returns the Sports Channels-

    <dir>
    <title>Sports Channels</title>
    <Airtable>sports_channels</Airtable>
    </dir>


    Returns the 24-7 Channels
    <dir>
    <title>24-7 Channels</title>
    <Airtable>247</Airtable>
    </dir>
    
    Custom
    <dir>
    <title>Custom title</title>
    <Airtable>tablename$$$tablekey</Airtable>
    
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
    return addDir3(name,'Airtable',193,icon,fanart,plot,id=url)
        
def next_level(url,icon,fanart,plot,name,id):
    import posixpath
    log.warning(id)
    if id=='247':
        table_name = 'twenty_four_seven'
        table_key='appMiehwc18Akz8Zv'
        key_header='keyikW1exArRfNAWj'
    elif id=='Tv_channels':
        table_key = 'appw1K6yy7YtatXbm'
        table_name = 'TV_channels'
        key_header='keyikW1exArRfNAWj'
    elif id=='Sports_channels':
        table_key = 'appFVmVwiMw0AS1cJ'
        table_name = 'Sports_channels'
        key_header='keyikW1exArRfNAWj'
    else:
        table_key = id.split('$$$')[0]
        table_name = name
        key_header=id.split('$$$')[1]
    ur=posixpath.join('https://api.airtable.com/','v0', table_key,table_name)
    
    headers={'Authorization': 'Bearer {0}'.format(key_header)}
    x=get_html(ur,headers=headers,verify=False).json()
    
    log.warning(x)
    all_d=[]
    for field in x['records']:
        links=[]
        res = field['fields']
        if 'name' in res:
            title=res['name']
        else:
            title=res['channel']
            channel = res['channel']
        thumbnail = res['thumbnail']
        fanart = res['fanart']
        category = res['category']
        if len(thumbnail)<2:
            thumbnail=icon
        for i in range(1, 5):
            if "link" + str(i) in res: 
                link=res["link" + str(i)]
                if "/live/" in link:
                    link = "ffmpegdirect://" + link
                if 'n/a' in link:
                    continue
                links .append(link )
                
        if len(links)==0:
            continue
        if len(links)>1:
            f_link='$$$$'.join(links)
        else:
            f_link=links[0]
        
        aa=addLink(title,f_link,6,False,thumbnail,fanart,category,original_title=title,place_control=True)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))