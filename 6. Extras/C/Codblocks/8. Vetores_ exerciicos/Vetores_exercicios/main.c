#include <stdio.h>
#include <conio.h>

int main ()
{
  int programa;

  printf ("- programa de vetores: \n");
  printf("1 - Problemanúmeros negativos\n");
  printf ("2 - Problema soma_vetor \n");
  printf ("3 - Problema alturas \n");
  printf ("4 - Problema numeros_pares \n");
  printf ("5 - Problema maior_posicao \n");
  printf ("6 - Problema soma_vetores \n");
  printf ("7 - Problema abaixo_da_media \n");
  printf ("8 - Problema media_pares \n");
  printf ("9 - Problema mais_velho \n");
  printf ("10 -Problema aprovados \n");
  printf ("11 - Problema dados_pessoas \n");
  printf ("12 - Problema comerciante \n");
  printf ("Escolha um programa de vetores: ");

  scanf("%d", &programa);

  switch ( programa )
  {
    case 1 :
    printf ("1 - Problema negativos \n");
    printf("info: O programa identifica os números negativos\n");
    float numero_1[10];
    printf("------Digite os 10 números: \n");
    for (int i = 0; i < 10; i++) {
        printf("Digite o número %d: ", i + 1);
        scanf("%f", &numero_1[i]);
    }
    printf("Os números negativos são:\n");
    for (int i = 0; i < 10; i++) {
        if (numero_1[i] < 0) {
            printf("Número %d: %f\n", i + 1, numero_1[i]);
        }
    }
    break;

    case 2 :
    printf ("2 - Problema soma_vetor \n");
    printf("info: o programa soma os vetores \n");
    int n_2, soma = 0;
    int numero_2[100];
    printf("Quantos numeros serao somados: ");
    scanf("%d",&n_2);
    for (int i = 0; i < n_2 ; i++) {
        printf("Digite o numero %d: ", i + 1);
        scanf("%d",&numero_2[i]);
        soma = soma + numero_2[i];
    }
    printf("Numeros Digitados: \n");
    for (int i = 0; i < n_2 ; i++) {
        printf("Digite o numero %d: %d \n", i + 1, numero_2[i]);
    }
    printf("a soma dos vetores: %d", soma);
    break;

    case 3 :
    printf("3 - Problema alturas \n");
    printf("info: programa recebe nome, idade, altura. calcula idade media de altura");
    printf("e a (%) de pessoas menores de 16 anos \n");
    char nome[100][100];
    int idade[100], n_3, i;
    float altura[100], soma_altura, media_altura;
    float soma_idade, menor_16 = 0, porcentagem_16;
    printf("Digite o total de pessoas: ");
    scanf("%d",&n_3);
        for (int i = 0 ; i < n_3 ; i++) {
        printf("Digite o nome %d: ", i + 1);
            scanf("%99s", &nome[i]);
        printf("Digita a idade %d: ", i + 1);
            scanf("%d",&idade[i]);
        printf("Digite a altura %d:", i + 1);
            scanf("%f",&altura[i]);
        if (idade[i] < 16) {
            printf("Menor de 16 anos: \n");
            printf("Nome: %s \n",nome[i]);
            printf("Idade: %d anos \n",idade[i]);
            printf("Altura: %.2f \n",altura[i]);
            menor_16 = menor_16 + 1;
            porcentagem_16 = menor_16 / n_3;
            }
            soma_altura = soma_altura + altura[i];
            media_altura = soma_altura / n_3;
            }
        printf("Cadastro: \n");
        for (int i = 0 ; i < n_3 ; i++) {
            printf("Nome: %s \n",nome[i]);
            printf("Idade: %d anos \n",idade[i]);
            printf("Altura: %.2f \n",altura[i]); }
        printf("Resultado: \n");
        printf("Media altura: %.2f \n",media_altura);
        printf("A  de pessoas com menos de 16 anos: %.2f (%)",porcentagem_16*100);
    break;

    case 4 :
    printf ("4 - Problema numeros_pares \n");
    printf("info: vetores que identificam numeros pares, mostrar , quantidade e soma");
    int n_4, numero_4[100];
    int quantidade_par, soma_par, resto;
    printf("Digite o total de numeros: ");
        scanf("%d", &n_4);
    for (int i = 0; i < n_4 ; i++) {
        printf("Digite o numero %d", i + 1);
        scanf("%d",&numero_4[i]);
        resto = numero_4[i] % 2;}
    for (int i = 0; i < n_4 ; i++) {
        if (resto == 0 ) {
        printf("numeros pares: %d, ",numero_4[i]);
        quantidade_par = quantidade_par + 1 ;
        soma_par = soma_par + numero_4[i];
        }
    }
    printf("Quantidade de numeros pares: %d \n", quantidade_par);
    printf("Soma dos numeros pares: %d",soma_par);
    break;

    case 5 :
    printf ("5 - Problema maior_posicao \n");
    break;

    case 6 :
    printf ("6 - Problema soma_vetores \n");
    break;

    case 7 :
    printf ("7 - Problema abaixo_da_media \n");
    break;

    case 8 :
    printf ("8 - Problema media_pares \n");
    break;

    case 9 :
    printf ("9 - Problema mais_velho \n");
    break;

    case 10 :
    printf ("10 -Problema aprovados \n");
    break;

    case 11 :
    printf ("11 - Problema dados_pessoas \n");
    break;

    case 12 :
    printf ("12 - Problema comerciante \n");
    break;

    default :
     printf("Valor invalido!\n");
     system("pause");  // Pause para que o usuário veja a mensagem
     system("cls");    // Limpa a tela
     return main();           // Retorna ao menu inicial

        } //switch
        return 0;
  } // int main

/* ### Problemas de Programação:

1. **Problema "negativos"**
   Escreva um programa que leia um número inteiro positivo \( N \) (máximo = 10) e depois \( N \) números inteiros.
   Armazene-os em um vetor e, em seguida, exiba todos os números negativos lidos.

2. **Problema "soma_vetor"**
   Escreva um programa que leia \( N \) números reais e os armazene em um vetor. Em seguida, o programa deve:
   - Imprimir todos os elementos do vetor.
   - Exibir a soma e a média dos elementos do vetor.

3. **Problema "alturas"**
   Crie um programa para ler nome, idade e altura de \( N \) pessoas. Depois, o programa deve:
   - Calcular e mostrar a altura média das pessoas.
   - Calcular e exibir a porcentagem de pessoas com menos de 16 anos, bem como os nomes dessas pessoas, caso haja.

4. **Problema "numeros_pares"**
   Escreva um programa que leia \( N \) números inteiros e os armazene em um vetor. O programa deve, em seguida,
   mostrar todos os números pares e também a quantidade total de números pares.

5. **Problema "maior_posicao"**
   Crie um programa para ler \( N \) números reais e armazená-los em um vetor. O programa deve então:
   - Exibir o maior número do vetor (supondo que não há empates).
   - Exibir a posição do maior número, considerando que a primeira posição é 0 (zero).

6. **Problema "soma_vetores"**
   Escreva um programa para ler dois vetores \( A \) e \( B \), contendo \( N \) elementos cada. Em seguida,
   o programa deve gerar um terceiro vetor \( C \) onde cada elemento de \( C \) é a soma dos elementos correspondentes de
   \( A \) e \( B \). Por fim, imprima o vetor \( C \) gerado.

7. **Problema "abaixo_da_media"**
   Escreva um programa para ler um número inteiro \( N \) e depois um vetor de \( N \) números reais. O programa deve:
   - Exibir a média aritmética de todos os elementos com três casas decimais.
   - Exibir todos os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.

8. **Problema "media_pares"**
   Crie um programa para ler um vetor de \( N \) números inteiros. O programa deve calcular e exibir
   a média aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for digitado,
   o programa deve exibir a mensagem "NENHUM NUMERO PAR".

9. **Problema "mais_velho"**
   Escreva um programa para ler um conjunto de nomes de pessoas e suas respectivas idades.
   Os nomes devem ser armazenados em um vetor e as idades em outro vetor.
   O programa deve, então, exibir o nome da pessoa mais velha.

10. **Problema "aprovados"**
   Crie um programa para ler um conjunto de \( N \) nomes de alunos e suas notas nos 1º e 2º semestres.
   Cada informação deve ser armazenada em um vetor. O programa deve, então, imprimir os nomes dos alunos aprovados,
   considerando aprovados aqueles cuja média das notas seja maior ou igual a 6.0.

11. **Problema "dados_pessoas"**
   Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de \( N \) pessoas.
   Crie um programa que calcule e escreva:
   - A maior e a menor altura do grupo.
   - A média de altura das mulheres.
   - O número total de homens.

12. **Problema "comerciante"**
   Um comerciante deseja fazer o levantamento do lucro das mercadorias que comercializa.
   Para isso, crie um programa que leia um conjunto de \( N \) mercadorias, onde cada mercadoria tem um nome,
   preço de compra e preço de venda. O programa deve determinar e escrever quantas mercadorias proporcionaram:
   - Lucro menor que 10%.
   - Lucro entre 10% e 20%.
   - Lucro superior a 20%.
   Além disso, o programa deve calcular e exibir:
   - O valor total de compra de todas as mercadorias.
   - O valor total de venda de todas as mercadorias.
   - O lucro total.
 */
