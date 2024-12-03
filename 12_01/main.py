# %%
if __name__ == "__main__":
    with open("./input_list.txt", 'r') as fp:
        lines = fp.readlines()
        
    pairs = [line.split() for line in lines]
    
    r = sorted([int(entry[1]) for entry in pairs])
    l = sorted([int(entry[0]) for entry in pairs])

    distances = [abs(l[i] - r[i]) for i in range(len(l))]
    total_distance = sum(distances)

    print(total_distance)
# %%
