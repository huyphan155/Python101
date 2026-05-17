name = "sum"
type = "Calico cat"
is_dog = False
is_cat = True


def print_sumInfo(name, type, is_dog, is_cat, sound):
    print(f'Hi,iam {name}')
    print(f'Iam a {type}')
    print(f'{is_dog}, Iam a dog')
    print(f'{is_cat}, Iam a cat')
    for i in range(sound):
        print('meoz')
    print(f'{sound+1} meozzzzzzzzzz, cause im a rebel cat')


sound = int (input("enter number of meoz : "))
print_sumInfo(name,type,is_dog,is_cat, sound)

