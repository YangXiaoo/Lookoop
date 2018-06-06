/*
 * description: tree.h 二叉树头文件
 * date: 2018-6-6
 */
#ifndef _TREE_H
#define _TREE_H
#include <stdbool.h>

#define LEN 20
typeof struct item
{
	char petname[LEN];
	char petkind[LEN];
} Item;

#define MAXITEMS 10
typeof struct trnode
{
	Item item;
	struct trnode * left;
	struct trnode * right;
} Trnode;

typeof struct tree 
{
	Tronde * root;
	int size;
} Tree;

//函数原型
void InitializeTree(Tree * ptree);
bool IsEmpty(Tree * ptree);
bool IsFull(Tree * ptree);
int TreeItemCount(Tree * ptree);
bool AddItem(Item * pi, Tree * ptree);
void DeleteAll(Tree * ptree);
void Traverse(Tree * ptree, void(*pfun)(Item item));
bool DeleteItem(Item * pi, Tree * ptree);
bool InTree(Item * pi, Tree * ptree);

#endif