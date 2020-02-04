import pyrebase
from flask import Flask, render_template, request, jsonify
from read_api import image_analyser
import os
from werkzeug.utils import secure_filename

config = {
		"apiKey": "AIzaSyCxnFqPQ4Rv3wxK8ajGWzDE_kIOtCaN2Bs",
		"authDomain": "test-f8bf5.firebaseapp.com",
		"databaseURL": "https://test-f8bf5.firebaseio.com",
		"projectId": "test-f8bf5",
		"storageBucket": "test-f8bf5.appspot.com",
		"messagingSenderId": "138404693159",
		"appId": "1:138404693159:web:c6f4edd5a809158560c782"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "upload_folder")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']


@app.route('/', methods =['GET', 'POST'])
def basic():
	# if request.method == "POST":
	#     if request.form["submit"] =='doctor':
	#         doctorcall()
	#     elif request.form["submit"] == 'patient':
	#         patientcall()
	return render_template('index.html')

@app.route('/doctor', methods=['GET', 'POST'])
def doctorcall():
		if request.method == "POST":
				if request.form["submit"] =='add':
						name = request.form['name']
						db.child("doctor").push(name)
						todo = db.child("doctor").get()
						# return todo.val()
						to = todo.val()
						return render_template('doctor.html', t= to.values())
		
		return render_template('doctor.html')


@app.route('/patient', methods=['GET', 'POST'])
def patientcall():
	 if request.method == "POST":
				if request.form["submit"] =='add':
						name = request.form['name']
						db.child("patient").push(name)
						todo = db.child("patient").get()
						# return todo.val()
						to = todo.val()
						return render_template('patient.html', t= to.values())
	 return render_template('patient.html')


@app.route('/image_analysis', methods=['GET','POST'])
def return_analysis():
		if request.method == "POST":
			if 'file' not in request.files:
					resp = {"Upload UnSuccessfull":"No file Present"}
					resp = jsonify(resp)
					resp.status_code = 400
					return resp
			input_file = request.files['file']
					# if user does not select file, browser also
					# submit a empty part without filename

			if input_file.filename == '':
				resp = {"Upload UnSuccessfull":"File Name not clear"}
				resp = jsonify(resp)
				resp.status_code = 400
				return resp
            
			f = request.files['file']
			file_name =secure_filename(f.filename)
			# check if file is allowed or not
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
			resp = image_analyser(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
			resp = jsonify(resp)
			os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
			resp.status_code = 200
			return resp
		else:
			return "use post request"
	 


if __name__ == '__main__':
		app.run(debug=True)    


