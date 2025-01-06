# from flask import Flask
# app=Flask(__name__)  # wsgi(web server The full form of WSGI is Web Server Gateway Interface.

# # WSGI is a specification that defines how web servers communicate with web applications in Python.)
# @app.route('/')
# def home():
#     return "Welcome to my repositry"
# @app.route('/member')
# def member():
#     return "Welcome to my repositry member"  # binding function 



# if __name__=="__main__":
#     app.run(debug= True)


# building url diamecally 

# from flask import Flask ,redirect,url_for,render_template
# app=Flask(__name__)







# @app.route('/succes/<int:score>')  ### if we are pass the url data then we are to this method  int is deternime the dtype 
# def succes(score):
#     return "the persom has passed and the marks is "+str(score)  # binding function 
# @app.route('/fail/<int:score>')
# def fail(score):
#     return "the persom has fail and the marks is "+str(score)  # binding function
# # result checker  
# @app.route('/result/<int:marks>')
# def myresult(marks):
#     result = ""
#     if marks<50:
#         result = 'fail'
#     else :
#         result = 'succes'
#     # return result
#     return redirect(url_for(result,score=marks))  #  that is used to call the direct other route 

# @app.route('')
# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/submit',method=['POST',"GET"])
# def submit():
    # if method =='POST':

from flask import Flask ,redirect,url_for,render_template
app=Flask(__name__)


if __name__=="__main__":
    app.run(debug= True)
@app.route('/')
def home():
    return render_template('index.html')