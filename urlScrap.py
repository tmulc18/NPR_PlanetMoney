import requests
from bs4 import BeautifulSoup

#Podcast paths and file names differ by year

#2013: 3
#2014: 2
#2015: none


def download_file(url):
    local_filename = url.split('/')[-1]
    local_filename = local_filename.split('?')[0]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: 
                f.write(chunk)
    return local_filename



endSuffix = "_pmoney_pmpod.mp3?dl=1"
endSuffix2 = "_blog_pmoney.mp3?dl=1"
endSuffix3 = "_specials_pmoney.mp3?dl=1"
baseURL = "http://pd.npr.org/anon.npr-mp3/npr/pmoney/"
baseURL2 = "http://pd.npr.org/anon.npr-mp3/npr/blog/"
baseURL3 = "http://pd.npr.org/anon.npr-mp3/npr/specials/"
MonthSet = ["01","02","03","04","05","06","07","08","09","10","11","12"]
YearSet=["2013","2014","2014"]
DaySet=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

for year in YearSet:
	for month in MonthSet:
		for day in DaySet:
			if year == "2014":
				suffix = year+"/"+month+"/"+year+month+day+endSuffix2
				url = baseURL2+suffix
			elif year == "2013":
				suffix = year+"/"+month+"/"+year+month+day+endSuffix3
				url = baseURL3+suffix
			else:
				suffix = year+"/"+month+"/"+year+month+day+endSuffix2
				url = baseURL+suffix
			download_file(url)