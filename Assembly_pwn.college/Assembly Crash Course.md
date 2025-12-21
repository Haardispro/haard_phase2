# Computer Architecture 

Source  Code -> Intermediate Language Bytecode -> Binary-encoded instructions

C/C++ -> compiler -> CPU 

![[Pasted image 20251219122751.png]]

Decoder, Multiplexer, Adder 

CPU -> Registers, Computing Unit, Arithmetic and Logical Unit and Cache 

![[Pasted image 20251219124340.png]]

Von Neumann Architecture 

---
# Assembly 

Text representation of binary is called Assembly. The binary and the assembly code is *equivalent*. 

Assembly is named "Assembly" because it is *assembled* (not compiled) into binary code. 

Assembly tells the CPU what to do. 

English equivalent: 
Sentence -> Instruction
Verb -> Operation
Noun -> Operand 

#### Nouns/Operands 

The types of operands we deal with is data. 

CPU is concerned with three types of data: 
- Data we directly give it as part of the instruction
- Data that is close at hand 
- Data in storage 

#### Verbs/Operations 

What to do with the data: 
- add
- sub
- mul
- div
- mov
- cmp
- test 

#### Assembly Dialects

- x86
- arm
- ppc
- mips 
- risc-v
- pdp-11

x86 Assembly -> AT&T syntax and Intel syntax 

Intel syntax better 

---

# Data 

Expressing Numbers: Binary, Hex, Octal, Decimal 

Expressing Text: ASCII, UTF-8 

Expressing Negative Numbers -> 2's Complement 

![[Pasted image 20251219143029.png]]

---

# Registers 

Registers are very fast, temporary stores for data 

You get several "general purpose" registers: 
- `x86`: `eax`, `ecx`, `edx`, `ebx`, `esp`, `ebp`, `esi`, `edi`
- `amd64`: `rax`, `rcx`, `rdx`, `rbx`, `rsp`, `rbp`, `rsi`, `rdi`, `r8`, `r9`,`r10`,`r11`,`r12`,`r13`, `r14`, `r15`

The address of the next instruction is in a register: 

`eip(x86)`, `rip(amd64)`, `r15(arm)`

Register size: Registers are (typically) the same size as the word width of the architecture. 

#### Setting registers 

```asm
mov rax, 0x539
mov rbx, 1337
mov <destination>, <source>
```


