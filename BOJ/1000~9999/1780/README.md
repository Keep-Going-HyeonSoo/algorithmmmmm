📅 Date: 2021-01-30 (토)

# 1780. 종이의 개수
출처: https://www.acmicpc.net/problem/1780

## 📝 Problem

### 문제
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.  

2. (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.  

이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

### 입력
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

### 출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

## Input/Output example
### Input

```
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
```

### Output
```
10
12
11
```

# ✅ Submit
## 👌 Solved Code 1

### 💡 Idea
[2630. 색종이 만들기]((/BOJ/1000~9999/2630))와 숫자만 다를뿐 똑같은 문제여서 쉬웠다.
paper 의 첫 번째 숫자를 기준 number 로 삼고, paper 의 나머지 값을 비교해서 다른 값이 있으면 종이를 자르고, 모두 같으면 해당 종이가 -1,0,1 인지 비교해서 count 시켜주면 된다. 


### 💻 Code
(Important part only)

``` python
import sys

N = int(sys.stdin.readline())

# paper = [ [0] *N ] * N 

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
countA, countB, conutC = 0, 0, 0    # 순서대로 -1, 0, 1 종이의 갯수

def check(y, x, sideLen):
    global countA, countB, conutC

    number = paper[y][x]
    divide = sideLen // 3

    for i in range(y, y+sideLen):
        for j in range(x, x+sideLen):
            if( paper[i][j] != number ):
                check(y, x, divide)
                check(y, x+divide, divide)
                check(y, x+divide*2, divide)
                check(y+divide, x, divide)
                check(y+divide, x+divide, divide)
                check(y+divide, x+divide*2, divide)
                check(y+divide*2, x, divide)
                check(y+divide*2, x+divide, divide)
                check(y+divide*2, x+divide*2, divide)
                return
    
    if( number == -1 ):
        countA += 1
    elif( number == 0):
        countB += 1
    else:
        conutC += 1

check(0, 0, N)

print(countA)
print(countB)
print(conutC)

```

### 💬 Commentary
입력 받을 때 리스트 컴프리헨션과 map 함수 사용법 헷갈렸음

