# time 모듈
import time

# 1부터 10까지 출력 - 1초 간격을 출력
start = time.time()

for i in range(1, 11):
    time.sleep(0.5)     # 여기서 출력 되는 시간 설절 현 - 0.5 초로 설정되어 있음
    print(i)

end = time.time()
# print(end - start)
et = end - start
# format을 사용할 때는 아래 처럼 사용함
print("수행 시간 : {0:.2}".format(et))
