def print_round(list1, list2):
    for i in range(len(list1)):
        print(" ",list1[i], list2[i])
    print()

participants = []

print("Type participant names follow by the 'Enter' key. Finish the list with ctrl + D")

while True:
    try:
        s=input()
        participants.append(s)
    except EOFError:
        break

if len(participants) % 2 == 1:
    participants.append("Skip")
mid = int(len(participants)/2)  

first_list =  list(participants[:-mid])
second_list =  list(participants[mid:])

for i in range(1, len(participants)):
    print("Round",i)
    print_round(first_list, second_list)
    aux = first_list.pop()
    second_list.append(aux)
    aux = second_list.pop(0)
    first_list.insert(1,aux)