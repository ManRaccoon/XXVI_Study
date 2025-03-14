## 📍문제 탐색하기

세가지 숫자 A, B, C가 공백을 기준으로 주어진다.

세 수의 합을 출력한다.

## 📍문제 설계하기

input().split()으로 입력받고 map을 사용해서 int로 타입캐스팅 후 list로 만들어서 nums에 저장한다.

sum(nums)로 출력한다.

## 🥕배운것

1. **split()**

 `split()` 을 통해 `10 20 30` 이라는 입력은 `[’10’, ‘20’, ‘30’]` 으로 변환됩니다.

→ split()은 문자열 리스트로 변환

1. **map()**

`map(int, … )` 

> 🍯 TIP ! 
map() 함수는 반복 가능한 객체(리스트, 튜플) 등의 요소에 대해 지정한 함수를 적용합니다.
여러 요소에 동일한 작업을 해야 될 때 주로 사용됩니다.
> 

1. **시간복잡도**

이 문제의 시간복잡도는 O(1) , 상수 연산입니다.

단 한번의 연산만 사용되었기 때문입니다.

> 🍯 TIP ! 
O(1)의 시간복잡도는 상수 연산으로, 입력의 크기와 상관없이 일정한 시간에 연산이 완료될 때를 말합니다.
입력의 크기가 아무리 커져도 항상 동일한 시간이 소요될 때의 시간복잡도를 의미하는데요,
이 문제에서 A와 B의 크기가 아무리 커져도 연산은 덧셈 연산 한번만 소요되는 것과 같습니다.
>
