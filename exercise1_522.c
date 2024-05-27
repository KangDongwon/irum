#include <stdio.h>

int i = 0;

int add(int x, int y)
{
    return x+y;
}

int sub(int x, int y)
{
    return x-y;
}

int mul(int x, int y)
{
    return x*y;
}

float div(int x, int y)
{
    return (float)x/(float)y;
}

void print_result(char c, int x, int y, int ret)
{
    printf("%d %c %d = %d\n", x, c, y, ret);
}

void print_result_f(char c, int x, int y, float ret)
{
    printf("%d %c %d = %f\n", x, c, y, ret);
}


void main()
{
    int x, y, ret;
    float f_ret;
    char c;

    printf("enter operator: ");
    scanf("%c", &c);

    printf("enter two number : ");
    scanf("%d %d", &x, &y);

    switch(c)
    {
    case '+':
        ret = add(x,y);
        print_result(c, x, y, ret);
        break;
    case '-':
        ret = sub(x,y);
        print_result(c, x, y, ret);
        break;
    case '*':
        ret = mul(x,y);
        print_result(c, x, y, ret);
        break;
    case '/':
        f_ret = div(x,y);
        print_result_f(c, x, y, f_ret);
        break;
    default:
        break;
    }

}
