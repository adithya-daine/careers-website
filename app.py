from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bangalore, India',
  'salary': 'Rs 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs 15,00,000'
}, {
  'id': 3,
  'title': 'Front End Engineer',
  'location': 'Remote, India',
  'salary': 'Rs 12,00,000'
}, {
  'id': 4,
  'title': 'Data Analyst',
  'location': 'LA, USA',
  'salary': '$ 120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  #to run the app locally, make sure the host is set to 0.0.0.0
  app.run(host='0.0.0.0', debug=True)
