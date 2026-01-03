# Race Conditions - Toy to the World 

### Core Concepts:

- **Race Condition:** occurs when **two or more actions** run at the same time, and the result depends on which finishes first. This usually happens when the application lacks proper `synchronisation`.
- **TOCTOU:** **Time-of-Check to Time-of-Use**: a program checks something first and uses it later, but the data changes in between. This means what was true at the time of the check might no longer be true when the action happens.
- **Shared Resource Race:** occurs when multiple users or systems try to change the same data simultaneously without proper control; the final result often depends on which one finishes last.
- **Atomicity Violation:** happens when parts of a process run separately, allowing another request to sneak in between and cause inconsistent results.
- **Mechanism:** Race conditions explicitly exploit **timing** discrepancies in processing


**Q1)** **What is the flag value once the stocks are negative for SleighToy Limited Edition?**

- `THM{WINNER_OF_R@CE007}`


**Q2)** **Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)?**

- `THM{WINNER_OF_Bunny_R@ce}`
