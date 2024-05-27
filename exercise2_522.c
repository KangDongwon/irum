#include <stdio.h>
#include <stdlib.h>

int a[3];

int cal_sum()
{
    int i, ret = 0;
    for(i=0; i<3; i++)
        ret += a[i];

    return ret;
}

void cal_avg(int sum)
{
    printf("avg is %f\n", sum/3.0f);
}

void sort()
{
    int i, j, temp;
    for(i=0; i<3; i++)
    {
        for(j=i+1; j<3; j++)
        {
            if(a[i] > a[j])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}

int cal_center()
{
    sort();
    return a[1];
}

int main()
{
    int sum, center;

    printf("enter three num ... \n");
    scanf("%d %d %d", &a[0], &a[1], &a[2]);

    sum = cal_sum();
    printf("sum is %d\n", sum);

    cal_avg(sum);

    center = cal_center();
    printf("center is %d\n", center);
}
