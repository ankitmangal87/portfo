from logging import error
import csv

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)

#Decorators, any time browser hits the address with '/' it will call the hello_world function.
#render_template is used to call .html files, you should put all the .html files in templates folder
# all the .css and .js files should be placed in 'static' folder
# {{...}} - double curly braces is treated as an expression
# Flask uses templating concept under the hood.
#Variable Rules </variablname>

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as databasecsv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(databasecsv, delimiter=",", quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

def write_to_file(data):
    with open('data.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/Thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'