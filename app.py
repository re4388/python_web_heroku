from flask import Flask, request, abort
import configparser


app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config.ini")
print(config['config']['Access_Token'])

@app.route("/")
def hello():
    return config['config']['Access_Token']



if __name__ == "__main__":
    app.run(port=5002)



