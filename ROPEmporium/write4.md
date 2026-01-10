A PLT entry for a function named print_file() exists within the challenge binary, simply call it with the name of a file you wish to read (like "flag.txt") as the 1st argument.

How do we modify this string? 

```
$ rabin2 -z write4
nth paddr      vaddr      len size section type  string
-------------------------------------------------------
0   0x000006b4 0x004006b4 11  12   .rodata ascii nonexistent
```

Useful gadget: 

```
$ ROPgadget --binary ./write4 | grep "400628"
0x0000000000400628 : mov qword ptr [r14], r15 ; ret
```

Useful function:

```
0000000000400617 <usefulFunction>:
  400617:	55                   	push   %rbp
  400618:	48 89 e5             	mov    %rsp,%rbp
  40061b:	bf b4 06 40 00       	mov    $0x4006b4,%edi
  400620:	e8 eb fe ff ff       	call   400510 <print_file@plt>
  400625:	90                   	nop
  400626:	5d                   	pop    %rbp
  400627:	c3                   	ret
```

Writable sections:

```
gef➤  info proc map
process 7259
Mapped address spaces:

          Start Addr           End Addr       Size     Offset  Perms  objfile
            0x400000           0x401000     0x1000        0x0  r-xp   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/write4
            0x600000           0x601000     0x1000        0x0  r--p   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/write4
            0x601000           0x602000     0x1000     0x1000  rw-p   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/write4
      0x7ffff7800000     0x7ffff7828000    0x28000        0x0  r--p   /usr/lib/x86_64-linux-gnu/libc.so.6
      0x7ffff7828000     0x7ffff79b0000   0x188000    0x28000  r-xp   /usr/lib/x86_64-linux-gnu/libc.so.6
      0x7ffff79b0000     0x7ffff79ff000    0x4f000   0x1b0000  r--p   /usr/lib/x86_64-linux-gnu/libc.so.6
      0x7ffff79ff000     0x7ffff7a03000     0x4000   0x1fe000  r--p   /usr/lib/x86_64-linux-gnu/libc.so.6
      0x7ffff7a03000     0x7ffff7a05000     0x2000   0x202000  rw-p   /usr/lib/x86_64-linux-gnu/libc.so.6
      0x7ffff7a05000     0x7ffff7a12000     0xd000        0x0  rw-p
      0x7ffff7c00000     0x7ffff7c01000     0x1000        0x0  r-xp   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/libwrite4.so
      0x7ffff7c01000     0x7ffff7e00000   0x1ff000     0x1000  ---p   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/libwrite4.so
      0x7ffff7e00000     0x7ffff7e01000     0x1000        0x0  r--p   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/libwrite4.so
      0x7ffff7e01000     0x7ffff7e02000     0x1000     0x1000  rw-p   /home/haard/Documents/recruitment/haard_phase2/ROPEmporium/bins/write4/libwrite4.so
      0x7ffff7f99000     0x7ffff7f9c000     0x3000        0x0  rw-p
      0x7ffff7fbd000     0x7ffff7fbf000     0x2000        0x0  rw-p
      0x7ffff7fbf000     0x7ffff7fc3000     0x4000        0x0  r--p   [vvar]
      0x7ffff7fc3000     0x7ffff7fc5000     0x2000        0x0  r-xp   [vdso]
      0x7ffff7fc5000     0x7ffff7fc6000     0x1000        0x0  r--p   /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
      0x7ffff7fc6000     0x7ffff7ff1000    0x2b000     0x1000  r-xp   /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
      0x7ffff7ff1000     0x7ffff7ffb000     0xa000    0x2c000  r--p   /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
      0x7ffff7ffb000     0x7ffff7ffd000     0x2000    0x36000  r--p   /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
      0x7ffff7ffd000     0x7ffff7fff000     0x2000    0x38000  rw-p   /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
      0x7ffffffdd000     0x7ffffffff000    0x22000        0x0  rw-p   [stack]
  0xffffffffff600000 0xffffffffff601000     0x1000        0x0  --xp   [vsyscall]
```