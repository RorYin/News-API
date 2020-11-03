import requests
import bs4

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
def getdata(query):
    
    url="https://www.india.com/topic/"+query+"/page/"
    output=[]
    
    

    for k in range(1,4):
        try:

            res = requests.get(url+f"{k}"+'/',headers).text
        except:
            
            return result

        soup = bs4.BeautifulSoup(res,'lxml')
        i = soup.find_all('li',class_="contentblk blkwrp")

        for a in range(0,len(i)):
            p=i[a].findAll("p")
            headline=i[a].img['title']
            paragraph=p[1].text
            image_url=i[a].img["data-lazy-src"]
            source_url=i[a].a['href']
            

            result={"headline":headline ,"paragraph":paragraph,"image url":image_url,"source url":source_url}
            output.append(result)
        
    
    return output





