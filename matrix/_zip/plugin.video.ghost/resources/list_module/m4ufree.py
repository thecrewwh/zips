
import xbmcaddon,os,xbmc,urllib,re,xbmcplugin,sys,logging
from  resources.modules.client import get_html
from resources.modules import public
addDir3=public.addDir3
addLink=public.addLink
base_header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',

            'Pragma': 'no-cache',
            
           
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            }
def main_list():
    all_d=[]
    aa=addDir3('Movies','https://m4ufree.tv/m4ufree-newadded-movies/page/1',199,'https://i1.wp.com/reviewvpn.com/wp-content/uploads/2020/07/How-to-Install-T2K-One-Click-Movie-Addon-e1595234117323.png?fit=305%2C321&ssl=1','https://i1.wp.com/paulsohn.org/wp-content/uploads/2012/05/movie-click.jpg','Movies')
    all_d.append(aa)
    
    aa=addDir3('Tv shows','https://m4ufree.tv/m4ufree-tvshow-series/page/2',199,'https://i1.wp.com/reviewvpn.com/wp-content/uploads/2020/07/How-to-Install-T2K-One-Click-Movie-Addon-e1595234117323.png?fit=305%2C321&ssl=1','https://i1.wp.com/paulsohn.org/wp-content/uploads/2012/05/movie-click.jpg','Movies')
    all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def m_list(name,url,iconimage,fanart):
    all_d=[]
    x=get_html(url,headers=base_header).content()
    regex=' <div class="item"><h3 class="title-mv">(.+?)</h3><div class="imagecover"><a href="(.+?)" title="(.+?)"><div class="imagecover" style=" background\: url\((.+?)\).+?<div class="quality" >(.+?)<.+?"tiptitle"><p>(.+?)</.+?IMDb\:(.+?)<.+?"jt-info">(.+?)<.+?"(.+?)</p>'
    m=re.compile(regex).findall(x)
    for title,link,title2,image,quality,tptitle,rating,year,plot in m:
        if '(' in title2:
            title2=title2.split('(')[0]
        aa=addLink(title2,'Solve m4u'+ link,6,False,image,image,quality+'\n'+plot,data=year,rating=rating,original_title=title,tmdb='unknown',year=year,place_control=True)
        all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))