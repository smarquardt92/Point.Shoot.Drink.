code that returns the drink name and ingredients (part 1)

import os
from flask import Flask, request, render_template, redirect, jsonify
from flask_mysqldb import MySQL
import pickle
mysql = MySQL()
from time import sleep
from ML import classify
app = Flask(__name__)
app.config['MYSQL_USER'] = 'ju78b2yixa3evno4'
app.config['MYSQL_PASSWORD'] = 'cqt4d0xvnqbtz1qt'
app.config['MYSQL_DB'] = 'mnmneqbmhy3vmj37'
app.config['MYSQL_HOST'] = 'ctgplw90pifdso61.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
#mysql.init_app(app)
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
            file.save(os.path.join("uploads/", filename))
            predict=classify.classifier(f"uploads/{filename}")
            # str1 = ''.join(predict)
            # print(str1)
            # c1 = str1.split(":")

            cur = mysql.connection.cursor()
            #var = "SELECT * FROM mnmneqbmhy3vmj37.cocktails1 where Ingredients Like '%"+predict+"%';"
            var = "SELECT Drink, Ingredients from mnmneqbmhy3vmj37.cocktails1 where Ingredients Like '%"+predict+"%';"
            
            cur.execute(var)
            #cur.execute("SELECT * From allrecipes WHERE Ingredients LIKE '%Apple%'")
            data = cur.fetchall()
           
            print(var)
        
            return render_template('index.html', object_list=data)
            #other_data= jsonify({'data': 'data'})
    
       
    return render_template('index.html')  
 
    
            
if __name__ == "__main__":
    app.run(debug=True)