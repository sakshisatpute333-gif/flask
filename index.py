
from flask import Flask, request

app = Flask(__name__)

@app.route("/")                    # ex ("flipkart/abc") @app.route
def home():
    return("home route")

# test means  api endpoint
@app.route("/test", methods=["POST"])            # method (post)=add.
def about():
    data = request.json
    print(data)
    return "about route"


@app.route("/update", methods=["PUT"])
def updateNote():
    return "Note Update Success"

@app.route("/delete", methods=["DELETE"])
def deleteNote():
    return "Note Delete Success"           # you can write remove also


# it is responsible to server on 
app.run(debug=True)        #shortcut to server on/off option