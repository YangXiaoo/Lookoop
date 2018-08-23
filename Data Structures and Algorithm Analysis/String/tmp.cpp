// Rabin Karp Algorithm 
 
#include<iostream>
#include<string>
 
using namespace std;
 
void Rabin_Karp_search(const string &T, const string &P, int d, int q)
{
    int m = P.length();
    int n = T.length();
    int i, j;
    int p = 0;  // hash value for pattern
    int t = 0; // hash value for txt
    int h = 1;
  
    // The value of h would be "pow(d, M-1)%q"
    for (i = 0; i < m-1; i++)
        h = (h*d)%q;
  
    // Calculate the hash value of pattern and first window of text
    for (i = 0; i < m; i++)
    {
        p = (d*p + P[i])%q;
        t = (d*t + T[i])%q;
    }
  
    // Slide the pattern over text one by one 
    for (i = 0; i <= n - m; i++)
    {
        
        // Chaeck the hash values of current window of text and pattern
        // If the hash values match then only check for characters on by one
        if ( p == t )
        {
            /* Check for characters one by one */
            for (j = 0; j < m; j++)
               if (T[i+j] != P[j])
				   break;
            
            if (j == m)  // if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
               cout<<"Pattern found at index :"<< i<<endl;
        }
         
        // Calulate hash value for next window of text: Remove leading digit, 
        // add trailing digit           
        if ( i < n-m )
        {
            t = (d*(t - T[i]*h) + T[i+m])%q;
             
            // We might get negative value of t, converting it to positive
            if(t < 0) 
              t = (t + q); 
        }
    }
}
  
int main()
{
    string T = "Rabin–Karp string search algorithm: Rabin-Karp";
    string P = "Rabin";
    int q = 101;  // A prime number
	int d = 16; // d进制数字
    Rabin_Karp_search(T, P,d,q);
    system("pause");
    return 0;
}
