from flask import Flask,render_template,url_for,request
from database import post,get_data

app = Flask(__name__)


@app.route('/' , methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        msg = request.form.get('message')
        post(name,msg)
    database = get_data()
    return render_template("home.html",database=database)

if __name__=="__main__":
    app.run(debug=True)
