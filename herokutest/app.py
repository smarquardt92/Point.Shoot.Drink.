import os
from flask import Flask, request, render_template, redirect, jsonify
from flask_mysqldb import MySQL
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Snowihop^9'
app.config['MYSQL_DB'] = 'Recipes'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)




mysql = MySQL(app)




@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)

        if request.files.get('file'):
            # read the file
            file = request.files['file']

            # read the filename, this is part of the image file you uplaod
            filename = file.filename 
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #predict=call sarahs code
            cur = mysql.connection.cursor()
            cur.execute("SELECT * From allrecipes WHERE Ingredients = 'Apple'")
            data = cur.fetchone()
            cur.close()
            print(data)
            return jsonify({'result': 'success', 'predictions': data})  

            # Save the file to the uploads folder
        return jsonify({'result': 'success', 'predictions': 'predictions'})  

    return render_template('index.html')    
            


    



if __name__ == "__main__":
    app.run(debug=True)