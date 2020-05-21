# Enter your code here. Read input from STDIN. Print output to STDOUT
phonebook = {}
n = int(input())
for i in range(n):
    x = input().split()
    phonebook[x[0]] = x[1]
while True:
    try:
        name = input().split()
        for na in name:
            if (na in phonebook):
                print(na + "=" + phonebook[na])
            else:
                print('Not found')
    except EOFError:
        break
            
