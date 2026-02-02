str = "Hey Abhinish you are amazing"
f = open("file.txt",'w')
data = f.write(str)
print(data)
f.close()