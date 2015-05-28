import string

class CategoryDAO(object):

#Initialise our DAO class with the database and set the MongoDB collection we want to use

		def __init__(self,database):
				self.db = database
				self.category = database.category

				
#This function will handle the finding of Category
		def find_category(self):
				l = []
				for each_category in self.category.find():
						l.append({'categorycode':each_category['categorycode'],'description':each_category['description']})
						
				return l

				
#This function will handle the insertion of category and display in the screen
		def insert_category(self,newcategorycode,newdescription):
				newcategoryitem = {'categorycode':newcategorycode,'description':newdescription}
				self.category.insert(newcategoryitem)
				
				
