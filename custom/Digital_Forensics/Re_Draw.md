# Re: Draw 

Description: 

Her screen went black and a strange command window flickered to life, lines of text flashed across before everything went silent. Moments later, the system crashed. By sheer luck, we recovered a memory dump.

Note: There are three stages to this challenge and you will find three flags.

What we know: just before the crash, a black command window flickered across the screen, something in its output might still be visible if you dig through memory. She was drawing when it happened, and remnants of a painting program linger, which could reveal more if inspected in the right way. Finally, a mysterious archive hides deeper in memory, likely holding the last piece of her work.

Hint:
Learn up on volatility 2 and its various plugins and what they are used for.

```bash
> volatility --filename=MemoryDump_Lab1.raw imageinfo
> volatility --filename=MemoryDump_Lab1.raw pstree 
> volatility --filename=MemoryDump_Lab1.raw consoles # stage 1 
> volatility --filename=MemoryDump_Lab1.raw hivelist # to get /sam /security
> volatility --filename=MemoryDump_Lab1.raw hashdump # to get ntlm hash
```

```
Alissa Simpson:1003:aad3b435b51404eeaad3b435b51404ee:f4ff64c8baac57d22f22edc681055ba6:::

user:1001:
```

goodmorningindia

Stage 1: `flag{th1s_1s_th3_1st_st4g3!!}`
Stage 2: 
Stage 3: `flag{w3ll_3rd_stage_was_easy}`

