from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(msg="Hello World")

if __name__=="__main__":
    from os import getenv
    from dotenv import load_dotenv
    load_env()
    h = getenv("HOST")
    p = getnev("PORT")
    d = getenv("DEBUG")
    app.run(host=h,port=p,debug=d)
