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

void mat_mul(int a[][2], int b[][2])
{
    int i, j;

    int c[2][2];

    for(i=0; i<2; i++)
    {
        for(j=0; j<2; j++)
        {
            c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
            //printf("c[%d][%d] >> a[%d][%d] * b[%d][%d] + a[%d][%d] * b[%d][%d]\n", i, j, i,0, 0,j, i,1, 1,j);
        }
    }

    printf("두 행렬의 곱셈 결과\n");
    print_mat(c);
}

int main()
{
    int mat1[2][2] = { {1,2}, {3,4} };
    int mat2[2][2] = { {1,2}, {3,4} };
    int mat3[2][3] = { {1,2,3}, {4,5,6}, {7,8,9} };

    mat_equal(mat1, mat2);
    mat_add(mat1, mat2);
    mat_sub(mat1, mat2);
    mat_scalar(3, mat1);
    mat_mul(mat1, mat2);

    return 0;
}
