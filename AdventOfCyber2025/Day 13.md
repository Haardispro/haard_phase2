# YARA Rules - YARA mean one! 

```
ubuntu@tryhackme:~/Downloads/easter$ ls
easter1.jpg   easter21.jpg  easter33.jpg  easter45.jpg  easter57.jpg
easter10.jpg  easter22.jpg  easter34.jpg  easter46.jpg  easter58.jpg
easter11.jpg  easter23.jpg  easter35.jpg  easter47.jpg  easter59.jpg
easter12.jpg  easter24.jpg  easter36.jpg  easter48.jpg  easter6.jpg
easter13.jpg  easter25.jpg  easter37.jpg  easter49.jpg  easter60.jpg
easter14.jpg  easter26.jpg  easter38.jpg  easter5.jpg   easter7.jpg
easter15.jpg  easter27.jpg  easter39.jpg  easter50.jpg  easter8.jpg
easter16.jpg  easter28.jpg  easter4.jpg   easter51.jpg  easter9.jpg
easter17.jpg  easter29.jpg  easter40.jpg  easter52.jpg  embeds
easter18.jpg  easter3.jpg   easter41.jpg  easter53.jpg
easter19.jpg  easter30.jpg  easter42.jpg  easter54.jpg
easter2.jpg   easter31.jpg  easter43.jpg  easter55.jpg
easter20.jpg  easter32.jpg  easter44.jpg  easter56.jpg
ubuntu@tryhackme:~/Downloads/easter$ cat embeds 
import glob, random

seed = 42
phrase = "Find me in HopSec Island"
words  = phrase.split()
images = sorted(glob.glob("easter*.jpg"))

random.seed(seed)
chosen = random.sample(images, len(words))   # 5 distinct random images
chosen.sort()                                # keep word order increasing by filename

for img, word in zip(chosen, words):
    with open(img, "ab") as f:
        f.write(f"\nTBFC:{word}\n".encode())
    print(f"{img}  <-  TBFC:{word}")

ubuntu@tryhackme:~/Downloads/easter$ python3 embeds
easter10.jpg  <-  TBFC:Find
easter16.jpg  <-  TBFC:me
easter25.jpg  <-  TBFC:in
easter46.jpg  <-  TBFC:HopSec
easter52.jpg  <-  TBFC:Island

```

**Q1) How many images contain the string TBFC?**

- `5`


**Q2) What regex would you use to match a string that begins with `TBFC:` followed by one or more alphanumeric ASCII characters?**

- `/TBFC:[A-Za-z0-9]+/`


**Q3) What is the message sent by McSkidy?**

- `Find me in HopSec Island`



