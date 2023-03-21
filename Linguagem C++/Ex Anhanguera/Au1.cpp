#include <iostream>
#include <cstdlib>

using namespace std;
int main(int argc, char const *argv[])
{
    setlocale(LC_ALL,"portuguese");
int idade; // Em C++ as variagens devem ser tipadas, embora que não tenham valor definidos
char nome[10];

cout<<"Digite seu nome: ";
cin>>nome;
cout<<"Digite sua idade: ";
cin>>idade;
cout<<"Olá "<<nome<<" , a sua idade foi registrada, idade informada: "<<idade;


    return 0;
}


