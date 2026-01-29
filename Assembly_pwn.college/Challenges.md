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

# 2. set-multiple-registers

```asm
section .text
	global _start

_start:
	mov rax, 0x1337
	mov r12, 0xCAFED00D1337BEEF
	mov rsp, 0x31337
```

# 3. add-to-register

```asm
section .text
	global _start

_start:
	add rdik, 0x331337
```

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

```asm
section .text
        global _start

_start:
        mov al, dil
        mov bx, si
```

**flag:** `pwn.college{4TrgZpP7ID1jPDz1FD14r98gIVz.dlTOxwyNwkzNyEzW}`

---

# 9. byte-extraction 

```asm
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

```asm
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

```asm
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

```asm
section .text
	global _start

_start:
	mov rax, [0x404000]
```

**flag:** `pwn.college{gN1rMtSEREoeen8wtpwM6XSy9LB.QXyEDOzwyNwkzNyEzW}`

# 13. memory-write 

```asm
section .text
	global _start

_start:
	mov [0x404000], rax
```


**flag:** `pwn.college{4GNAkABYNkhDEwniYHuif1b7wRP.QXzEDOzwyNwkzNyEzW}`

# 14. memory-increment 

```asm
section .text
        global _start

_start:
        mov rax, [0x404000]
        add rax, 0x1337
        mov [0x404000], rax
        sub rax, 0x1337
```

**flag:** `pwn.college{Iy9niJgbER7UdUF3FK86L2ap4fE.dNDMywyNwkzNyEzW}`

# 15. byte-access

```asm
section .text
	global _start
	
_start:
	mov al, byte [0x404000]
```

**flag:** `pwn.college{UFXvLKXhaq8dRANnRjX5cbzwMqa.QX0EDOzwyNwkzNyEzW}`

# 16. memory-size-access

```asm
section .text
	global _start

_start:
	mov al, [0x404000]
	mov bx, [0x404000]
	mov ecx, [0x404000]
	mov rdx, [0x404000]
```

**flag:**`pwn.college{0DbDSMd77n1ZiEYOplbOrkVeGLi.dRDMywyNwkzNyEzW}`


# 17. little-endian-write 

```asm
section .text
	global _start

_start:
	mov rax, [rdi]
	mov rax, 0xdeadbeef00001337
	mov [rdi], rax

	mov rbx, [rsi]
	mov rbx, 0xc0ffee0000
	mov [rsi], rbx
```

**flag:** `pwn.college{UlhLrhwsG67Kaq7ZUtRSIjXUCWB.dVDMywyNwkzNyEzW}`

# 18. memory-sum 

Perform the following:

- Load two consecutive quad words from the address stored in `rdi`.
- Calculate the sum of the previous steps' quad words.
- Store the sum at the address in `rsi`.

```asm
section .text
	global _start

_start:
	mov rax, [rdi]
	mov rbx, [rdi+8]
	
	add rax, rbx
	mov [rsi], rax
```

**flag:**`pwn.college{Ij3S7MQ3WzuDlgxL2NkgJwSCs5q.dZDMywyNwkzNyEzW}`

# 19. stack-subtraction 

```asm
section .text
	global _start

_start:
	pop rax
	sub rax, rdi
	push rax
```

**flag:** `pwn.college{Qp3nHX52fmnOCtfKV-IbIR_v21l.ddDMywyNwkzNyEzW}`

# 20. swap-stack-values 

Using only the following instructions:

- `push`
- `pop`

Swap values in `rdi` and `rsi`.

Example:

- If to start `rdi = 2` and `rsi = 5`
- Then to end `rdi = 5` and `rsi = 2`

```asm
section .text
	global _start
	
_start:
	push rdi
	push rsi
	pop rdi
	pop rsi
```

**flag:** `pwn.college{wKcx5VVZWh9kBJ2DqjFZlsBdt7F.dhDMywyNwkzNyEzW}`

# 21. average-stack-values 

```asm
section .text
	global _start

_start:
	mov rbx, qword [rsp+8]
	add rbx, qword [rsp+16]
	add rbx, qword [rsp+24]
	add rbx, qword [rsp]
	mov rcx, 4
	mov rax, rbx
	div rcx
	push rax
```

**flag:** `pwn.college{k3etjTkJ6fuveeoCZxJkH5tLsQv.dlDMywyNwkzNyEzW}`

# 22. absolute-jump

```asm
section .text
	global _start

_start:
	mov rax, 0x403000
	jmp rax
```

**flag:** `pwn.college{ESgspj6qhJkCTlfSqT6rg6zl-zW.QX1EDOzwyNwkzNyEzW}`

# 23. relative-jump

```asm
section .text
	global _start

_start:
	jmp huh
	%rep 0x51
	nop
	#endrep
huh:
	mov rax, 0x1
```

**flag:** `pwn.college{wGJBLgVKbAabogmejaoZ_RayGuY.QX2EDOzwyNwkzNyEzW}`

# 24. jump-trampoline 

```asm
section .text
	global _start

_start:
	jump huh
	%rep 0x51
	nop
	%endrep
huh:
	pop rdi
	mov rax, 0x403000
	jmp rax
```


**flag:** `pwn.college{8Xe99zo6t-UV3P9pSJQwUfiecAs.dBTMywyNwkzNyEzW}`

# 25. conditional-jump (good) 

Implement this in assembly

```plaintext
if [x] is 0x7f454c46:
    y = [x+4] + [x+8] + [x+12]
else if [x] is 0x00005A4D:
    y = [x+4] - [x+8] - [x+12]
else:
    y = [x+4] * [x+8] * [x+12]
```

`x = rdi, y = rax`

```asm 
section .text
        global _start

_start:
        mov eax, dword [rdi]
        cmp eax, 0x7f454c46
        je first

        cmp eax, 0x00005A4D
        je second

        mov eax, dword [rdi+4]
        imul eax, dword [rdi+8]
        imul eax, dword [rdi+12]
        jmp done
first:
        mov eax, dword [rdi+4]
        add eax, dword [rdi+8]
        add eax, dword [rdi+12]
        jmp done
second:
        mov eax, dword [rdi+4]
        sub eax, dword [rdi+8]
        sub eax, dword [rdi+12]
        jmp done

done:
```

**flag:** `pwn.college{Qlo8-eMkX7S6vBx2qAqY6SvgyWA.dFTMywyNwkzNyEzW}`

# 26. indirect-jump 

Using the above knowledge, implement the following logic:

```plaintext
if rdi is 0:
  jmp 0x40301e
else if rdi is 1:
  jmp 0x4030da
else if rdi is 2:
  jmp 0x4031d5
else if rdi is 3:
  jmp 0x403268
else:
  jmp 0x40332c
```

Please do the above with the following constraints:

- Assume `rdi` will NOT be negative.
- Use no more than 1 `cmp` instruction.
- Use no more than 3 jumps (of any variant).
- We will provide you with the number to 'switch' on in `rdi`.
- We will provide you with a jump table base address in `rsi`.

Here is an example table:

```
[0x40427c] = 0x40301e (addrs will change)
[0x404284] = 0x4030da
[0x40428c] = 0x4031d5
[0x404294] = 0x403268
[0x40429c] = 0x40332c
```

```asm
section .text
        global _start

_start:
        cmp rdi, 3
        ja default_case

        jmp qword [rsi + rdi*8]
default_case:
		jmp qword [rsi + 32]
```

**flag:** `pwn.college{E43ni7CQXWCxCWY8Y3QhgdT07ZQ.dJTMywyNwkzNyEzW}`

# 27. average-loop

```plaintext
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
```

Please compute the average of `n` consecutive quad words, where:

- `rdi` = memory address of the 1st quad word
- `rsi` = `n` (amount to loop for)
- `rax` = average computed

```asm
section .text
	global _start

_start:
	mov rbx, 1 ; i = 1
	mov rcx, qword [rdi]
.loop:

	cmp rbx, rsi
	ja .default
	
	add rcx, qword [rdi+rbx*8]
	inc rbx

	jmp .loop

.default:
	mov rax, rcx
	xor rdx, rdx
	div rsi
```

**flag:** `pwn.college{gGHJGwmbJOom2VO4-GA1lU_hobr.dNTMywyNwkzNyEzW}`

# 28. count-non-zero

Count the consecutive non-zero bytes in a contiguous region of memory, where:

- `rdi` = memory address of the 1st byte
- `rax` = number of consecutive non-zero bytes

Additionally, if `rdi = 0`, then set `rax = 0` (we will check)!

An example test-case, let:

- `rdi = 0x1000`
- `[0x1000] = 0x41`
- `[0x1001] = 0x42`
- `[0x1002] = 0x43`
- `[0x1003] = 0x00`

Then: `rax = 3` should be set.

```asm
section .text
	global _start
	
_start:
	mov rax, 0
	cmp rdi, 0 
	je .done
	
.check:
	cmp byte [rdi+rax], 0
	je .done
	inc rax
	jmp .check

.done:

```

**flag:** `pwn.college{4YfFYaFyEa239sa2AEvUSkEoOXw.dRTMywyNwkzNyEzW}`
# 29. string-lower 

Please implement the following logic:

```plaintext
str_lower(src_addr):
  i = 0
  if src_addr != 0:
    while [src_addr] != 0x00:
      if [src_addr] <= 0x5a:
        [src_addr] = foo([src_addr])
        i += 1
      src_addr += 1
  return i
```

`foo` is provided at `0x403000`. `foo` takes a single argument as a value and returns a value.

All functions (`foo` and `str_lower`) must follow the Linux amd64 calling convention (also known as System V AMD64 ABI): [System V AMD64 ABI](https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI)

Therefore, your function `str_lower` should look for `src_addr` in `rdi` and place the function return in `rax`.

An important note is that `src_addr` is an address in memory (where the string is located) and `[src_addr]` refers to the byte that exists at `src_addr`.

Therefore, the function `foo` accepts a byte as its first argument and returns a byte.

```asm
section .text
    global str_lower

str_lower:
    mov rcx, 0x0
    cmp rdi, 0x0
    je done
loop:
	mov rbx, rdi
	mov rax, 0x403000
	xor rdi, rdi
	mov dil, byte [rbx]
	cmp dil, 0x0
	je done
	cmp dil, 0x5a
	jg greater 
	inc rcx
	call rax
	mov byte [rbx], al

greater:
	mov rdi, rbx
	inc rdi
	jmp loop

done:
	mov rax, rcx
	ret 
```

**flag:** `pwn.college{UbwcToyuSFYq6Ckh5rXotFitDn5.dVTMywyNwkzNyEzW}`

# 30. most-common-byte 

Once again, please make function(s) that implement the following:

```plaintext
most_common_byte(src_addr, size):
  i = 0
  while i <= size-1:
    curr_byte = [src_addr + i]
    [stack_base - curr_byte * 2] += 1
    i += 1

  b = 0
  max_freq = 0
  max_freq_byte = 0
  while b <= 0xff:
    if [stack_base - b * 2] > max_freq:
      max_freq = [stack_base - b * 2]
      max_freq_byte = b
    b += 1

  return max_freq_byte
```

**Assumptions:**

- There will never be more than `0xffff` of any byte
- The size will never be longer than `0xffff`
- The list will have at least one element

**Constraints:**

- You must put the "counting list" on the stack
- You must restore the stack like in a normal function
- You cannot modify the data at `src_addr`

```asm
section .text
        global common_byte

common_byte:
        mov rbp, rsp
        sub rsp, 0x100
        xor r10, r10

loop1:
        cmp r10, rsi
        jg assign_freq
        mov dl, byte [rdi+r10]
        add byte [rsp+rdx], 1
        inc r10
        jmp loop1

assign_freq:
        xor rax, rax
        xor rbx, rbx
        xor rcx, rcx
        jmp loop2

loop2:
        cmp rbx, 0xff
        jg done
        cmp [rsp+rbx], cl
        jg update
        inc rbx
        jmp loop2
update:
        mov cl, [rsp+rbx]
        mov rax, rbx
        inc rbx
        jmp loop2
done:
        mov rsp, rbp
        ret
```


**flag:** `pwn.college{0KLbtNqqE7fz6qleyytxW3BS_cW.dZTMywyNwkzNyEzW}`
