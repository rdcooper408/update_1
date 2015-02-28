
def colony_db_search(db_file, index_file):
    import re
    colony_db = open(db_file, "rU")
    colony_file = open(index_file, "rU")
    aa = colony_db.readlines()
    bb = colony_file.readlines() 
    with open('name_date.txt', 'w') as ND:
        for BBlines in bb:
            BBpattern = r"^(\d,\d,\d,)(\w+)"
            index1 = re.search(BBpattern, BBlines, re.I)
     	    if index1 is not None:
     	    	index = index1.group(2)
     	        for AAlines in aa:
       	            AApattern = r"^(\d,\d,\d,)(\w+),,"
       	            master1 = re.search(AApattern, AAlines, re.I)
       	            master = master1.group(2)
       	            if master == index:
       	                ND.write(AAlines)
       	                ND.write('\n') 
                    else:
                    	break     
            else:
                break
