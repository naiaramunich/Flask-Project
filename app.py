# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
#    return "Hello World!"
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
#    return "<p>This is my <b>1006 </b> website! <p>"
    return render_template("aboutme.html")

@app.route("/myclasses")
def myclasses(): 
    return render_template("myclasses.html")

#start the server
if __name__ == "__main__":
    app.run()