from flask import Flask, render_template, request
# from models import db, User
# from forms import SignupForm

app = Flask(__name__)



@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port=8080)