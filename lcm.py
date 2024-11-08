def generate_numbers(seed, a, b, M, count=12):
    print(f'a:{a}, b:{b}, M:{M}, seed:{seed}')
    for i in range(count):
        
        seed = (a * seed + b) % M
        
        print(f'x{i+1}: {seed}')
    print()

generate_numbers(0, 1, 3, 10)
generate_numbers(0, 2, 1, 10)
generate_numbers(0, 22, 1, 72)
generate_numbers(1, 11, 37, 100)
generate_numbers(10, 8, 20, 100)