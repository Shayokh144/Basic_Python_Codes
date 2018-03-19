

'''
------------------------------Optional argument

'''
def name(firstName,middleName,lastName):
	print(firstName+" "+middleName+" "+lastName)

name('Lionel','Andres', 'Messi')# all  these arguments ar mandetory



def name_with_optional_parameter(firstName,lastName,middleName=''): 
	# here middleName is optional
	# optional parameters must be declared last
	if len(middleName)>0:
		print(firstName+" "+middleName+" "+lastName)
	else:
		print(firstName+' '+lastName)


name_with_optional_parameter('Cristiano', 'Ronaldo')



'''
------------------------------variable number of argument

'''

def name_with_variable_num_of_parametrs(palyerName, *teamName):
	print(palyerName+" playes for:")
	for team in teamName:
		print(team)

name_with_variable_num_of_parametrs('LM10', 'Argentina', 'Barcelona')
name_with_variable_num_of_parametrs('CR7','Portugal','ManU','Real Madrid')

'''
---------------------Arbitary keyword argument...
'''

def name_with_variable_num_of_parametrs(palyerName, **teamName):
	print(palyerName+" playes for:", teamName)
	

name_with_variable_num_of_parametrs('LM10', home = 'Argentina', club =  'Barcelona')
name_with_variable_num_of_parametrs('CR7',club1= 'Portugal',club2 ='ManU',club3 = 'Real Madrid')
