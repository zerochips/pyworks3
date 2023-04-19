# 딕셔너리
d = {'Tomas': 13, 'Jane':9}

# 요소 추가 - Mike가 10살
d['Mike'] = 10
d['Mero'] = 40
d['yori'] = 60
d['han'] = 100
print(d)
print()

# 모든 key 값을 가져오는 방법이 있어요 - keys()
# 그런데 리스트로 나오죠
print('모든 key 값:\n',d.keys(), '\n여긴 다 이름만 나왔지롱~')
print()
# 이렇게하면 리스트로 자료로 변환
print(list(d.keys()))
print()

# 모든 값(value) 가져오기 - values()
# 현재 나이가 나타남
print('모든 values 값: ',d.values())

# 모든 키와 값 가져오기 - items()
for key, val in d.items():
    print(key, ':', val)
