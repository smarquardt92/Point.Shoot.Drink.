import os
from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)

        if request.files.get('file'):
            # read the file
            file = request.files['file']

            # read the filename, this is part of teh image file you uplaod
            filename = file.filename

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Image Saved!"

    return render_template('index.html')


    



if __name__ == "__main__":
    app.run(debug=True)