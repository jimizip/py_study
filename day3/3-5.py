# 1. 빈 리스트를 만든 후, 키보드로 5개의 양수 숫자를 입력받아 리스트에 저장하시오. 리스트의 값을 오름차순으로 정렬하는 프로그램을 작성하고, 실행 결과를 적으시오. 
print('양수 5개를 입력하세요: ')
a = []
for i in range(5):
  i = int(input())
  a.append(i)
  a.sort()
print(a)
