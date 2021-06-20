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
                                'three' : 'sqlite:///TDS.db'  ,      # Today Stocks Database
                                'four' : 'sqlite:///products.db', # products items
                                'five' : 'sqlite:///products_database.db', #Individual Product saving for a while
                                "blog_post" : "sqlite:///database/blog_post.db"  , #Blog and Post 
                                'react':"sqlite:///database/reacts.db" , #React to Database
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

class products(db.Model):
    __bind_key__ = 'four'
    sno = db.Column(db.Integer , primary_key=True)
    product_size = db.Column(db.String(20))
    product_name = db.Column(db.String(500))


    def __repr__(self) -> str:
        return f'{self.sno}'

class products_database(db.Model):
    __bind_key__ = 'five'
    sno = db.Column(db.Integer , primary_key=True)
    date_created = db.Column(db.String(500))
    product_size = db.Column(db.String(20))
    product_name = db.Column(db.String(500))
    product_quantity = db.Column(db.Integer)
    product_per_price = db.Column(db.Float)


    def __repr__(self) -> str:
        return f'{self.sno}'

#End DataBase Conectivity
#
#
#
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

def product_database_function(size , name):
    df1 = pd.read_sql("SELECT * FROM products" , create_engine("sqlite:///products.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    df2 = pd.read_sql("SELECT * FROM sheet" , create_engine("sqlite:///sheet.db"))
    DataFrame_main_Product = df2.loc[:, ["product_size" , 'product_name']]
    main_server_product = np.array(DataFrame_main_Product)
    k=0
    number = [k for k in range(len(server_product)) if [size] in server_product[k] and [name] in server_product[k]]
    if len(number) == 1:
        j = 0
        list_of_search = [j for j in range(len(main_server_product)) if [size] in main_server_product[j] and [name] in main_server_product[j]]
        if len(list_of_search) != 0:
            Server_of_products = pd.DataFrame(list(df2.values[list_of_search[i]] for i in range(len(list_of_search))) , columns=df2.columns , index=None)
            engine = create_engine("sqlite:///products_database.db")
            Server_of_products.to_sql("products_database" , engine , if_exists='replace')

def litte_search_engine_2(size , name):
    df1 = pd.read_sql("SELECT * FROM products" , create_engine("sqlite:///products.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    k=0
    number = [k for k in range(len(server_product)) if [size] in server_product[k] and [name] in server_product[k]]
    return number

        
            
#End Executable Function in BackEnds
#
#
#
#Calling Pages
@app.route('/' , methods=['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        date_created = date1
        product_size = request.form.get("product_size")
        product_name = request.form['product_name']
        product_quantity = request.form['product_quantity']
        product_per_price = request.form['product_per_price']
        stocks = Sheet(product_size=product_size, date_created=date_created , product_name=product_name.lower() ,product_quantity=product_quantity , product_per_price=product_per_price)
        db.session.add(stocks)
        db.session.commit()
    todayStock()
    stocks = TDS.query.all()
    return render_template('stocks.html' , stocks=stocks) 

@app.route("/all_stocks")
def all_stocks():
    stocks = Sheet.query.all()
    return render_template('all_stocks.html' , stocks=stocks) 
        

@app.route("/show_30days_stocks")
def show_30days_stocks():
    ThirtydaysDataMaker()
    stocks = LTDS.query.all()
    return render_template('show_30days_stocks.html' , stocks=stocks) 

@app.route('/includings_of_products' , methods=['GET', 'POST'])
def includings_of_products():
    if request.method == 'POST':
        product_size = request.form.get('product_size')
        product_name = request.form['product_name']
        number = litte_search_engine_2(product_size , product_name.lower())
        if len(number) == 0:
            stocks = products(product_size = product_size , product_name=product_name.lower())
            db.session.add(stocks)
            db.session.commit()
        
            

    stocks = products.query.all()
    return render_template('includings_of_products.html' , stocks=stocks)

@app.route("/product_wise_stock", methods=["GET" , "POST"])
def product_wise_stock():
    if request.method == 'POST':
        product_size = request.form.get('product_size')
        product_name = request.form["product_name"]
        number = litte_search_engine_2(product_size , product_name.lower())
        if len(number) == 0:
            includings_of_products()
            return redirect("/includings_of_products")
        else:
            product_database_function(product_size , product_name.lower())

    stocks = products_database.query.all()
    return render_template('product_wise_stock.html' , stocks=stocks)
#End Calling Pages
#
#
#Update Place

@app.route('/update/<int:sno>' , methods=['GET' ,"POST"])
def update_main(sno):
    if request.method == 'POST':
        product_size = request.form.get('product_size')
        product_quantity = request.form['product_quantity']
        product_name = request.form['product_name']
        product_per_price = request.form['product_per_price']
        n_Sheet = Sheet.query.filter_by(sno=sno).first()
        n_Sheet.product_size = product_size
        n_Sheet.product_name = product_name.lower()
        n_Sheet.product_quantity = product_quantity
        n_Sheet.product_per_price = product_per_price
        db.session.add(n_Sheet)
        db.session.commit()
        return redirect('/show_daily_stocks')

    stock = Sheet.query.filter_by(sno=sno).first()
    return render_template('update.html' , stock=stock)

@app.route("/update_products/<int:sno>" , methods=["GET" , 'POST'])
def update_products(sno):
    if request.method == "POST":
        product_size = request.form.get("product_size")
        product_name = request.form["product_name"]
        stocks = products.query.filter_by(sno=sno).first()
        stocks.product_size = product_size
        stocks.product_name = product_name.lower()
        db.session.add(stocks)
        db.session.commit()
        return redirect("/includings_of_products")

    stock = products.query.filter_by(sno=sno).first()
    return render_template('update_products.html' , stock=stock)
#End Update Place
#
#
#Delete Place

@app.route('/delete/<int:sno>')
def delete(sno):
    stock = Sheet.query.filter_by(sno=sno).first()
    db.session.delete(stock)
    db.session.commit()
    return redirect("/")


@app.route('/delete_products/<int:sno>')
def delete_products(sno):
    stock1 = products.query.filter_by(sno=sno).first()
    db.session.delete(stock1)
    db.session.commit()
    return redirect("/includings_of_products")


#End Delete Place




#Blog Post   -------   Blog Post



class blog_post(db.Model):
    __bind__key_ = "blog_post"
    sno = db.Column(db.Integer , primary_key=True)
    address = db.Column(db.String(200))
    post = db.Column(db.String(1000) , nullable=False)
    

    def __repr__ (self) -> str:
        return f"{self.sno}"

@app.route("/blog_post" , methods=["GET" , "POST"])
def blog_post_():
    if request.method == "POST":
        address = request.form["address"]
        post = request.form["post"]
        post_blog = blog_post(address=address , post=post)
        db.session.add(post_blog)
        db.session.commit()

    posts = blog_post.query.all()
    return render_template("dist/blog_post.html" , posts=posts)

class reacts(db.Model):
    __bind_key__ = 'react'
    sno = db.Column(db.Integer , primary_key=True)
    sno_ = db.Column(db.Integer)
    react = db.Column(db.String(100))
    

    def __repr__ (self) -> str:
        return f"{self.sno}"

@app.route("/blog_show" , methods=["GET" , "POST"])
def blog_show_():
    posts = blog_post.query.all()
    return render_template("dist/blog_show.html" , posts=posts)

@app.route("/<int:sno>" , methods=["GET" , "POST"])
def blog_show_react(sno):
    if request.method == "POST":
        react = request.form.get("react")
        react_ = reacts(sno_=sno , react=react)
        db.session.add(react_)
        db.session.commit()
        return redirect("/blog_show")



if __name__ == '__main__':
    app.run(port=4000 , debug=True)
    
