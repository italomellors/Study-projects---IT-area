#include <stdio.h>
#include <string.h>

int main() {
    char nome[50];

    printf("Digite o nome da pessoa: ");
    fgets(nome, sizeof(nome), stdin);

    // Remove o '\n' ao final da string, se presente
    nome[strcspn(nome, "\n")] = '\0';

    printf("Nome: %s\n", nome);

    return 0;
}
