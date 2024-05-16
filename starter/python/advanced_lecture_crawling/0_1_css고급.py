# 웹사이트 구조가 정말 다양하다.
# 어떠한 html 구조에서도 원하는 결과를 얻기 위해 노력해야 한다.
# 4가지 선택자를 추가로 학습할 것이다.

# 1. 형제 선택자 (Sibling Selector)
# 동일한 부모를 가진 요소들 중에 특정 요소를 선택하는 데 사용
# 인접 형제 선택자 (A + B) - A 다음 하나의 B만 선택해준다.
# 일반 형제 선택자 (A ~ B) - A 다음 모든 B를 선택한다.

# nth-of-type() 선택자
# - 특정 유형(type)의 요소 중 특정 순서에 해당하는 요소를 선택할 때 사용

# ex)   div.main > a:nth-of-type(3)     3번 째 녀석을 선택하는 것
#       div.main > a:nth-of-type(even)  짝수만 골라준다.
#       div.main > a:nth-of-type(2n+3)

