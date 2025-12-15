# musl 

```
➜  ~/Documents/recruitment/niteCTF/2025/musl file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./libc.so, not stripped
➜  ~/Documents/recruitment/niteCTF/2025/musl checksec --file=chall
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Full RELRO      Canary found      NX enabled    No PIE          No RPATH   RUNPATH     47 Symbols	  No	0		2		chall
```


This program contains a format string vulnerability 

it will only allow 13 `%` signs to be used, then it just return `No one can handle that much knowledge` 


If you choose a name of 32 bytes, then it will allow you to leave a message. 

That message is then printed out using `printf(buf)` , this is the vulnerability. 

# Quick Mistake

attacker IP = `192.0.2.66`

`nite{192.0.2.66_2457ce19cb87e0eb_sslkeylog}`

IEEE Dancer: 
`nite{W4stem4n_dr41nss_aLLth3_fl04Ts_int0_ex3cut5bl3_sp4ce}`




