# pwnable.tw_starbound
#rop  
어려울줄 알고 쫄았던 문제  
그냥 인덱스 범위 체크를 안하는 취약점을 이용해서 음수 값을 넣어줘서 임의의 지점을 call할 수 있는 취약점을 이용한다.  
키포인트는 ROP를 할 때, popa를 사용하는 것과 leave ret 가젯을 이용해서 fake ebp를 활용해주는 것이다.  
아주 간단한 ROP문제!  
libc가 주어지지 않았지만 내 로컬과 offset이 같아 풀 수 있었다. 만약에 달랐다면 libc database에 있는 libc들의 offset을 모두 넣어봤었을 것이다..  
