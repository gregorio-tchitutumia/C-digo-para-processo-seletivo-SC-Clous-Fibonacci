#0+1+1+2+3+5+8+13+21
def fib(numero):
    inicial=0
    inicial2=1
    for _ in range(numero):
        inicial, inicial2 = inicial2, inicial + inicial2
    ultimo=abs(inicial-inicial2)
    print(ultimo)


def get_input():
    while True:
        user_input = input("Bem-vindo coloque um número ")
        try:
            numero = int(user_input)
            if numero >= 0:
                return numero
            else: 
                print("Coloque o numero correto")
        except ValueError:
            print("Coloque apenas numero")

def main():
    n = get_input()
    fib(n)

if __name__ == "__main__":
   main()
