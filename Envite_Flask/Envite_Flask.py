from flask import Flask, render_template, redirect
from flask import send_from_directory, request

import entry.py

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def main():
    #execfile("entry.py")
    return render_template('index.html')

@app.route('/getID', methods= ['GET', 'POST'])
def static_form_root():
    ID = request.form['enterID']
    entry.card(ID)



    print("Your ID is " + ID)
    return redirect('/')

if __name__ == '__main__':
    app.run()