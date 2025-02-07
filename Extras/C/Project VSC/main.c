#include <stdio.h>

// Estrutura para armazenar uma data
struct Data {
    int dia;
    int mes;
    int ano;
};

// Função para verificar se um ano é bissexto
int isBissexto(int ano) {
    if ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0)) {
        return 1;
    }
    return 0;
}

// Função para calcular o número de dias em um mês específico
int diasNoMes(int mes, int ano) {
    int diasMes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (mes == 2 && isBissexto(ano)) {
        return 29;
    }
    return diasMes[mes - 1];
}

// Função para calcular o número total de dias desde 01/01/0000 até uma data específica
int diasTotais(struct Data data) {
    int totalDias = data.dia;

    for (int i = 0; i < data.mes - 1; i++) {
        totalDias += diasNoMes(i + 1, data.ano);
    }

    for (int i = 0; i < data.ano; i++) {
        totalDias += (isBissexto(i) ? 366 : 365);
    }

    return totalDias;
}

// Função para calcular a diferença em dias entre duas datas
int diferencaDias(struct Data data1, struct Data data2) {
    int dias1 = diasTotais(data1);
    int dias2 = diasTotais(data2);

    return (dias1 > dias2) ? (dias1 - dias2) : (dias2 - dias1);
}

int main() {
    struct Data data1, data2;

    printf("Digite a primeira data (dia mes ano): ");
    scanf("%d %d %d", &data1.dia, &data1.mes, &data1.ano);

    printf("Digite a segunda data (dia mes ano): ");
    scanf("%d %d %d", &data2.dia, &data2.mes, &data2.ano);

    int diferenca = diferencaDias(data1, data2);
    printf("A diferença entre as datas é de %d dias.\n", diferenca);

    return 0;
}