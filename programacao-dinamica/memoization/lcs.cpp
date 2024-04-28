#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int LCSlength(string X, string Y, int m, int n, auto &lookup){
    if(m == 0 || n == 0) return 0;

    string key == to_string(m) + "|" + to_string(n);

    if(lookup.find(key) == lookup.end()){
        if(X[m-1] == Y[n-1]){
            lookup[key] = LCSlength(X, Y, m-1, n-1, lookup) +1;
        } else{
            lookup[key] = max(LCSlength(X, Y, m, n-1, lookup), LCSlength(X, Y, m-1, n, lookup));
        }
    }
    return lookup[key];
}

int main(){
    string x = "ABCBDAB", y = "BDCABA";
    unordered_map<string, int> lookup; // tabela pra guardar os valores na recursão (lookup table)
    cout << "O tamanho da LCS é " << LCSlength(x,y, x.length(), y.length(), lookup) <<endl;
    return 0;

}