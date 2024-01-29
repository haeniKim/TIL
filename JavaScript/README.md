## Javascript

> 자료 : [코딩앙마] 왕 초보 자바스크립트
> ca_chapterX.js

### 1. 변수
* alert() : 경고창을 찍는 함수
* console.log() : 로그를 찍는 함수

* let : 최초로 선언하는 모든 변수에 붙여 중복을 방지, 변할 수 있음 
* const : 절대로 바뀌지 않는 상수

### 2. 자료형
* 문자형 : ' ', " ", ₩ ₩
* 숫자형 : 사칙연산 가능 (0으로 나누면 무한대, 문자를 숫자로 나누면 NaN)
* bool형 : true, false
* null -> 존재하지 않는 값
* undefined -> 할당되지 않은 값
* 객체형
* 심볼형
* typeof 연산자 : 변수의 자료형 확인

* 숫자형 + 문자형 => 숫자형이 문자형으로 변환
### 3. alert, prompt, confirm
**alert**
* 알려줌
* 메세지를 띄우고 확인 용도

**prompt**
* 입력 받음
* prompt("message", "default")
* 문자형으로 

**confirm**
* 확인 받음
* 확인, 취소(null 할당) 버튼이 있음
* 사용자 액션 확인시 자주 사용

=> 
장점:
    빠르고 간단함
단점:
    1. 스크립트 일시 정지
    2. 스타일링 X

 
### 4. 형변환 (명시적)
* 자동 형변환

**String()**
* 문자형으로 변환

**Number()**
* 숫자형으로 변환
* 문자가 들어있으면 NaN

**Boolean()**
* 불린형으로 변환
* 0, 빈 문자열, null, undefined, NaN => false

* !주의
    * Number(null) => 0
    * Number(undefined) => NaN

### 5. 기본 연산자