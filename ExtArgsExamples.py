def hypervolume(*lengths):
    i = iter(lengths)
    volume = 1 if len(lengths) > 0 else 0
    for length in lengths:
        volume *= length
    return volume

print(hypervolume(3,4))
print(hypervolume(3,4,5))
print(hypervolume(3))
print(hypervolume())