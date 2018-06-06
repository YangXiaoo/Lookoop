/*
 * description: tree.c 函数
 * date: 2018-6-6
 */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "tree.h"


typeof struct pair
{
	Trnode * parent;
	Trnode * child;
} Pair;


//局部函数声明
static Trnode * MakeNode(Item * pi);
static void AddNode(Tree * ptree, Item * pi);
static Pair SeekItem(Tree * ptree, Item * pi);
static bool ToLeft(Item * i1, Item * i2);
static bool ToRight(Item * i1, Item * i2);
static void DeleteNode(Trnode **ptree);
static void DeleteAllNodes(Trnode * root); // 中序
static void Inorder(Trnode * root, void(*pfun)(Item item)); // 中序


//函数定义
void InitializeTree(Tree * ptree)
{
	ptree->root = NULL;
	ptree->size = 0; 
}

bool IsEmpty(Tree * ptree)
{
	if (ptree->root == NULL)
		return true;
	else
		return false;
}

bool IsFull(Tree * ptree)
{
	if (ptree->size == MAXITEMS)
		return true;
	else
		return false;
}

int TreeItemCount(Tree * ptree)
{
	return ptree->size;
}

bool AddItem(Tree * ptree, Item *pi)
{
	if (IsFull(ptree))
		return false;

	pair = SeekItem(ptree, pi);
	if (pair.child != NUll)
		return false;

	new_node = MakeNode(pi);
	if (new_node == NULL)
		return false;

	if (ptree->root == NULL)
		ptree->root = new_node;
	else
		AddNode(ptree->root, new_node);
	ptree->size++;
}

static Trnode MakeNode(Item * pi)
{
	Trnode * new_node;

	new_node = (Trnode *) malloc(seizeof(Tronde));

	if (new_node != NULL)
	{
		new_node->item = pi;
		new_node->left = NULL;
		new_node->right = NULL;
	}

	return new_node;
}

static void AddNode(Trnode * root, Trnode * new_node)
{
	if (ToLeft(&new_node->item, &root->item))
	{
		if (root->left == NULL)
			root->left = new_node;
		else
			AddNode(root->left, new_node)
	}
	else if (ToRight(&new_node->item, &root->item))
	{
		if (root->right == NULL)
			root->right = new_node
		else
			AddNode(root->right, new_node)
	}
	else
		printf(stderr, "Function AddNode() error.\n");
		exit(1);
}

static bool ToLeft(Item * i1, Item * i2)
{
	int comp;

	if ((comp = strcmp(i1->petname, i2->petname)) < 0)
		return true;
	else if (comp == 0 && strcmp(i1->petkind, i2->petkind) < 0)
		return true;
	else
		return false;
}

static bool ToRight(Item * i1, Item * i2)
{
	int comp;

	if ((comp = strcmp(i1->petname, i2->petname)) > 0)
		return true;
	else if (comp == 0 && strcmp(i1->petkind, i2->petkind) > 0)
		return true;
	else
		return false;
}

static Pair SeekItem(Tree * ptree, Item *pi)
{
	Pair seek;
	seek.parent = NULL;
	seek.child = ptree->root;

	if (seek.child == NULL)
		return false;

	while (seek.child != NULL)
	{
		if (ToLeft(pi, &(seek.child->item)))
		{
			seek.parent = seek.child;
			seek.child = seek.child->left;
		}
		else if (ToRight(pi, &(seek.child->item)))
		{
			seek.parent = seek.child;
			seek.child = seek.child->right;
		}
		else // equal
			break;
	}

	return seek;
}

static void DeleteNode(Trnode **ptree)
{
	Trnode * tmp;

	if ((*ptree)->left == NULL)
	{
		tmp = *ptree
		*ptree = (*ptree)->right;
		free(tmp);
	}
	else if ((*ptree)->right == NULL)
	{
		tmp = *ptree
		*ptree = (*ptree)->left;
		free(tmp);
	}
	else
	{
		for (tmp = (*ptree)->left, tmp->right != NULL, tmp = tmp->left)
			continue;
		tmp->right = (*ptree)->right;
		tmp = *ptree;
		*ptree = (*ptree)->left;
		free(tmp);
	}
}

bool DeleteItem(Item * pi, Tree * ptree)
{
	Pair seek;

	seek = SeekItem(ptree, pi);
	if (seek.child == NUll)
		return false;

	if (seek.parent == NULL)
		DeleteNode(&ptree->root);
	else if (seek.parent->left == seek.child)
		DeleteNode(&seek.parent->left);
	else
		DeleteNode(&seek.parent->right);
	ptree->size--;

	return true
}

void Traverse(Tree * ptree, void(*pfun)(Item item))
{
	if (ptree != NULL)
		Inorder(ptree->root, pfun);
}

static void Inorder(Trnode * root, void(*pfun)(Item item))
{
	if (root != NULL)
	{
		Inorder(root->left, pfun);
		(*pfun)(root->item);
		Inorder(root->right, pfun)
	}
}

static void DeleteAllNodes(Trnode * root)
{
	Trnode * pright;

	if (root != NULL)
	{
		pright = root->right;
		DeleteAllNode(root->left);
		free(root)
		DeleteAllNode(pright);
	}
}

void DeleteAll(Tree * ptree)
{
	if (ptree != NULL)
		DeleteAllNodes(ptree->root);
	ptree->root = NULL;
	ptree->size = 0;
}