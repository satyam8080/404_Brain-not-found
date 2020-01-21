def read_data_set():
    f = open('dataset.csv')
    text = f.readlines()
    print(text)
    f.close()

    cities = set()

    for line in text:
        data = line.split(',')
        cities.add(data[2])       

    generate_csv(text, cities)


def generate_csv(line_list: list, cities: set):
    f = open('minimum_hop.csv', 'w+')
    print('airline,city1,city2,passengers from city1 to city2,passengers from city2 to city1'.swapcase(), file=f)

    for city in sorted(cities):
        for line in line_list:
            data = line.split(',')
            if city == data[2]:
                print(line, end='', file=f)

    f.close()    
    

def main():
    read_data_set()


if __name__ == '__main__':
    main()    