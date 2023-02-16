from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Peeps!!"

if __name__ == "__main__":
  #to run the app locally, make sure the host is set to 0.0.0.0
  app.run(host='0.0.0.0', debug=True)
