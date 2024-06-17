#include <stdio.h>
#include <time.h>

int check_dupl(int arr[], int size, int n)
{
    int i;
    for(i=0; i<size; i++)
    {
        if(arr[i] == n)
            return 1;
    }
    return 0;
}

void make_rand(int arr[], int size)
{
    int n, i=0;

    while(1)
    {
        n = rand() % 45 + 1;
        if(check_dupl(arr, size, n) == 1) //이미 들어있는 값이면 다시
            continue;

        arr[i] = n;
        i++;

        if(arr[size-1] != 0) //배열의 마지막 값까지 채워졌으면 중지
            break;
    }
}

void selection_sort(int arr[], int size)
{
    int i,j,min,temp;

    for(i=0; i<size-1; i++)
    {
        min = i;
        for(j=i+1; j<size; j++)
        {
            if(arr[min] > arr[j])
            {
                min = j;
            }
        }
        temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}

int main()
{
    srand(time(NULL));

    int i;
    int arr[7] = {0};

    make_rand(arr, 7); //배열과 배열의 크기를 함수로 넘겨줌

    selection_sort(arr, 6); //마지막 번호는 보너스 번호, 보너스 번호는 정렬 제외라 사이즈를 1줄여서 넘겨줌

    for(i=0; i<6; i++) //보너스 번호 전까지 출력
    {
        printf("%d ", arr[i]);
    }
    printf("bonus : %d", arr[6]); //보너스 번호는 따로 출력

    return 0;
}
