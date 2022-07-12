x = input().lower()
a = x.count(max(x))
print(type(a))
print(a)
print(max(x))
# if(x.count(a)>len(a)):
#     print("?")
# else:
#     print(x[a])


#시간초과
# x = input().lower()
# cnt = []
# if len(x) > 1:
#     for i in x:
#         a = x.count(i)
#         cnt.append(a) 
#     a = max(cnt)
#     if(cnt.count(a) > a):
#         print("?")
#     else:
#         print(x[cnt[a]].upper())
# else:
#     print(x.upper())