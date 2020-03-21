n = int(input())
s = input()
word = 'b'

for i in range(n):
    if (word==s):
        print(i)
        break

    if ((i+1)%3==0):
        word = 'b' + word + 'b'
    
    elif ((i+1)%3==1):
        word = 'a' + word + 'c'
    
    elif ((i+1)%3==2):
        word = 'c' + word + 'a'
    
    if (len(word)>n):
        print(-1)
        break