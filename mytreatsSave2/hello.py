from flask import Flask,render_template, request ,redirect, url_for,flash
from flask_mysqldb import MySQL

from flask_cors import CORS

from flask import jsonify

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/unema/imageflask'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'baim'
app.config['MYSQL_HOST'] = 'exadev.mytreats.asia'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'devserver'
app.config['MYSQL_DB'] = 'mytreats'

CORS(app)

mysql = MySQL(app)



@app.route('/promotion_save')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM promotion_save''')
    rv = cur.fetchall()
 #  return str(rv)
    return jsonify(rv)

@app.route('/approve/<string:iddata>', methods=["GET"])
def approve(iddata):
    cur = mysql.connection.cursor()
    # cur.execute("UPDATE promotion_save (partner_id,title,price,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title,harga,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at))
    #"UPDATE promotion save SET title=baim,image=dsadsa,price=333 where id = 1 "
    cur.execute("UPDATE promotion_save SET status = 1 where id ="+iddata)
    mysql.connection.commit()
    return "sukses"

@app.route('/decline/<string:iddata>', methods=["GET"])
def decline(iddata):
    cur = mysql.connection.cursor()
    # cur.execute("UPDATE promotion_save (partner_id,title,price,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title,harga,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at))
    #"UPDATE promotion save SET title=baim,image=dsadsa,price=333 where id = 1 "
    cur.execute("UPDATE promotion_save SET status = 2  where id ="+iddata)
    mysql.connection.commit()
    return "sukses"


@app.route('/create', methods=["POST"])
def simpan():
    title = request.form['title']
    harga = request.form['price']
    discount_price = request.form['discount_price']
    image = request.form['image']
    qty = request.form['qty']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    qr_code = request.form['qr_code']
    status = request.form['status']
    description = request.form['description']
    created_at = request.form['created_at']
    updated_at = request.form['updated_at']
    
#   return price
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO promotion_save (partner_id,title,price,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title,harga,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at))
    mysql.connection.commit()
    return "sukses"

@app.route('/update', methods=["POST"])
def update():
    
    title = request.form['title']
    harga = request.form['price']
    discount_price = request.form['discount_price']
    image = request.form['image']
    qty = request.form['qty']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    qr_code = request.form['qr_code']
    status = request.form['status']
    description = request.form['description']
    created_at = request.form['created_at']
    updated_at = request.form['updated_at']

    cur = mysql.connection.cursor()
    # cur.execute("UPDATE promotion_save (partner_id,title,price,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title,harga,discount_price,image,qty,start_date,end_date,qr_code,status,description,created_at,updated_at))
    #"UPDATE promotion save SET title=baim,image=dsadsa,price=333 where id = 1 "
    cur.execute("UPDATE promotion_save SET title=title,image=image,price=500 where id =1")
    mysql.connection.commit()
    return "sukses"

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM promotion_save WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return "sukses"

'''
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
'''
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
'''
'''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
'''
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']

      f.save(secure_filename(f.filename))
      return render_template('end.html')
'''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_gambar', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # This will be executed on POST request.
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # flash("File uploaded: Thanks!", "success")
            return "sukses"


if __name__ == '__main__':
    app.run(debug=True)