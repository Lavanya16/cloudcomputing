import string

class ProductDAO(object):

#Initialise our DAO class with the database and set the MongoDB collection we want to use

		def __init__(self,database):
				self.db = database
				self.products = database.products

				
#This function will handle the finding of products
		def find_products(self):
				l = []
				for each_product in self.products.find():
						l.append({'item':each_product['item'],'code':each_product['code'],'price':each_product['price'],'aquantity':each_product['aquantity'],'threshold':each_product['threshold'],'rquantity':each_product['rquantity']})
						
				return l

				
#This function will handle the insertion of products and display in the screen
		def insert_products(self,newitem,newcode,newprice,newaquantity,newrquantity,newthreshold):
				newitem = {'item':newitem,'code':newcode,'price':newprice,'aquantity':newaquantity,'rquantity':newrquantity,'threshold':newthreshold}
				self.products.insert(newitem)
				
				
