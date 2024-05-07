#include <stdio.h>
#include <stdbool.h>

int main()
{
    int score, value;

    printf("점수를 입력하세요..");
    scanf("%d", &score);

    value = score / 10;

    switch(value)
    {
    case 9:
        printf("%d점, A학점입니다.\n", score);
        break;
    case 8:
        printf("%d점, B학점입니다.\n", score);
        break;
    case 7:
        printf("%d점, C학점입니다.\n", score);
        break;
    case 6:
        printf("%d점, D학점입니다.\n", score);
        break;
    default:
        printf("%d점, F학점입니다.\n", score);
        break;
    }

    return 0;
}
