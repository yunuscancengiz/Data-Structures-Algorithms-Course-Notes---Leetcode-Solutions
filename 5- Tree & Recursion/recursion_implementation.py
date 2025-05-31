''' 
Recursion:
    * İç içe geçme durumudur
    * Bir fonksiyonun kendi içinde tekrar çağrılması
    * Bir veri yapısının kendi instance'ını kendi içinde kullanması
'''

def calculate_factorial(num):
    # edge case - exit condition --> yazılmazsa sonsuz döngü
    if num == 0:
        return 1
    return num * calculate_factorial(num=num - 1)


def calculate_contigous_sum(num):
    if num == 0:
        return 0
    return num + calculate_contigous_sum(num=num - 1)


if __name__ == '__main__':
    print(calculate_factorial(num=5))
    print(calculate_contigous_sum(num=120))