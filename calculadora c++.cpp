#include <iostream>
using namespace std;
int main (){
int n1,n2;
int suma = 0;
int resta=0,mul=0,div=0,res=0;
cout<<"esta es una calculadora de c++:p\n";
cout<<"digite el primer numero ";cin>>n1;
cout<<"digite el segundo numero ";cin>>n2;
cout<<"bien ahora que quiere hacer suma(1) resta(2) multiplicacion(3)division(4)\n";cin>>res;
switch (res) {
        case 1:
            suma = n1 + n2;
            cout << "Resultado de la suma: " << suma << endl;
            break;
        case 2:
            resta = n1 - n2;
            cout << "Resultado de la resta: " << resta << endl;
            break;
        case 3:
            mul = n1 * n2;
            cout << "Resultado de la multiplicacion: " << mul << endl;
            break;
        case 4:
            if (n2 != 0) {
                div = n1 / n2;
                cout << "Resultado de la division: " << div << endl;
            } else {
                cout << "No se puede dividir entre cero." << endl;
            }
            break;
        default:
            cout << "Opción no válida." << endl;
    }
return 0;
}