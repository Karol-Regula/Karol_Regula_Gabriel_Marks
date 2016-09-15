def read_csv(filename):
    with open(filename, 'r') as f:
        pairs = f.readlines()
    pair_dict = {}
    for i in pairs:
        pair = i.strip()
        if i[0] == '"':
            comma_index = pair.find('"', 1) + 1
            key = pair[1:comma_index - 1]
        else:
            comma_index = pair.find(',')
            key = pair[:comma_index]
        val = pair[comma_index + 1:]
        pair_dict[key] = val
    return pair_dict

print read_csv('occupations.csv')
            
