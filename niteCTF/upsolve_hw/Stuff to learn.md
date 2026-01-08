Side Channel Analysis
Timing Attacks 
Power traces 
fault injection 
power analysis 


# Side Channel Analysis 


## Timing Attacks 

Let us assume that the correct password is 5263987149, and the attacker starts guessing from the first digit (beginning from 0000000000). He measures that the system returns false after x seconds. After getting the same response time x for the first five guesses (i.e., from 0000000000 to 4000000000), he notices that the system takes a slightly longer time to respond ( x + ∆ x) when he tries 5000000000. This is because the for loop during its first iteration doesn’t return false since the first digit of the user input and the stored password is equal. Hence, the loop runs another iteration, thereby taking more time (∆x). Therefore, the attacker knows that the first digit he tried now is correct. He can repeat the same procedure to guess the remaining digits by observing the pattern of ∆x. In this way, it would take the attacker only 10^10 guesses at the maximum to find the correct password, compared to 10¹⁰ possible combinations while trying to brute force it…


Basically, we can calculate the amount of time it takes to return a function and using that return time, we can decipher the required contents. 



