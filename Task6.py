import json

files=open('/home/the-freak-coder/coder/python/Imdb_Scrape/Task5_6.json', 'r')
v3=json.load(files)
dic={}
def analyse_movies_language(movies_list):
    global s
    for cout in movies_list:
    
        if cout in dic:
            s=dic[cout]
            s+=1
            dic.update({cout:s})
        else:
            if len(cout)<=10 and " " not in cout:
                dic.update({cout:s})

for details in v3:
    s=1
    analyse_movies_language(details['Language'])
print(dic)
    
