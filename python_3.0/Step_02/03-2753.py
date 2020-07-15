# Baekjun_Programming

# Title : 윤년
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-05-2753-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 15, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (56.403 %)
#  문제 : 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
#         * 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
#         * 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
#         * 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
#
#  입력 : 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
#  출력 : 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
#  예제 입력_01 : 2000
#  예제 출력_01 :  1
#  예제 입력_02 : 1999
#  예제 출력_02 :  0
# -----------------------------------------------------------------------------------------------------------
# 잘못된 조건의 오류
# 문제풀이 : 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 4의 배수 --> A % 4 == 0
# 100의 배수가 아닐 때, A % 100 != 0
# 400의 배수일 때, A % 400 == 0
# 정리 : (A % 4 == 0) 그리고 ((A % 100 != 0) 또는 (A % 400 == 0))
# 코드 : (A % 4 == 0) and ((A % 100 != 0) or (A % 400 == 0))
#
# A = int(input())
# if ((A % 100) == 0 or (A % 4) == 0): print("1")
# elif ((A % 100) != 0 or (A % 400) == 0) : print("0")
  
A = int(input())
if A % 4 == 0 and (A % 100 != 0 or A % 400 == 0): print(1)
else: print(0)
