#include <iostream>
#include <string>
using namespace std;
// longest common subsequence

int LCSlength(string X, string Y, int m, int n){
    if(m == 0 || n == 0) return 0;
    if(X[m-1] == Y[n-1]) return LCSlength(X, Y, m-1, n-1) + 1;
    return max(LCSlength(X,Y,m,n-1), LCSlength(X,Y,m-1, n));
}

int main(){
    string x = "ABCBDAB", y = "BDCABA";
    cout << "O tamanho da LCS é " << LCSlength(x,y, x.length(), y.length()) <<endl;
    return 0;
}