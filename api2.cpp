#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main() {
    int numeroGenerado, numeroIngresado, min, max, intentos, intentosRestantes;

    cout << "Bienvenido al juego de adivinar el numero!" << endl;
    cout << "Ingrese el rango inferior: ";
    cin >> min;
    cout << "Ingrese el rango superior: ";
    cin >> max;
    cout << "Ingrese la cantidad de intentos: ";
    cin >> intentos;

    if (min < 0 || max > 100 || intentos <= 0) {
        cout << "Los valores ingresados no son validos. Intente nuevamente." << endl;
        return 0;
    }

    srand(time(0));
    numeroGenerado = rand() % (max - min + 1) + min;

    for (intentosRestantes = intentos; intentosRestantes > 0; intentosRestantes--) {
        cout << "Intento #" << (intentos - intentosRestantes + 1) << " de " << intentos << "." << endl;
        cout << "Ingrese su numero: ";
        cin >> numeroIngresado;

        if (numeroIngresado < min || numeroIngresado > max) {
            cout << "El numero ingresado no se encuentra dentro de los rangos establecidos." << endl;
        } else if (numeroIngresado < numeroGenerado) {
            cout << "El numero ingresado es menor que el numero generado." << endl;
        } else if (numeroIngresado > numeroGenerado) {
            cout << "El numero ingresado es mayor que el numero generado." << endl;
        } else {
            cout << "Felicidades! Usted ha adivinado el numero." << endl;
            return 0;
        }
    }

    cout << "Lo siento, no ha podido adivinar el numero en los intentos dados." << endl;
    cout << "El numero generado era: " << numeroGenerado << endl;

    return 0;
}

