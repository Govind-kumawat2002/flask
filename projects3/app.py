from flask import Flask ,url_for ,render_template ,request ,redirect
app=Flask(__name__)
# app.config[]
# app.config    == {  }  # confige is defien a dict 

#flask apna ek global storage rkhta hai jo kuch time tk hold rkta hai 
import mysql.connector # type: ignore

# Connect to the database
conn = mysql.connector.connect(
    host="13.53.40.215",
    user="govind",
    password="govind12345",
    database="login"

)
if conn.is_connected():
    print("hm connect ho chuke ")
else:
    print("not conn")  

# mysql_cursor = conn.cursor()
# query = "INSERT INTO login (user_name, user_email, user_pass) VALUES (%s, %s, %s)"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods =['GET',"POST"])
def predict():
    if request.method=='POST':
        user_name =request.form['username']
        user_email=request.form['email']
        user_pass=request.form['password']
        # lst = [[user_name,user_email,user_pass]]
        # app.config['username']=user_name
        # app.config['useremail']=user_email
        # app.config['userpassword']=user_pass
        mysql_cursor = conn.cursor()                 #dictionary=True
        # Execute the SELECT query to fetch historical data
        query = "SELECT * FROM logine_system"
        query = "INSERT INTO logine_system (user_name, user_email,user_pass) VALUES (%s, %s, %s)"
        values= (user_name,user_email,user_pass)
        mysql_cursor.execute(query,values)
        print("row is instered :", mysql_cursor.rowcount)
    
    # Commit the transaction
        conn.commit()
        mysql_cursor.close()
        conn.close()
        print("hello ")
        print("jgfjgsfjgsjf")

        



        # return redirect(url_for('profile',username =user_name,email=user_email,password=user_pass))
        return render_template('index.html')
    
    print("hello ")
    print("hiiii")
      print("hello ")
    print("hiiii")
     print("hello ")
    print("hiiii")
      print("hello ")
    print("hiiii")
    






















    


@app.route('/profile/<username>/<email>/<password>')
def profile(username, email, password):
    print(app.config['username'])
    print(app.config['useremail'])
    print(app.config['userpassword']) # local var acces in local block 
    app.config['username']=username
    app.config['useremail']=email
    app.config['userpassword']=password


    # return render_template('profile.html',name=username,email=email,password=password)    
    # return "hello "
    
    

# @app.route('/logout')
# def logout():
#     user=app.config['username'] 
#     email=app.config['useremail']
#     pas=app.config['userpassword']
    
#     return render_template('logout.html',name=user,email=email) 
# @app.route('/signout/<username>/<email>')
# def signout(username,email):
#     # return f"username {username,}and email {email}"
#     return render_template('logout.html',name=username,email=email) 


# @app.route('/jinja')
# def jinja():


#     # sub = ['math','science','bio']
#     user_details = {"username":'Radhey',"email":'raj@gmail.com','city':'jaipur','state':'rajasthan'}
#     x = 2
#     return render_template('jinja.html',sub =user_details,x=x)

    



if __name__=='__main__':
    app.run(debug=True)