from flask  import Flask, render_template, request, redirect, url_for, session

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='static'
)


@app.route('/')
def intro_page():
	return render_template("intro.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/login',methods = ['POST', 'GET'])
def loginerrori():
  LoginPassword = request.form["Password"]
  LoginEmail = request.form["Email"]
  if LoginPassword == "":
    return render_template("errore2.html")
  elif LoginEmail == "":
    return render_template("errore2.html")
  else:
    return redirect(url_for('base_page'))

@app.route('/register')
def register():
  return render_template("register.html")

@app.route('/register',methods = ['POST', 'GET'])
def errori():
  Password = request.form["Password"]
  Email = request.form["Email"]
  Nome = request.form["Nome"]
  Cognome = request.form["Cognome"]
  RipetiPassword = request.form["RipetiPassword"]
  if Password == "":
    return render_template("errore2.html")
  elif RipetiPassword == "":
    return render_template("errore2.html")
  elif Nome == "":
    return render_template("errore2.html")
  elif Cognome == "":
    return render_template("errore2.html")
  elif Email == "":
    return render_template("errore2.html")
  elif Password!=RipetiPassword:
    return render_template("errore1.html")
  else:
    return redirect(url_for('base_page'))

@app.route('/shop')
def base_page():
  return render_template("base.html")

@app.route('/contact-us')
def contact_us():
	return render_template("contact-us.html")

@app.route('/about-us')
def about_us():
	return render_template("about-us.html")

@app.route('/aleks')
def aleks():
	return render_template('aleks.html')

if __name__ == "__main__":
  app.run(
		host='0.0.0.0',
		port=8080,
    debug=True
	)
