CARD_PUBLIC_KEY = 14012298
DOOR_PUBLIC_KEY = 74241

def find_loop(subject_nbr):
    n = 1
    loop_size = 1
    while True:
        n = subject_nbr * n
        n = n % 20201227
        if n == DOOR_PUBLIC_KEY:
            return loop_size 
        loop_size += 1

def find_encryption(pub_key, loop_size):
    e = 1
    for _ in range(loop_size):
        e = pub_key * e
        e = e % 20201227
    return e

loop_size= find_loop(7)
encryption_key = find_encryption(CARD_PUBLIC_KEY, loop_size)
print(encryption_key)