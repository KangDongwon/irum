#include <stdio.h>
#include <stdlib.h>

enum employ_type {
    part_time,
    full_time
};

struct student {
    char name[20];
    char subject[6][10];
    int tuition;
    int score;
};

struct professor {
    char name[20];
    char major[20];
    enum employ_type et;
    int pay;
};

union share {
    struct student s;
    struct professor p;
};

int main()
{
    union share sh;
    char c;

    c = 'p';
    sh.p.pay = 200000000;
    sh.p.et = full_time;
    strcpy(sh.p.name, "Professor X");
    strcpy(sh.p.major, "Computer Science");

    if(c == 'p')
    {
        printf("%s\n", sh.p.name);
        printf("%s\n", sh.p.major);
        printf("%d\n", sh.p.pay);
    }
    else if(c == 's')
    {
        printf("%s\n", sh.s.name);
        printf("%s\n", sh.s.subject[0]);
        printf("%d\n", sh.s.tuition);
        printf("%d\n", sh.s.score);
    }
    else
    {
        printf("union type error");
    }

    return 0;
}
