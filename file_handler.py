def save_data(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data
