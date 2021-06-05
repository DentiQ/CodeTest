"""
https://www.acmicpc.net/problem/15828
Router
문제
인터넷을 사용하기 위해서는 컴퓨터에 인터넷 회선을 연결하거나 Wi-Fi를 연결해야 한다.
이렇게 연결된 네트워크를 통해 컴퓨터에는 통신이 가능하다. 마음에 드는 노래나 동영상이 있는 곳에 파일을 전송해달라는 요청을 보내고 파일을 받는 식으로 말이다.

우리가 보낸 요청은 어떻게 목적지까지 도달하는 것일까? 컴퓨터에서는 패킷이라고 하는 형태로 정보를 주고 받는다.
네트워크의 유저들은 1:1로 연결되어 있지 않으므로, 일반적으로 패킷은 라우터라는 장비를 여러 번 거친다.
그러면 라우터에서는 패킷을 다른 라우터로 보내거나, 만약 목적지와 직접적으로 연결되어 있다면 그곳으로 보낼 수도 있다. 즉, 택배 회사의 물류 센터와 비슷한 역할을 한다고 보면 된다.

그림1. 네트워크에 존재하는 라우터들의 구성 예시
라우터 내부를 들여다보면 처리해야 할 패킷을 임시적으로 보관하기 위한 버퍼가 존재한다.
이 버퍼에는 라우터에 입력으로 들어온 패킷들이 순서대로 위치하고, 라우터에서는 먼저 온 패킷부터 하나씩 처리한 후 버퍼에서 제거한다.
만약 라우터가 패킷을 처리하는 속도보다 패킷이 들어오는 속도가 더 빠를경우 버퍼가 꽉 차거나 넘쳐버릴 것이다. 그렇게 되면 버퍼에 공간이 생길 때까지 입력받는 패킷은 모두 버려진다.

통신의 원리를 배웠으니까 간단하게 라우터의 작동 원리를 구현해보자. 물론 하나의 라우터만 존재한다고 가정하며,
우리가 다룰 부분은 라우터의 입출력이 주어졌을 때 버퍼의 상태가 어떻게 변하는가이다.
그러니까 라우터가 패킷을 구체적으로 어떤 방식으로 처리하고, 어디로 보내고 이런 것들은 생각하지 말자.

입력
첫 줄에는 라우터 내부에 존재하는 버퍼의 크기를 나타내는 자연수 N이 주어진다.

둘째 줄부터 한 줄에 하나씩 라우터가 처리해야 할 정보가 주어진다. 모든 정보는 발생한 시간순으로 주어졌다고 가정한다.
양의 정수는 해당하는 번호의 패킷이 입력으로 들어왔다는 것을 의미하고, 0은 라우터가 패킷 하나를 처리했다는 것을 의미한다.
이때, 버퍼가 비어있을때는 0이 입력으로 들어오지 않는다. -1은 입력의 끝을 나타낸다.

출력
라우터에 남아있는 패킷을 앞에서부터 순서대로 공백으로 구분해서 출력하면 된다. 만약 비어있을 경우 empty라고 출력한다.
"""
from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

q = deque()

size = 0

while True:
    k = int(input())
    if k == -1:
        break
    elif k == 0:
        q.popleft()
    else:
        if len(q) < N:
            q.append(k)

if q:
    print(*q)
else:
    print('empty')


