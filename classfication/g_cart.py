# Cart 클래스 정의
# 클래스 리스트
class Cart:
    li = []                         # 클래스 리스트

    def add_cart(self, goods):      # 제품 추가
        Cart.li.append(goods)

cart1 = Cart()
cart1.add_cart("계란")
print(Cart.li)

cart2 = Cart()
cart2.add_cart("오징어")
print(Cart.li)

cart3 = Cart()
cart3.add_cart("소고기")
print(Cart.li)

# for문 출력
str1 = ""
for i in Cart.li:                    # 클래스 이름으로 직접 접근
    str1 += i

print(str1)