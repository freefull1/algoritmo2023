def log_ent(n, b):
    if n < b:
        return 0
    else:
        return 1 + log_ent(n//b, b)

print(log_ent(16, 2)) 

