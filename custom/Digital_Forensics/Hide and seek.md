# Hide and seek 

**Description:**

Sakamoto’s at it again with a game of hide and seek, but this time, it’s not with Shin or his daughter. An old friend hid some secret data in this image. Can you find it before the others do?
Hint:
Even in retirement, Sakamoto never loses at hide and seek. Maybe stegseek can help you keep up.


Was provided with a file called `sakamoto.jpg` 

![](../assets/sakamoto.jpg)

According to the hint, I installed `stegseek` on my system, and looked at its manual. 
```
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek


=== StegSeek Help ===
To crack a stegofile:
stegseek [stegofile.jpg] [wordlist.txt]

Commands:
 --crack                 Crack a stego file using a wordlist. This is the default mode.
 --seed                  Crack a stego file by attempting all embedding patterns.
                         This mode can be used to detect a file encoded by steghide.
                         In case the file was encoded without encryption, this mode will
                         even recover the embedded file.
Positional arguments:
 --crack [stegofile.jpg] [wordlist.txt] [output.txt]
 --seed  [stegofile.jpg] [output.txt]

Keyword arguments:
 -sf, --stegofile        select stego file
 -wl, --wordlist         select the wordlist file
 -xf, --extractfile      select file name for extracted data
 -t, --threads           set the number of threads. Defaults to the number of cores.
 -f, --force             overwrite existing files
 -v, --verbose           display detailed information
 -q, --quiet             hide performance metrics (can improve performance)
 -s, --skipdefault       don't add guesses to the wordlist (empty password, filename, ...)
 -n, --nocolor           disable colors in output
 -c, --continue          continue cracking after a result has been found.
                         (A stego file might contain multiple embedded files)
 -a, --accessible        simplify the output to be more screen reader friendly

Use "stegseek --help -v" to include steghide's help.
```

Stegseek is basically a steganography extractor, which uses wordlists to crack the password of a steg file. 

I had `rockyou.txt` already downloaded on my system, so I used that to crack the password. 

Command used: 
```
> stegseek -sf sakamoto.jpg -wl /usr/share/wordlists/rockyou.txt
```

```
➜  ~/Documents/recruitment/haard_phase2/custom/assets git:(main) ✗ stegseek  -sf sakamoto.jpg -wl /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "iloveyou1"
[i] Original filename: "flag.txt".
[i] Extracting to "sakamoto.jpg.out".

➜  ~/Documents/recruitment/haard_phase2/custom/assets git:(main) ✗ cat sakamoto.jpg.out
nite{h1d3_4nd_s33k_but_w1th_st3g_sdfu9s8}
```

**flag:** `nite{h1d3_4nd_s33k_but_w1th_st3g_sdfu9s8}`


