def malli():
    try:
        print(1)
        raise("error")
    finally:
        print(5)


K = malli()
print(K)
