from re import DEBUG
from flask import Flask, json, render_template,jsonify
app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengluru,India',
    'salary':'Rs.10,00,000'
  },
   {
    'id':2,
    'title':'MLE',
    'location':'PUNE,India',
    'salary':'Rs.15,00,000'
   },
   {
    'id':3,
    'title':'FULL STACK',
    'location':'Noida,India',
     'salary':'Rs.15,00,000'
   
   }
]



@app.route("/")
def helloworld():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
