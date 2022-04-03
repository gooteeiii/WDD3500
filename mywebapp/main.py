# importing of flask for use
from flask import Flask, url_for
# imported for use of redirect cmd
from werkzeug.utils import redirect

# app instance creation
app = Flask(__name__)

# index page
@app.route('/')
def hello_world():
 return 'Hello World'

# admin page
@app.route('/admin')
def admin_page():
 return "welcome to the admin page"

# guest page
@app.route('/guest/<guest>')
def hello_guest(guest):
 return 'Hello %s as Guest' % guest

# takes name entered in address and checks if user is admin,
# if so redirected to admin page, all others are redirected to guest page
@app.route('/user/<name>')
def get_user(name):
 if name == 'admin':
  return redirect('/admin')
 else:
  return redirect('/guest/' + name)

# runs app is module name matches
if __name__ == '__main__':
 app.run()