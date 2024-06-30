mylist = ['apple','mango','orange']
print(type(mylist))

newlist = [4,6,9,8,False]
print(type(newlist))

mylist_numbers =['cat','dog',True,7]
print(type(mylist_numbers))

# LIST CONSTRUCTOR

worklist = list (('mike','juliet','jovia','Angel'))
print(worklist)

# TUPLE
thistuple = ('tissue','paper','soap','apple')
# print(thistuple)

new_tuple = list(thistuple)
new_tuple.remove('tissue')

newnew_tuple = tuple(new_tuple)
print(new_tuple)

listnames = ('chinasa','Judith','mike','myra')
# convert the tuple into list
newnames = list(listnames)
newnames.remove('chinasa')

newname_list = tuple(newnames)
print(newname_list)

