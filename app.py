from os import replace
import requests
import bs4
from flask import Flask,jsonify,request


#Setting the flask app
app = Flask(__name__)
app.url_map.strict_slashes=False

url="https://www.india.com/news/world/page/"

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
            date=p[0].text
            date=date.replace('<a href="https://www.india.com/author/newsdesk/">India.com </a>',"")
            date=date.replace("\nIndia.com News Desk\n","")
            date=date.replace("India.com","")
            date=date.strip()

            result={"headline":headline ,"paragraph":paragraph,"image url":image_url,"source url":source_url,"date":date}
            output.append(result)
        
    
    return output
    
    

    


@app.route('/')
def home():
    query=request.args.get('q')
    out="Thank You for using api,you have sucessfully deployed it \nHead over to documentation to know how to use api https://github.com/RorYin/News-API"
    if query == None:
        return out
    else:
        data=getdata(query)
 
        
    return jsonify(data)






if __name__ == '__main__':
    app.debug=True
    app.run()    