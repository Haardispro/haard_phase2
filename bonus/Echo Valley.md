The echo valley is a simple function that echoes back whatever you say to it.But how do you make it respond with something more interesting, like a flag?Download the source: [valley.c](https://challenge-files.picoctf.net/c_shape_facility/3540df5468ae2357d00a7a3e2d396e6522b24f7a363cbaff8badcb270d186bda/valley.c)Download the binary: [valley](https://challenge-files.picoctf.net/c_shape_facility/3540df5468ae2357d00a7a3e2d396e6522b24f7a363cbaff8badcb270d186bda/valley)

valley.c : 

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_flag() {
    char buf[32];
    FILE *file = fopen("/home/valley/flag.txt", "r");
    if (file == NULL) {
      perror("Failed to open flag file");
      exit(EXIT_FAILURE);
    }
    fgets(buf, sizeof(buf), file);
    printf("Congrats! Here is your flag: %s", buf);
    fclose(file);
    exit(EXIT_SUCCESS);
}

void echo_valley() {
    printf("Welcome to the Echo Valley, Try Shouting: \n");
    char buf[100];
    while(1)
    {
        fflush(stdout);
        if (fgets(buf, sizeof(buf), stdin) == NULL) {
          printf("\nEOF detected. Exiting...\n");
          exit(0);
        }
        if (strcmp(buf, "exit\n") == 0) {
            printf("The Valley Disappears\n");
            break;
        }
        printf("You heard in the distance: ");
        printf(buf);
        fflush(stdout);
    }
    fflush(stdout);
}

int main()
{
    echo_valley();
    return 0;
}
```

