# 다들 실습을 너무 열심히해서 내가 계속 push를 못하는 건에 대하여

import time

# 0.5초씩 인내심이 카운트다운 되는 코드
patience = [i for i in range(10, 0, -1)]

for i in patience:
    print(i)
    time.sleep(0.5)
