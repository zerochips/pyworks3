# 리스트 - ['a', 'b', 'a' ] 대괄호 - 리스트 중복가능
# 튜플 - ('a', 'b', 'a' ) 소괄호 - 튜플 중복 가능
# 딕셔너리 - {'진':30} 중괄호 - 딕셔너리 중복 안됨
# 집합 - {'a', 'b'} 중괄호 - 중복 허용안됨, 순서가 없음

# 집합 - set(), {}를 사용, 순서가 없다 - 출력이 지멋대로 됨, 중복허용안됨
s = {2, 4, 6, 8}

# 집합에 요소를 추가한다
# 추가할 때는 add를 사용한다
s.add(10)

# 요소 삭제
s.remove(4)
print(s)

# 2가 s에 들어있냐?
print(2 in s)
# 3이 있느냐?
print(3 in s)

# 전체 삭제
s.clear()

# 전체 조회
# 순서가 없으니까 인덱싱이 안 될것 같은데
# 한 번 해보죠, 되긴 되네요
for i in s:
    print(i, end=' ')

print(s)

# 이거 집합이잖아요
# 집합에 뭐뭐 있죠 A집합 B 집합 있는데
# 교집합(A&B), 합집합(A|B), 차집합(A-B)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)
print(A | B)
print(A - B)

# 자료 중복 제거
a = [1, 1, 1, 2, 2, 3]  # 얘를 set에 넣으면 됩니다
s = set(a)              # set()을 통해서 중복제거가 돼요
print(s)

# 리스트로 변환
print(list(s))

say = set('Hello')
print(say) # { } 순서 없고, 중복 없음

# 1에서 10까지 자연수를 저장
C = { x for x in range(1, 11)}
print(C)

# 1에서 20까지의 자연수 중에서 3의 배수 저장
D = { x for x in range(1, 21) if x % 3 == 0}
print(D)