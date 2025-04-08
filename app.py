from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contacts')
def contact_details():
    return render_template('contact.html')
if __name__=='__main__':
    app.run(debug=True)    #make sure it should be false while project is in delivered to production. 

