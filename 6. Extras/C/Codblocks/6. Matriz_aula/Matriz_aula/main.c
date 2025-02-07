#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m, n, i, j;
    printf("Quntas linhas vai ter essa matiriz: ");
    scanf("%d", &m);
    printf("Quntas colunas vai ter essa matiriz: ");
    scanf("%d", &n);

    int mat [m][n];
    for (i = 0; i < M; i++)
    {
        for (j = 0; j < N; j++)
        {
            printf("Elemento [%d,%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }
    printf("\nMATRIZ DIGITADA:\n");
    for (i = 0; i < M; i++)
    {
        for (j = 0; j < N; j++)
        {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
    return 0;
}


return 0;
}
