# 리스트 복사
a = [1, 2, 3, 4]
a2 = []

# 3의 배수를 출력할 때 이렇게 하죠
"""for i in a:
    a2.append(3 * i)
print(a2)"""

# for 문을 넣고
# 리스트 내부에 포함 - for 문이 리스트 내포
a3 = [ 3 * i for i in a]
print(a3)

# 3의 배수 중에 짝수만 저장해라
# 3의 배수이면서 짝수인 수 저장
"""a4 = []
for i in a:
    if i % 2 == 0:
        a4.append(3 * i)
print(a4)"""

# 이걸 리스트로는 다시
a4 = [ 3 * i for i in a if i % 2 == 0]
print(a4)

a5 = [ 5 * i for i in a if i % 2 == 1]
print(a5)

# 1부터 10까지 저장하는 리스트
# b 배열이 생겼죠
b = [ i for i in range(1, 11)]
print(b)

# 더 심화해서 여기서
b2 = [ i for i in range(1, 11) if i % 2 == 0]
print(b2)