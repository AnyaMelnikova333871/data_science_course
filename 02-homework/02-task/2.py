lst = list(map(int, input().split()))

if lst[0] == lst[2] or lst[1] == lst[3]:
    print("YES")
else:
    print("NO")