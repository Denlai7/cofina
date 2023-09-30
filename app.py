from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from coffee import create_table, insert_data, get_all_coffee, remove_coffee

app = Flask(__name__, static_folder='static')


# Initialize the database table
create_table()

@app.route('/')
def index():
    title = "Cofina"
    content = "This is a coffee menu website."
    return render_template('index.html', title=title, content=content)

@app.route('/add_coffee', methods=['POST'])
def add_coffee():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        
        insert_data(name, description, price)
        
        return redirect(url_for('index'))

@app.route('/coffee_list')
def coffee_list():
    return render_template('coffees.html', coffees=get_all_coffee())

@app.route('/delete_coffee', methods=['POST'])
def delete_coffee():
    coffee_id = request.form['coffee_id']
    remove_coffee(coffee_id)
    return redirect(url_for('coffee_list'))


if __name__ == '__main__':
    app.run(debug=True)
