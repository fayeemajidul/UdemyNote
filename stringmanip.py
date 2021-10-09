#String Properties and methods:
#immutabiltiy of Strings
name  = "Sam"
#Changing it to Pam with immutability
last_name = "P" + name[1:]
print(name) 
print(last_name)

#Concatination = putting strings together when you do "+" sign to merge
#Can't concatinate numbers and letters
string1 = "Hello world" + " it is very beautiful outside"
print(string1)
x = "Hello World"

#x.split() --> Creates strings and puts them into a list
print(x.split()) #---> Whatever is in parenthesis is removed.

List = ["Hello", "My Name", "is"]
Finish_List  = "Goldman Burg"
Product = Finish_List.split()
Product.append("Goldman")
List.append(Finish_List)
print(List)
#Practicing Splitting