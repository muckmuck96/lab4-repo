
from app import app
from flask import request, render_template, redirect, url_for
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.ethereal.email'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'candida72@ethereal.email'
app.config['MAIL_PASSWORD'] = 'XWT1NcmYBaZ6gAktuJ'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def bio():
    return render_template('index.html')


@app.route('/contact-me')
def contact():
    return render_template('contact-me.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        email = request.form['email']
        cnt = request.form['content']
        msg = Message('Hello', sender = 'candida72@ethereal.email', recipients = [email])
        msg.body = cnt
        mail.send(msg)
        return redirect(url_for('bio'))
    else:
        return render_template('contact-me-form.html')

