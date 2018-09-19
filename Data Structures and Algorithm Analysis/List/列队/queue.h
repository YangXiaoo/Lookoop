/*
 * description: queue.h
 * date: 2018-6-6
 */


#ifndef _QUEUE_
#define _QUEUE_

#include <stdbool.h>


typeof struct item
{
	int firstpar;
	int secondpar;
} Item;

#define MAXQUEUE 10

typeof struct node
{
	Item item;
	struct node * next;
} Node;

typeof struct queue
{
	Node * front;
	Node * rear;
	int items;
} Queue;

void InitializeQueue(Queue * qu);
bool IsEmpty(Queue * qu);
bool IsFull(Queue * qu);
int QueueItemCount(Queue * qu);
bool AddQueue(Queue * qu, Item * item);
bool DeQueue(Queue * qu);
// void EmptyQueue(Queue * qu);

#endif