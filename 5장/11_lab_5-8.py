'''
2023-10-04
컴퓨터공학부 202395004 김나현
while문으로 별 그리기
'''

#터틀 모듈을 사용하기 위한 준비
#turtle 클래스 객체를 t로 생성(별명)
import turtle as t

t.shape("turtle")
#초기 값
su = 0

#5개의 선분을 그리기 위하여 5회 반복
#50 픽셀 길이의 선분을 그린다.
#144도 거북을 회전 시킨다.
#변수 su를 1만큼 증가 시킨다.
while su < 5 :
    t.forward(50)
    t.right(144)
    su += 1

#그림판 사라지지 않음
t.mainloop()