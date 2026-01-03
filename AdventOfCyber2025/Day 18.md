# Obfuscation - The egg shell file 

### Core Concepts:

- **Obfuscation:** a technique that makes data hard to read or analyze. It allows attackers to evade detection, delay analysis, and bypass simple keyword-based security tools.
- **ROT Ciphers:** a basic substitution method.
    - `ROT1`: Shifts each letter forward by 1.
    - `ROT13`: Shifts letters by 13 places.
- **XOR Obfuscation:** a technique where each byte of data is `XOR`'ed with a specific key, often used to hide malicious payloads.
- **CyberChef:** a useful tool recommended for decoding these basic obfuscation techniques.


**Q1) What is the first flag you get after deobfuscating the C2 URL and running the script?**

- `THM{C2_De0bfuscation_29838}`


**Q2) What is the second flag you get after obfuscating the API key and running the script again?**

- `THM{API_Obfusca4tion_ftw_0283}`





**Notes:** 

Deobfuscated base64 encoded C2 url 

Obfuscated API key by XORing it by 0x37 and converting to a hex string 




