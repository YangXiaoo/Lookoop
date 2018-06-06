/*
 * description: simple_list.c 简单链表
 * date: 2018-6-6
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 40


struct film
{
    char title[SIZE];
    int rating;
    struct film * next;
};
char * s_get(char * st, int n);


int main(void)
{
    struct film * head = NULL;
    struct film * prev, * current;
    char input[SIZE];

    puts("Enter movie title:");
    while (s_get(input, SIZE) != NULL && input[0] != 'q')
    {
        current = (struct film *) malloc(sizeof(struct film));
        if (head == NULL)
            head = current;
        else
            prev->next = current;

        current->next = NULL;
        strcpy(current->title, input);
        puts("Enter your rating[0-10]:");
        scanf("%d", &current->rating);
        while (getchar() != '\n')
            continue;
        puts("Enter next movie title(q to quit):");
        prev = current;
        //prev->next = NULL;
    }

    if (head == NULL)
        printf("No movie.\n");
    else
        printf("List:\n");

    current = head;
    while (current != NULL)
    {
        printf("Movie: %s   Rating: %d\n",current->title,current->rating);
        current = current->next;
    }

    current = head;
    while (current != NULL)
    {
        current = head;
        head = current->next;
        free(current);
    }

    printf("Bye\n");

    return 0;
}


char * s_get(char * st, int n)
{
    char * ret_val;
    char * find;

    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        find = strchr(st, '\n');
        if (find)
            *find = '\0';
        else
            while (getchar() != '\n')
                continue;
    }

    return ret_val;
}
