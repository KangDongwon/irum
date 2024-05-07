#include <stdio.h>
#include <stdbool.h>

int main()
{
    int a, b, c, score = 0;

    printf("주사위 3개 숫자를 입력하세요..");
    scanf("%d %d %d", &a, &b, &c);

    if(a==b && b==c)
    {
        score = 10000 + a*1000;
    }
    else if(a==b || a==c)
    {
        score = 1000 + a*100;
    }
    else if(b==c)
    {
        score = 1000 + b*100;
    }
    else
    {
        if(a>b && a>c)
        {
            score = a * 100;
        }
        else if(b>a && b>c)
        {
            score = b * 100;
        }
        else
        {
            score = c * 100;
        }
    }

    printf("점수는 %d 점입니다.\n", score);

    return 0;
}
