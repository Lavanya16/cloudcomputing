import string

class MemberDAO(object):

#Initialise our DAO class with the database and set the MongoDB collection we want to use

		def __init__(self,database):
				self.db = database
				self.member = database.member

				
#This function will handle the finding of member
		def find_member(self):
				lmem = []
				for each_member in self.member.find():
						lmem.append({'firstname':each_member['firstname'],'lastname':each_member['lastname'],'memberid':each_member['memberid']})
						
				return lmem
				
#This function will handle the insertion of member
		def insert_member(self,firstname,lastname,memberid):
				newmember = {'firstname':firstname,'lastname':lastname,'memberid':memberid}
				self.member.insert(newmember)
				