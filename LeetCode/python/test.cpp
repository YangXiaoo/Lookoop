const int MAXN=100000+100;
typedef long long LL;
#define lson i*2,l,m
#define rson i*2+1,m+1,r
LL sum[MAXN*4];
LL addv[MAXN*4];
void PushDown(int i,int num)//这就是延迟操作，更新当前结点的叶子
{
    if(addv[i])
    {
        sum[i*2] +=addv[i]*(num-(num/2));//每个点的需要更新的值乘以的个数
        sum[i*2+1] +=addv[i]*(num/2);//同上
        addv[i*2] +=addv[i];//这个区间需要更新的个数
        addv[i*2+1]+=addv[i];
        addv[i]=0;
    }
}
void PushUp(int i)
{
    sum[i]=sum[i*2]+sum[i*2+1];
}
void build(int i,int l,int r)
{
    addv[i]=0;//将延迟操作更改的值需要记录到addv数组中，现在将它初始化
    if(l==r)
    {
        scanf("%I64d",&sum[i]);
        return ;
    }
    int m=(l+r)/2;
    build(lson);
    build(rson);
    PushUp(i);
}
void update(int ql,int qr,int add,int i,int l,int r)
{
    if(ql<=l&&r<=qr)
    {
        addv[i]+=add;
        sum[i] += (LL)add*(r-l+1);
        return ;
    }
    PushDown(i,r-l+1);//向下更新枝叶的值
    int m=(l+r)/2;
    if(ql<=m) update(ql,qr,add,lson);
    if(m<qr) update(ql,qr,add,rson);
    PushUp(i);
}
LL query(int ql,int qr,int i,int l,int r)
{
    if(ql<=l&&r<=qr)
    {
        return sum[i];
    }
    PushDown(i,r-l+1);
    int m=(l+r)/2;
    LL res=0;
    if(ql<=m) res+=query(ql,qr,lson);
    if(m<qr) res+=query(ql,qr,rson);
    return res;
}