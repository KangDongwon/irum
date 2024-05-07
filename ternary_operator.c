#include <stdio.h>
#include <stdbool.h>

int main()
{
    int x = 5, y = 2, z = 4;
    int M;

    //M = (x>y? x:y) && (y>z? y:z) && (x>z? x:z);  // M = 1 출력
    //M = (x>y)? x:y && (y>z)? y:z && (x>z)? x:z;  // M = 3 출력
    //M = x>y? x:((y && y)>z? y:((z && x)>z? x:z)); // M = 3 출력

    M = x>y? (x>z? x:z) : (y>z? y:z); //정답 코드

    printf("%d\n", M);

    return 0;
}
