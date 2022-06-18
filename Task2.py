import json
from pprint import pprint
def group_by_year():
    jfile=open('/home/the-freak-coder/coder/python/Imdb_Scrape/Task1.json', 'r')
    imdbmovies=json.load(jfile)
    moviesdic={}
    for movies in imdbmovies:
        listdic=[]
        for same in imdbmovies:
            if movies['Year']==same['Year']:
                listdic.append(same)
        moviesdic.update({int(movies['Year']):listdic})
    jfile1=open('/home/the-freak-coder/coder/python/Imdb_Scrape/Task2.json', 'w')
    json.dump(moviesdic, jfile1, indent=4)
    jfile.close()
    return moviesdic

pprint(group_by_year())
        







