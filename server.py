from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
    session['count'] += 1
    # print(session['count'])
    # print(session)
    return render_template("code.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/addtwo', methods=['POST'])
def create_user():
    #print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
    session['count'] +=1 #one from redirect, one from create user
    return redirect('/')  # Notice that we changed where we redirect to
                              # Now we go to the page that displays the name and email!

@app.route('/reset',methods=['POST'])
def show_user():
    session.clear()
    session['count'] = 0
    # if 'count' in session:
    #     print('name exists!')
    # else:
    #     print("key 'name' does NOT exist")
    #session.clear()
    return redirect('/')

if __name__=="__main__":
    # run our server
    app.run(debug=True)