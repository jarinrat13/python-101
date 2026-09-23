<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
=======
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
>>>>>>> 36e2367c506c94705546caf13817ba0e32d9cbfa
    app.run(debug=True)