# set-register 

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
# linear-equation-registers 

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
# integer-division 

```asm

section .text
    global _start 

_start:
    mov rax, rdi
    div rsi
```


**flag:**

---
# modulo-operation 

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
# set-upper-byte  

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
# efficient-modulo 

```
section .text
        global _start

_start:
        mov al, dil
        mov bx, si
	
```

**flag:** `pwn.college{4TrgZpP7ID1jPDz1FD14r98gIVz.dlTOxwyNwkzNyEzW}`

---

# byte-extraction 

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

# bitwise-and 

```
section .text
	global _start

_start:
	and rdi, rsi
	and rax, rdi
```

**flag:** `pwn.college{UBz7aRoKhAEoSZxg4BhwN7iPByR.dFDMywyNwkzNyEzW}`

---

# check-even 

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
	
```


