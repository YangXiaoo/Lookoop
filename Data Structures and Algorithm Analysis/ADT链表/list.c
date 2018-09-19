/*
 * description: list.c ADT链表
 * date: 2018-6-6
 */

#include <stdio.h>
#include <stdlib.h>
#include "list.h"

/*
 * List movies;	// &movies 表示指向List指针的地址, *(&movies) 表示指向List的指针
 * Item temp;
 * InitializeList(&movies)
 * AddItem(temp, &movies)
 * ...
 */


void InitializeList(List * plist)
{
	*plist = NULL;
}

bool IsEmpty(List * plist)
{
	if (*plist == NULL)
		return true;
	else
		return false;
}

bool IsFull(List * plist)
{
	Node *pnew;

	pnew = (Node *) malloc(seizeof(Node))
	if (pnew == NULL)
		return true;
	else
		return false;

	free(pnew);
}

int ListItemCount(List *plist)
{
	Node *pnode = *plist;
	int count = 0;

	while (pnode != NULL)
	{
		count++;
		pnode = pnode->next;
	}

	return count;
}

bool AddItem(List * plist, Item * item)
{
	Node * pnew;
	Node * seek = *plist;

	pnew = (Node *) malloc(sizeof(Node));
	if (pnew == NULL)
		return false;

	pnew->item = item;
	pnew->next = NULL;
	if (seek == NULL)
		*plist = pnew;
	else
	{
		while (seek->next != NULL)
			seek = seek->next;
		seek->next = pnew;
	}

	return true;
}

void Traverse(List * plist, void(*pfun)(Item item))
{
	Node * pt = *plist;

	while (pt != NULL)
	{
		(*pfun)(pt->item);
		pt = pt->next;
	}
}

void EmptyList(List * plist)
{
	Node * pn;

	while (*plist != NULL)
	{
		pn = (*plist)->next;
		free(*plist);
		*plist = pn;
	}
}