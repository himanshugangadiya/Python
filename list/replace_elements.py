# Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

list =["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

list[1]="NOSQL"
list[3]="Flutter"
print(list)

for x in list:
    if x=="SQL":
        list[list.index(x)]="NOSQL"
    if x=="Reactnative":
        list[list.index(x)]="Flutter"

print(list)