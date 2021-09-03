'''
음료수 얼려 먹기
N , M 크기의 얼음 틀이 있다. 
구멍 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표기
구멍 뚫려 있는 부분끼리 상하좌우 붙어 잇는 경우 서로 연결된 것으로 간주.

얼음 틀 모양 주어지면 생성되는 아이스크림의 개수를 구하는 프로그램

'''
# N, M을 공백으로 구분하여 입력 받기 
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보를 입력 받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정한 노드 방문한 뒤에 연결된 모든 노드들도 방문한다. 
def dfs(x,y):
    #주어진 범위를 벗어나는 경우 즉시 종료한다.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        #해당 노드를 방문 처리한다.
        graph[x][y]=1
        #상하좌우 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 모든 노드에 대해여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j)==True:
            result+=1

print(result)
