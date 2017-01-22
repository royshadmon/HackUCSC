from flask import Flask, render_template, redirect
from flask import send_from_directory, request
import os
import tablib

import entry

application = Flask(__name__) #static_folder='static', static_url_path='/static')

#filepath = os.path.join(os.path.dirname(__file__),'attendees.csv')

#open_read = open(filepath, 'r')
#page=''

#while True:
#    read_data = open_read.readline()
#    page += '<p>%s</p>' % read_data
#    if open_read.readline() == '':
#        break



@application.route("/")
def main():
    return render_template('index.html')

@application.route("/getID", methods= ['GET', 'POST'])
def static_form_root():

    ID = request.form['enterID']
    print("Your ID is " + ID)

    entry.cardSwipe(ID)
    entry.main()



    return redirect('/')

if __name__ == '__main__':
    application.run()
