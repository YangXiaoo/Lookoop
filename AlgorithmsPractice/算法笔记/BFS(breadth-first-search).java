/**
# 2018-7-19
# BFS(Breadth-First-Search) 广度优先搜索算法
# https://blog.csdn.net/m0_37316917/article/details/70879977
*/

// 伪代码
bool visited[MAX_VERTEX_NUM];//访问数组，也就是顶点个数

void BFSTraverse(Graph G)
//外层的函数，为准备实现遍历做一些准备工作。
{
　for（int i=0;i<G.vexnum;++i）
    　visited[i]=false;//先将所有的顶点都设置为没有被访问过
  InitQueue(Q);//初始化辅助队列方便遍历顶点
  for(int i=0;i<G.vexnum;++i)
      if(!visited[i])
           BFS(G,i);
//外层循环使用if语句来调用BFS的原因是为了防止有的顶点它不能从初始顶点出发而遍历到，所以这里需要一个完全的循环来避免这种极端情况。
}

void BFS(Graph G,int v)
//从顶点v出发，广度优先遍历图G，算法借助了一个辅助队列Q
 visit(v);//visit函数访问这个顶点的信息
 visited[v]=true;//访问过了这个顶点之后就将这个顶点设置为已访问，即true
 Enqueue(Q,v);//将顶点v入队列，这样就可以从队列中出队并访问它的相邻顶点
 while(!isEmpty(Q)){
    DeQueue(Q,v);//将队头的元素出队列存储在v
    for(w=FirstNeighbor(G,v);w>=0;w=NextNeighbor(G,v,w))//这一步是检查v的所有邻接顶点
    if(!visited[w]){
    visit(w);
    visited[w]=true;
    EnQueue(Q,w);
    //如果w没有被访问过，那么访问这个顶点，并把它入队
    }
}