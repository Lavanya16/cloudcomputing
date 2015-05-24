import bottle
import pymongo
import guestbookDAO
import productDAO

from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template

#This is the default route, our index page. Here we need to read the documents from MongoDB.

@route('/')
def primary_index():
		return bottle.template('index')

@route('/guestbook')
def guestbook_index():
		mynames_list = guestbook.find_names()
		return bottle.template('guest',dict(mynames = mynames_list))
		
#We will post new entries to this route so we can insert them into MongoDB
@route('/newguest',method='POST')
def insert_newguest():
		name = bottle.request.forms.get("name")
		email = bottle.request.forms.get("email")
		guestbook.insert_name(name,email)
		bottle.redirect('/guestbook')

@route('/hello/:name')
def hello_name(name):
    page = request.GET.get('page', '1')
    return '<h1>HELLO %s <br/>(%s)</h1>' % (name, page)		


@route('/css/:filename')
def serve_static(filename):
    return static_file(filename, root='/Users/lavanya/documents/Cloud Computing/Assignment Cloud/webapp/css/')



@route('/images/:filename')
def serve_static(filename):
    return static_file(filename, root='/Users/lavanya/documents/Cloud Computing/Assignment Cloud/webapp/images/')

@route('/js/:filename')
def serve_static(filename):
    return static_file(filename, root='/Users/lavanya/documents/Cloud Computing/Assignment Cloud/webapp/js/')


@get('/upload')
def upload_view():
    return """
        <form action="/upload" method="post" enctype="multipart/form-data">
          <input type="text" name="name" />
          <input type="file" name="data" />
          <input type="submit" name="submit" value="upload now" />
        </form>
        """    
 
@post('/upload')
def do_upload():
    name = request.forms.get('name')
    data = request.files.get('data')
    if name is not None and data is not None:
        raw = data.file.read() # small files =.=
        filename = data.filename
        return "Hello %s! You uploaded %s (%d bytes)." % (name, filename, len(raw))
    return "You missed a field."	

@route('/products')
def products_index():
		products_list = product.find_products()
		return bottle.template('products',dict(products = products_list))

@route('/newitem',method='POST')
def insert_newitem():
		item = bottle.request.forms.get("item")
		code = bottle.request.forms.get("code")
		price = bottle.request.forms.get("price")
		product.insert_products(item,code,price)
		bottle.redirect('/products')

#This is to setup the connection


#First, setup a connection string. My server is running on this computer so localhost is ok
connection_string = "mongodb://localhost"

#Next, let PyMongo know about the MongoDB connection we want to use. PyMongo will manage the connection pool.
connection = pymongo.MongoClient(connection_string)
#Now we want to set a context to the names database we created using the Mongo interactive shell
database = connection.names
#Finally, let out data access object class we built which acts as out data layer know about this
guestbook = guestbookDAO.GuestbookDAO(database)
product = productDAO.ProductDAO(database)

bottle.debug(True)
bottle.run(host='localhost',port=8082)