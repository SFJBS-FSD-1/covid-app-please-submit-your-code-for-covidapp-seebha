import requests
from flask import Flask,render_template,request
import urllib.request

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])  #""" default method is get"""
def covid_page():
    if request.method=="POST":
        country=request.form["country_name"]
        print(country)
        url="https://api.covid19api.com/summary"
        print(url)
        response = requests.get(url).json()
        print(response['Countries'])
        for i in response['Countries']:
            if i['Country']==country:
                Total_Confirmed_cases=i['TotalConfirmed']
                Total_Deaths=i['TotalDeaths']
                break
        data={'Confirmed':Total_Confirmed_cases,'Total_deaths':Total_Deaths}
        return render_template("details.html",data=data)
    else:
        return render_template("details.html",data=None)


if __name__=="__main__":
    app.run()


