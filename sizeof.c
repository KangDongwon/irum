#include <stdio.h>

int main()
{

    printf("short : %d byte\n", sizeof(short));
    printf("unsigned short : %d byte\n", sizeof(unsigned short));
    printf("int : %d byte\n", sizeof(int));
    printf("unsigned int : %d byte\n", sizeof(unsigned int));

    printf("float : %d byte\n", sizeof(float));
    printf("double : %d byte\n", sizeof(double));

    printf("char : %d byte\n", sizeof(char));

    printf("long : %d byte\n", sizeof(long));
    printf("unsigned long : %d byte\n", sizeof(unsigned long));

    printf("long long : %d byte\n", sizeof(long long));
    printf("unsigned long long : %d byte\n", sizeof(unsigned long long));

    return 0;
}
