int f(int n)
{
    int k = 5;
    int r = 0;
    while( n >= k)
    {
        r += n/k;
        k *= 5;
    }
    return r;
}