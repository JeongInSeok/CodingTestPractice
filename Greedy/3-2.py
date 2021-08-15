
# N은 data 에 들어갈 숫자 갯수, M은 더하는 횟수, K는 같은 숫자 연속되는거 제한

N, M, K = map(int,input().split())

data = list(map(int,input().split()))

result = [0]*M
# 오름차순 정렬을 시켜주자 
for j in range(len(data)):
    k = len(data)-j
    for i in range(1,k):
        if data[i-1]>= data[i]:
            data[i-1], data[i] = data[i], data[i-1]
print(data)
cnt = 0 
while cnt != M:
    for i in range(K): # K가 3이면 0 1 2 
        result[cnt]=data[-1]
        cnt+=1

    print(result[cnt])
    print('cnt = {}'.format(cnt))
    result[cnt]=data[-2]
    cnt +=1
# result 가 잘 들어갔는지 확인하려고 
print(result)
ans = 0 
for w in result:
    ans += w

print(ans)
print()
print("다른 풀이 방법")

'''
N,M,K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수
result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result+= first
        M-=1
    for M == 0:
        break
    result+=second
    M-=1
print(result)
'''