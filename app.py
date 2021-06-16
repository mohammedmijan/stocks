from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import numpy as np
import time

from werkzeug.utils import html


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sheet.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
date1 = f"{time.strftime('%d')}/{time.strftime('%m')}/{time.strftime('%Y')}"

class Sheet(db.Model):
    sno = db.Column(db.Integer , primary_key=True)
    date_created = db.Column(db.String(500) , nullable=False)
    product_name = db.Column(db.String(500) , nullable=False)
    product_quantity = db.Column(db.Integer , primary_key=False )
    product_per_price = db.Column(db.Float , primary_key=False)


    def __repr__(self) -> str:
        return f'{self.sno}'


@app.route('/' , methods=['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        date_created = date1
        product_name = request.form['product_name']
        product_quantity = request.form['product_quantity']
        product_per_price = request.form['product_per_price']
        

        stocks = Sheet(date_created=date_created , product_name=product_name ,product_quantity=product_quantity , product_per_price=product_per_price)
        db.session.add(stocks)
        db.session.commit()
        return redirect('/')


    stocks = Sheet.query.all()
    return render_template('stocks.html' , stocks=stocks) 

@app.route('/update/<int:sno>' , methods=['GET' ,"POST"])
def update(sno):
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_quantity = request.form['product_quantity']
        product_per_price = request.form['product_per_price']
        n_Sheet = Sheet.query.filter_by(sno=sno).first()
        n_Sheet.product_name = product_name
        n_Sheet.product_quantity = product_quantity
        n_Sheet.product_per_price = product_per_price
        db.session.add(n_Sheet)
        db.session.commit()
        return redirect('/')

    stock = Sheet.query.filter_by(sno=sno).first()
    return render_template('update.html' , stock=stock)

@app.route("/plot" , methods=["GET" , "POST"])
def plot():
    if request.method == "POST":
        X = request.form.get("X")
        Y = request.form.get("Y")
        df = pd.read_sql('SELECT * FROM sheet;' , create_engine("sqlite:///sheet.db"))
        plt.figure(figsize=(10 ,10))
        plt.scatter(df[f"{X}"] , df[f"{Y}"] , c="red" , label="Your Graph")
        plt.xlabel(f"{X}")
        plt.ylabel(f"{Y}")
        plt.plot(df[f"{X}"] , df[f"{Y}"] , c="green" , label="Your Graph in Plot")
        plt.xlabel(f"{X}")
        plt.ylabel(f"{Y}")
        ticks = np.array(range(1 ,len(df[f"{X}"].unique())+1))
        labels = np.array(df[f"{X}"].unique())
        plt.xticks(ticks,labels=labels )
        plt.legend()
        plt.tight_layout()
        plt.savefig("static\sheet.png")
    
    return render_template('plot.html')
        

    

    



if __name__ == '__main__':
    app.run(port=4000 , debug=True)
    
