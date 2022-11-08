import pymysql

class Data:

	def __init__(self):
		self.conn = pymysql.connect(
			host="localhost",
			user="root",
			password="1234",
			db="crm"
			)

		self.cursor = self.conn.cursor()


	
	def InsertItems(self, element):
		#our element contend the name, age and the carreer of the student
		#in position 0, 1, 2
		sql = "insert into cliente(nombre, telefono , empresa) values('{}', '{}', '{}')".format(element[0],element[1],element[2])
		#execute the query
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios


	
	def ReturnOneItem(self, ref):
		#we have ref like name of the element
		sql = "select * from  cliente where nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		#return the element or nil
		return self.cursor.fetchone()


	def Returnempresa(self, ref):
		sql = "select * from cliente where empresa = '{}'".format(ref)
		self.cursor.execute(sql)
		return self.cursor.fetchall() 
	

	def returnAllElements(self):
		sql = "select * from cliente"
		self.cursor.execute(sql)
		return self.cursor.fetchall()


	def Delete(self, ref):
		sql = "delete from cliente where nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		self.conn.commit()


	def UpdateItem(self, element, ref):
		#element contains the values and ref is the name of the item that we want change
		sql = "update cliente set nombre = '{}',telefono = '{}', empresa='{}' where nombre = '{}'".format(element[0],element[1],element[2], ref)
		#execute the query
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios

