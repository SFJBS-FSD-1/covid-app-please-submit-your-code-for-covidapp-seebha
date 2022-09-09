from flask import Flask
import os

app=Flask(__name__)



@app.route("/")
def home_page():
    return ("<h1>Welcome to the APP</h1>")

port=int(os.environ.get("PORT",5000))


if __name__=="__main__":
    app.run(port=port)


#git commands in terminal
#git init
#git status