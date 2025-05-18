# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

def Josh(person, k, i):
  if len(person) == 1:
    print(person[0])
    return

  index = ((i+k)%len(person))
  person.pop(i)

  Josh(person,k,i)
