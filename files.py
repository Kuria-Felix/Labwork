#open files
f= open('C:\\Users\\user\\Desktop\\Lab work\\demofile.txt')
print('File content before appending')
#print(f.read())
# print(f.read(5))

i=1
for x in f:
   print('Line' +str(i)+""+x)