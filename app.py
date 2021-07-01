from flask import Flask , render_template , request , redirect , send_from_directory
from flask_sqlalchemy import SQLAlchemy
import time
import os
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from datetime import date , timedelta
import pdfkit




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sheet.db' #main database
app.config["SQLALCHEMY_BINDS"] = {'two' : 'sqlite:///LTDS.db' ,    #Last thirty days Stocks Database
                                'three' : 'sqlite:///TDS.db'  ,      # Today Stocks Database
                                'four' : 'sqlite:///products.db',       # products items
                                'five' : 'sqlite:///products_database.db', #Individual Product saving temporary
                                "total" : "sqlite:///total.db" ,  #Total database 
                                "bill_frame1":"sqlite:///bill_frame1.db" ,# bill frame one
                                   "bill_frame2": "sqlite:///bill_frame2.db", # bill frame two
                                   "bill" : 'sqlite:///bill.db' # bill main file
                                   ,  "blog_post" : "sqlite:///database/blog_post.db"  , #Blog and Post 
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

class total(db.Model):
    __bind_key__ = 'total'
    index = db.Column(db.Integer , primary_key=True)
    date_created = db.Column(db.String(500))
    product_size = db.Column(db.String(20))
    product_name = db.Column(db.String(500))
    product_quantity = db.Column(db.Integer)
    product_per_price = db.Column(db.Float)


    def __repr__(self) -> str:
        return f'{self.index}'

class bill(db.Model):
    __bind_key__ = "bill"
    index = db.Column(db.Integer , primary_key=True)
    shop_number = db.Column(db.String(500), nullable=False)
    customer_name = db.Column(db.String(500), nullable=False)
    phone_number = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)

    
    product_name1 = db.Column(db.String(200) , nullable=True)
    product_size1 = db.Column(db.String(20)  , nullable=True)
    product_peice1 = db.Column(db.String(100)  , nullable=True)
    product_per_price1 = db.Column(db.String(100)  , nullable=True)
    product_price1 = db.Column(db.String(100)  , nullable=True)

    product_name2 = db.Column(db.String(200) , nullable=True)
    product_size2 = db.Column(db.String(20)  , nullable=True)
    product_peice2 = db.Column(db.String(100)  , nullable=True)
    product_per_price2 = db.Column(db.String(100)  , nullable=True)
    product_price2 = db.Column(db.String(100)  , nullable=True)


    product_name3 = db.Column(db.String(200) , nullable=True)
    product_size3 = db.Column(db.String(20)  , nullable=True)
    product_peice3 = db.Column(db.String(100)  , nullable=True)
    product_per_price3 = db.Column(db.String(100)  , nullable=True)
    product_price3 = db.Column(db.String(100)  , nullable=True)

    product_name4 = db.Column(db.String(200) , nullable=True)
    product_size4 = db.Column(db.String(20)  , nullable=True)
    product_peice4 = db.Column(db.String(100)  , nullable=True)
    product_per_price4 = db.Column(db.String(100)  , nullable=True)
    product_price4 = db.Column(db.String(100)  , nullable=True)

    product_name5 = db.Column(db.String(200) , nullable=True)
    product_size5 = db.Column(db.String(20)  , nullable=True)
    product_peice5 = db.Column(db.String(100)  , nullable=True)
    product_per_price5 = db.Column(db.String(100)  , nullable=True)
    product_price5 = db.Column(db.String(100)  , nullable=True)

    product_name6 = db.Column(db.String(200) , nullable=True)
    product_size6 = db.Column(db.String(20)  , nullable=True)
    product_peice6 = db.Column(db.String(100)  , nullable=True)
    product_per_price6 = db.Column(db.String(100)  , nullable=True)
    product_price6 = db.Column(db.String(100)  , nullable=True)

    product_name7 = db.Column(db.String(200) , nullable=True)
    product_size7 = db.Column(db.String(20)  , nullable=True)
    product_peice7 = db.Column(db.String(100)  , nullable=True)
    product_per_price7 = db.Column(db.String(100)  , nullable=True)
    product_price7 = db.Column(db.String(100)  , nullable=True)

    product_name8 = db.Column(db.String(200) , nullable=True)
    product_size8 = db.Column(db.String(20)  , nullable=True)
    product_peice8 = db.Column(db.String(100)  , nullable=True)
    product_per_price8 = db.Column(db.String(100)  , nullable=True)
    product_price8 = db.Column(db.String(100)  , nullable=True)

    product_name9 = db.Column(db.String(200) , nullable=True)
    product_size9 = db.Column(db.String(20)  , nullable=True)
    product_peice9 = db.Column(db.String(100)  , nullable=True)
    product_per_price9 = db.Column(db.String(100)  , nullable=True)
    product_price9 = db.Column(db.String(100)  , nullable=True)

    product_name10 = db.Column(db.String(200) , nullable=True)
    product_size10 = db.Column(db.String(20)  , nullable=True)
    product_peice10 = db.Column(db.String(100)  , nullable=True)
    product_per_price10 = db.Column(db.String(100)  , nullable=True)
    product_price10 = db.Column(db.String(100)  , nullable=True)


    def __repr__(self) -> str:
        return f"{self.index}"

#End DataBase Conectivity
#
#
#
#Executable Function in BackEnds
def ThirtydaysDataMaker():
    df = pd.read_sql('SELECT * FROM sheet;' , create_engine('sqlite:///sheet.db'))
    DataFrame_date = df.loc[:, ["date_created"]]
    server_date = np.array(DataFrame_date).tolist()
    list_of_last_30_days = [[f'{(date.today()-timedelta(days=i)).isoformat()}'] for i in range(7)] 
    list_of_filter_last_30_days = [list_of_last_30_days[l] for l in range(len(list_of_last_30_days)) if list_of_last_30_days[l] in server_date]
    Index_Df = []
    for j in range(len(list_of_filter_last_30_days)):
        Last_30_days = list_of_filter_last_30_days[j]
        Index_DataFrame = [k for k in range(len(server_date)) if np.array(DataFrame_date.isin(Last_30_days).loc[:, ["date_created"]])[k]== True]
        Index_Df.extend(Index_DataFrame)
    Server_of_last_30_days = pd.DataFrame(list(df.values[i] for i in Index_Df) , columns=df.columns)
    engine = create_engine('sqlite:///LTDS.db')
    Server_of_last_30_days.to_sql("LTDS" , engine , if_exists='replace')
    #print(Server_of_last_30_days)
    
def todayStock():
    df = pd.read_sql('SELECT * FROM sheet;' , create_engine('sqlite:///sheet.db'))
    DataFrame_date = df.loc[:, ["date_created"]]
    server_date = np.array(DataFrame_date).tolist()
    today = [(date.today()).isoformat()]
    Index_DataFrame = [k for k in range(len(server_date)) if np.array(DataFrame_date.isin(today).loc[:, ["date_created"]])[k]== True]
    Server_of_today = pd.DataFrame(list(df.values[i] for i in Index_DataFrame) , columns=df.columns)
    engine=create_engine('sqlite:///TDS.db')
    Server_of_today.to_sql('TDS' , engine , if_exists='replace' , index=False)

def product_database_function(size , name):
    df1 = pd.read_sql("SELECT * FROM products" , create_engine("sqlite:///products.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    df2 = pd.read_sql("SELECT * FROM sheet;" , create_engine("sqlite:///sheet.db"))
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
            Server_of_products.to_sql("products_database" , engine , if_exists='replace' , index=False)

def litte_search_engine_2(size , name):
    df1 = pd.read_sql("SELECT * FROM products" , create_engine("sqlite:///products.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    k=0
    number = [k for k in range(len(server_product)) if [size] in server_product[k] and [name] in server_product[k]]
    return number

def update_quantity(size , name , new_quantity , product_per_price):
    df1 = pd.read_sql("SELECT * FROM total;" , create_engine("sqlite:///total.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    k=0
    number = [k for k in range(len(server_product)) if [size] in server_product[k] and [name] in server_product[k]]
    DataFrame_Product_quantity = df1.loc[:, ["product_quantity"]]
    server_product_quantity = np.array(DataFrame_Product_quantity)
    m = len(number)
    server_product_quantity_number = [server_product_quantity[number[i]] for i in range(m)]
    if m == 0:
        df = pd.DataFrame({
        "product_name" : name,
        "product_size" : size ,
        "product_quantity" : new_quantity ,
        "product_per_price" : product_per_price ,
        "date_created" : date1
        } , index=np.array(range(m , m+1)))
        df.to_sql("total" , create_engine("sqlite:///total.db") , if_exists="append" , index=False)
    elif m == 1:
        df1 = df1.drop(index=number)
        add_quantity = new_quantity + server_product_quantity_number[m-1]
        df = pd.DataFrame({
        "product_name" : name,
        "product_size" : size ,
        "product_quantity" : add_quantity , 
        "product_per_price" : product_per_price ,
         "date_created" : date1
        })
        df2 = pd.concat([df , df1] ,axis=0)
        df3 = df2.drop(columns='index')
        df4 = df3.ilos[::-1]
        print(df4)
        df4.to_sql("total" , create_engine("sqlite:///total.db") , if_exists="replace" , index=False)
    
def update_quantity_minus(size , name , new_quantity , product_per_price):
    df1 = pd.read_sql("SELECT * FROM total;" , create_engine("sqlite:///total.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    k=0
    number = [k for k in range(len(server_product)) if [size] in server_product[k] and [name] in server_product[k]]
    DataFrame_Product_quantity = df1.loc[:, ["product_quantity"]]
    server_product_quantity = np.array(DataFrame_Product_quantity)
    m = len(number)
    server_product_quantity_number = [server_product_quantity[number[i]] for i in range(m)]
    if m == 0:
        df = pd.DataFrame({
        "product_name" : name,
        "product_size" : size ,
        "product_quantity" : new_quantity ,
        "product_per_price" : product_per_price ,
        "date_created" : date1
        } , index=np.array(range(m , m+1)))
        df.to_sql("total" , create_engine("sqlite:///total.db") , if_exists="append" , index=False)
    elif m == 1:
        df1 = df1.drop(index=number)
        add_quantity = server_product_quantity_number[m-1] - new_quantity
        df = pd.DataFrame({
        "product_name" : name,
        "product_size" : size ,
        "product_quantity" : add_quantity , 
        "product_per_price" : product_per_price ,
         "date_created" : date1
        })
        df2 = pd.concat([df , df1] ,axis=0)
        df3 = df2.drop(columns='index')
        df3.to_sql("total" , create_engine("sqlite:///total.db") , if_exists="replace" , index=False)
    
def reversed_sheet():
    df = pd.read_sql("sheet" , create_engine("sqlite:///sheet.db"))
    df = df[::-1]
    df.to_sql("sheet", create_engine("sqlite:///sheet.db") , if_exists="replace")
            
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
        update_quantity(size=product_size , name=product_name.lower() , new_quantity=int(product_quantity) , product_per_price=product_per_price)
        
    todayStock()
    stocks = TDS.query.all()
    return render_template('stocks.html' , stocks=stocks) 

@app.route("/all_stocks")
def all_stocks():
    reversed_sheet()
    stocks = Sheet.query.all()
    stocks1 = total.query.all()
    return render_template('all_stocks.html' , stocks=stocks , stocks1=stocks1) 
        
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
        return redirect('/')

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
    update_quantity_minus(size=stock.product_size , name=stock.product_name ,
         new_quantity=stock.product_quantity , product_per_price=stock.product_per_price)
    return redirect("/")


@app.route('/delete_products/<int:sno>')
def delete_products(sno):
    stock1 = products.query.filter_by(sno=sno).first()
    db.session.delete(stock1)
    db.session.commit()
    return redirect("/includings_of_products")

#End Delete Place

####____Bill Main Page____####

@app.route('/base', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        shop_number = request.form["shop_number"]
        customer_name = request.form["customer_name"]
        phone_number = request.form["phone_number"]
        email = request.form['email']

        #print(shop_number , customer_name , phone_number , email)

        product_name1 = request.form["product_name1"]
        product_size1 = request.form.get("product_size1")
        product_peice1 = request.form["product_peice1"]
        product_per_price1 = request.form["product_per_price1"]
        product_price1 = request.form["product_price1"]
        
        product_name2 = request.form["product_name2"]
        product_size2 = request.form.get("product_size2")
        product_peice2 = request.form["product_peice2"]
        product_per_price2 = request.form["product_per_price2"]
        product_price2 = request.form["product_price2"]
        

        product_name3 = request.form["product_name3"]
        product_size3 = request.form.get("product_size3")
        product_peice3 = request.form["product_peice3"]
        product_per_price3 = request.form["product_per_price3"]
        product_price3 = request.form["product_price3"]

        product_name4 = request.form["product_name4"]
        product_size4 = request.form.get("product_size4")
        product_peice4 = request.form["product_peice4"]
        product_per_price4 = request.form["product_per_price4"]
        product_price4 = request.form["product_price4"]
        

        product_name5 = request.form["product_name5"]
        product_size5 = request.form.get("product_size5")
        product_peice5 = request.form["product_peice5"]
        product_per_price5 = request.form["product_per_price5"]
        product_price5 = request.form["product_price5"]
        


        product_name6 = request.form["product_name6"]
        product_size6 = request.form.get("product_size6")
        product_peice6 = request.form["product_peice6"]
        product_per_price6 = request.form["product_per_price6"]
        product_price6 = request.form["product_price6"]
        

        product_name7 = request.form["product_name7"]
        product_size7 = request.form.get("product_size7")
        product_peice7 = request.form["product_peice7"]
        product_per_price7 = request.form["product_per_price7"]
        product_price7 = request.form["product_price7"]
        

        product_name8 = request.form["product_name8"]
        product_size8 = request.form.get("product_size8")
        product_peice8 = request.form["product_peice8"]
        product_per_price8 = request.form["product_per_price8"]
        product_price8 = request.form["product_price8"]
        

        product_name9 = request.form["product_name9"]
        product_size9 = request.form.get("product_size9")
        product_peice9 = request.form["product_peice9"]
        product_per_price9 = request.form["product_per_price9"]
        product_price9 = request.form["product_price9"]


        product_name10 = request.form["product_name10"]
        product_size10 = request.form.get("product_size10")
        product_peice10 = request.form["product_peice10"]
        product_per_price10 = request.form["product_per_price10"]
        product_price10 = request.form["product_price10"]
        
        
        

        save1 = bill(shop_number=shop_number,
        customer_name=customer_name , 
        phone_number=phone_number ,
        email=email
        
        
        ,product_name1=product_name1 ,
        product_size1=product_size1,
        product_peice1=product_peice1,
        product_per_price1=product_per_price1, 
        product_price1=product_price1
        
        
        
        ,product_name2=product_name2 ,
        product_size2=product_size2,
        product_peice2=product_peice2,
        product_per_price2=product_per_price2, 
        product_price2=product_price2
        
        
        ,product_name3=product_name3 ,
        product_size3=product_size3,
        product_peice3=product_peice3,
        product_per_price3=product_per_price3, 
        product_price3=product_price3
        
        
        ,product_name4=product_name4 ,
        product_size4=product_size4,
        product_peice4=product_peice4,
        product_per_price4=product_per_price4, 
        product_price4=product_price4
        
        
        ,product_name5=product_name5 ,
        product_size5=product_size5,
        product_peice5=product_peice5,
        product_per_price5=product_per_price5, 
        product_price5=product_price5
        
        
        ,product_name6=product_name6 ,
        product_size6=product_size6,
        product_peice6=product_peice6,
        product_per_price6=product_per_price6, 
        product_price6=product_price6
        
        
        ,product_name7=product_name7 ,
        product_size7=product_size7,
        product_peice7=product_peice7,
        product_per_price7=product_per_price7, 
        product_price7=product_price7
        
        
        ,product_name8=product_name8 ,
        product_size8=product_size8,
        product_peice8=product_peice8,
        product_per_price8=product_per_price8, 
        product_price8=product_price8
        
        
        ,product_name9=product_name9 ,
        product_size9=product_size9,
        product_peice9=product_peice9,
        product_per_price9=product_per_price9, 
        product_price9=product_price9
        
        
        ,product_name10=product_name10 ,
        product_size10=product_size10,
        product_peice10=product_peice10,
        product_per_price10=product_per_price10, 
        product_price10=product_price10)


        db.session.add(save1)
        db.session.commit()
        

    
    return render_template("dist/base.html")

####____End Bill Main Page____####


#### ----Bill Sendings---- ####

def bill_frame():
    df = pd.read_sql("SELECT * FROM bill" , create_engine("sqlite:///bill.db"))
    #print(len(df.sno))
    df2 = df.values[len(df.index) - 1]
    list1 = [ df2[i] for i in range(5 , 50 , 5)]
    list2 = [  df2[i]for i in range(6 , 51 , 5)]
    list3 = [ df2[i] for i in range(7 , 52 , 5)]
    list4 = [df2[i] for i in range(8 , 53 , 5)]
    list5 = [ df2[i] for i in range(9 , 54 , 5)]

    bill_frame1 = pd.DataFrame({
        "customer_shop_number" : df2[1],
        "customer_name" : df2[2] ,
        "customer_phone_number" : df2[3] ,
        "customer_mail" : df2[4] , 
    } , index=[df2[0]])
    bill_frame1.to_sql("bill_frame1", create_engine("sqlite:///bill_frame1.db") , if_exists="replace")

    bill_frame2 = pd.DataFrame({"product_name" : list1 ,
        "product_size" : list2 , 
        "product_peice" : list3 ,
        "product_per_price" : list4 ,
        "product_price" : list5 })
    bill_frame2.to_sql("bill_frame2", create_engine("sqlite:///bill_frame2.db") , if_exists="replace")


def send_bill():
    url = "http://stocks-mijan.herokuapp.com/bill_" #"http://127.0.0.1:4000/bill_"
    config = pdfkit.configuration(wkhtmltopdf=b"wkhtmltox\\bin\\wkhtmltopdf.exe")
    pdfkit.from_url(url , "templates/dist/bill_.pdf" , configuration=config , options={
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-left': '0',
            'margin-bottom': '0',
            'zoom': '1.2',
            'encoding': "UTF-8"
        })
    """df3 = df.values[3]
    mailer = MailSender()
    mailer.send(to=["mejan601@gmail.com"], subject=f"Bill Number{3}" , body="Bill From User")"""
    """yagmail.SMTP("mejan601@gmail.com").send("mejan601@gmail.com" , "Mail" , contents)
    print("Sent Successfull.")
    """
    
### ----DataBase Update---- ###
def update_quantity(size , name , new_quantity , product_per_price):
    df1 = pd.read_sql("SELECT * FROM total;" , create_engine("sqlite:///total.db"))
    DataFrame_Product = df1.loc[:, ["product_size" , 'product_name']]
    server_product = np.array(DataFrame_Product)
    k=0
    number = [k for k in range(len(server_product)) if [size] in server_product[k] and [name] in server_product[k]]
    DataFrame_Product_quantity = df1.loc[:, ["product_quantity"]]
    server_product_quantity = np.array(DataFrame_Product_quantity)
    m = len(number)
    server_product_quantity_number = [server_product_quantity[number[i]] for i in range(m)]
    if m == 0:
        df = pd.DataFrame({
        "product_name" : name,
        "product_size" : size ,
        "product_quantity" : new_quantity ,
        "product_per_price" : product_per_price
        } , index=np.array(range(m , m+1)))
        df.to_sql("total" , create_engine("sqlite:///total.db") , if_exists="append")
    elif m == 1:
        df1 = df1.drop(index=number)
        add_quantity = new_quantity + server_product_quantity_number[m-1]
        df = pd.DataFrame({
        "product_name" : name,
        "product_size" : size ,
        "product_quantity" : add_quantity , 
        "product_per_price" : product_per_price
        })
        df2 = pd.concat([df , df1] ,axis=0)
        df4 = df2.drop(columns='index')
        df4.to_sql("total" , create_engine("sqlite:///total.db") , if_exists="replace")
    

def update_all():
    df1 = pd.read_sql("SELECT * FROM total;" , create_engine("sqlite:///total.db"))
    df = pd.read_sql("SELECT * FROM bill_frame2;" , create_engine("sqlite:///bill_frame2.db"))
    #print(df.values[0])
    for i  in range(0 ,len(df.index)):
        prod = df.values[i]
        if prod[1] != '' and np.array(df1["product_name"])[i] in np.array(df["product_name"]):
            update_quantity(size=prod[2] , name=prod[1] , new_quantity=int(prod[3]) , product_per_price=prod[4])


###Page Connection###
class bill_frame1(db.Model):
    __bind_key__ = "bill_frame1"
    index = db.Column(db.Integer, primary_key=True)
    customer_shop_number = db.Column(db.String(300))
    customer_name = db.Column(db.String(500))
    customer_phone_number = db.Column(db.String(500))
    customer_mail = db.Column(db.String(500))


class bill_frame2(db.Model):
    __bind_key__ = "bill_frame2"
    index = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(500))
    product_size = db.Column(db.String(500))
    product_peice = db.Column(db.String(500))
    product_per_price = db.Column(db.String(500))
    product_price = db.Column(db.String(500))

@app.route("/bill_" , methods=["GET" , "POST"])
def bill_frame_page():
    if request.method == "POST":
        send_bill()
        workingdir = os.path.abspath(os.getcwd())
        filepath = workingdir + "/templates/dist/"
        return send_from_directory(filepath , 'bill_.pdf')
    bill_frame()
    update_all()
    
    bill_frame1_ = bill_frame1.query.all()
    bill_frame2_ = bill_frame2.query.all()
    return render_template("dist/bill_.html" ,bill_frame1_=bill_frame1_ , bill_frame2_=bill_frame2_)




#Blog Post   -------   Blog Post



class blog_post(db.Model):
    __bind_key__ = "blog_post"
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
    
