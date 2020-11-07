from flask import Flask, render_template
import data as data
from random import sample


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',
                            tours=data.tours,
                            departures=data.departures,
                            samples = sample(range(1,len(data.tours)), 6), # return 6 unique numbers, it will be numers of random hotels from data
                            )


@app.route('/departures/<departure>/')
def departure(departure):
    filtered_tours = {}
    for tour in data.tours:
        if departure in data.tours[tour].values() and departure in data.departures:
            filtered_tours[tour] = data.tours[tour]
    return render_template('departure.html',
                            tours=filtered_tours,
                            departure=departure,
                            departures=data.departures,
                            )


@app.route('/tours/<id>/')
def tours(id):
    return render_template('tour.html',
                            tour=data.tours[int(id)],
                            departures=data.departures,
                            )


@app.route('/data/')
def data_():
    article = 'все туры:'
    return render_template('data.html', article=article, tours=data.tours, )


@app.route('/data/departures/<departure>')
def data_dep(departure):
    article = 'Туры по направлению ' + data.departures[departure] + ':'
    filtered_tours = {}
    for tour in data.tours:
        if departure in data.tours[tour].values():
            filtered_tours[tour] = data.tours[tour]
    return render_template('data.html', article=article, tours=filtered_tours)


@app.route('/data/tours/<id>')
def data_id(id):
    return render_template('data_tour.html', tour=data.tours[int(id)])


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500


@app.errorhandler(404)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error.original_exception), 404


app.run()
