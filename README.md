유튜브 링크 대입기
=============
파워무비 이스터에그를 찾기 쉽게 하려고 만든 유튜브 링크 대입기입니다!

exe 파일은 아래 링크를 참조해주세요! (압축파일 비밀번호: 123)

> https://drive.google.com/file/d/13qzd4GhUNEE2XoKmvExRNAHnpr8ym-T4/view

사용 전 준비
-------------
> https://www.python.org/downloads/

먼저 위 링크에서 python 최신버전을 다운로드해 설치해주세요.(설치할 때 ADD Python 3.9 to PATH 항목을 꼭 체크해주셔야 합니다)

cmd를 켜고 pip install requests를 입력해 설치가 완료될 때까지 기다려주세요.

설치가 완료되었다면 다운받은 py파일을 python으로 실행해주면 됩니다.

사용 방법
-------------
아래와 같이 입력하시면 됩니다.

> \[글자1후보] \[글자2후보] \[글자3후보] ... \[글자11후보]

?를 넣으면 유튜브 링크에 들어갈 수 있는 문자 64개 모두를 대입합니다.

> 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-\_

!를 넣으면 유튜브 링크 마지막 글자에 들어가는 문자 16개를 대입합니다.

> 048AEIMQUYcgkosw

사용 예시
-------------
1. BUOyDLMgycg에서 여러 글자들이 헷갈릴 때:
> B U OQ0 y D L M gpqo y c go

2. 4TCjHyNHbn4의 마지막 두 글자를 모를 때:
> 4 T C j H y N H b ? !

3. B7XCd4wi0TA의 대소문자 여부를 모를 때:
> Bb 7 Xx Cc Dd 4 Ww Ii 0 Tt A

원리
-------------
사용자의 입력을 토대로 가능한 코드의 경우를 모두 구한 뒤,
구해진 모든 코드에 대해 영상의 존재 여부를 확인합니다.

영상의 존재 여부 확인은 최저화질 썸네일 링크의 응답코드를 통해 확인합니다.

> https://img.youtube.com/vi/코드/default.jpg

썸네일이 존재할 시 200으로, 아닐 시 404로 응답이 돌아오므로,
이 점을 이용해 영상이 존재하는지를 확인할 수 있습니다.

주의점
-------------
Ctrl + C를 누르면 프로그램이 종료됩니다.

인터넷에 연결되지 않은 경우 찍기를 진행할 수 없습니다

만약 일치하는 링크가 발견되었다면 브라우저에서 자동으로 링크를 열지만,
링크가 발견되더라도 링크 대입은 계속 진행됩니다.

유튜브 링크 확인을 위해 만든 것이므로 11글자를 찍을 때만 작동합니다.

경우의 수가 10000가지가 넘을 시 작동되지 않습니다.

마지막 글자에 들어갈 수 없는 문자를 자동으로 제외합니다.

향후 업데이트 계획
-------------
- 프로그램 내에 도움말 내장
- 덩어리 배열 순서 찍기 기능 추가
- 경우의 수 한도 조정(현재 10000개 이상부터는 지원하지 않음)
