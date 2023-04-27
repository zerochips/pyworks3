import time

start = time.time()
def getgob(n):
    gob = 1
    for i in range(1, n+1):
        gob *= i
    return gob
print(getgob(995))
end = time.time()
print(f"소요시간 : {end-start:.10f}")

# 재귀함수 측정
start = time.time()
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(995))
end = time.time()
print(f"소요시간 : {end-start:.10f}")
