file=open('codingal.txt')
print(file.read())
file.close()
#write a content
file=open('codingal.txt','w')
(file.write("my name is arish"))
file.close()
#append a content
file=open('codingal.txt','a')
(file.write("\n i like to play cricket"))
file.close()