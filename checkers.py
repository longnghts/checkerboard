from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkers():
    return render_template('checker.html')

@app.route('/<x>/<y>')
def numRows(x, y):
    rows = int(x)
    columns = int(y)
    return render_template('checker2.html', rows = rows, columns = columns)


if __name__=="__main__":
    app.run(debug=True)      
