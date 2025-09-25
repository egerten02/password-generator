import random, string

def main():
    sL = string.ascii_lowercase
    sU = string.ascii_uppercase
    sD = string.digits
    sP = string.punctuation

    pass_len = int(input("Password length\n>"))

    cluster = []
    cluster.extend(list(sL))
    cluster.extend(list(sU))
    cluster.extend(list(sD))
    cluster.extend(list(sP))

    password = ''
    password = password.join(random.sample(cluster, pass_len))

    print("Your password:", password)

main()