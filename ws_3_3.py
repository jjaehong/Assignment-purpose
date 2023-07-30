
import book

def rental_book(name,n)
    book.decrease_book(n)
    print(f"{name}님이 {n}권의 책을 대여했습니다")

rental_book("홍길동", 3)