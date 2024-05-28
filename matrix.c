#include <stdio.h>
#include <stdlib.h>

void print_mat(int a[][2])
{
    int i, j;

    for(i=0; i<2; i++)
    {
        for(j=0; j<2; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}

void mat_equal(int a[][2], int b[][2])
{
    int i, j;

    for(i=0; i<2; i++)
    {
        for(j=0; j<2; j++)
        {
            if(a[i][j] != b[i][j])
            {
                printf("두 행렬이 다릅니다.\n");
                return;
            }
        }
    }

    printf("두 행렬이 같습니다.\n");
}

void mat_add(int a[][2], int b[][2])
{
    int i, j;

    int c[2][2];

    for(i=0; i<2; i++)
    {
        for(j=0; j<2; j++)
        {
            c[i][j] = a[i][j] + b[i][j];
        }
    }

    printf("두 행렬의 덧셈 결과\n");
    print_mat(c);
}

void mat_sub(int a[][2], int b[][2])
{
    int i, j;

    int c[2][2];

    for(i=0; i<2; i++)
    {
        for(j=0; j<2; j++)
        {
            c[i][j] = a[i][j] - b[i][j];
        }
    }

    printf("두 행렬의 뺄셈 결과\n");
    print_mat(c);
}

void mat_scalar(int n, int a[][2])
{
    int i, j;

    int c[2][2];

    for(i=0; i<2; i++)
    {
        for(j=0; j<2; j++)
        {
            c[i][j] = a[i][j] * n;
        }
    }

    printf("행렬의 스칼라 %d 곱셈 결과\n", n);
    print_mat(c);
}

void mat_mul(int a[][3], int b[][4])
{
    int i, j, k;

    int c[2][4] = {0,};

    //c00 = a00*b00 + a01*b10 + a02*b20
    //c01 = a00*b01 + a01*b11 + a02*b21
    //c02 = a00*b02 + a01*b12 + a02*b22
    //c03 = a00*b03 + a01*b13 + a02*b23
    //c10 = a10*b00 + a11*b10 + a12*b20
    //c01 = a10*b01 + a11*b11 + a12*b21
    //c02 = a10*b02 + a11*b12 + a12*b22
    //c03 = a10*b03 + a11*b13 + a12*b23

    for(i=0; i<2; i++)
    {
        for(j=0; j<4; j++)
        {
            //c[i][j] = a[i][0]*b[0][j] + a[i][1]*b[1][j] + a[i][2]*b[2][j];
            for(k=0; k<3; k++)
            {
                c[i][j] = c[i][j] + a[i][k]*b[k][j];
            }
        }
    }

    printf("두 행렬의 곱셈 결과\n");
    for(i=0; i<2; i++)
    {
        for(j=0; j<4; j++)
        {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int mat1[2][2] = { {1,2}, {3,4} };
    int mat2[2][2] = { {1,2}, {3,4} };

    int a[2][3] = { {1,2,3},{4,5,6} };
    int b[3][4] = { {1,2,3,4}, {5,6,7,8}, {9,10,11,12} };

    mat_equal(mat1, mat2);
    mat_add(mat1, mat2);
    mat_sub(mat1, mat2);
    mat_scalar(3, mat1);

    mat_mul(a, b);

    return 0;
}
