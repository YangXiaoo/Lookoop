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