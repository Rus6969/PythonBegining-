from flask import Flask

 

app = Flask(__name__)

 

@app.route('/')

def home():

    return "Website Content"


#second

@app.route('/about')

def about():

    return "about page make sure methods should have different names "

 

if __name__=="__main__":

    app.run(debug=True)