#the random- access memory is volatile and cell its contents are lost once a program
#terminates in order to persists the data forever, we use files.

'''Types of files.
there are 2 types:
1= text files(.txt, .c)
2 = binary files(.jpg, .dat)'''

#create and write new File
str = "abhinish is python developer"
f = open("first.txt", "w")
f.write(str)
f.close()


