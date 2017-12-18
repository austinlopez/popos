import random
f = open("number.txt", "w+")

write = ''
length = 0
while length < 200:
    number = random.randrange(1,100)
    write += str(number)+ "\n"
    length += 1

f.write(write)
f.close()