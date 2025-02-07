#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int main()
{
    /* Desafio: Crie um programa em C que peça ao usuário para adivinhar um número secreto entre 1 e 100.
    O programa deve ter as seguintes características:
    O número secreto deve ser fixo (por exemplo, 42).
    O programa deve permitir que o usuário faça até 10 tentativas para adivinhar o número.
    Se o usuário acertar o número, o programa deve parabenizá-lo e encerrar.
    Se o usuário errar, o programa deve dizer se o palpite foi muito alto ou muito baixo.
    Se o usuário não conseguir acertar em 10 tentativas, o programa deve informar que ele perdeu e exibir o número secreto. */

    printf("----------| Descubra o Numero sorteado |--------  \n");
    srand(time(0));
    int numero_sorteado = rand() % 1000;
    int numero_escolhido;
    int tentativas = 1;
    int acerto = 0;

    printf("Digite o numero sorteado (0 a 1000): ");
    scanf("%d",&numero_escolhido);

    while (tentativas < 10) {
        if (numero_escolhido == numero_sorteado) {
            printf("Parabens voce acertou !!! ");
            printf("Tentativa %d de 10 \n",tentativas);
            tentativas = tentativas + 10;
            acerto = acerto + 1;}
        else  {
                if (numero_escolhido > 1000 ) {
                   printf("Numero invalido ! maior que o limite \n");
                   printf (" | Tentativa %d de 10 | \n",tentativas);
                   tentativas = tentativas + 1;
                   printf("Digite o numero sorteado (0 a 1000): ");
                   scanf("%d",&numero_escolhido);}
                else {
                        if (numero_escolhido < numero_sorteado) {
                            printf("Numero escolhido menor que o sorteado \n");
                            printf (" | Tentativa %d de 10 | \n",tentativas);
                            tentativas = tentativas + 1;
                            printf("Digite o numero sorteado (0 a 1000): ");
                            scanf("%d",&numero_escolhido);}
                        else {
                             printf("Numero escolhido maior que o sorteado \n");
                             printf (" | Tentativa %d de 10 | \n",tentativas);
                             tentativas = tentativas + 1;
                             printf("Digite o numero sorteado (0 a 1000): ");
                             scanf("%d",&numero_escolhido);}
                        }
                }
   }

   if (tentativas >= 10 && acerto == 0 ) {
        printf("VOCE NAO ACERTOU , O NUMERO SORTEADO: %d",numero_sorteado);}
return 0;
}



