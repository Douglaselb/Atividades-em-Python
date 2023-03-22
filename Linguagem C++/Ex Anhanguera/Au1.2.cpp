#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char const *argv[])
{
    float nota1, nota2, nota3, media;

/*    printf("Informe o valor da primeira nota: ");
    scanf("%f", &nota1);

    printf("Digite o valor da segunda nota: ");
    scanf("%f", &nota2);

    printf("Digite o valor da terceira nota: ");
    scanf("%f", &nota3);

    media = (nota1 + nota2 + nota3)/3;
    printf("A media do semestre: %f", media);
*/

    cout<<"Digite o valor da primeira nota: ";
    cin>>nota1;

    cout<<"Digite o valor da segunda nota: ";
    cin>>nota2;

    cout<<"Digite o valor da terceira nota: ";
    cin>>nota3;

    media = (nota1 + nota2 + nota3)/3;

    cout<<"Media do semestre foi: "<<media;

    return 0;
}
