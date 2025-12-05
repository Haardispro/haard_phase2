# NineTails 

Description:

Looks like I got a little too clever and hid the flag as a password in Firefox, tucked away like one of NineTails’ many tails. Recover the "logins" and the "key4" and let it guide you to the flag.

Hint:
VI named my Ninetails "j4gjesg4", quite a peculiar name isn't it?





Passwords are stored in a hash  in `logins.json` and `key4.db` in firefox. 

On windows, these files can usually be found in 

We can crack these hashes to get the passwords for the logins, to get the flag. 

We are using a tool called `firefox_decrypt` to get the flag.  

```
(.venv) ➜  ~/Documents/recruitment/haard_phase2/forensics/NineTails/firefox_decrypt git:(main) ✗ python3 firefox_decrypt.py ../firefox_profile
2025-12-05 11:53:12,049 - WARNING - profile.ini not found in ../firefox_profile
2025-12-05 11:53:12,049 - WARNING - Continuing and assuming '../firefox_profile' is a profile location

Website:   https://www.rehack.xyz
Username: 'warlocksmurf'
Password: 'GCTF{m0zarella'

Website:   https://ctftime.org
Username: 'ilovecheese'
Password: 'CHEEEEEEEEEEEEEEEEEEEEEEEEEESE'

Website:   https://www.reddit.com
Username: 'bluelobster'
Password: '_f1ref0x_'

Website:   https://www.facebook.com
Username: 'flag'
Password: 'SIKE'

Website:   https://warlocksmurf.github.io
Username: 'Man I Love Forensics'
Password: 'p4ssw0rd}'
```








flag: `GCTF{m0zarella_f1ref0x_p4ssw0rd}`


