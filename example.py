from flask import Flask
api = Flask(__name__)

@api.route("/")
def route_1():
    return {"msg":"Welcome To Home Api"}

if __name__=="__main__":
    api.run("0.0.0.0",debug=True)
