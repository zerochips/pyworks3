# testdb -> book 테이블 만듦
import sqlite3

def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/testdb.db")
    return conn

# 테이블 삽입
def create():
    conn = getconn()
    cursor = conn.cursor()  # cursor 객체는 sql을 조작함
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title   TEXT NOT NULL,
            author  TEXT NOT NULL,
            page    INTEGER
        )
    """
    cursor.execute(sql)     # 실행
    conn.commit()           # 커밋 완료
    conn.close()

# 책 추가
def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO book(title, author, page) "\
          "VALUES(?, ?, ?)"
    # cursor.execute(sql, ('반응형 웹페이지', '김운아', 300))
    # cursor.execute(sql, ('혼자 공부하는 자바', '신용권', 600))
    cursor.execute(sql, ('python projects', '켄 유엔스', 500))
    conn.commit()
    conn.close()

# 책 전체 검색
def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)       # 리스트로 출력
    for i in rs:
        print(i)      # 튜플로 출력
    conn.close()

# 책 한 권 검색
def select_one():
    conn = getconn()
    cursor = conn.cursor()
    # ? 동적 바인딩 방식
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2, ))  # 튜플 자료구조이므로 1개 사용(쉼표 사용)
    rs = cursor.fetchone()      # cursor.fetchone() 하나 검색
    print(rs)
    conn.close()

# 책 수정
def update():
    conn = getconn()
    cursor = conn.cursor()
    # 책번호가 2번인 페이지를 650페이지로 변경하기
    # 순서대로 cursor.execute(sql, (650, 2))
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (650, 2))
    conn.commit()
    conn.close()

def delete():
    conn = getconn()
    cursor = conn.cursor()
    # 책번호가 1번인 책을 삭제하시오, 동적 바인드 방식 ?
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1,))
    conn.commit()
    conn.close()

# 호출
# print(getconn(), "연결 객체 생성")        # <sqlite3.Connection object at 0x0000017D31551030> 이게 지금 객체입니다.
# create()
# insert()
update()
select()
# select_one()
# delete()