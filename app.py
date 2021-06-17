from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
import time
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from datetime import date , timedelta




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sheet.db'
app.config["SQLALCHEMY_BINDS"] = {'two' : 'sqlite:///LTDS.db' ,    #Last thirty days Stocks Database
                                'three' : 'sqlite:///TDS.db'        # Today Stocks Database
                                }     
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
date1 = f"{time.strftime('%Y')}-{time.strftime('%m')}-{time.strftime('%d')}"

#DataBase Conectivity
class Sheet(db.Model):
    sno = db.Column(db.Integer , primary_key=True)
    date_created = db.Column(db.String(500))
    product_size = db.Column(db.String(20))
    product_name = db.Column(db.String(500))
    product_quantity = db.Column(db.Integer)
    product_per_price = db.Column(db.Float)


    def __repr__(self) -> str:
        return f'{self.sno}'

class LTDS(db.Model):
    __bind_key__ = 'two'
    sno = db.Column(db.Integer , primary_key=True)
    date_created = db.Column(db.String(500))
    product_size = db.Column(db.String(20))
    product_name = db.Column(db.String(500))
    product_quantity = db.Column(db.Integer)
    product_per_price = db.Column(db.Float)


    def __repr__(self) -> str:
        return f'{self.sno}'

class TDS(db.Model):
    __bind_key__ = 'three'
    sno = db.Column(db.Integer , primary_key=True)
    date_created = db.Column(db.String(500))
    product_size = db.Column(db.String(20))
    product_name = db.Column(db.String(500))
    product_quantity = db.Column(db.Integer)
    product_per_price = db.Column(db.Float)


    def __repr__(self) -> str:
        return f'{self.sno}'





#Executable Function in BackEnds
def ThirtydaysDataMaker():
    df = pd.read_sql('SELECT * FROM sheet;' , create_engine('sqlite:///sheet.db'))
    DataFrame_date = df.loc[:, ["date_created"]]
    server_date = np.array(DataFrame_date).tolist()
    list_of_last_30_days = [[f'{(date.today()-timedelta(days=i)).isoformat()}'] for i in range(30)] 
    list_of_filter_last_30_days = [list_of_last_30_days[l] for l in range(len(list_of_last_30_days)) if list_of_last_30_days[l] in server_date]
    Index_Df = []
    for j in range(len(list_of_filter_last_30_days)):
        Last_30_days = list_of_filter_last_30_days[j]
        Index_DataFrame = [k for k in range(len(server_date)) if np.array(DataFrame_date.isin(Last_30_days).loc[:, ["date_created"]])[k]== True]
        Index_Df.extend(Index_DataFrame)
    Server_of_last_30_days = pd.DataFrame(list(df.values[i] for i in Index_Df) , columns=df.columns)
    engine = create_engine('sqlite:///LTDS.db')
    Server_of_last_30_days.to_sql("LTDS" , engine , if_exists='replace')
    
def todayStock():
    df = pd.read_sql('SELECT * FROM sheet;' , create_engine('sqlite:///sheet.db'))
    DataFrame_date = df.loc[:, ["date_created"]]
    server_date = np.array(DataFrame_date).tolist()
    today = [(date.today()).isoformat()]
    Index_DataFrame = [k for k in range(len(server_date)) if np.array(DataFrame_date.isin(today).loc[:, ["date_created"]])[k]== True]
    Server_of_today = pd.DataFrame(list(df.values[i] for i in Index_DataFrame) , columns=df.columns)
    engine=create_engine('sqlite:///TDS.db')
    Server_of_today.to_sql('TDS' , engine , if_exists='replace')

#Calling Pages
@app.route('/' , methods=['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        date_created = date1
        product_size = request.form.get("product_size")
        product_name = request.form['product_name']
        product_quantity = request.form['product_quantity']
        product_per_price = request.form['product_per_price']
        stocks = Sheet(product_size=product_size, date_created=date_created , product_name=product_name ,product_quantity=product_quantity , product_per_price=product_per_price)
        db.session.add(stocks)
        db.session.commit()
    return render_template("stocks.html")
        

@app.route("/show_daily_stocks")
def show_daily_stocks():
    todayStock()
    stocks = TDS.query.all()
    return render_template('show_daily_stocks.html' , stocks=stocks) 

@app.route("/show_30days_stocks")
def show_30days_stocks():
    ThirtydaysDataMaker()
    stocks = LTDS.query.all()
    return render_template('show_30days_stocks.html' , stocks=stocks) 


@app.route('/update/<int:sno>' , methods=['GET' ,"POST"])
def update(sno):
    if request.method == 'POST':
        product_size = request.form.get('product_size')
        product_quantity = request.form['product_quantity']
        product_name = request.form['product_name']
        product_per_price = request.form['product_per_price']
        n_Sheet = Sheet.query.filter_by(sno=sno).first()
        n_Sheet.product_size = product_size
        n_Sheet.product_name = product_name
        n_Sheet.product_quantity = product_quantity
        n_Sheet.product_per_price = product_per_price
        db.session.add(n_Sheet)
        db.session.commit()
        return redirect('/show_daily_stocks')

    stock = Sheet.query.filter_by(sno=sno).first()
    return render_template('update.html' , stock=stock)

@app.route('/delete/<int:sno>')
def delete(sno):
    stock = Sheet.query.filter_by(sno=sno).first()
    db.session.delete(stock)
    db.session.commit()
    return redirect("/show_daily_stocks")


if __name__ == '__main__':
    app.run(port=4000 , debug=True)
    
