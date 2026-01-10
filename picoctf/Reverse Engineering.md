# GDB Baby Step 1 

Description:
Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

GDB -> GNU Debugger 

In this challenge I was given a file called `debugger0_a`. 

I found which type of file it was using the `file` command. 

In order to find the `eax` register, I had to first look at the Assembly code of the file. 
I found out using the Internet, that I had to use the built in Linux tool called `gdb` to disassemble the code to return a dump of the assembler code for the function `main`. 

The commands I used for the same are as follows:

```bash
chmod +x debugger0_a # Could not disassemble without root permissions

gdb debugger0_a
```

`gdb` commands:
```text
(gdb) disassemble main 
```

This is how the Assembler code for the function `main` looked like:
![GDB](assets/GDB.png)

On further inspection, I could clearly see what the register `eax` in the `main` function contained. 

This is what it contained: 
`$0x86342`

On converting `0x86342` to decimal, I got `549698`, which was the answer for the given challenge. 

Final answer: `picoCTF{549698}`

---
# ARMssembly 1 

Description: 
For what argument does this program print `win` with variables `83`, `0` and `3`? File: [chall_1.S](https:;mercury.picoctf.net/static/b4fd1dabc9dec63c37180b5b05783b55/chall_1.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

Command required to compile ARM Assembly on x86  

```
aarch64-linux-gnu-gcc -o chall_1 chall_1.S 
qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_1 <argument_in_integer>
```

Initial tests: 
```
> qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_1 21
You Lose :( 
```

We are provided with a file called chall_1.S, lets trace the ARM assembly program to check what it does. 

```assembly
	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32      ; sp=sp-32  ; sp = stack pointer, allocate 32 bytes on the stack  
	str	w0, [sp, 12]     ; store register w0 at mem location sp+12, which is the user input 
	mov	w0, 83           ; move 83 in w0 register, w0 = 83 
	str	w0, [sp, 16]     ; store value of w0 in sp+16, sp+16 = 83 
	str	wzr, [sp, 20]    ; store value of wzr in sp+20, sp+20 = 0 ; wzr is a zero register
	mov	w0, 3            ; move 3 in w0 register, w0 = 3
	str	w0, [sp, 24]     ; store value of w0 in sp+24, sp+24 = 3
	ldr	w0, [sp, 20]     ; load from mem addr sp+20 to register w0, w0 = 0
	ldr	w1, [sp, 16]     ; load from mem addr sp+16 to register w1, w1 = 83
	lsl	w0, w1, w0       ; logical shift left, w0 = w1 << w0 => w0=83<<0=83
	str	w0, [sp, 28]     ; store w0 at sp+28, sp+28 = w0 = 83
	ldr	w1, [sp, 28]     ; load from mem addr sp+28 to register w1, w1=83
	ldr	w0, [sp, 24]     ; load from mem addr sp+24 to register w0, w0=3
	sdiv	w0, w1, w0   ; signed division, w0 = w1 / w0 => w0 = 83/3 = 27 (integer division)
	str	w0, [sp, 28]     ; sp+28 = w0 = 27
	ldr	w1, [sp, 28]     ; load from mem addr sp+28 to register w1, w1=27
	ldr	w0, [sp, 12]     ; w0 = sp+12, w0 = input 
	sub	w0, w1, w0       ; w0 = w1 - input = 27 - input 
	str	w0, [sp, 28]     ; sp+28 = w0 
	ldr	w0, [sp, 28]     ; load from mem addr sp+28 to register w0 
	add	sp, sp, 32       ; sp=sp+32, free 32 allocated bytes  
	ret                  ; return w0, which is 27 - input  
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]    ; w0 = x29+44
	bl	func             ; branch with link instruction, used for function calls, links w0 of func to w0 of main 
	cmp	w0, 0            ; compare w0 with 0, if 27-input = 0, then run .LC0
	bne	.L4              ; branch not equal to, run if 27-input not 0  
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits

```

Now, we can conclude that, we need to input 27 as an argument to make the `w0` register 0 and return You Win. 

```
> qemu-aarch64 -L /usr/aarch64-linux-gnu ./chall_1 27
You win!
```

Converting 27 to hex, we get 1B

flag: `picoCTF{0000001B}`

Reference: 
https://developer.arm.com/documentation/107829/0201/Assembly-language-basics

---
# Vault Door 3

Description: 
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https:;jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)

VaultDoor3.java: 
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}

```

This is what the above mentioned program does: 
- takes in user input and runs that input through a function called `checkPassword`. 
- this function runs a bunch of for loops on the string and scrambles it. 
- if the scrambled string is equals to `jU5t_a_sna_3lpm18gb41_u_4_mfr340`, then the password is correct, otherwise it says Access Denied. 

I wrote a python script which just reverses what the for loops did. 
this is what the for loops did: 
- from char `0-8` -> as it is
- from char `8-16` -> reverses its order 
- from char `16-32` -> reverses order every 2nd step
- from char `31-17` -> as it is 

solve.py
```python
buff = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"

password = []


for i in range(32):
    password.append("")

for i in range(0, 8):
    password.insert(i, buff[i])
    print(i)

for i in range(8, 16):
    password.insert(i, buff[23-i]) 
    print(23-i)


for i in range(16, 32, 2):
    password.insert(i, buff[46-i])
    print(46-i)
for i in range(31, 16, -2):
    password.insert(i, buff[i])
    print(i)

print(password)

x = "".join(password)

print(x)

```

output: 
```text
0
1
2
3
4
5
6
7
15
14
13
12
11
10
9
8
30
28
26
24
22
20
18
16
31
29
27
25
23
21
19
17
['j', 'U', '5', 't', '_', 'a', '_', 's', '1', 'm', 'p', 'l', '3', '_', 'a', 'n', '4', 'g', '', 'r', '4', '', 'm', '_', '', '4', '_', '', 'u', '_', '', '1', 'f', '', 'b'
, '3', '', '8', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jU5t_a_s1mpl3_an4gr4m_4_u_1fb380
```

flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}`



