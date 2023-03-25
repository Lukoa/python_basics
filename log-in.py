from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

#a directory to store the usernames and the passwords
users={'carline': 'lukoa12', 'Akala': 'akala12'}

#define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))

    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']
        if username in user and users[username]==password:
            session['username']=username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

        username=session['username']
        return
    render_template('dashboard.html', username=username)

@app.route('/logout')
def logout():
    
      
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.secert_key='secret_key'
    app.run(debug=True)

