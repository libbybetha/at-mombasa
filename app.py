from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
 	return '<h1>Hello mombasa !!</h1>'



@app.route('/bamburi')
def bamburi():
	return '<h1> we are now in bamburi!!</h1>'

@app.route('/town/<name>')
def town(name):
	return '<h1>I am in {name}</h1>'

if __name__ == '__main__':
    app.run()


 	


 			