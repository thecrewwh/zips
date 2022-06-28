"""
    Usage Examples:

	### Search ###
	
	** Returns a list of Movies searched for from IMDB
    <dir>
      <title>Search IMDB Movies</title>
      <imdburl>searchmovies</imdburl>
      <thumbnail></thumbnail>
    </dir>
	
	** Returns a list of TV Shows searched for from IMDB
    <dir>
      <title>Search IMDB TV Shows</title>	
      <imdburl>searchseries</imdburl>
      <thumbnail></thumbnail>
    </dir>


	### Movies ###

	** Returns a list of the IMDB Trending Movies
    <dir>
      <title>IMDB Trending Movies</title>
      <imdburl>movies/trending</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Box Office Movies
    <dir>
      <title>IMDB Box Office Movies</title>
      <imdburl>movies/boxoffice</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Most Popular Movies
    <dir>
      <title>IMDB Most Popular Movies</title>
      <imdburl>movies/popular</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Most Voted Movies
    <dir>
      <title>IMDB Most Voted Movies</title>
      <imdburl>movies/voted</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of IMDB Movies by a specific Year.  Change Year at the end of the Second Tag as desired.
    <dir>
      <title>IMDB 2018 Movies</title>
      <imdburl>years/2018</imdburl>                       * other Years found in movies_years-imdb.xml
      <thumbnail></thumbnail>
    </dir>


	### TV Shows ###

	** Returns a list of the IMDB Newest TV Shows
    <dir>
      <title>IMDB Newest TV Shows</title>
      <imdburl>tvshows/new</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Most Viewed TV Shows
    <dir>
      <title>IMDB Most Viewed TV Shows</title>
      <imdburl>tvshows/mostviews</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Best User Rated TV Shows
    <dir>
      <title>IMDB Best User Rated TV Shows</title>
      <imdburl>tvshows/rating</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Most Popular TV Shows	
    <dir>
      <title>IMDB Most Popular TV Shows</title>
      <imdburl>tvshows/popular</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of the IMDB Box Office TV Shows	
    <dir>
      <title>IMDB Box Office TV Shows</title>
      <imdburl>tvshows/boxoffice</imdburl>
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of IMDB TV Shows in Alphabetical order
    <dir>
      <title>IMDB A to Z TV Shows</title>
      <imdburl>tvshows/alphabetical</imdburl>
      <thumbnail></thumbnail>
    </dir>
	
	
	### Charts ###

	** Returns a list of the IMDB Top Rated TV Shows
    <dir>
      <title>IMDB Top Rated TV Shows</title>
      <imdburl>charttv/toptv</imdburl>
      <thumbnail></thumbnail>
    </dir>


	### Genres ###

	** Returns a list of IMDB Movies by a specific Genre.  Switch out "action" Genre as desired at the end Of the Second Tag.
    <dir>
      <title>IMDB Action Movies</title>
      <imdburl>genres/action</imdburl>                     * other Genres found in movies_genres-imdb.xml
      <thumbnail></thumbnail>
    </dir>

	** Returns a list of IMDB TV Shows by a specific Genre.  Switch out "history" Genre as desired at the end Of the Second Tag.
    <dir>
      <title>IMDB History TV Shows</title>
      <imdburl>genrestv/history</imdburl>                  * other Genres found in tvshows_genres-imdb.xml
      <thumbnail></thumbnail>
    </dir>
		
		
	### User Lists ###
    
	** Returns ALL public IMDB Lists from a specific user
    <dir>
      <title>Someone's IMDB Lists</title>
	  <imdburl>user/ur19947955/lists</imdburl>             # If you have a IMDB account with lists, add YOUR user ID like this and it will 
	  <thumbnail></thumbnail>							     return all public lists on YOUR account
    </dir>
	
	** Returns a SINGLE public IMDB List from a specific user
    <dir>
      <title>Someone's IMDB List</title>
      <imdburl>/list/ls068927829/</imdburl>
      <thumbnail></thumbnail>
    </dir>
	
	** Returns a specific user's IMDB Top 100 Gangster Movies public list
    <dir>
      <title>IMDB TOP 100 Gangster Movies</title>
      <imdburl>list/ls001818278</imdburl>
      <thumbnail></thumbnail>
    </dir>
		
		
	### Calendar ###
    
	** Returns a List of Upcoming Releases by Country.
    <dir>
        <title>IMDB Upcoming Releases in the United States</title>
        <imdburl>moviecalendar/US</imdburl>
    </dir>
    
	** Returns a List of Upcoming Releases by Country
    <dir>
        <title>IMDB Upcoming Releases in the United Kingdom</title>
        <imdburl>moviecalendar/GB</imdburl>
    </dir>
    
	** Returns a List of Upcoming Releases by Country
    <dir>
        <title>IMDB Upcoming Releases in Mexico</title>
        <imdburl>moviecalendar/MX</imdburl>
    </dir>

	-------------------------------------------------------------
"""
from resources.modules import log
from resources.modules import public
import logging,xbmcplugin,sys,re,xbmc,json
addDir3=public.addDir3
addLink=public.addLink
from  resources.modules.client import get_html
def run(url,lang,icon,fanart,plot,name):
    return addDir3(name,'imdburl',193,icon,fanart,plot,id=url)
        
def next_level(url,icon,fanart,plot,name,id):
    COLOR1 = ""
    COLOR2 = ""
    all_d=[]
    if 'searchmovies' in id:
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Enter Title')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','+')
        if len(search_entered)>1:
            id = 'movies$$$$$https://www.imdb.com/search/title/?title=' + search_entered
        else:
            return 0
    if 'movies' in id:
        id=id.replace('movies$$$$$','')
        id = id.replace("movies/popular","https://www.imdb.com/search/title/?title_type=feature").replace("movies/voted","https://www.imdb.com/search/title/?title_type=feature&num_votes=1000,&sort=year,desc").replace("movies/trending","https://www.imdb.com/search/title/?title_type=feature&groups=top_1000&sort=year,desc").replace("movies/boxoffice","https://www.imdb.com/search/title/?title_type=feature&groups=now-playing-us&sort=year,desc")
        log.warning(id)
        listhtml = get_html(id).content()
        match = re.compile(
                '<img alt=".+?"\nclass="loadlate"\nloadlate="(.+?)"\ndata-tconst="(.+?)"\nheight="98"\nsrc=".+?"\nwidth="67" />\n</a>.+?</div>\n.+?<div class="lister-item-content">\n<h3 class="lister-item-header">\n.+?<span class="lister-item-index unbold text-primary">.+?</span>\n.+?\n.+?<a href=".+?"\n>(.+?)</a>\n.+?<span class="lister-item-year text-muted unbold">(.+?)</span>',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        for thumbnail, imdb, title, year in match:
            name = title + " " + year
            year = year.replace("(","").replace(")","")
            thumbnail = thumbnail.replace("@._V1_UX67_CR0,0,67,98_AL_.jpg","@._V1_UX520_CR0,0,520,700_AL_.jpg")
            if not COLOR1 == "":
                name = "[COLOR %s]%s[/COLOR]" % (COLOR1, name)
            aa=addDir3( name, 'www',15, thumbnail,thumbnail,name,data=year,original_title=name,id=imdb,eng_name=name,show_original_year=year,heb_name=name)
            all_d.append(aa)
        next_page = re.compile(
                    '<a href="([^"]+)"\nclass="lister-page-next next-page"',
                    re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        if not COLOR2 == "":
            myPage = "[COLOR %s]Next Page >>[/COLOR]" % COLOR2
        else:
            myPage = "Next Page >>"
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]','imdburl',193,'https://thumbs.dreamstime.com/b/next-page-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-135740961.jpg','http://copasi.org/images/next.png','Next page',id='movies$$$$$http://www.imdb.com/'+next_page)
        all_d.append(aa)
        
        
               
        
    elif "tvshows/" in id:
        id=id.replace('tvshows/$$$$$','')
        id = id.replace("tvshows/popular","https://www.imdb.com/search/title/?title_type=tv_series")
        id = id.replace("tvshows/new","https://www.imdb.com/search/title/?title_type=tv_series&release_date=2022-01-01,")
        id = id.replace("tvshows/rating","https://www.imdb.com/search/title/?title_type=tv_series&num_votes=5000,")
        id = id.replace("tvshows/mostviews","https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100,&sort=year,desc")
        id = id.replace("tvshows/boxoffice","https://www.imdb.com/search/title/?title_type=tv_series&sort=boxoffice_gross_us,asc")
        id = id.replace("tvshows/alphabetical","https://www.imdb.com/search/title/?title_type=tv_series&sort=alpha,desc")

        listhtml = get_html(id).content()
        match = re.compile(
                '<img alt=".+?"\nclass="loadlate"\nloadlate="(.+?)"\ndata-tconst="(.+?)"\nheight="98"\nsrc=".+?"\nwidth="67" />\n</a>.+?</div>\n.+?<div class="lister-item-content">\n<h3 class="lister-item-header">\n.+?<span class="lister-item-index unbold text-primary">.+?</span>\n.+?\n.+?<a href=".+?"\n>(.+?)</a>\n.+?<span class="lister-item-year text-muted unbold">(.+?)</span>',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        for thumbnail, imdb, title, year in match:
            name = title + " " + year
            year = year.replace("(","").replace(")","")
            thumbnail = thumbnail.replace("@._V1_UX67_CR0,0,67,98_AL_.jpg","@._V1_UX520_CR0,0,520,700_AL_.jpg")
            if not COLOR1 == "":
                name = "[COLOR %s]%s[/COLOR]" % (COLOR1, name)
            aa=addDir3(name,'imdburl',193,thumbnail,thumbnail,plot,id='season/%s'%imdb)
            all_d.append(aa)
        next_page = re.compile(
                    '<a href="([^"]+)"\nclass="lister-page-next next-page"',
                    re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        if not COLOR2 == "":
            myPage = "[COLOR %s]Next Page >>[/COLOR]" % COLOR2
        else:
            myPage = "Next Page >>"
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]','imdburl',193,'https://thumbs.dreamstime.com/b/next-page-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-135740961.jpg','http://copasi.org/images/next.png','Next page',id='tvshows/$$$$$http://www.imdb.com/'+next_page)
        all_d.append(aa)
        
        
               
        
    elif 'season/' in id:
        
        
        id = id.replace("season/","title/")
        id = 'http://www.imdb.com/' + id
        log.warning(id)
        imdb=id.replace('http://www.imdb.com/title/','')
        listhtml = get_html(id).content()
        
        match2 = re.compile(
                '<h4 class="float-left">Years</h4><hr />\n.+?</div>\n.+?<br class="clear" />\n.+?<div>\n.+?<a href="/title/(.+?)/episodes.+?season=.+?&ref_=tt_eps_sn_.+?"\n>(.+?)</a>&nbsp;&nbsp;',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        
                
        #match3 = re.compile('<div id="main">\n.+?<div class=seasonAndYearNav>.+?<select id="bySeason".+?tconst="(.+?)".+?<option.+?value="(.+?)"',re.IGNORECASE | re.DOTALL).findall(listhtml)
        for season in range(1,int(match2[0][1])+1):
            
            name = "Season: %s" % (str(season))
            
            episodeURL='https://www.imdb.com/title/%s/episodes?season=%s&ref_=tt_eps_sn_%s'%(imdb,season,season)
            
            aa=addDir3(name,'imdburl',193,icon,fanart,plot,id=episodeURL,season=season)
            all_d.append(aa)
           
    elif 'episodes' in id:
        o_imdb=re.compile('https://www.imdb.com/title/(.+?)/').findall(id)[0]
        log.warning(id)
        listhtml = get_html(id).content()
        match = re.compile(
                '<div data-const="(.+?)" class="hover-over-image zero-z-index ">\n<img width=".+?" height=".+?" class="zero-z-index" alt="(.+?)" src="(.+?)">\n<div>S(.+?), Ep(.+?)</div>\n</div>\n</a>.+?</div>\n.+?<div class="info" itemprop="episodes" itemscope itemtype=".+?">\n.+?<meta itemprop="episodeNumber" content=".+?"/>\n.+?<div class="airdate">\n.+?([^"]+)\n.+?</div>',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        for imdb, title, thumbnail, season, episode, premiered in match:
                tvshowtitle = re.compile(
                                '<h3 itemprop="name">\n<a href="/title/.+?/.+?ref_=ttep_ep_tt"\nitemprop=.+?>(.+?)</a>',
                                re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
                summery=re.compile(
                                '<div class="item_description" itemprop="description">(.+?)</div>',
                                re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
                thumbnail = thumbnail.replace("@._V1_UX200_CR0,0,200,112_AL_.jpg","@._V1_UX600_CR0,0,600,400_AL_.jpg")
                if int(season) > 0 and int(season) < 10:
                    mySeason = "0" + str(season)
                else:
                    mySeason = str(season)
                if int(episode) > 0 and int(episode) < 10:
                    myEpisode = "0" + str(episode)
                else:
                    myEpisode = str(episode)
                if not COLOR1 == "" and not COLOR2 == "":
                    name = "[COLOR %s]S%sE%s[/COLOR] - [COLOR %s]%s[/COLOR]" % (COLOR2, mySeason, myEpisode, COLOR1, title)
                else:
                    name = "S%sE%s - %s" % (mySeason, myEpisode, title)
                aa=addDir3(name,'www',15,thumbnail,thumbnail,summery,original_title=tvshowtitle,season=season,episode=episode,id=o_imdb)
                all_d.append(aa)
                
    elif 'charttv' in id:
        id = id.replace("charttv/","chart/")
        id = 'http://www.imdb.com/' + id
        log.warning(id)
        listhtml = get_html(id).content()
        match = re.compile(
                '<a href="/title/(.+?)/.+?pf_rd_m=.+?pf_rd_i=.+?&ref_=.+?"\n> <img src="(.+?)" width=".+?" height=".+?"/>\n</a>.+?</td>\n.+?<td class="titleColumn">\n.+?\n.+?<a href=".+?"\ntitle=".+?" >(.+?)</a>\n.+?<span class="secondaryInfo">(.+?)</span>',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        for imdb, thumbnail, title, year in match:
            name = title + " " + year
            year = year.replace("(","").replace(")","")
            thumbnail = thumbnail.replace("@._V1_UY67_CR0,0,45,67_AL_.jpg","@._V1_UX520_CR0,0,520,700_AL_.jpg")
            if not COLOR1 == "":
                name = "[COLOR %s]%s[/COLOR]" % (COLOR1, name)
            aa=addDir3(name,'imdburl',193,thumbnail,thumbnail,' ',id='season/%s'%imdb)
            all_d.append(aa)
    elif 'genres/' in id:
        id=id.replace('genres/$$$$$','')
        id = id.replace("genres/","")
        id = 'http://www.imdb.com/search/title?genres=' +id + '&explore=title_type,genres&title_type=tvMovie&ref_=adv_explore_rhs'
        listhtml = get_html(id).content()
        match = re.compile(
                '<img alt=".+?"\nclass="loadlate"\nloadlate="(.+?)"\ndata-tconst="(.+?)"\nheight="98"\nsrc=".+?"\nwidth="67" />\n</a>.+?</div>\n.+?<div class="lister-item-content">\n<h3 class="lister-item-header">\n.+?<span class="lister-item-index unbold text-primary">.+?</span>\n.+?\n.+?<a href=".+?"\n>(.+?)</a>\n.+?<span class="lister-item-year text-muted unbold">(.+?)</span>',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        for thumbnail, imdb, title, year in match:
            name = title + " " + year
            year = year.replace("(","").replace(")","").replace(" TV Movie","")
            thumbnail = thumbnail.replace("@._V1_UX67_CR0,0,67,98_AL_.jpg","@._V1_UX520_CR0,0,520,700_AL_.jpg")
            if not COLOR1 == "":
                name = "[COLOR %s]%s[/COLOR]" % (COLOR1, name)
            aa=addDir3( name, 'www',15, thumbnail,thumbnail,name,data=year,original_title=name,id=imdb,eng_name=name,show_original_year=year,heb_name=name)
            all_d.append(aa)
        next_page = re.compile(
                    '<a href="([^"]+)"\nclass="lister-page-next next-page"',
                    re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        if not COLOR2 == "":
            myPage = "[COLOR %s]Next Page >>[/COLOR]" % COLOR2
        else:
            myPage = "Next Page >>"
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]','imdburl',193,'https://thumbs.dreamstime.com/b/next-page-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-135740961.jpg','http://copasi.org/images/next.png','Next page',id='genres/$$$$$http://www.imdb.com/'+next_page)
        all_d.append(aa)
    elif 'genrestv/' in id:
        if '$$$$$' in id:
            id = id.replace("genrestv/$$$$$","")
        else:
            id = id.replace("genrestv/","")
            id = 'http://www.imdb.com/search/title?genres=' + url + '&explore=title_type,genres&title_type=tvSeries&ref_=adv_explore_rhs'
        listhtml = get_html(id).content()
        match = re.compile(
                '<img alt=".+?"\nclass="loadlate"\nloadlate="(.+?)"\ndata-tconst="(.+?)"\nheight="98"\nsrc=".+?"\nwidth="67" />\n</a>.+?</div>\n.+?<div class="lister-item-content">\n<h3 class="lister-item-header">\n.+?<span class="lister-item-index unbold text-primary">.+?</span>\n.+?\n.+?<a href=".+?"\n>(.+?)</a>\n.+?<span class="lister-item-year text-muted unbold">(.+?)</span>',
                re.IGNORECASE | re.DOTALL).findall(listhtml)
        for thumbnail, imdb, title, year in match:
            name = title + " " + year
            year = year.replace("(","").replace(")","")
            thumbnail = thumbnail.replace("@._V1_UX67_CR0,0,67,98_AL_.jpg","@._V1_UX520_CR0,0,520,700_AL_.jpg")
            if not COLOR1 == "":
                name = "[COLOR %s]%s[/COLOR]" % (COLOR1, name)
            aa=addDir3(name,'imdburl',193,thumbnail,thumbnail,plot,id='season/%s'%imdb)
            all_d.append(aa)
        next_page = re.compile(
                    '<a href="([^"]+)"\nclass="lister-page-next next-page"',
                    re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        if not COLOR2 == "":
            myPage = "[COLOR %s]Next Page >>[/COLOR]" % COLOR2
        else:
            myPage = "Next Page >>"
        log.warning('next_page:')
        log.warning(next_page)
        aa=addDir3('[COLOR aqua][I]Next page[/I][/COLOR]','imdburl',193,'https://thumbs.dreamstime.com/b/next-page-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-135740961.jpg','http://copasi.org/images/next.png','Next page',id='genrestv/$$$$$http://www.imdb.com/'+next_page)
        all_d.append(aa)
    
        
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))