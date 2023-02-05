<h1>팬명록 만들기- homework</h1>

1. 기능
   1. 응원 남기기[POST] : 정보 입력 후 '응원남기기' 버튼 클릭 시 주문 목록에 추가
      1. 클라이언트: 
        - data out : 닉네임, 응원 댓글
        - data in : 메시지
      2. 서버 :
         - data in : 닉네임, 응원 댓글
         - data out : 메시지 
   2. 응원 보기[GET] : 페이지 로딩 후 하단 응원 목록이 자동으로 보이기
      1. 클라이언트 
         - data out : x
         - data in : 응원 목록
      2. 서버 :
         - data in : x
         - data out : 응원 목록
   3. 날씨 갱신 기능[GET] : 현재 날씨 갱신
      1. 클라이언트 
         - data out : x
         - data in : 현 날씨
      2. 서버 : API 사용
2. 기타 파일
   1. front_prac : 클라이언트 연습용 파일