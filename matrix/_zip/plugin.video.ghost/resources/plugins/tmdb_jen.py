"""
    Usage Examples:


	### Search ###
	
	** Returns a list of items Searched for from TMDB
	<dir>
	  <title>Search TMDB</title>
	  <tmdb>search</tmdb>
	</dir>


	### Movies ###
	
	** Returns a list of Now Playing Movies
	<dir>
	  <title>TMDB Movies Now Playing</title>
	  <tmdb>movies/now_playing</tmdb>
	</dir>

	** Returns a list of the TMDB Most Popular Movies
	<dir>
	  <title>TMDB Popular Movies</title>
	  <tmdb>movies/popular</tmdb>
	</dir>

	** Returns a list of the TMDB Top Rated Movies
	<dir>
	  <title>TMDB Top Rated Movies</title>
	  <tmdb>movies/top_rated</tmdb>
	</dir>

	** Returns upcoming movies, then Trailers for the movies.  Second Tag must be movie/upcoming
	<dir>
	  <title>TMDB Upcoming Movies</title>
	  <tmdb>movie/upcoming</tmdb>
	  <summary>Shows Trailers For Upcoming Movies</summary>
	</dir>

	** Returns a list of the TMDB Popular People Movies.  Results show only Movie Titles currently.
	<dir>
	  <title>TMDB Popular People Movies</title>
	  <tmdb>people/popular</tmdb>
	</dir>

	** Returns a list of the TMDB Movies by a specific Year.  Must change Year at the end Of the Second Tag.
	<dir>
	  <title>Movies Released In 2018</title>
	  <tmdb>year/movies/2018</tmdb>
	</dir>

	** Returns a list of Movies by a specific Genre.  Must change Genre ID at the end Of the Second Tag.
	<dir>
	  <title>TMDB Action Movies</title>
	  <tmdb>genre/movies/28</tmdb>
	</dir>

	** Returns a list of Movies by a Specific Actor.  Must change Actor ID at the end Of the Second Tag.
	<dir>
	  <title>Al Pacino</title>
	  <tmdb>person/movies/1158</tmdb>
	</dir>

	** Returns a list of Movies by a Production Companies.  Must change Production Company ID at the end Of the Second Tag.
	<dir>
		<title>Pixar Animation</title>
		<tmdb>company/movies/3</tmdb>
	</dir>

	** Returns a list of a specific Movie Collection.  Must change Movie Collection ID at the end Of the Second Tag.
	<dir>
	  <title>TMDB Star Wars Collection</title>
	  <tmdb>collection/10</tmdb>
	</dir>

	** Returns a list of Movies by a specific Keyword.  Must change Keyword ID at the end of the Second Tag.
	<dir>
	  <title>TMDB Army Movies</title>
	  <tmdb>keyword/movies/6092</tmdb>
	</dir>

	** Returns the Trailer for a specific Movie.   Must change Movie Trailer ID at the end of the Second Tag.
	<dir>
	  <title>Star Wars: The Last Jedi TRAILER</title>
	  <tmdb>trailer/181808</tmdb>
	</dir>


	### TV Shows ###
	
	** Returns a list of TV Shows Airing Today
	<dir>
	  <title>TMDB Shows Airing Today</title>
	  <tmdb>tv/today</tmdb>
	</dir>

	** Returns a list of the TMDB Popular TV Shows
	<dir>
	  <title>TMDB Popular Shows</title>
	  <tmdb>tv/popular</tmdb>
	</dir>

	** Returns a list of the TMDB Top Rated TV Shows
	<dir>
	  <title>TMDB Top Rated Shows</title>
	  <tmdb>tv/top_rated</tmdb>
	</dir>

	** Returns a list of the TMDB TV Shows Airing in the Next 7 Days
	<dir>
	  <title>TMDB Shows On The Air</title>
	  <tmdb>tv/on_the_air</tmdb>
	</dir>

	** Returns a list of the TMDB TV Shows by Genre.  Must change Genre ID at the end of the second Tag
	<dir>
	  <title>TMDB Animation Shows</title>
	  <tmdb>genre/shows/16</tmdb>
	</dir>

	** Returns a list of the TMDB TV Shows by Network.  Must change Network ID at the end of the second Tag
	<dir>
		<title>ABC</title>
		<tmdb>network/shows/2</tmdb>
	</dir>

	** Returns a list of the TMDB TV Shows by Actor.  Must change Actor ID at the end of the second Tag
	<dir>
	  <title>TMDB Bryan Cranston Shows</title>
	  <tmdb>person/shows/17419</tmdb>
	</dir>

	** Returns a list of the TMDB TV Shows by a specific Keyword.  Must change Keyword ID At The End Of The Second Tag
	<dir>
	  <title>TMDB King Shows</title>
	  <tmdb>keyword/shows/13084</tmdb>
	</dir>

	** Returns a list of the TMDB Animal Kingdom TV Shows.  Must change List ID at the end of the second Tag
	<dir>
	  <title>TMDB List: Animal Kingdom</title>
	  <tmdb>list/13488</tmdb>
	</dir>

    -------------------------------------------------------------
"""
from resources.modules import public
import logging
addDir3=public.addDir3

def run(url,lang,icon,fanart,plot,name):
    url=url.replace('movies','movie').replace('tv/today','tv/airing_today')
    
    id=''
    if 'year/movie' in url:
        url2='https://api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=%s&with_original_language=en&page=1'%(lang,url.split('year/movie/')[1])
        mode=14
    elif 'company/movie/' in url:
        split_url = url.split("/")
        if len(split_url) == 3:
            
            split_url.append(1)
       
        company_id = split_url[-2]
        url2='https://api.themoviedb.org/3/discover/movie?api_key=fb981e5ab89415bba616409d5eb5f05e&with_companies={0}&language={1}&sort_by=popularity.desc&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(company_id,lang)
        mode=14
    elif 'keyword' in url:
        split_url = url.split("/")
        if len(split_url) == 3:
            
            split_url.append(1)
        
        keyword_id = split_url[-2]
        media = split_url[-3]
        if media == "movie":
            s_type='movie'
        else:
            s_type='tv'
        
        url2='http://api.themoviedb.org/3/discover/%s?with_keywords=%s&api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(s_type,keyword_id,lang)
        mode=14
    elif 'collection/' in url:
        split_url = url.split("/")
        id = split_url[-1]
        url2='http://api.themoviedb.org/3/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(url,lang)
        mode=179
    elif 'network' in url:
        split_url = url.split("/")
        if len(split_url) == 3:
            
            split_url.append(1)
        
        network_id = split_url[-2]
        
        url2='https://api.themoviedb.org/3/discover/tv?api_key=fb981e5ab89415bba616409d5eb5f05e&with_networks={0}&language={1}&sort_by=popularity.desc&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(network_id,lang)
        mode=14
    elif 'genre' in url:
        split_url = url.split("/")
        if len(split_url) == 3:
            
            split_url.append(1)
       
        genre_id = split_url[-2]
        media = split_url[-3]
        if media == "movie":
            s_type='movie'
        else:
            s_type='tv'
        url2='http://api.themoviedb.org/3/discover/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&sort_by=popularity.desc&with_genres=%s&language=%s&page=1'%(s_type,genre_id,lang)
        mode=14
    elif 'list/' in url:
        id = url.split("/")[-1]
        url2='http://api.themoviedb.org/3/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(url,lang)
        mode=192
    elif 'people/popular' in url:
        url2='www'
        mode=72
    elif 'person' in url:
        split_url = url.split("/")
        url2 = split_url[-1]
        plot = split_url[-2]
        mode=73
    elif 'trailer/' in url:
        id = url.split("/")[-1]
        url2='movie'
        mode=25
        plot='play_now'
    elif 'search' in url:
        mode=5
        url2='www'
    else:
        url2='http://api.themoviedb.org/3/%s?api_key=fb981e5ab89415bba616409d5eb5f05e&language=%s&page=1'%(url,lang)
        mode=14
    
    return addDir3(name,url2,mode,icon,fanart,plot,id=id)
    