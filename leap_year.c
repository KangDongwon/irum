#include <stdio.h>
#include <stdbool.h>

int main()
{
    int year;

    printf("연도를 입력하세요..");
    scanf("%d", &year);

    if(year % 4 == && (year % 100 != 0 or year % 400 == 0))
    {
        printf("%d년은 윤년입니다.\n")
    }
    else
    {
        printf("%d년은 윤년이 아닙니다.\n")
    }
    return 0;
}
