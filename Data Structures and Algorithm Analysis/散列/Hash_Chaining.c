// 2018-8-4
// https://blog.csdn.net/duan19920101/article/details/51579136/
// 算法导论 P142
// 数据结构与算法分析-C语言描述 P111
/*
	Key - Value
	[1] 构造哈希映射
		1. 除法散列
			求模
		2. 平方散列法
		3. Fibonacci
	[2] 解决冲突
		1. 开地址法(用数组存key和value)
			--线性再探测：再index的周围进行Index-1,index+1或index-2,index+2....选取确定哈希值
			--随机再探测：在index的周围进行随机查找确定位置
		2. 链接法
			直接链接到相同地址的链表末尾(缺点：基本上会超过O(1))
	[3] 优化方法
		1. 除法散列中除数尽量取大的素数。 [https://blog.csdn.net/c602273091/article/details/54798805]
		2. 尽量取一个大的数组来存储hash值，消耗内存得到性能。使容量是需求的120%

	[4] 评价
		1. 优点
			速度快几乎为O(N)
		2. 缺点 
			--当数据规模接近上界或下界时，hash表不能体现高效特点，甚至不如一般算法.
			--hash索引仅能满足"=","<=>","IN"查询，不能使用范围查询;没有排序大小,不能利用部分索引键进行查询[http://blog.sina.com.cn/s/blog_6776884e0100pko1.html]
			--一个关键字可能对应多个散列地址
*/
// name: Hash_Chaning.c
// datetime: 2018-8-4
// author: Yauno
#ifndef _HASH_
#define _HASH_
#include <stdio.h>


#define TABLESIZE 100
#define MINSIZE 10

// 定义链表
typedef struct node	
{
	int key; // 利用链表来存储key值
	ElementType value; // 存储value, 任意类型ElementType
	struct node *next;
} List;

// 定义hash表
typedef struct Hash
{
	int TableSize; // 散列大小
	List *Lists[TableSize]; // 数据存储
} HashTable;

HashTable Initialize(int TableSize); // 初始化哈希表
static int NextPrime(int TableSize); // 第一个比TableSize大的素数
int Hash(int key, int TableSize);
ElementType Find(int key, HashTable *H);
void Insert(int key, ElementType value, HashTable *H)
void Empty(HashTable *H);


static int NextPrime(int TableSize)
{
	int i, flag = 0;

	// 偶数必不是素数
	if (TableSize % 2 == 0)
		TableSize++;

	for ( ; ; N += 2)
	{
		for (i = 3; i * i <= N; i += 2)
			if (N % i == 0)
			{吧
				flag = 1;
				break;
			}
			else
			{
				flag == 0;
			}

		if (flag == 0) return N;
	}
}


// 初始化
HashTable Initialize(int TableSize)
{
	HashTable *H;

	// too small
	if (TableSize < MINSIZE)
		return NULL;

	H = (HashTable *)malloc(sizeof(HashTable));
	if (H == NULL)
		return NULL;

	H->TableSize = NextPrime(TableSize);

	H->Lists = (List *)malloc( sizeof( List ) * H->TableSize );
	if (H->Lists == NULL)
		return NULL;

	// 定义链表
	for (int i = 0; i < H->TableSize; i++)
	{
		H->Lists[i] = (List *)malloc(sizeof(List));
		if (H->Lists[i] == NULL)
			return NULL;
		H->Lists[i]->key = i;
		H->Lists[i]->value = NULL;
		H->Lists[i]->next = NULL;
	}

	return H;
}


int Hash(int key, int TableSize)
{
	return key % TableSize;
}


List Get(int key, HashTable *H)
{
	ElementType value;
	List L, P;

	int k = Hash(key, H->TableSize);

	L = H->Lists[k];
	P = L->next;

	while (P != NULL && P->key != key && P->value != NULL)
		P = P->next;

	return P;
}


void Insert(int key, ElementType value, HashTable *H)
{
	int k = Hash(key, H->TableSize);
	List L, newList, P;
	ElementType val;

	// 查看是否已经存在
	P = Get(key, H);


	if (P != NULL)
		return NULL;
	L = H->Lists[k];

	while (L->next != NULL)
	{
		if (L->key == key && L->value != NULL)
		{
			L->value = value;
			return NULL;
		}		

		L = L->next;
	}

	newList = (List *)malloc(sizeof(List));
	newList->key = key;
	newList->value = value;
	newList->next = NULL;

	L->next = newList;
}


void Empty(HashTable *H)
{
	for (int i = 0; i < H->TableSize; i++)
	{
		List *L = H->Lists[i];
		List *tmp;

		while (L != NULL)
		{
			tmp = L->next;
			free(L);
			L = tmp;
		}
	}

	free(H->Lists); // 待证
	free(H);
}