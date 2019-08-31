w = int(input())
h = int(input())

for i in range(h):
    if not i or i == h-1:
        print('#'*w, end ='')
        print()
    else:
         print('#' + ' '*(w-2) + '#')