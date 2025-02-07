#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>

int main()
{
    printf("------------------\n");
    printf("Questionario \n");
    printf("------------------\n");

    int n, i;
    char nome[100][100];  // Matriz para armazenar o nome de cada morador
    int idade[100], escolaridade[100], filho[100];
    float renda[100];

    printf("Digite o numero de moradores: ");
    scanf("%d", &n);
    getchar(); // Limpa o buffer ap�s o scanf

    for (i = 0; i < n; i++)
    {
        printf("Digite seu nome: ");
        fgets(nome[i], sizeof(nome[i]), stdin); // L� o nome do morador atual

        printf("Digite a idade: ");
        scanf("%d", &idade[i]);

        printf(" 1 - Ensino Basico ou sem escola \n");
        printf(" 2 - Ensino Fundamental \n");
        printf(" 3 - Ensino Medio \n");
        printf(" 4 - Ensino Superior \n");
        printf(" 5 - P�s, Mestrado ou Doutorado \n");
        printf("Digite o n�vel de escolaridade (1-5): ");

        scanf("%d", &escolaridade[i]);

        printf("Digite o n�mero de filhos: ");
        scanf("%d", &filho[i]);

        printf("Digite a renda: ");
        scanf("%f", &renda[i]);

        getchar(); // Limpa o buffer ap�s cada entrada num�rica
        printf("----------------------------------\n");
    }

    printf("Resultado do formulario\n");
    printf("----------------------------------\n");

    for (i = 0; i < n; i++)
    {
        printf("Morador %d\n", i + 1);
        printf("Nome: %s", nome[i]);
        printf("Idade: %d\n", idade[i]);
        printf("Escolaridade: %d \n", escolaridade[i]);
        // printf("Escolaridade: %d \n", escolaridade[i]);

        if (escolaridade[i] == 1)
        {
            printf("1 - Ensino Basico ou sem escola \n");
        }
        else if (escolaridade[i] == 2)
        {
            printf("2 - Ensino Fundamental \n");
        }
        else if (escolaridade[i] == 3)
        {
            printf("3 - Ensino M�dio \n");
        }
        else if (escolaridade[i] == 4)
        {
            printf("4 - Ensino Superior \n");
        }
        else if (escolaridade[i] == 5)
        {
            printf("5 - P�s-gradua��o ou al�m \n");
        }
        else
        {
            printf("Escolaridade n�o informada \n");
        }

        printf("Filhos: %d\n", filho[i]);
        printf("Renda: %.2f\n", renda[i]);
        printf("----------------------------------\n");
    }

    return 0;
}
