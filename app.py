from os import replace
import requests
import bs4
from flask import Flask,jsonify,request
import bytopic

#Setting the flask app
app = Flask(__name__)
app.url_map.strict_slashes=False

url="https://www.india.com/news/world/page/"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
def getdata(query):
       
    switch={
        "entertainment":"https://www.india.com/entertainment/page",
        "topnews":"https://www.india.com/news/india/page",
        "world":"https://www.india.com/news/world/page",
        "business":"https://www.india.com/business/page",
        "education":"https://www.india.com/education/page",
        "technology":"https://www.india.com/technology/page",
        "cricket":"https://www.india.com/cricket/page",
        "food":"https://www.india.com/food/page",
        "travel":"https://www.india.com/travel/page",
        "viral":"https://www.india.com/viral/page",
        "lifestyle":"https://www.india.com/lifestyle/page"
    }
    q=switch.get(query,"NA")
    if q== "NA":
        data=bytopic.getdata(query)
        if data != [] :
            return data
    else:
        cl="catPgListitem"
        url=q
    output=[]
    
    

    for k in range(1,6):
        try:

            res = requests.get(url+f"{k}",headers).text
        except:
            return "Please enter a keyword or a valid topic"
        soup = bs4.BeautifulSoup(res,'lxml')
        i = soup.find_all('li',class_=cl)
        print(i)

        for a in range(0,len(i)):
            t=i[a]
            p=t.findAll("p") 
            temp=p[1].text
            temp2=temp.replace('\n','')
                               
            temp3=temp2.strip()
            headline=i[a].h3.text
            paragraph=temp3.strip()
            image_url=i[a].img["data-lazy-src"]
            source_url=i[a].a['href']
            date=p[0].text
            date=date.replace('<a href="https://www.india.com/author/newsdesk/">India.com </a>',"")
            date=date.replace("\nIndia.com News Desk\n","")
            date=date.replace("India.com","")
            date=date.strip()

            result={"headline":headline ,"paragraph":paragraph,"image url":image_url,"source url":source_url,"date":date}
            output.append(result)
        
    #print(output)
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
