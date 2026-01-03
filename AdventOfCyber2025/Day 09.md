# Passwords - A Cracking Christmas 

Cracked passwords using wordlists. 

```
ubuntu@tryhackme:~/Desktop$ pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
PDF version 1.7
Security Handler: Standard
V: 2
R: 3
P: -1060
Length: 128
Encrypted Metadata: True
FileID: 3792b9a3671ef54bbfef57c6fe61ce5d
U: c46529c06b0ee2bab7338e9448d37c3200000000000000000000000000000000
O: 95d0ad7c11b1e7b3804b18a082dda96b4670584d0044ded849950243a8a367ff
found user-password: 'naughtylist'

ubuntu@tryhackme:~/Desktop$ xreader flag.pdf
xreader: command not found
ubuntu@tryhackme:~/Desktop$ zip2john flag.zip > ziphash.txt
ubuntu@tryhackme:~/Desktop$ john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Cost 1 (HMAC size [KiB]) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
winter4ever      (flag.zip/flag.txt)
1g 0:00:00:00 DONE (2025-12-11 07:33) 3.704g/s 15170p/s 15170c/s 15170C/s friend..sahara
Use the "--show" option to display all of the cracked passwords reliably
Session completed

ubuntu@tryhackme:~/Desktop$ cat ziphash.txt
flag.zip/flag.txt:$zip2$*0*3*0*db58d2418c954f6d78aefc894faebf54*d89c*1d*b8370111f4d9eba3ca5ff6924f8c4ff8636055dce00daec2679f57bde1*57445596ac0bc2a29297*$/zip2$:flag.txt:flag.zip:flag.zip

ubuntu@tryhackme:~/Desktop$ unzip flag.zip
Archive:  flag.zip
   skipping: flag.txt                unsupported compression method 99
ubuntu@tryhackme:~/Desktop$ cat flag.txt
THM{Cr4ck1n6_z1p$_1s_34$yyyy}
```

**flag:** `THM{Cr4ck1n6_z1p$_1s_34$yyyy}`


