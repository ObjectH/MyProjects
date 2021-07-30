// Эта программа может определить, сколько лет было/будет человеку в каком-либо году.
// Она принимает нынешний возраст пользователя, год его рождения и год, который интересует пользователя.
// Затем проверяется, был ли ввод корректным, после чего считается разница между годами, прибавляется к возрасту,
// и в зависимости от полученного результата выводится сообщение.

#include <sstream>
#include <iostream>
#include <string>
using namespace std;
//Проверка, точно ли пользователь ввёл число, подходящее для типа integer
 bool check(string s, int n, bool* is_num) {
	try {
		n = stoi(s);
		*is_num = true;
	}
	catch (std::invalid_argument) {
		cout << "Input an integer, please.\n";
		*is_num = false;
	}
	catch (std::out_of_range) {
		cout << "Too big number.\n";
		*is_num = false;
	}
	catch (...) {
		cout << "Try again, please.\n";
		*is_num = false;
	}
	if (not *is_num) {
		cout << "\n";
	}
	return *is_num;
}
int main()
{
    while (true) 
	{
        bool is_num = true;
		int age = 0;
        int year = 0;
        int year_future = 0;
        int difference = 0;
		string age_str = "";
		string year_str = "";
		string year_future_str = "";
        //Запрос возраста пользователя
        cout << "How old are you? ";
        cin >> age_str;
		check(age_str, age, &is_num);
		if (is_num) {
			//Проверка, не ввёл ли польователь возраст, которого не может быть
			age = stoi(age_str);
			if (age >= 0 && age <= 122) {
				//Запрос нынешнего года
				cout << "What year is it now? ";
				cin >> year_str;
				check(year_str, year, &is_num);
				if (is_num){
					year = stoi(year_str);
					//Запрос интересующего пользователя года
					cout << "Your age in what year do you need to know? ";
					cin >> year_future_str;
					check(year_future_str, year_future, &is_num);
					if (is_num){
						year_future = stoi(year_future_str);
						//Подсчёт разницы между годами и возраста, который был/будет в запрашиваемом году
						difference = year_future - year;
						age += difference;
						//Запрашиваемый год меньше нынешнего, при этом возраст выражен положительным числом
						if (difference < 0 && age > 0) {
							cout << "You were " << age << " years old.\n";
						}
						//Если запрашиваемый год меньше нынешнего, при этом возраст оказался отрицательным, т. е. в то время пользователь ещё не родился
						else if (difference < 0 && age < 0) {
							cout << "It was " << age * -1 << " years before your birth.\n";
						}
						//Если пользователь ввёл одинаковые годы
						else if (year == year_future) {
							cout << "You have inputed identical years\n";
						}
						//Если возраст оказался больше, чем 122 (рекордный возраст человека)
						else if (difference > 0 && age > 122) {
							cout << "As calculated, you will be " << age << " years old, but the oldest human in the world was only 122.\n";
						}
						//Если возраст оказался равен нулю
						else if (age == 0) {
							cout << "This is your birth year\n";
						}
						//Если возраст меньше 122, выражен положительным числом, и пользователь ввёл разные годы
						else {
							cout << "You will be " << age << " years old.\n";
						}
					}
					else {
						continue;
					}
				}
				else {
					continue;
				}
			}
			else {
				"Are you sure?\n";
			}
		}
		else {
			continue;
		}
		cout << "\n";
	}

    return 0;
}
