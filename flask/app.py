from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/department')
def department():
	return render_template('department.html')

@app.route('/Student Corner')
def service():
 	return render_template('Student Corner.html')

if __name__ == '__main__':
	    app.run(debug=True)