## IOT 프로젝트

팀 : zeroFire

팀원 : 김진우 ,강민성, 이채환, 심상진, 강기범

### 프로젝트 정보

#### 1. 프로젝트 주제

화제시 통합 시스템 구현

#### 2. 주제 선정배경 또는 이유

최근 많이 발생하는 화재를 예방하고 문제를 해결할 수 있는 IoT 통합 서비스를 개발하여 제공하고자 합니다.

##### 시장조사

- LG유플러스, 지능형 IOT 소화시전 개발
	- 소화전 누수 상태, 동결 여부, 방수 압력 모니터링
	- 직접 현장에 출동하지 않더라도 관제센터에서 확인


- 윈드리버, 소방차 원격 관리 위해 ‘디바이스 클라우드’ 공급
	- 소방차에 텔루루스를 탑재해 운영
	- 원격으로 소프트웨어 업데이트
	- 문제 해결을 위한 기술 자원 및 디바이스 구성 지원
	
- IDEX Fire & Safety, “smart tuck” iot에서 microsoft와 협력
	- 실시간 통찰력을 제공을 통해 진단 통찰력과 네트워크 기능
	- 차량 신뢰성을 높이고 생명을 구하는 데 도움
	


#### 3. 프로젝트 계획

- 1주차 계획(04-25~05-01) : 프로젝트 계획 및 요구사항 설계 
- 2주차 계획(05-02~05-08) : mqtt 장비 테스트 및 설계, 웹 구현
- 3주차 계획(05-09~05-15) : 안드로이드 구현, mqtt 통신 테스트
- 4주차 계획(05-16~05-19) : 구현 시스템 점검 및 발표 준비 및 장비 결함 테스트

#### 4. 아키텍처 

- 웹
  - 화재가 발생할 시 라즈베리 카메라를 통해 화면 실시간 스트리밍
  - 화재가 발생하면 부저 센서에서 삐 소리 나게끔
  - gps 센서이용해서 화재발생 지역을 지도api 로표시 표시
- 라즈베리파이(소방차)
  - 수중펌프모터(SZH-GNP155)와 서보모터(SG-90)을 이용해서 방수로 불을 제거
  - gps 센서를 이용해서 현재 지역을 표시
- 라즈베리파이(지역)
  -  불꽃감지 센서와 온도습도 센서로 지역 현황 확인
  -  이상 상황 발생시 부저를 통한 경보
- 모바일
  -  차량제어
  -  차량 모바일 화면 스트리밍
  -  서보모터 제어

### 5. 데이터베이스

(https://user-images.githubusercontent.com/73889507/169018814-991e299f-47e3-4dc8-b315-cb86b1d9f140.png)

<img src = "https://user-images.githubusercontent.com/73889507/169018814-991e299f-47e3-4dc8-b315-cb86b1d9f140.png" >

웹사이트, 안드로이드 

<img src = "https://user-images.githubusercontent.com/73889507/169019045-f5467d8d-a7c6-4aaf-97d3-9d1b8f4f2bf0.PNG" >




### 6. 코드 컨베이션
- 공통
  - 함수명 : 동사 + 명사
  - 변수명 : 명사 + 명사 or 형용사 + 명사
  - 변수 최대 길이 220자
  - 명사는 다수로 쓰지 않되 개수를 나타내는 단어 꼭 적어주기
  - 세미클론, 콤마 뒤에는 공백 ex) print(hi, sendMessage, count)
  - 함수끼리 한줄 개행
  ```pychon
  if(조건식) {
	  조건문
  }

  if(조건식) {
	  조건문
  }

  ```
- 스타일
  - 주석은  한줄 // 회원가입 메소드
- 여러줄 
  /*
  tmap api
    api 주소 및 설정
  */
  
### 6. Github Role
  - 각자 맡은 파일이외의 다른 파일은 건드리지 말 것
  - git pull는 5시에 다 같이 pull
  - git fetch는 pull이 끝나는 즉시 fetch 해서 점검
  - 5시 이외에 pull 한 것 있으면 이슈에 내용을 적고 다음날 9시에 pull하고 fetch
  - commit 타입 
    - feat 새로운 기능 구현
    - add 부수적인 코드 추가, 라이브러리 추가, 새로운 파일 생성
    - chore : 코드 수정, 내부 파일 수정
    - fix : 버그 수정
    - del : 쓸모 없는 코드 삭제
    - style : 코드 형식, 정렬, 주석 등의 변경
    - refactor : 코드 리펙토링
    - test : 테스트 추가, 테스트 리펙토링
    - do;s 문서작성![데이터베이스]

    - ex) fix (파일이름) -- 회원가입 구현

### 7. ui

#### 웹사이트 탬플릿

- https://startbootstrap.com/theme/sb-admin-2

#### 프로토타입

- https://ovenapp.io/project/nsLNeZiTvuQQw22yHoQNiM0TSPsmtFaA#YDnQQ


코틀린(안드로이드)
네이밍 lowerCamelCase 사용 ex) goodidea (x) goodIdea 



파이썬(장고)
두번째 문장에는 밑줄(underscore) 하기 ex) goodidea (x) good_idea(0)


### 8. 테스트 시나리오

1. 지역 라즈베리파이에 라이터로 불을 비추고 부저 센서가 울린다
2. 웹에서 경고창이 삐 소리가 울린다
3. 움직여서 화제 지역으로 이동한다
4. 화제 지역에 이동한후 서브모터로 불이난 방향을 조준한다
5. 안드로이드 버튼을 눌러서 불이난 지역에 불을 끈다

### 9. 테스트 시나리오 시연

![완성스](https://user-images.githubusercontent.com/73889507/169022443-b187322c-b33f-4cd4-b7b4-f64d58551067.gif)


#### 문서 참고기록

https://docs.google.com/document/d/1xxr2f3yGGx7rId-788glnKZvJHw1qTh6U0MxFwSPnmU/edit?userstoinvite=shimhotdog@gmail.com&actionButton=1#

안드로이드 - https://github.com/project-travel-mate/Travel-Mate 지도 ,전체적인 틀 https://www.instructables.com/IoT-Home-Weather-Monitoring-System-With-Android-Ap/



