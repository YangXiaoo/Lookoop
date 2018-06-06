/*
 * description: queue.c 函数
 * date: 2018-6-6
 */

#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

void InitializeQueue(Queue * qu)
{
	qu->front = NULL;
	qu->rear = NULL;
	qu->items = 0;
}

bool IsEmpty(Queue * qu)
{
	if (qu->items == 0)
		return true;
	else
		return false;

	// return qu->items == 0
}

bool IsFull(Queue * qu)
{
	return qu->items == MAXQUEUE;
}

int QueueItemCount(Queue * qu)
{
	return qu->items;
}

bool AddQueue(Queue * qu, Item * item)
{
	Queue * pnew;

	if (IsFull(qu))
		return false;

	pnew = (Node *) malloc(sizeof(Node));
	if (pnew == NULL)
		return false;

	pnew->item = item;
	pnew->next = NULL;
	if (qu->front == NULL)
		qu->front = pnew
	else
		qu->rear->next = pnew;

	qu->rear = pnew;
	qu->items++;

	return true;
}

bool DeQueue(Queue * qu)
{
	Node *pt;

	if (IsEmpty(qu))
		return false;
	// *pi = qu->front->item;
	pt = qu->front;
	qu->front = qu->front->next;
	free(pt)
	qu->items--;
	if (qu->items == 0)
		qu->rear = NULL;

	return true;
}
