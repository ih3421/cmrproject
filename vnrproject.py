import urllib.request
from flask import Flask,render_template,request,redirect,session,url_for
from db import Database
app=Flask(__name__)  #Create Flask app instance
db=Database()  #Create Database instance
app.secret_key='lokesh i wanna **** ur ***'
@app.route('/') #when app is initialized, this will be called
def index():   
    return render_template('Home.html')

@app.route('/register',methods=['GET','POST']) 
def register_page():
    user_type=request.args.get('user_type')
    session['user_type']=user_type
    return render_template('register.html')
    
@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    user_type=session.get('user_type')
    print(name,email,password,user_type)
    response=db.insert(name,email,password,user_type)
    if response:
        return redirect(url_for('login_page'))
    else:
        message="Email already registered, please login"
        return redirect(url_for('login_page',message=message))

@app.route('/login',methods=['POST','GET'])
def login_page():
    message1=request.args.get('message')
    if message1:
        print('in if')
        return render_template('Login.html',message=message1)
    return render_template('Login.html')

@app.route('/perform_login',methods=['POST','GET'])
def perform_login():
    email=request.form.get('User_email')
    password=request.form.get('User_password')
    print(email,password)
    response=db.search(email,password)
    print('response',response)
    if response:
        user_type=session.get('user_type')
        s=(user_type+'_Dashboard')
        return redirect(url_for(s))
    else:
        message="Email not in database, please register"
        return redirect(url_for('re_register',message=message))

@app.route('/re_register',methods=['POST','GET'])
def re_register():
    message = request.args.get('message')
    return render_template('re-register.html', message=message)

@app.route('/PwD_Dashboard',methods=['GET'])
def PwD_Dashboard():
    return render_template('PwD_Dashboard.html')

@app.route('/Volunteer_Dashboard',methods=['GET'])
def Volunteer_Dashboard():
    return render_template('Volunteer_Dashboard.html')

@app.route('/NGO_Dashboard',methods=['GET'])
def NGO_Dashboard():
    return render_template('NGO_Dashboard.html')

@app.route('/help_request')
def help_request_page():
    return render_template('help_request.html')

@app.route('/profile_page',methods=['POST'])
def profile_page():
    name='x'
    return render_template('profile.html',name=name)


if __name__=='__main__':

    app.run(debug=True)
