from flask import Flask, render_template, request
import google.generativeai as palm
import replicate
import os

flag = 1
name = ""

palm.configure(api_key= "AIzaSyC09-f0hyofybVT86uuypO_HTXgXL5__kw")
os.environ["REPLICATE_API_TOKEN"] = "r8_Wn2CfyxiKU3wJOZo2Fa5l2NrNih4kh71yEjwn"

model = {"model": "models/chat-bison-001"}
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return (render_template("index.html"))
    
@app.route("/main",methods=["GET","POST"])
def main():
    global flag, name 
    if flag == 1: 
        name = request.form.get("q")
        flag = 0
    return (render_template("main.html",r = name))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return (render_template("prediction.html"))

@app.route("/text",methods=["GET","POST"])
def dbs_price():
    q = float(request.form.get("q"))
    return (render_template("dbs_price.html",r=(q*-50.6)+90.2))

@app.route("/text_result_makersuite",methods=["GET","POST"])
def text_result_makersuite():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return (render_template("text_result_makersuite.html",r=r.last))
                            
@app.route("/generate_image",methods=["GET","POST"])
def generate_image():
    return (render_template("generate_image.html"))

@app.route("/image_result",methods=["GET","POST"])
def image_result():
    q = request.form.get("q")
    r = replicate.run ("stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                   input = {"prompt":q}
                      )
    return (render_template("image_result.html",r=r[0]))
                            
@app.route("/generate_text",methods=["GET","POST"])
def generate_text():
    return (render_template("generate_text.html"))

@app.route("/end",methods=["GET","POST"])
def end():
    global flag
    flag = 1 
    return (render_template("index.html"))
    
if __name__ == "__main__":
    app.run()
    
