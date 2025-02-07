#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;

    printf("Quantos numeros voce vai digitar? ");
    scanf("%d", &n);

    double vet[n];  // Se o compilador não suportar VLA, use: double *vet = malloc(n * sizeof(double));

    for (i = 0; i < n; i++) {
        printf("Digite um numero: ");
        scanf("%lf", &vet[i]);  // Corrigido para %lf
    }

    printf("\nNumeros Digitados:\n");
    for (i = 0; i < n; i++) {
        printf("%.1lf\n", vet[i]);  // Adicionado vet[i] como argumento
    }

    // Se tiver usado malloc, liberar a memória:
    // free(vet);

    return 0;
}
