#wap to read the text from the given file poem.txt and find out wheather it
# contain the word twinkle ;
'''poem = "Twinkle Twinkle Little star , How I wounder " \
"what you are."
f = open("poem.txt",'w')
data = f.write(poem)
print(data)
f.close()
'''
f = open('poem.txt','r')
data = f.read()
if ('Twinkle' in data):
    print("THe Word twinkles is present")
else:
    print("not present")
f.close()