"""
    Returns the Harry Potter list-

    <dir>
    <title>Harry Potter Movie List</title>
    <temp5_movie>movies</temp5_movie>
    </dir>


    ---------------------

    Possible Genre's are:
    Documentary
    Extras
    Movie
    Audio Books

    -----------------------

    Genre tag examples

    <dir>
    <title>Harry Potter Movies</title>
    <temp5_movie>genre/Movie</temp5_movie>
	<fanart></fanart>
	<thumbnail></thumbnail>
	<summary>All Harry Potter Movies</summary>
    </dir>

    <dir>
    <title>Harry Potter Documentaries</title>
    <temp5_movie>genre/Documentary</temp5_movie>
	<fanart></fanart>
	<thumbnail></thumbnail>
	<summary>Harry Potter Docs</summary>
    </dir>    
	
	<dir>
    <title>Harry Potter Extras</title>
    <temp5_movie>genre/Extras</temp5_movie>
	<fanart></fanart>
	<thumbnail></thumbnail>
	<summary>Extras & Fan Made</summary>
    </dir> 
	
	<dir>
    <title>Harry Potter Audio Books</title>
    <temp5_movie>genre/Audio Books</temp5_movie>
	<fanart></fanart>
	<thumbnail></thumbnail>
	<summary>Audio Books</summary>
    </dir> 
    --------------------------------------------------------------

"""
from resources.modules import public
import logging,xbmcplugin,sys,base64,json
addDir3=public.addDir3
addLink=public.addLink
from  resources.modules.client import get_html
def run(url,lang,icon,fanart,plot,name):
    return addDir3(name,'temp5_movie',193,icon,fanart,plot,id=url)
        
def next_level(url,icon,fanart,plot,name,id):
    table_id = "appfHeBBhg44AlpMO"
    table_name = "Harry%20Potter"
    api_key = "keyFw4tAzBr8ximp0"
    
    genre = id.split("/")[-1]

    
    # App ID, Table ID, Max Results, Sort ID, View Mode, API Key
    headers={'Authorization': 'Bearer {}'.format(api_key)}
    import posixpath
    ur=posixpath.join('https://api.airtable.com/','v0', table_id,table_name)

    x=get_html(ur,headers=headers,verify=False).json()
    
    
    all_d=[]
    
    for field in x['records']:
        links=[]
        res = field['fields']   
        if genre.lower() not in res['type'].lower() and 'movies' not in id:
            continue
        name = res['name']
        name = (name).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
        summary = res['summary']
        summary = (summary).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
        fanart = res['fanart']
        thumbnail = res['thumbnail']
        
        if len(thumbnail)<2:
            thumbnail=icon
        if len(res['link1'])>2:
            links .append( res['link1'])
        if len(res['link2'])>2:
            links .append( res['link2'])
        if len(res['link3'])>2:
            links .append( res['link3'])
        if len(res['link4'])>2:
            links .append( res['link4'])
        if len(res['link5'])>2:
            links .append( res['link5'])
        if len(links)==0:
            continue
        if len(links)>1:
            f_link='$$$$'.join(links)
        else:
            f_link=links[0]
        
        aa=addLink(name,f_link,6,False,thumbnail,fanart,summary,original_title=name,place_control=True)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    