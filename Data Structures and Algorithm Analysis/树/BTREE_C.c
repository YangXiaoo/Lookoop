#ifndef _BTREE_H 
#define _BTREE_H
 
#define MINDEGREE 3 // 定义BTree的最小度
#define MAXDEGREE (MINDEGREE*2)
 
// 定义BTree的数据结构
typedef void* NodeData;
 
typedef struct _targBTreeNode
{
	NodeData	data; // 
	_targBTreeNode*	cs[MAXDEGREE]; //孩子指针数组
	int	keys[MAXDEGREE-1]; //关键字数组
	int count; // 关键字个数
	int is_leaf; // 是否为叶子结点
} BTreeNode, *BTree;
 
#define BTREE_SIZE sizeof(BTreeNode)
 
void alloc_tree(BTree &tree); //分配内存 
void insert_keys_to_tree(BTree &tree, int keys[], int n); //将keys插入至tree中
void insert_key_to_tree(BTree &tree, int key); // 将key插入至根树tree中
void insert_key_to_unfull_tree(BTree &tree, int key); // 将key关键字插入至未满子树tree中 
void break_tree_child(BTree &tree, BTree &child, int i); // 将tree的第i个子孩子分裂
void disk_read(const BTree tree); // 代表读磁盘，未实现
void disk_write(const BTree tree); // 代表写磁盘，未实现
void display_tree(const BTree tree); // 显示BTree
int search_tree(const BTree tree, int key); // 搜索BTree中是否存在关键字
void delete_tree(BTree &tree, int key); // 删除BTree中的某一关键字，主要处理BTree为空的两种情况~
void delete_unless_tree(BTree &tree, int key); // 删除BTree中的某一子树~
int pre_succor_tree(const BTree tree, int i); // 找tree中第i位关键字的前驱~
int after_succor_tree(const BTree tree, int i); // 找Btree中第i位关键字的后继~
 
#endif




#include "BTree.h"
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <assert.h>
 
void alloc_tree(BTree &tree)
{
	if(0 == (tree = (BTree) malloc (BTREE_SIZE)))
	{
		exit(-1);
	}
	memset(tree, 0, BTREE_SIZE);
	tree->is_leaf = 1;
}
 
void insert_keys_to_tree(BTree &tree, int keys[], int n)
{
	for(int i = 0; i < n; i++)
	{
		insert_key_to_tree(tree, keys[i]);
	}
}
 
void insert_key_to_tree(BTree &tree, int key)
{
	if(tree == NULL)
	{
		alloc_tree(tree);
	}
	// 如果根关键字已满，则进行分裂
	if(tree->count == (MAXDEGREE-1))
	{
		BTree new_root = NULL;
		alloc_tree(new_root);
		new_root->is_leaf = 0;
		new_root->cs[0] = tree;
		break_tree_child(new_root, tree, 0); // 分裂
		tree = new_root;
		insert_key_to_unfull_tree(tree, key);
	}
	else
	{
		insert_key_to_unfull_tree(tree, key);
	}
}
 
void break_tree_child(BTree &tree, BTree &child, int i)
{
	int j = 0;
	BTree rchild = NULL;
 
	alloc_tree(rchild);
	rchild->is_leaf = child->is_leaf; // 和原child一致
	// 将原child分成两个孩子
	// 将原child的右侧r-1个关键字移至rchild的keys中
	for(j = 0; j < (MINDEGREE-1); j++)
	{
		rchild->keys[j] = child->keys[MINDEGREE+j];
	}
	rchild->count = MINDEGREE - 1;
	// 将原child的右侧的r+1个孩子移至rchild的cs中
	for(j = 0; j < MINDEGREE; j++)
	{
		rchild->cs[j] = child->cs[MINDEGREE+j];
	}
	child->count = MINDEGREE - 1;
	
	//将child的第r个结点关键字插入tree的第i个位置
	// 将tree从第i+1至第(tree->count)位置的cs后移一位
	for(j=tree->count;j > i; j--)
	{
		tree->cs[j+1] = tree->cs[j];
	}
	tree->cs[i+1] = rchild;
	// 将从第i至(tree->count-1)位置的关键字全部向后挪1
	for(j=tree->count-1; j > i; j--)
	{
		tree->keys[j+1] = tree->keys[j];
	}
	tree->keys[i] = child->keys[MINDEGREE-1];
	tree->count++;	
	disk_write(tree);
	disk_write(child);
	disk_write(rchild);
}
 
void insert_key_to_unfull_tree(BTree &tree, int key)
{
	int i = 0;
	
	// 如果是叶子结点，则直接插入即可，由于tree未全满，则符合BTree定义
	if(tree->is_leaf == 1)
	{
		// 找到需要沿下插入的位置
		i=tree->count-1;
		while(i>=0 && key < tree->keys[i])
		{
			tree->keys[i+1] = tree->keys[i];
			i--;
		}
		tree->keys[i+1] = key;
		tree->count++;
		disk_write(tree);
	}
	else
	{ // 如果是内结点，则需找到继续寻找位置后，判断其子结点是否已经全满，如全满则分裂，并继续沿下寻找
		i=tree->count-1;
		while(i>=0 && key < tree->keys[i])
		{
			i--;
		}
		i++; // 找到继续寻找位置
		
		disk_read(tree->cs[i]);
		// 如果子树已满，则将其分裂
		if(tree->cs[i]->count == (MAXDEGREE-1))
		{
			break_tree_child(tree, tree->cs[i], i);
			if(key > tree->keys[i])
			i++;
		}
		insert_key_to_unfull_tree(tree->cs[i], key);
	}
}
 
void disk_read(const BTree tree)
{
 
}
 
void disk_write(const BTree tree)
{
 
}
 
void display_tree(const BTree tree)
{
	if(tree==NULL || tree->count == 0)
	{
		return;
	}
 
	printf("(%d", tree->keys[0]);
	int i = 0;
	for(i = 1; i < tree->count; i++)
	{
		printf(",%d", tree->keys[i]);
	}
	printf(")");
	if(0 == tree->is_leaf)
	{
		printf("(");
		for(i = 0; i < tree->count+1; i++)
		{
			display_tree(tree->cs[i]);
		}
		printf(")");
	}
}
 
int search_tree(const BTree tree, int key)
{
	if(tree==NULL)
		return 0;
	for(int i = tree->count-1; (i >= 0) && (key < tree->keys[i]); i--);
	// 在遍历结束之前找到匹配关键字
	if((i != -1) && (key == tree->keys[i]))
	{
		return 1;
	}
	i++;
 
	if(1 == tree->is_leaf)
	{
		return 0;
	}
	else
	{
		return search_tree(tree->cs[i], key);
	}
}
 
void delete_tree(BTree &tree, int key)
{
	if(0 == search_tree(tree, key))
	{
		return;
	}
	
	// 查找关键字位置，或子树
	if( (tree->count==1) && (1 == tree->is_leaf))
	{
		free(tree);
		tree = NULL;
		return;
	}
	else if((tree->count==1) && (tree->keys[0] == key) && (tree->cs[0]->count == MINDEGREE-1) && (tree->cs[1]->count == MINDEGREE-1))
	{
		int j = 0;
		BTree l_child = tree->cs[0], r_child = tree->cs[1];
		
		l_child->keys[MINDEGREE-1] = tree->keys[0];
		for(j = 0; j < r_child->count; j++)
		{
			l_child->keys[j+MINDEGREE] = r_child->keys[j];
		}
		for(j = 0; j < MINDEGREE; j++)
		{
			l_child->cs[MINDEGREE+j] = r_child->cs[j];
		}
		l_child->count = MAXDEGREE - 1;
		free(r_child);
				
		free(tree);
		tree = l_child;
		delete_unless_tree(tree, key);
	}
	else
	{
		delete_unless_tree(tree, key);
	}
}
 
void delete_unless_tree(BTree &tree, int key)
{	
	// 查找关键字位置，或子树
	int i = 0, j = 0;
	for(i = tree->count-1; (i>=0) && (key < tree->keys[i]); i--);
	
	// 由于已经确保关键字在此树中，且无子树，故直接删除
	if(1 == tree->is_leaf)
	{
		// 即将从第i+1位置至(tree->count-1)位置关键字都往前挪1位，并tree->count--
		for(j = i + 1; j < (tree->count); j++)
		{
			tree->keys[j-1] = tree->keys[j];
		}
		tree->count--;	
	}
	else if((i != -1) && (tree->keys[i] == key))
	{// 如果关键字在此树当中，但为内结点，~
		// case2a 若其左孩子有大于等于r个结点，则将其前继代替tree->key[i]，并移至左孩子，将其递归删除~
		if(tree->cs[i]->count >= MINDEGREE)
		{
			int new_key = pre_succor_tree(tree, i);
			tree->keys[i] = new_key;
			delete_unless_tree(tree->cs[i], new_key);
		}
		else if(tree->cs[i+1]->count >= MINDEGREE)
		{//case2b 若右孩子大于等于r个结点，则将其后继代替tree->key[i], 并移至右孩子，递归删除~
			int new_key = after_succor_tree(tree, i+1);
			delete_unless_tree(tree->cs[i+1], new_key);
		}
		else
		{//case2c 若左右孩子均为r-1个关键字，则需将删除结点下沉并左右孩子合并，再删除~
			BTree l_child = tree->cs[i], r_child = tree->cs[i+1];
			
			l_child->keys[MINDEGREE-1] = tree->keys[i];
			for(j = 0; j < r_child->count; j++)
			{
				l_child->keys[j+MINDEGREE] = r_child->keys[j];
			}
			for(j = 0; j < MINDEGREE; j++)
			{
				l_child->cs[MINDEGREE+j] = r_child->cs[j];
			}
			l_child->count = MAXDEGREE - 1;
			free(r_child);
			
			// 将keys域中(i+1)位至(tree->count-1)位向前移1位
			for(j = i+1; j < (tree->count -1); j++)
			{
				tree->keys[j-1] = tree->keys[j];
			}
			// 将cs域中从(i+2)位至(tree->count）位向前移1位
			for(j = i+2; j < tree->count; j++)
			{
				tree->cs[j-1] = tree->cs[j];
			}
			tree->count--;
			
			delete_unless_tree(tree->cs[i], key);
		}
	}
	else
	{ // 如果不在tree的keys中，且为内结点~
		i++; // 找至子孩子的正确位置
		if(tree->cs[i]->count >= MINDEGREE)
		{// 如果关键字个数>=最小度
			delete_unless_tree(tree->cs[i], key);
		}
		else
		{// 如果子树根只有MINDEGREE-1个关键字，则需要考虑从兄弟借，或与兄弟合并情况
			// case 3a 如果可以从其左孩子借一关键字
			if((i != 0) &&(tree->cs[i-1]->count >= MINDEGREE))
			{
				BTree ichild = tree->cs[i], lchild = tree->cs[i-1];
				// 将i孩子的所有子孩子右移1，以便为lchild的最后一个子孩子移至第0位置
				for(j = tree->count; j >= 0; j--)
				{
					ichild->cs[j+1] = ichild->cs[j]; 
				}
				ichild->cs[0] = lchild->cs[lchild->count];
				// 将i孩子的所有关键字右移1，以便为tree中第(i-1)位置的key移至第1个位置
				for(j = tree->count-1; j >= 0; j--)
				{
					ichild->keys[j+1] = ichild->keys[j];
				}
				ichild->keys[0] = tree->keys[i-1];
				ichild->count++;
				
				// 将tree中第(i-1)位关键字替换成lchild中最右关键字
				tree->keys[i-1] = lchild->keys[lchild->count-1];
				
				// 将lchild中左孩子左移1
				for(j = 0; j < lchild->count; j++)
				{
					lchild->cs[j] = lchild->cs[j+1];
				}
				// 将lchild中左孩子关键字左移1
				for(j = 0; j < (lchild->count-1); j++)
				{
					lchild->keys[j] = lchild->keys[j+1];
				}
				lchild->count--;
				delete_unless_tree(ichild, key);
			}// if case 3a
			else if((i != tree->count) && tree->cs[i+1]->count >= MINDEGREE)
			{// case3a' 如果child i的右兄弟关键字够“借”(即>=MINDEGREE)
				BTree ichild = tree->cs[i], rchild = tree->cs[i+1];
				// 将rchild的第0个子孩子移至ichild中子孩子最未位置中
				ichild->cs[ichild->count+1] = rchild->cs[0];
				// 将tree的第i个关键字加至ichild的关键字中
				ichild->keys[ichild->count] = tree->keys[i];
				ichild->count++;				
				
				// 将rchild的第0个关键字覆盖至tree中
				tree->keys[i] = rchild->keys[0];
 
				// 将rchild的所有子孩子左移1
				for(j = 0; j < rchild->count; j++)
				{
					rchild->cs[j] = rchild->cs[j+1];
				}
				for(j = 0; j < (rchild->count-1); j++)
				{
					rchild->keys[j] = rchild->keys[j+1];
				}
				rchild->count--;
				delete_unless_tree(ichild, key);
			}// else if
			else
			{// case3b 左右兄弟都为MINDEGREE-1的情况
				// 如没有左兄弟，则将i+1,转至有左兄弟的情况进行处理
				if(i == 0)
				{
					i++; 
				}
 
				BTree ichild = tree->cs[i];
				BTree lchild = tree->cs[i-1];
				// 将i的子孩子移至左兄弟
				for(j = 0; j < MINDEGREE; j++)
				{
					lchild->cs[j+MINDEGREE] = ichild->cs[j];
				}
				// 将tree的关键字i-1移至左兄弟中
				lchild->keys[MINDEGREE-1] = tree->keys[i-1];
				// 将i的关键字都移至左兄弟中
				for(j = 0; j < MINDEGREE-1; j++)
				{
					 lchild->keys[MINDEGREE+j] = ichild->keys[j];
				}
				lchild->count = MAXDEGREE-1;
				free(ichild);
				
				// 调整tree中的子孩子位置
				for(j=i; j < tree->count; j++)
				{
					tree->cs[j] = tree->cs[j+1];
				}
				// 调整tree中关键字位置
				for(j=i-1; j < (tree->count-1); j++)
				{
					tree->keys[j] = tree->keys[j+1];
				}
				tree->count--;
				delete_unless_tree(lchild, key);
			}
		}// else
	}// else
}
 
int pre_succor_tree(const BTree tree, int i)
{
	BTree p = tree->cs[i];
	//前驱为tree的最左子树的最右叶子结点的最后右一个关键字
	while((p->is_leaf == 0))
	{
		p = p->cs[p->count];
	}
	return p->keys[p->count-1];
}
 
int after_succor_tree(const BTree tree, int i)
{
	BTree p = tree->cs[i+1];	
	//后继为tree的右子树最左叶子结点的第一个关键字
	while(p->is_leaf == 0)
	{
		p = p->cs[0];
	}
	return p->keys[0];
}
////////////////////////////////////
// 定义测试数据
#define TEST_NUM 11
int test_keys[TEST_NUM] = {10, 2, 1, 5, 4, 7, 8, 6, 13, 11, 14};
 
int main()
{
	BTree tree = NULL;
 
	insert_keys_to_tree(tree, test_keys, TEST_NUM);
	display_tree(tree);
	
	delete_tree(tree, 1);
	printf("\n\nafter delete 1:\n");
	display_tree(tree);
 
	delete_tree(tree, 7);
	printf("\n\nafter delete 7:\n");
	display_tree(tree);
 
	delete_tree(tree, 4);
	printf("\n\nafter delete 4:\n");
	display_tree(tree);
 
	delete_tree(tree, 2);
	printf("\n\nafter delete 2:\n");
	display_tree(tree);
 
	printf("\n");
	return 0;
}
