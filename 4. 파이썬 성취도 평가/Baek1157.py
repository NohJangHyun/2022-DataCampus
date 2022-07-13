w = input().upper()
w_set = list(set(w))
cnt = []		

for i in w_set:
    cnt.append(w.count(i))	

if cnt.count(max(cnt)) > 1:	
    print('?')
else : 
    print(w_set[cnt.index(max(cnt))])


# 시간초과 solution
# x = input().upper()
# cnt = []
# if len(x) > 1:
#     for i in x:
#         a = x.count(i)
#         cnt.append(a) 
#     a = max(cnt)
#     if(cnt.count(a) > a):
#         print("?")
#     else:
#         print(x[cnt[a]])
# else:
#     print(x)