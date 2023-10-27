fullname = input("Please enter a full name: ")
print(fullname)
print(fullname[0])
print(fullname.split()[0])
print(fullname[-1])
print(fullname.split()[-1])
print(fullname[:3])
print(fullname[-3])

question27 = (fullname.split()[0])
print(question27[-4:])

question28 = (fullname.split()[-1])
print(question28[2],question28[3])

print(fullname[::2])
print(fullname[::-1])
print(fullname.split())

target = "a"
counter = 0
for item in fullname:
    if item == target:
        counter +=1
    #endif
#endfor
print(counter)

names = []
n = 0
while n < 5:
    names2 = input("Please enter a name: ")
    names.append(names2)
    n +=1
#endwhile
for item in names:
    print(item)
#endfor
