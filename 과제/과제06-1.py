def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def generate_divisors_list():
    divisors_list = [None, None]
    for i in range(2, 101):
        divisors_list.append(get_divisors(i))
    return divisors_list

def print_divisors_list(divisors_list):
    for i, divisors in enumerate(divisors_list):
        print(f"{i}: {divisors}")

def main():
    divisors_list = generate_divisors_list()
    print_divisors_list(divisors_list)

if __name__ == "__main__":
    main()
