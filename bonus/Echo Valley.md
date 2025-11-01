# Echo Valley 

The echo valley is a simple function that echoes back whatever you say to it.But how do you make it respond with something more interesting, like a flag?Download the source: [valley.c](https://challenge-files.picoctf.net/c_shape_facility/3540df5468ae2357d00a7a3e2d396e6522b24f7a363cbaff8badcb270d186bda/valley.c)Download the binary: [valley](https://challenge-files.picoctf.net/c_shape_facility/3540df5468ae2357d00a7a3e2d396e6522b24f7a363cbaff8badcb270d186bda/valley)

I haven't solved this challenge yet, but I am writing everything that I found till now.  

valley.c : 

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_flag() {
    char buf[32];
    FILE *file = fopen("/home/valley/flag.txt", "r");
    if (file == NULL) {
      perror("Failed to open flag file");
      exit(EXIT_FAILURE);
    }
    fgets(buf, sizeof(buf), file);
    printf("Congrats! Here is your flag: %s", buf);
    fclose(file);
    exit(EXIT_SUCCESS);
}

void echo_valley() {
    printf("Welcome to the Echo Valley, Try Shouting: \n");
    char buf[100];
    while(1)
    {
        fflush(stdout);
        if (fgets(buf, sizeof(buf), stdin) == NULL) {
          printf("\nEOF detected. Exiting...\n");
          exit(0);
        }
        if (strcmp(buf, "exit\n") == 0) {
            printf("The Valley Disappears\n");
            break;
        }
        printf("You heard in the distance: ");
        printf(buf);
        fflush(stdout);
    }
    fflush(stdout);
}

int main()
{
    echo_valley();
    return 0;
}
```


This is what the program does:
- Runs the function `echo_valley`
- `echo_valley` function takes input of 100 bytes, and prints that using `printf(buf)`, which is the vulnerability here. There is no format specifier given, so it makes it vulnerable to format string attacks, which can be used to leak memory addresses and even overwrite existing addresses. 
- Then there's another function called `print_flag`, that prints the flag from a file in the remote server. Its not called by any other function in the program. 

This is what I concluded from my analysis of the program: 
I need to somehow return the function `print_flag` using format string attack. 

After referring to the video mentioned in the references, I need to overwrite the return address of the `printf` function from the GOT(Global Offset Table), to the return address of the `print_flag` function. 

I can easily do that using GDB.

First of all, lets disassemble the `echo_valley` function. 
**Note:** In my machine, I have to run the program once in `gdb` to get the memory address which can be accessed by `gdb`. I don't have a valid explanation as to why this happens.  

```
(gdb) disas echo_valley
Dump of assembler code for function echo_valley:
   0x0000555555555307 <+0>:	endbr64
   0x000055555555530b <+4>:	push   %rbp
   0x000055555555530c <+5>:	mov    %rsp,%rbp
   0x000055555555530f <+8>:	sub    $0x70,%rsp
   0x0000555555555313 <+12>:	mov    %fs:0x28,%rax
   0x000055555555531c <+21>:	mov    %rax,-0x8(%rbp)
   0x0000555555555320 <+25>:	xor    %eax,%eax
   0x0000555555555322 <+27>:	lea    0xd37(%rip),%rax        # 0x555555556060
   0x0000555555555329 <+34>:	mov    %rax,%rdi
   0x000055555555532c <+37>:	call   0x5555555550e0 <puts@plt>
   0x0000555555555331 <+42>:	mov    0x2cd8(%rip),%rax        # 0x555555558010 <stdout@GLIBC_2.2.5>
   0x0000555555555338 <+49>:	mov    %rax,%rdi
   0x000055555555533b <+52>:	call   0x555555555140 <fflush@plt>
   0x0000555555555340 <+57>:	mov    0x2cd9(%rip),%rdx        # 0x555555558020 <stdin@GLIBC_2.2.5>
   0x0000555555555347 <+64>:	lea    -0x70(%rbp),%rax
   0x000055555555534b <+68>:	mov    $0x64,%esi
   0x0000555555555350 <+73>:	mov    %rax,%rdi
   0x0000555555555353 <+76>:	call   0x555555555120 <fgets@plt>
   0x0000555555555358 <+81>:	test   %rax,%rax
   0x000055555555535b <+84>:	jne    0x555555555376 <echo_valley+111>
   0x000055555555535d <+86>:	lea    0xd27(%rip),%rax        # 0x55555555608b
   0x0000555555555364 <+93>:	mov    %rax,%rdi
   0x0000555555555367 <+96>:	call   0x5555555550e0 <puts@plt>
   0x000055555555536c <+101>:	mov    $0x0,%edi
   0x0000555555555371 <+106>:	call   0x555555555170 <exit@plt>
   0x0000555555555376 <+111>:	lea    -0x70(%rbp),%rax
   0x000055555555537a <+115>:	lea    0xd24(%rip),%rdx        # 0x5555555560a5
   0x0000555555555381 <+122>:	mov    %rdx,%rsi
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000555555555384 <+125>:	mov    %rax,%rdi
   0x0000555555555387 <+128>:	call   0x555555555130 <strcmp@plt>
   0x000055555555538c <+133>:	test   %eax,%eax
   0x000055555555538e <+135>:	jne    0x5555555553c1 <echo_valley+186>
   0x0000555555555390 <+137>:	lea    0xd14(%rip),%rax        # 0x5555555560ab
   0x0000555555555397 <+144>:	mov    %rax,%rdi
   0x000055555555539a <+147>:	call   0x5555555550e0 <puts@plt>
   0x000055555555539f <+152>:	nop
   0x00005555555553a0 <+153>:	mov    0x2c69(%rip),%rax        # 0x555555558010 <stdout@GLIBC_2.2.5>
   0x00005555555553a7 <+160>:	mov    %rax,%rdi
   0x00005555555553aa <+163>:	call   0x555555555140 <fflush@plt>
   0x00005555555553af <+168>:	nop
   0x00005555555553b0 <+169>:	mov    -0x8(%rbp),%rax
   0x00005555555553b4 <+173>:	sub    %fs:0x28,%rax
   0x00005555555553bd <+182>:	je     0x5555555553ff <echo_valley+248>
   0x00005555555553bf <+184>:	jmp    0x5555555553fa <echo_valley+243>
   0x00005555555553c1 <+186>:	lea    0xcf9(%rip),%rax        # 0x5555555560c1
   0x00005555555553c8 <+193>:	mov    %rax,%rdi
   0x00005555555553cb <+196>:	mov    $0x0,%eax
   0x00005555555553d0 <+201>:	call   0x555555555110 <printf@plt>
   0x00005555555553d5 <+206>:	lea    -0x70(%rbp),%rax
   0x00005555555553d9 <+210>:	mov    %rax,%rdi
   0x00005555555553dc <+213>:	mov    $0x0,%eax
   0x00005555555553e1 <+218>:	call   0x555555555110 <printf@plt>
   0x00005555555553e6 <+223>:	mov    0x2c23(%rip),%rax        # 0x555555558010 <stdout@GLIBC_2.2.5>
   0x00005555555553ed <+230>:	mov    %rax,%rdi
   0x00005555555553f0 <+233>:	call   0x555555555140 <fflush@plt>
   0x00005555555553f5 <+238>:	jmp    0x555555555331 <echo_valley+42>
   0x00005555555553fa <+243>:	call   0x555555555100 <__stack_chk_fail@plt>
--Type <RET> for more, q to quit, c to continue without paging--
   0x00005555555553ff <+248>:	leave
   0x0000555555555400 <+249>:	ret
```

Here, we can see that, the `printf` function is being called at the address `0x1110`. Lets disassemble the contents of that address: 
```
(gdb) disas 0x555555555110
Dump of assembler code for function printf@plt:
   0x0000555555555110 <+0>:	endbr64
   0x0000555555555114 <+4>:	jmp    *0x2e86(%rip)        # 0x555555557fa0 <printf@got.plt>
   0x000055555555511a <+10>:	nopw   0x0(%rax,%rax,1)
End of assembler dump.
```

The function jumps to the address `0x555555557fa0` in the GOT. 
```
(gdb) x 0x555555557fa0
0x555555557fa0 <printf@got.plt>:	0xf7c60100
```
Now, we got the address of `printf` function on the GOT.

Lets find the address of `print_flag` function. 
```
(gdb) x print_flag
0x555555555269 <print_flag>:	0xfa1e0ff3
```

Now that we have the addresses of both the functions, we can overwrite the value of the address of `printf` function with the address of `print_flag` function. 

But before that, lets set two break points, just before and after the `printf(buf)` instruction. 
```
(gdb) break *0x00005555555553e1
Breakpoint 3 at 0x5555555553e1: file /home/valley/valley.c, line 39.
(gdb) break *0x00005555555553e6
Breakpoint 4 at 0x5555555553e6: file /home/valley/valley.c, line 40.
```
Just so that, we can do the overwrite, while the program is running and see the result in real time.

```
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/haard/Documents/recruitment/haard_phase2/binex/valley
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Welcome to the Echo Valley, Try Shouting:
hello

Breakpoint 1, 0x00005555555553e1 in echo_valley () at /home/valley/valley.c:39
39	        printf(buf);
(gdb) set {long}0x555555557fa0=0x555555555269
(gdb) c
Continuing.
Failed to open flag file: No such file or directory
You heard in the distance: [Inferior 1 (process 45654) exited with code 01]
```
As we can see, the function `print_flag` is being run, but it cannot find the flag file, as we are running the binary locally. 

I can implement the overwrite using `gdb`, but I cannot implement the same method using format strings. 

This is what I have to do: 

Read off the memory from the stack and find the addresses of the `printf` and `print_flag` using the `%x` or `%p` format string. Then I can overwrite their values using `%n` format string. 


Reference: 
https://youtu.be/t1LH9D5cuK4?si=6qsgudvmZ6hcqGt8


Random Notes: 
command for overwrite: 
```
(gdb) set {long}printf_plt=print_flag
printf_plt = 0x555555557fa0
print_flag = 0x555555555269
```

```
(gdb) set {long}0x555555557fa0=0x555555555269
```

```
(gdb) set {int}printf_plt=print_flag # must be replaced with the req addresses
```

```python
import struct 
print_flag = #address of print_flag
fflush_addr = #address of fflush 

buff_len = # length of buffer 

def pad(s):
	return s+"X"*(buff_len-len(s))
exploit = ""
exploit += "%x "*4
print(pad(exploit))
```

PUTS_PLT = 0x555555557fa0
PRINT_FLAG = 0x1269
0x555555555269
0x555555557f88
PUTS = 0x3f88
