# 1. set-register 

In this level, you will be working with registers. You will be asked to modify or read from registers.

In this level, you will work with registers! Please set the following:

`rdi = 0x1337`

`chall.asm`:
```asm
section .text
	global _start

_start:
	mov rdi, 0x1337
```

Compilation:
```
$ nasm -f elf64 chall.asm -o chall.o
$ ld chall.o -o chall
$ /challenge/run chall

In this level you will be working with registers. You will be asked to modify
or read from registers.


In this level you will work with registers! Please set the following:
  rdi = 0x1337

Extracting binary code from provided ELF file...
Executing your code...
---------------- CODE ----------------
0x400000:	mov   	edi, 0x1337
--------------------------------------
pwn.college{gPUoqdPhHsvzGEgSrOAiBlUwy8K.dRTOxwyNwkzNyEzW}
```

**flag:** `pwn.college{gPUoqdPhHsvzGEgSrOAiBlUwy8K.dRTOxwyNwkzNyEzW}`

---

# 2. 

# 3. 

# 4. linear-equation-registers 

```asm
section .text
	global _start

_start:
	mov rax, rdi
	imul rax, rsi
	add rax, rdx  
```

- `f(x) = mx + b`, where:
    - `m = rdi`
    - `x = rsi`
    - `b = rdx`

Place the result into `rax`.

**flag:**

---
# 5. integer-division 

```asm

section .text
    global _start 

_start:
    mov rax, rdi
    div rsi
```


**flag:**

---
# 6. modulo-operation 

```asm

section .text
    global _start 

_start:
    mov rax, rdi
    div rsi
    mov rax, rdx 

```


**flag:**

---
# 7. set-upper-byte  

```
MSB                                    LSB
+----------------------------------------+
|                   rax                  |
+--------------------+-------------------+
                     |        eax        |
                     +---------+---------+
                               |   ax    |
                               +----+----+
                               | ah | al |
                               +----+----+
```


```asm

section .text
    global _start

_start:
    mov ah, 0x42

```


**flag:**

---
# 8. efficient-modulo 

```
section .text
        global _start

_start:
        mov al, dil
        mov bx, si
	
```

**flag:** `pwn.college{4TrgZpP7ID1jPDz1FD14r98gIVz.dlTOxwyNwkzNyEzW}`

---

# 9. byte-extraction 

```
section .text
	global _start

_start: 
	mov rax, rdi 
	shl rax, 32
	shr rax, 56
	shl rax, 56 
```

flag: `pwn.college{w_m4Lgwt4GL8_AajKnMBPhCoQL7.dBDMywyNwkzNyEzW}`

---

# 10. bitwise-and 

```
section .text
	global _start

_start:
	and rdi, rsi
	and rax, rdi
```

**flag:** `pwn.college{UBz7aRoKhAEoSZxg4BhwN7iPByR.dFDMywyNwkzNyEzW}`

---

# 11. check-even (Good one)

Using only the following instructions:

- `and`
- `or`
- `xor`

Implement the following logic:

```plaintext
if x is even then
  y = 1
else
  y = 0
```

Where:

- `x = rdi`
- `y = rax`

```
section .text
	global _start

_start:
	and rax, 0x0
	or rax, 0x1
	and rdi, rax
	and rax, rdi
	xor rax, 0x1 
```

---

# 12. memory-read 

In x86, we can access the thing at a memory location, called dereferencing, like so:

```
mov rax, [some_address]        <=>     Moves the thing at 'some_address' into rax
```

This also works with things in registers:

```
mov rax, [rdi]         <=>     Moves the thing stored at the address of what rdi holds to rax
```

This works the same for writing to memory:

```
mov [rax], rdi         <=>     Moves rdi to the address of what rax holds.
```

So if `rax` was `0xdeadbeef`, then `rdi` would get stored at the address `0xdeadbeef`:

```
[0xdeadbeef] = rdi
```

```
section .text
	global _start

_start:
	mov rax, [0x404000]
```

**flag:** `pwn.college{gN1rMtSEREoeen8wtpwM6XSy9LB.QXyEDOzwyNwkzNyEzW}`

# 13. memory-write 

```
section .text
	global _start

_start:
	mov [0x404000], rax
```


**flag:** `pwn.college{4GNAkABYNkhDEwniYHuif1b7wRP.QXzEDOzwyNwkzNyEzW}`

# 14. memory-increment 

```
section .text
        global _start

_start:
        mov rax, [0x404000]
        add rax, 0x1337
        mov [0x404000], rax
        sub rax, 0x1337
```

**flag:** `pwn.college{Iy9niJgbER7UdUF3FK86L2ap4fE.dNDMywyNwkzNyEzW}`

