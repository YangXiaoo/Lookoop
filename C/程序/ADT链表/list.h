/*
 * description: list.h
 * date: 2018-6-6
 */

#ifndef _LIST_H_
#define _LIST_H_
#include <stdbool.h>

#define SIZE 40


struct film
{
	char title[SIZE];
	int rating;
};

typeof struct film Item;

typeof struct node
{
	Item item;
	struct node * next;
} Node;

typeof Node * List;


void InitializeList(List * plist);
bool IsEmpty(List * plist);
bool IsFull(List * plist);
int ListItemCount(List *plist);
bool AddItem(List * plist, Item * item);
void Traverse(List * plist, void(*pfun)(Item item));
void EmptyList(List * plist);

#endif