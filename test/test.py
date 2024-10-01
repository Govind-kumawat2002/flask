from flask import Flask,render_template,request
app=Flask(__name__)

import mysql.connector as conn
server=conn.connect(host = '13.60.207.151',
             user='govind',
             password ='govind12345',
              database= 'boss' )


@app.route('/')
def home():
    return render_template('basic.html')

@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method=="POST":
        user1 =request.form['username']
        password1 = request.form['password']
        a=server.cursor()


        query = 'select *from logine'
        query= 'insert into logine(user,password)values(%s,%s)'
        values= (user1,password1)
        a.execute(query,values)
        server.commit()
       

        return render_template('basic.html')


if __name__=="__main__":
    app.run(debug=True)