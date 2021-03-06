# Baekjun_Programming

# Title : N 찍기
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-05-2741-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 16, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (49.385 %)
#  문제 : 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
#  출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
#  예제 입력 : 5
#  예제 출력 : 1
#             2
#             3
#             4
#             5
# -----------------------------------------------------------------------------------------------------------
import sys

case = sys.stdin.readline()

for i in range(0, int(case)):
    print(i+1)
