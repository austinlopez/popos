final = 0
sequence = [1,2]

while sequence[len(sequence)-1] < 4000000:
    #length = len(sequence)
    #print(length)
    #print(sequence[len(sequence)-2])
    #print()
    sequence.append(sequence[len(sequence)-2]+sequence[len(sequence)-1])

if sequence[len(sequence)-1] > 4000000:
    sequence.pop(len(sequence)-1)
for x in sequence:
    if x%2 == 0:
        final += x
print(sequence)
print(final)