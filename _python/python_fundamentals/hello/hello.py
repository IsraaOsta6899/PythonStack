# 1. TASK: print 
print( "Hello World" )
# 2. print  with the name in a variable
name = "Noelle"
print( "Hello Noelle!", name)	# with a comma
print( "Hello Noelle!", name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name1 = 42
print("Hello 42!" ,name1)	# with a comma
print( "Hello 42!" +name1 )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2)) # with .format()
