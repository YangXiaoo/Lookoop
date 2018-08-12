//
//  MBTree.h
//  MBTree
//
//  Created by Wuyixin on 2017/8/4.
//  Copyright © 2017年 Coding365. All rights reserved.
//
 
#ifndef MBTree_h
#define MBTree_h
 
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
 
#define M (4)
#define LIMIT_M_2 (M % 2 ? (M + 1)/2 : M/2)
 
typedef struct MBNode *MBTree,*Position;
typedef int KeyType;
struct MBNode{
    int KeyNum;/* 关键字个数 */
    KeyType Key[M + 1];/* 内部节点从1开始(实际上0的位置存储了第一棵子树的最小值)，树叶节点从0开始 */
    MBTree Children[M + 1];/* 存储M个孩子节点 */
};
 
/* 初始化 */
extern MBTree Initialize();
/* 插入 */
extern MBTree Insert(MBTree T,KeyType Key);
/* 删除 */
extern MBTree Remove(MBTree T,KeyType Key);
/* 销毁 */
extern MBTree Destroy(MBTree T);
/* 遍历节点 */
extern void Travel(MBTree T);
 
#endif /* MBTree_h */
//
//  MBTree.c
//  MBTree
//
//  Created by Wuyixin on 2017/8/4.
//  Copyright © 2017年 Coding365. All rights reserved.
//
 
#include "MBTree.h"
 
 
static KeyType Unavailable = INT_MIN;
 
/* 生成节点并初始化 */
static MBTree MallocNewNode(){
    MBTree NewNode;
    int i;
    NewNode = malloc(sizeof(struct MBNode));
    if (NewNode == NULL)
        exit(EXIT_FAILURE);
    
    
    i = 0;
    while (i < M + 1){
        NewNode->Key[i] = Unavailable;
        NewNode->Children[i] = NULL;
        i++;
    }
    NewNode->KeyNum = 0;
    
    return NewNode;
}
 
/* 初始化 */
extern MBTree Initialize(){
    
    MBTree T;
    if (M < (3)){
        printf("M最小等于3！");
        exit(EXIT_FAILURE);
        
    }
    /* 根结点 */
    T = MallocNewNode();
    
    return T;
}
 
/* 寻找一个兄弟节点，其存储的关键字未满，否则返回NULL */
static Position FindSibling(Position Parent,int i){
    Position Sibling;
    int Limit;
    
    Limit = M;
    
    Sibling = NULL;
    if (i == 0){
        if (Parent->Children[1]->KeyNum < Limit)
            Sibling = Parent->Children[1];
    }
    else if (Parent->Children[i - 1]->KeyNum < Limit)
        Sibling = Parent->Children[i - 1];
    else if (i + 1 < Parent->KeyNum && Parent->Children[i + 1]->KeyNum < Limit){
        Sibling = Parent->Children[i + 1];
    }
    
    return Sibling;
}
 
/* 查找兄弟节点，其关键字数大于M/2 ;没有返回NULL*/
static Position FindSiblingKeyNum_M_2(Position Parent,int i,int *j){
    int Limit;
    Position Sibling;
    Sibling = NULL;
    
    Limit = LIMIT_M_2;
    
    if (i == 0){
        if (Parent->Children[1]->KeyNum > Limit){
            Sibling = Parent->Children[1];
            *j = 1;
        }
    }
    else{
        if (Parent->Children[i - 1]->KeyNum > Limit){
            Sibling = Parent->Children[i - 1];
            *j = i - 1;
        }
        else if (i + 1 < Parent->KeyNum && Parent->Children[i + 1]->KeyNum > Limit){
            Sibling = Parent->Children[i + 1];
            *j = i + 1;
        }
        
    }
    
    return Sibling;
}
 
/* 当要对X插入Key的时候，i是X在Parent的位置，j是Key要插入的位置
 当要对Parent插入X节点的时候，i是要插入的位置，Key和j的值没有用
 */
static Position InsertElement(int isKey, Position Parent,Position X,KeyType Key,int i,int j){
    
    int k;
    if (isKey){
        /* 插入key */
        k = X->KeyNum - 1;
        while (k >= j){
            X->Key[k + 1] = X->Key[k];k--;
        }
        
        X->Key[j] = Key;
        
        if (Parent != NULL)
            Parent->Key[i] = X->Key[0];
        
        X->KeyNum++;
        
    }else{
        /* 插入节点 */
        
        k = Parent->KeyNum - 1;
        while (k >= i){
            Parent->Children[k + 1] = Parent->Children[k];
            Parent->Key[k + 1] = Parent->Key[k];
            k--;
        }
        Parent->Key[i] = X->Key[0];
        Parent->Children[i] = X;
        
        Parent->KeyNum++;
        
    }
    return X;
}
 
 
static Position RemoveElement(int isKey, Position Parent,Position X,int i,int j){
    
    int k,Limit;
    
    if (isKey){
        Limit = X->KeyNum;
        /* 删除key */
        k = j + 1;
        while (k < Limit){
            X->Key[k - 1] = X->Key[k];k++;
        }
        
        X->Key[X->KeyNum - 1] = Unavailable;
        
        Parent->Key[i] = X->Key[0];
        
        X->KeyNum--;
    }else{
        /* 删除节点 */
        Limit = Parent->KeyNum;
        k = i + 1;
        while (k < Limit){
            Parent->Children[k - 1] = Parent->Children[k];
            Parent->Key[k - 1] = Parent->Key[k];
            k++;
        }
        
        Parent->Children[Parent->KeyNum - 1] = NULL;
        Parent->Key[Parent->KeyNum - 1] = Unavailable;
        
        Parent->KeyNum--;
        
    }
    return X;
}
 
/* Src和Dst是两个相邻的节点，i是Src在Parent中的位置；
 将Src的元素移动到Dst中 ,n是移动元素的个数*/
static Position MoveElement(Position Src,Position Dst,Position Parent,int i,int n){
    KeyType TmpKey;
    Position Child;
    int j,SrcInFront;
    
    SrcInFront = 0;
    
    if (Src->Key[0] < Dst->Key[0])
        SrcInFront = 1;
    
    j = 0;
    /* 节点Src在Dst前面 */
    if (SrcInFront){
        if (Src->Children[0] != NULL){
            while (j < n) {
                Child = Src->Children[Src->KeyNum - 1];
                RemoveElement(0, Src, Child, Src->KeyNum - 1, Unavailable);
                InsertElement(0, Dst, Child, Unavailable, 0, Unavailable);
                j++;
            }
        }else{
            while (j < n) {
                TmpKey = Src->Key[Src->KeyNum -1];
                RemoveElement(1, Parent, Src, i, Src->KeyNum - 1);
                InsertElement(1, Parent, Dst, TmpKey, i + 1, 0);
                j++;
            }
            
        }
        
        Parent->Key[i + 1] = Dst->Key[0];
        
    }else{
        if (Src->Children[0] != NULL){
            while (j < n) {
                Child = Src->Children[0];
                RemoveElement(0, Src, Child, 0, Unavailable);
                InsertElement(0, Dst, Child, Unavailable, Dst->KeyNum, Unavailable);
                j++;
            }
            
        }else{
            while (j < n) {
                TmpKey = Src->Key[0];
                RemoveElement(1, Parent, Src, i, 0);
                InsertElement(1, Parent, Dst, TmpKey, i - 1, Dst->KeyNum);
                j++;
            }
            
        }
        
        Parent->Key[i] = Src->Key[0];
        
    }
    
    return Parent;
}
 
/* 分裂节点 */
static MBTree SplitNode(Position Parent,Position X,int i){
    int j,k,Limit;
    Position NewNode;
    
    NewNode = MallocNewNode();
    
    k = 0;
    j = X->KeyNum / 2;
    Limit = X->KeyNum;
    while (j < Limit){
        if (X->Children[0] != NULL){
            NewNode->Children[k] = X->Children[j];
            X->Children[j] = NULL;
        }
        NewNode->Key[k] = X->Key[j];
        X->Key[j] = Unavailable;
        NewNode->KeyNum++;X->KeyNum--;
        j++;k++;
    }
    
    if (Parent != NULL)
        InsertElement(0, Parent, NewNode, Unavailable, i + 1, Unavailable);
    else{
        /* 如果是X是根，那么创建新的根并返回 */
        Parent = MallocNewNode();
        InsertElement(0, Parent, X, Unavailable, 0, Unavailable);
        InsertElement(0, Parent, NewNode, Unavailable, 1, Unavailable);
        
        return Parent;
    }
    
    return X;
}
 
/* 合并节点,X只有一个关键字，S有大于或等于M/2个关键字*/
static Position MergeNode(Position Parent, Position X,Position S,int i){
    int Limit;
    
    /* S的关键字数目大于M/2 */
    if (S->KeyNum > LIMIT_M_2){
        /* 从S中移动一个元素到X中 */
        MoveElement(S, X, Parent, i,1);
    }else{
        /* 将X全部元素移动到S中，并把X删除 */
        Limit = X->KeyNum;
        MoveElement(X,S, Parent, i,Limit);
        RemoveElement(0, Parent, X, i, Unavailable);
        
        free(X);
        X = NULL;
    }
    
    return Parent;
}
 
static MBTree RecursiveInsert(MBTree T,KeyType Key,int i,MBTree Parent){
    int j,Limit;
    Position Sibling;
    
    /* 查找分支 */
    j = 0;
    while (j < T->KeyNum && Key >= T->Key[j]){
        /* 重复值不插入 */
        if (Key == T->Key[j])
            return T;
        j++;
    }
    if (j != 0 && T->Children[0] != NULL) j--;
    
    /* 树叶 */
    if (T->Children[0] == NULL)
        T = InsertElement(1, Parent, T, Key, i, j);
    /* 内部节点 */
    else
        T->Children[j] = RecursiveInsert(T->Children[j], Key, j, T);
    
    /* 调整节点 */
    
    Limit = M;
    
    if (T->KeyNum > Limit){
        /* 根 */
        if (Parent == NULL){
            /* 分裂节点 */
            T = SplitNode(Parent, T, i);
        }
        else{
            Sibling = FindSibling(Parent, i);
            if (Sibling != NULL){
                /* 将T的一个元素（Key或者Child）移动的Sibing中 */
                MoveElement(T, Sibling, Parent, i, 1);
            }else{
                /* 分裂节点 */
                T = SplitNode(Parent, T, i);
            }
        }
        
    }
    
    if (Parent != NULL)
        Parent->Key[i] = T->Key[0];
    
    
    return T;
}
 
/* 插入 */
extern MBTree Insert(MBTree T,KeyType Key){
    return RecursiveInsert(T, Key, 0, NULL);
}
 
static MBTree RecursiveRemove(MBTree T,KeyType Key,int i,MBTree Parent){
    
    int j,NeedAdjust;
    Position Sibling,Tmp;
    
    Sibling = NULL;
    
    /* 查找分支 */
    j = 0;
    while (j < T->KeyNum && Key >= T->Key[j]){
        if (Key == T->Key[j])
            break;
        j++;
    }
    
    if (T->Children[0] == NULL){
        /* 没找到 */
        if (Key != T->Key[j] || j == T->KeyNum)
            return T;
    }else
        if (j == T->KeyNum || Key < T->Key[j]) j--;
    
    
    
    /* 树叶 */
    if (T->Children[0] == NULL){
        T = RemoveElement(1, Parent, T, i, j);
    }else{
        T->Children[j] = RecursiveRemove(T->Children[j], Key, j, T);
    }
    
    NeedAdjust = 0;
    /* 树的根或者是一片树叶，或者其儿子数在2到M之间 */
    if (Parent == NULL && T->Children[0] != NULL && T->KeyNum < 2)
        NeedAdjust = 1;
    /* 除根外，所有非树叶节点的儿子数在[M/2]到M之间。(符号[]表示向上取整) */
    else if (Parent != NULL && T->Children[0] != NULL && T->KeyNum < LIMIT_M_2)
        NeedAdjust = 1;
    /* （非根）树叶中关键字的个数也在[M/2]和M之间 */
    else if (Parent != NULL && T->Children[0] == NULL && T->KeyNum < LIMIT_M_2)
        NeedAdjust = 1;
    
    /* 调整节点 */
    if (NeedAdjust){
        /* 根 */
        if (Parent == NULL){
            if(T->Children[0] != NULL && T->KeyNum < 2){
                Tmp = T;
                T = T->Children[0];
                free(Tmp);
                return T;
            }
            
        }else{
            /* 查找兄弟节点，其关键字数目大于M/2 */
            Sibling = FindSiblingKeyNum_M_2(Parent, i,&j);
            if (Sibling != NULL){
                MoveElement(Sibling, T, Parent, j, 1);
            }else{
                if (i == 0)
                    Sibling = Parent->Children[1];
                else
                    Sibling = Parent->Children[i - 1];
                
                Parent = MergeNode(Parent, T, Sibling, i);
                T = Parent->Children[i];
            }
        }
        
    }
    
    
    return T;
}
 
/* 删除 */
extern MBTree Remove(MBTree T,KeyType Key){
    return RecursiveRemove(T, Key, 0, NULL);
}
 
/* 销毁 */
extern MBTree Destroy(MBTree T){
    int i,j;
    if (T != NULL){
        i = 0;
        while (i < T->KeyNum + 1){
            Destroy(T->Children[i]);i++;
        }
        
        printf("Destroy:(");
        /* 树叶的Key从0开始，内部节点从1开始 */
        if (T->Children[0] == NULL)
            j = 0;
        else
            j = 1;
        while (j < T->KeyNum)/*  T->Key[i] != Unavailable*/
            printf("%d:",T->Key[j++]);
        printf(") ");
        free(T);
        T = NULL;
    }
    
    return T;
}
 
static void RecursiveTravel(MBTree T,int Level){
    int i;
    if (T != NULL){
        printf("  ");
        printf("[Level:%d]-->",Level);
        printf("(");
        
        /* 树叶的Key从0开始，内部节点从1开始 */
        if (T->Children[0] == NULL)
            i = 0;
        else
            i = 1;
        
        while (i < T->KeyNum)/*  T->Key[i] != Unavailable*/
            printf("%d:",T->Key[i++]);
        printf(")");
        
        Level++;
        
        i = 0;
        while (i <= T->KeyNum) {
            RecursiveTravel(T->Children[i], Level);
            i++;
        }
        
        
    }
}
 
/* 遍历 */
extern void Travel(MBTree T){
    RecursiveTravel(T, 0);
    printf("\n");
}


//
//  main.c
//  MBTree
//
//  Created by Wuyixin on 2017/8/4.
//  Copyright © 2017年 Coding365. All rights reserved.
//
 
#include <stdio.h>
#include <time.h>
#include "MBTree.h"
 
int main(int argc, const char * argv[]) {
    MBTree T;
    T = Initialize();
    
    clock_t c1 = clock();
    int i = 50000000;
    while (i > 0)
        T = Insert(T, i--);
    i = 50000001;
    while (i < 100000000)
        T = Insert(T, i++);
    
    i = 100000000;
    while (i > 100)
        T = Remove(T, i--);
    
    Travel(T);
    Destroy(T);
    
    clock_t c2 = clock();
    
    printf("\n用时： %lu秒\n",(c2 - c1)/CLOCKS_PER_SEC);
    return 0;
}
