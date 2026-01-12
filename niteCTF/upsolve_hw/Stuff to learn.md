Side Channel Analysis
Timing Attacks 
Power traces 
fault injection 
power analysis 

http://wiki.newae.com/CHES2016_CTF
https://eshard.com/posts/pico-ctf-power-analysis-challenges



Binex: 

Learn what each of these terms mean:

```
ELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   36 Symbols	  No	0		1		main
```


# ELF Sections

- `.text` ->	where code live, as said above. objdump -drS .process.o will show you that
- `.data` -> where global tables, variables, etc. live. objdump -s -j .data .process.o will hexdump it.
- `.bss` -> don't look for bits of .bss in your file: there's none. That's where your uninitialized arrays and variable are, and the loader 'knows' they should be filled with zeroes ... there's no point storing more zeroes on your disk than there already are, is it?
- `.rodata`	that's where your strings go, usually the things you forgot when linking and that cause your kernel not to work. objdump -s -j .rodata .process.o will hexdump it. Note that depending on the compiler, you may have more sections like this.
- `.comment & .note` -> just comments put there by the compiler/linker toolchain
- `.stab & .stabstr` -> debugging symbols & similar information.




# Side Channel Analysis 


## Timing Attacks 

Let us assume that the correct password is 5263987149, and the attacker starts guessing from the first digit (beginning from 0000000000). He measures that the system returns false after x seconds. After getting the same response time x for the first five guesses (i.e., from 0000000000 to 4000000000), he notices that the system takes a slightly longer time to respond ( x + ∆ x) when he tries 5000000000. This is because the for loop during its first iteration doesn’t return false since the first digit of the user input and the stored password is equal. Hence, the loop runs another iteration, thereby taking more time (∆x). Therefore, the attacker knows that the first digit he tried now is correct. He can repeat the same procedure to guess the remaining digits by observing the pattern of ∆x. In this way, it would take the attacker only 10^10 guesses at the maximum to find the correct password, compared to 10¹⁰ possible combinations while trying to brute force it…


Basically, we can calculate the amount of time it takes to return a function and using that return time, we can decipher the required contents. 



# Correlation Power Analysis (CPA)


http://wiki.newae.com/Correlation_Power_Analysis

# Timing Analysis 



---


Explain ROP

what does ret gadget do? 

SPI/CAN/I2C/UART protocol identification 

READ AOC 

Why is the last gate XOR 

Explain NPN transistor 

what is Buffer overflow ?


Format String 

nite CTF writeups 

what is shift-key ? 

what is a .ctf32 file? 

what is encoding and modulation ? 

Why is the last gate XOR? 


