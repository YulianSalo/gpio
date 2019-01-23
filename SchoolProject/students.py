from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect
engine = create_engine('sqlite:///college.db')

meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String)
   Column('student_id', String), 
)
meta.create_all(engine)

class Student(object):
	"""docstring for ClassName"""
	def __init__(self, name, lastName, studentId):
		self.name = name
		self.lastName = lastName
		self.studentId = studentId	

	def getName(self):
			return self.name	

	def getLastName(self):
			return self.lastName

	def getStudentId(self):
			return self.studentId

	def setName(name):
			self.name = name	

	def setLastName(lastName):
			self.lastName = lastName

	def setStudentId(studentId):
			self.studentId = studentId

	def __str__(self):
		return 'Name: {}: Surname: {} StudentID: {}'.format(self.name, self.lastName, self.studentId)

def main():

	print("""Welcome! Please choose an action to start:
			1. Input data.
			2. Clear data.
			3. See data. \n""")
	action = int(input("..."))

	conn = engine.connect()

	while action != 1 or action !=2 or action !=3:
		if action == 1:

			inputListLength = int(input("Please enter length of inputList: "))
			inputList =  []
			#s = []

			conn = engine.connect()

			for i in range(inputListLength):
				inputList.append("-")
				#s.append(" ")

			for i in range(inputListLength):
				sName = input("{}. Input  S_name: ".format(i+1))
				sLastName = input("{}. Input S_LASTNAME:".format(i+1))
				sStudentID = input("{}. Input StudentID:".format(i+1))
				inputList[i] = Student(sName, sLastName, sStudentID)
				conn.execute(students.insert(), [
			   {'name': sName, 'lastname' : sLastName, 'student_id' : sStudentID },
			   
			])
				print ("\n")
			
			
			s = students.select()
			result = conn.execute(s)

			for row in result:
		   		print (row)

		elif action == 2:

			students.drop(engine)
			inspector = inspect(engine)

			if inspector == True: 
				print("Your data was cleared successfully.")
			else:
				print("Something went wrong.")

			break

		elif action == 3:

			s = students.select()
			result = conn.execute(s)

			for row in result:

		   		print(row)

			break

		else:

			print("Your input is not correct. Please try again.")
			

if __name__ == '__main__':
	main()
	
