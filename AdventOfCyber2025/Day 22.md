# C2 Detection - Command & Carol 

  
## Task 1 : Introduction

#### Learning Objectives

-  Convert a PCAP to Zeek logs
-  Use RITA to analyze Zeek logs
-  Analyze the output of RITA
## Task 2 : Detecting C2 with RITA

#### The Magic of RITA

 **Real Intelligence Threat Analytics (RITA)** is an open-source framework created by Active Countermeasures. Its core functionality is to detect command and control (C2) communication by analyzing network traffic captures and logs. Its primary features are:

-  C2 beacon detection
-  DNS tunneling detection
-  Long connection detection
-  Data exfiltration detection
-  Checking threat intel feeds
-  Score connections by severity
-  Show the number of hosts communicating with a specific external IP
-  Shows the datetime when the external host was first seen on the network
 The magic behind RITA is its analytics. It correlates several captured fields, including IP addresses, ports, timestamps, and connection durations, among others. Based on the normalized and correlated dataset, RITA runs several analysis modules collecting information like:

-  Periodic connection intervals
- Excessive number of DNS queries
- Long FQDN
- Random subdomains
- Volume of data over time over HTTPS, DNS, or non-standard ports
- Self-signed or short-lived certificates
- Known malicious IPs by cross-referencing with public threat intel feeds or blocklists

RITA only accepts network traffic input as **Zeek** logs. **Zeek** is an open-source network security monitoring (NSM) tool. **Zeek** is not a firewall or IPS/IDS; it does not use signatures or specific rules to take an action. It simply observes network traffic via configured SPAN ports (used to copy traffic from one port to another for monitoring), physical network taps, or imported packet captures in the PCAP format. **Zeek** then analyzes and converts this input into a structured, enriched output. This output can be used in incident detection and response, as well as threat hunting. Out of the box, **Zeek** covers two of the four types of NSM data: transaction data (summarized records of application-layer transactions) and extracted content data (files or artifacts extracted, such as executables).

 Github Link : [https://github.com/activecm/rita](https://github.com/activecm/rita)**
#### Answer the questions below

Q1) How many hosts are communicating with **[malhare.net](http://malhare.net/)**?

 A1) `6`

 Q2) Which Threat Modifier tells us the number of hosts communicating to a certain destination?

 A2)`prevalence`

 Q3) What is the highest number of connections to **[rabbithole.malhare.net](http://rabbithole.malhare.net/)**?

 A3)`40`

 Q4) Which search filter would you use to search for all entries that communicate to **[rabbithole.malhare.net](http://rabbithole.malhare.net/)** with a **beacon score** greater than 70% and sorted by **connection duration (descending)**? 
 
 A4) `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc`

 Q5) Which port did the host 10.0.0.13 use to connect to **[rabbithole.malhare.net](http://rabbithole.malhare.net/)**?

 A5) `80`