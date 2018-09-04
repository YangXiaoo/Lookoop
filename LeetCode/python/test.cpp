#include<bits/stdc++.h>
#define LL long long
using namespace std;
LL op,n,m,x,y,k,a[300005],low_bit,tempt;
struct fkt{
    LL left;
    LL right;
    LL tot;
    LL add;
}tree[300005];
namespace qaq{
    LL change(LL test){LL ans=0;while(test){test>>=1;ans++;}test=1;while(ans--)test*=2;return test;} 
    void build(LL lef,LL rig,LL root){        
tree[root].left=lef;
        tree[root].right=rig;
        tree[root].add=0;
        if(lef==rig){tree[root].tot=a[lef];}
        else{
            LL mid=(lef+rig)>>1;
            build(lef,mid,root<<1);
            build(mid+1,rig,root<<1|1);
            tree[root].tot=tree[root<<1].tot+tree[root<<1|1].tot;
        }
    }
    void pushdown(LL root){
        if(tree[root].add){
            tree[root<<1].add+=tree[root].add;
            tree[root<<1|1].add+=tree[root].add;
            tree[root<<1].tot+=tree[root].add*(tree[root<<1].right-tree[root<<1].left+1);
            tree[root<<1|1].tot+=tree[root].add*(tree[root<<1|1].right-tree[root<<1|1].left+1);
            tree[root].add=0;
        }
    } 
    void pushup(LL root){
        tree[root].tot=tree[root<<1].tot+tree[root<<1|1].tot;
    }     
    void update(LL nl,LL nr,LL root,LL c){
        if(tree[root].left>nr||tree[root].right<nl)    return;
        if(tree[root].left>=nl&&tree[root].right<=nr){
            tree[root].add+=c;
            tree[root].tot+=c*(tree[root].right-tree[root].left+1);
            return;
        }
        pushdown(root);
        LL mid=(tree[root].left+tree[root].right)>>1;
        if(nl<=mid)        update(nl,nr,root<<1,c);
        if(mid+1<=nr)    update(nl,nr,root<<1|1,c);
        pushup(root);
    } 
    LL query(LL nl,LL nr,LL root){
        if(tree[root].left>nr||tree[root].right<nl)    return 0; 
        if(tree[root].left>=nl&&tree[root].right<=nr)    return tree[root].tot;
        pushdown(root); 
        return query(nl,nr,root<<1)+query(nl,nr,root<<1|1);
    }
    
    int main(){
        scanf("%lld%lld",&n,&m);
        for(LL i=1;i<=n;i++)    scanf("%lld",&a[i]);
        tempt=change(n);
        build(1,tempt,1);
        while(m--){
            scanf("%lld",&op);
            if(op==1){
                scanf("%lld%lld%lld",&x,&y,&k);
                update(x,y,1,k);
            }
            else{
                scanf("%lld%lld",&x,&y);
                printf("%lld\n",query(x,y,1));
            }
        }
        return 0;
    }
}
int main(){
    qaq::main();
    return 0;
}