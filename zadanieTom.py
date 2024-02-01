from flask import Flask,jsonify , request

app=Flask(__name__)

@app.route("/")

def witajswiecie():
    return "Hello World"

@app.route("/dane")
def dane():
    return jsonify({'imie':'Tomek', 'nazwisko':'Rogowski', 'email': 'tomasz.rogowski75@gmail.com'})

@app.route("/dane", methods=['POST'])
def LoadJson():
    content_type=request.headers.get('Content-type')
    if(content_type=='application/json'):
        mojeDane=request.get_jason()
        return mojeDane
app.run()
