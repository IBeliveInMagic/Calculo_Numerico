#include<iostream>

using namespace std;

/* Definir variaveis globais */

int weight[110],value[110];		/*  */
int pesomax , qtd;				/* */
long long dp[110][100009];

long long funcao(int i, int pesoatual){
	if(i==qtd || pesoatual <= 0){
		return 0;
	}

	if(dp[i][pesoatual]>=0){

		return dp[i][pesoatual];

	}

	long long naocoloca = funcao(i+1,pesoatual);

	if(pesoatual-weight[i] >= 0){

		long long coloca = funcao(i+1,pesoatual-weight[i]) + value[i];
		return dp[i][pesoatual] = max(coloca,naocoloca);

	}

	return dp[i][pesoatual] = naocoloca;
}


int main(){

	int i; 				/* contador */
	int Case = 0;		/* Variável que armazena o número de casos */
	int peso,grau;		/* Variáveis que armazenam o peso de cada livro 
						e o grau de interesse no livro respectivamente */

	while(1){

		Case++;

	    cin >> qtd >> pesomax;
	    
	    if(qtd == 0 && pesomax == 0) break;		/* Critério de parada do loop */
            
        for(i = 0; i < qtd; i++){

            cin >> peso >> grau;
            weight[i] = peso;
            value[i] = grau;

        }
        
        memset(dp,-1,sizeof(dp));
            
        long long resposta = funcao(0,pesomax);
            
        cout << "Caso " << Case << ": " << resposta << endl;    

	}

	return 0;
}