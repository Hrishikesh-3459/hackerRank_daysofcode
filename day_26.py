# Enter your code here. Read input from STDIN. Print output to STDOUT
return_date = list(map(int, input().rstrip().split()))
due_date = list(map(int, input().rstrip().split()))
if (return_date == due_date):
    print('0')
if (return_date[2] == due_date[2]):
    if (return_date[1] == due_date[1]):
        val = return_date[0] - due_date[0]
        if (val < 0):
            print('0')
        else:
            print(val * 15)
    else:
        val = return_date[1] - due_date[1]
        if (val < 0):
            print('0')
        else:
            print(val * 500)
else:
    if (return_date[2] < due_date[2]):
        print('0')
    else:
        print("10000")
