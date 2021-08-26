from flask import Flask,render_template,request
import pyqrcode


app = Flask(__name__)

@app.route("/" ,methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        words=request.form.get("word")
        url=pyqrcode.create(words)
        url.svg("static/QRCODE.svg",scale=10)
        return render_template("result.html")
    return render_template("index.html")

@app.route("/index" ,methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        words=request.form.get("word")
        url=pyqrcode.create(words)
        url.svg("static/QRCODE.svg",scale=10)
        return render_template("result.html")




if __name__=="__main__":
    app.run(debug=True)