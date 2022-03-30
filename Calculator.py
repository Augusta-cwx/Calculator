from flask import Flask,render_template,url_for,flash,redirect

app=Flask(__name__)

app.config['SECRET_KEY']='91d8760e655343e3b91fd4486536f5f6'

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/calc")
def calc():
	return render_template('calc.html')

if __name__=="__main__":
	app.run(debug==True)