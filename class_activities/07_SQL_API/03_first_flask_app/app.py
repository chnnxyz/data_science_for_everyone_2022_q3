from flask import Flask, render_template, request
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

countries = {
    'usa': {
        'population': 'a lot',
        'language': 'english',
        'position': 1
    },
    'mexico': {
        'population': 'a little less than a lot',
        'language': 'spanish',
        'position': 2
    },
    'rwanda': {
        'population': 'a little',
        'language': 'afrikaans',
        'position': 3       
    }
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return f"hello {name}"

@app.route('/sum')
def sum():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return f'sum is {a + b}'

@app.route('/fizzbuzz')
def fizzbuzz():
    n = int(request.args.get('n', 0))
    if n == 0:
        return "please provide n"
    else:
        fb = [(i%3==0)*"Fizz" + (i%5==0)*"Buzz" or i for i in range(1,n+1)]
        return fb

@app.route('/demographics/<country>')
def demographics(country):
    if country in countries:
        return countries[country]
    else:
        countries_list = list(countries.keys())
        error_msg = {
            'error': 404,
            'message': f'supported countries are {countries_list}'
        }
        return error_msg

@app.route('/classify_iris')
def classify():
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    print('loading iris')
    df = sns.load_dataset('iris')
    X = df.drop('species', axis =1)
    y = df['species']
    print('training model')
    m = RandomForestClassifier()
    m.fit(X,y)
    params = [sepal_length, sepal_width, petal_length, petal_width]
    print('predicting')
    return str(m.predict([params]))
