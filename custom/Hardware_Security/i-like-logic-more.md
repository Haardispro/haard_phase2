# i-like-logic more 

**Description:** 
idk man, i feel like microsd cards are a thing of the past.

Provided with a `.sal` file.  

My first thought was to check what protocol does the SD card run on.  
On looking it up, I got to know, that it runs on SPI protocol. 

SPI -> Serial Peripheral Interface 

I opened the file using Saleae logic software to look at its structure. 

SPI signal has 4 channels: 
- MOSI -> Master Out Slave In
- MISO -> Master In Slave Out
- Enable -> (slave select or chip select line)
- Clock 

![[Pasted image 20251201200234.png]]



![](../assets/logic.png)

**flag:** `HTB{unp2073c73d_532141_p2070c015_0n_53cu23_d3v1c35}`