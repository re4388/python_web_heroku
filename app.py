from flask import Flask, request, abort
import os 
from boto.s3.connection import S3Connection



app = Flask(__name__)

var1 = S3Connection(os.environ['Access_Token'])


@app.route("/")
def hello():
    return ('hello', var1)



if __name__ == "__main__":
    app.run(port=5002)



