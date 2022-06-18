import json

file2point0=open('/home/the-freak-coder/coder/python/Imdb_Scrape/Task1.json', 'r')

loading=json.load(file2point0)

def analyse_movies_language(movies_list):
    hr=movies_list['Runtime']//60
    min=movies_list['Runtime']%60
    movies_list['Runtime']={'hours':hr, 'minutes':min}
for details in loading:
    analyse_movies_language(details)
    
file2point1=open('/home/the-freak-coder/coder/python/Imdb_Scrape/Task5_6.json', 'w')
f=open('/home/the-freak-coder/coder/python/Imdb_Scrape/Task5_6.json', 'r')
f2=json.load(f)
json.dump(f2, file2point1, indent=4)    

