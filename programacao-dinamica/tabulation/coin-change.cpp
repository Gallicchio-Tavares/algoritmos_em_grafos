#include <iostream>
#include <bits/stdc++.h>
using namespace std;

const int inf = 0x3f3f3f3f;
int valor = 11; // valor que queremos sacar
int moedas[] = {1,5,6,8}; //valor das moedas no caixa disponíveis
int tamanho = sizeof(moedas)/sizeof(moedas[0]);
int memo[2020];

int troco(int valor){
    if(valor < 0) return inf;
    if(valor == 0) return 0;

    int& pdm = memo[valor];
    if(pdm != -1) return pdm;

    int min = inf, opt[tamanho];

    for(int i=0; i<tamanho; i++){
        opt[i] = troco(valor - moedas[i]) + 1;
        if(opt[i] < min){
            min = opt[i];
        }
    }
    return pdm=min;
}

int main(){
    memset(memo, -1, sizeof(memo));
    cout << troco(valor) <<endl;
    return 0;
}