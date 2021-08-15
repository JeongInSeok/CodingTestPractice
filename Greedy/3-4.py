# 숫자 카드 게임
# 여러개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.
# N은 행 y M은 열 x 

N, M = map(int, input().split())
result = 0

for y in range(N):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    
    result = max(result,min_value)

print(result)

