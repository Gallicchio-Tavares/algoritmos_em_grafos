# int tabFib[MaxSize];
# memset(tabFib,-1,sizeof(int)*MaxSize);
# int Fib(int n){
# if(tabFib[n] != -1) return tabFib[n];
# if(n==0) return tabFib[0] = 0;
# if(n==1) return tabFib[1] = 1;
# return tabFib[n] = Fib(n-1)+Fib(n-2);
# }