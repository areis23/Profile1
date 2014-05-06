from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/more')
def more():
	return render_template('more.html')

@app.route('/thing/<something>')
def thing(something=None):
	return render_template('thing.html', something=something)
 
if __name__ == '__main__':
  app.run(debug=True)