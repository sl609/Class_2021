def create_database_entry(name, id_no, age):
	new_patient = [name, id_no, age, []]
	return new_patient

def main():

	db = list()
	db.append(create_database_entry("Ann Ables",1,30))
	#x = create_database_entry("Ann Ables",1 , 30)
	db.append(create_database_entry("Sup",2,22))
	print(db)

if __name__ == "__main__":
	main()
