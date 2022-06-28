"""
    Usage Examples:

Movies coming out on dvd with release date:

<dir>
<title>Metacritic DVD Releases</title>
<metacritic>dvd</metacritic>
</dir>

Movies in theaters now:

<dir>
<title>Metacritic In Theaters</title>
<metacritic>theaters/0</metacritic>
</dir>

Movies coming soon with release date:

<dir>
<title>Metacritic Coming Soon</title>
<metacritic>coming/0</metacritic>
</dir>

TV Show trailers:

<dir>
<title>Metacritic TV Show Trailers</title>
<metacritic>tvshow/0</metacritic>
</dir>

"""    

from resources.modules import public
import logging,xbmcplugin,sys,re
addDir3=public.addDir3
addLink=public.addLink
from  resources.modules.client import get_html
def clean_search(title):
    if title == None: return
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace("&#039;","")
    title = re.sub('\\\|/|\(|\)|\[|\]|\{|\}|-|:|;|\*|\?|"|\'|<|>|\_|\.|\?', ' ', title)
    title = ' '.join(title.split())
    return title  
def run(url,lang,icon,fanart,plot,name):
    return addDir3(name,'metacritic',193,icon,fanart,plot,id=url)
        
def next_level(url,icon,fanart,plot,name,id):
    all_d=[]
    
    base_link = 'https://www.metacritic.com'
    if "dvd" in id:
        url = "https://www.metacritic.com/browse/dvds/release-date/coming-soon/date"
        next_page = None
    elif 'theaters' in id:
        if 'page' in id:
            
            current = str(int((id.split("page=")[1]))+1)
        else:
            current ='0'
        url = "https://www.metacritic.com/browse/movies/release-date/theaters/date?page="+current
        next_page = int(current)+1
    elif "coming" in id:
        if 'page' in id:
            
            current = str(int((id.split("page=")[1]))+1)
        else:
            current ='0'
        url = "https://www.metacritic.com/browse/movies/release-date/coming-soon/date?page="+current
        next_page = int(current)+1
    elif "tvshow" in id or 'tv-shows' in id:
        if 'page' in id:
            
            current = str(int((id.split("page=")[1]))+1)
        else:
            current ='0'
        
        url = "https://www.metacritic.com/browse/tv-shows/trailers/date?page="+current
       
        next_page = int(current)+1
        change_regex=True
        
    r = get_html(url).content()
    if change_regex:
        m = re.compile('<h3 class="trailer_title">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)"',re.DOTALL).findall(r)
        for oglink, image, name in m:
            f = oglink.split("trailers/")[0]
            p = oglink.split("/")[-1]
            link = base_link + f + "season-1/trailers/" + p                 
            name = (name).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
            name = clean_search(name)
            name = name
          
            summary=' '
            
            aa=addLink(name,link,6,False,image,image,summary,original_title=name,place_control=True)
            all_d.append(aa)
            
            
    else:
        m = re.compile('<td class="clamp-image-wrap">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span>(.+?)</span>.+?<div class="summary">(.+?)</div>',re.DOTALL).findall(r)
        for link, image, name, date, summary in m:
            link = base_link + link                  
            name = (name).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
            name = clean_search(name)
            name = name
            summary = clean_search(summary)
            summary = (summary).encode('ascii', errors='ignore').decode('ascii', errors='ignore')
            summary = summary
            image = image.replace("-98","-250h")      
            aa=addLink(name,link,6,False,image,image,summary,original_title=name,place_control=True)
            all_d.append(aa)
    if next_page:
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]','metacritic',193,'https://thumbs.dreamstime.com/b/next-page-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-135740961.jpg','http://copasi.org/images/next.png','Next page',id=url)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    return 0
    