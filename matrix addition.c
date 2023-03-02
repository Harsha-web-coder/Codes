//matrix addition
#include <stdio.h>
int main() {
    int rows, columns, a[10][10], b[10][10], sum[10][10], i, j;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &columns);

    printf("\nEnter elements of 1st matrix:\n");
    for (i = 0; i < rows; ++i)
        for (j = 0; j < columns; ++j) {
            printf("Enter element a%d%d: ", i + 1, j + 1);
            scanf("%d", &a[i][j]);
        }

    printf("Enter elements of 2nd matrix:\n");
    for (i = 0; i < rows; ++i)
        for (j = 0; j < columns; ++j) {
            printf("Enter element b%d%d: ", i + 1, j + 1);
            scanf("%d", &b[i][j]);
        }

    // adding two matrices
    for (i = 0; i < rows; ++i)
        for (j = 0; j < columns; ++j) {
            sum[i][j] = a[i][j] + b[i][j];
        }

    // printing the result
    printf("\nSum of two matrices: \n");
    for (i = 0; i < rows; ++i)
        for (j = 0; j < columns; ++j) {
            printf("%d   ", sum[i][j]);
            if (j == columns - 1) {
                printf("\n\n");
            }
        }

    return 0;
}
