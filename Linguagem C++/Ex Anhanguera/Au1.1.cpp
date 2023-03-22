#include <iostream>
#include <cstdio>

int main(int argc, char const *argv[])
{
    int idade;
    char nome[10];

    printf("Informe seu nome: ");
    scanf("%s", &nome);
    printf("Informe sua idade ");
    scanf("%d", &idade);
    printf("Nome: %s", nome);
    printf("Idade: %d", idade);

    return 0;
}
