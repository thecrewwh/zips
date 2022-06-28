"""
    Usage Examples:

    Text inside the tags are a formatted base64 encoded string. The format is below.
    View Mode and Sort By can both be ignored in the searches by using None in those blocks.
    Format: Base ID|Table Name|Max Results|Sort By|View Mode|API Key

    Returns the Tv Channels

    -- Base64 Unencoded String: appycq5PhSS0tygok|tv_channels|700|channel|None|keyikW1exArRfNAWj
    <dir>
        <title>TV Channels #1</title>
        <arraki_air>YXBweWNxNVBoU1MwdHlnb2t8dHZfY2hhbm5lbHN8NzAwfGNoYW5uZWx8Tm9uZXxrZXlpa1cxZXhBclJmTkFXag==</arraki_air>
    </dir>


    --------------------------------------------------------------

"""
from resources.modules import public
import logging,xbmcplugin,sys,base64,json
addDir3=public.addDir3
addLink=public.addLink
from  resources.modules.client import get_html
def run(url,lang,icon,fanart,plot,name):
    return addDir3(name,'arraki_air',193,icon,fanart,plot,id=url)
        
def next_level(url,icon,fanart,plot,name,id):
    param_string = base64.b64decode(id).decode('utf-8')
    param_string = param_string.split('|')

    view = param_string[4]
    sort = param_string[3]
    maxRecords = param_string[2]
    api_key=param_string[5]
    # App ID, Table ID, Max Results, Sort ID, View Mode, API Key
    headers={'Authorization': 'Bearer {}'.format(api_key)}
    import posixpath
    ur=posixpath.join('https://api.airtable.com/','v0', param_string[0],param_string[1])
    
    x=get_html(ur,headers=headers,verify=False).json()
    
    
    all_d=[]
    
    for field in x['records']:
        links=[]
        res = field['fields']
        title=res['channel']
        channel = res['channel']
        thumbnail = res['thumbnail']
        fanart = res['fanart']
        category = res['category']
        if len(thumbnail)<2:
            thumbnail=icon
        if len(res['link'])>2:
            links .append( res['link'])
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
        
        aa=addLink(title,f_link,6,False,thumbnail,fanart,category,original_title=title,place_control=True)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    