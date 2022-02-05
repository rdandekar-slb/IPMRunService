from flask import Flask,render_template,request
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


# def home():
#     return 'Hello, World!'
@app.route('/')
def base_page():
	return render_template(
		'index.html'  # Template file path, starting from the templates folder. 
	)

# post method for getting folders
@app.route('/submitfolders', methods=(['POST']))
def submitfolders():
  data=request.form;
  print(data)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)