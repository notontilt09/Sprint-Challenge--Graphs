f = open('history.txt', 'r')
path_lengths = f.read().split('\n')
f.close

clean_up = [int(x) for x in path_lengths[:-1]]
print(min(clean_up))
