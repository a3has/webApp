from flask import Flask, render_template
from markupsafe import escape
from datetime import datetime
#from flask import render_template
from flask2act import app

myweb_obj = Flask(__name__)

@myweb_obj.route("/")

def view():
    Admin = {'username': 'Aboudi'}
    userList = [{'username': 'Mike'},{'username': 'Fred'}]
    return render_template('template.html')

myweb_obj.run()