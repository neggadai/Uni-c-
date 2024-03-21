#include <iostream>
int main() {
    using namespace std;
    int s;
    int sum;
    cin >> s;

    if(s < 9) {
        if (s % 2 == 0) {
            while (s != 0) {
                s -= 2;
                sum += 1;
            }
        } else{
            sum = 1;

        }
    }
    else{
        if(s % 2 == 0){
            while (s != 0){
                s -= 2;
                sum += 1;
            }
        }
        else{
            s -= 9;
            sum +=2;

            while (s != 0){
                s -= 2;
                sum += 1;
                cout << s << endl;
                cout << sum << endl;
            }
        }
    }
    cout << sum;
    return 0;
}