import math

all_cities = set()
all_airlines = set()

def city_pair_wise() -> dict:
    f = open('Citypairwise Quarterly International  Air Traffic To And From The Indian Territory.csv')
    cities = set()
    text = f.readlines()
    f.close()

    line_list = []
    for line in text:
        line_list.append(line.split(','))
    line_list.pop(0)
    
    for line in text:
        data = line.split(',')
        cities.add(data[3])
    cities.remove('CITY2')

    global all_cities
    
    for city in cities:
        all_cities.add(city)
        # print(city)

    # print('no of cities: ', len(cities))    

    passengers_citywise_quarterly = dict()    

    for line in line_list:
        city = line[3]
        year = line[0]
        quarter = line[1]
        traffic_flow = line[4]
        key = city+'_'+year+'_'+quarter
        passengers_citywise_quarterly[key] = passengers_citywise_quarterly.get(key, 0)+int(traffic_flow)

    # print(passengers_citywise_quarterly)
    # print()
    # print()
    return passengers_citywise_quarterly


def airline_wise() -> dict:
    f = open('Airlinewise Monthly International Air Traffic To And From The Indian Territory.csv')
    text = f.readlines()
    f.close()

    line_list = []
    for line in text:
        line_list.append(line.split(','))
    line_list.pop(0)

    airlines = set()
    airline_traffic = dict()
    airline_traffic_quarterly = dict()

    for line in line_list:
        if line[4] == 'DOMESTIC':
            year = line[0]
            quarter = line[2]
            airline = line[3]
            airlines.add(airline)
            traffic_flow = line[5]

            key1 = airline+'_'+year+'_'+quarter
            key2 = year+'_'+quarter

            airline_traffic[key1] = airline_traffic.get(key1, 0) + int(traffic_flow) 
            airline_traffic_quarterly[key2] = airline_traffic_quarterly.get(key2, 0) + int(traffic_flow)

    global all_airlines
    for airline in airlines:
        all_airlines.add(airline)
        # print(airline)

    # print(airline_traffic)
    # print()
    # print(airline_traffic_quarterly)        

    airline_percent = dict()

    for airline in airlines:
        for line in line_list:
            if line[4] == 'DOMESTIC':
                year = line[0]
                quarter = line[2]
                airline = line[3]
                traffic_flow = line[5]

                key1 = airline+'_'+year+'_'+quarter
                key2 = year+'_'+quarter

                airline_percent[key1] = (airline_traffic[key1]/airline_traffic_quarterly[key2]) * 100
        
    # print()
    # print(airline_percent)
    return airline_percent


def generate_csv(passengers_citywise_quarterly: dict, airline_percent: dict):
    # year, quarter, city, airline, predicted_traffic
    f = open('predicted_traffic.csv', 'w+')
    quarters = ('Q1', 'Q2', 'Q3', 'Q4')
    years = (2015, 2016, 2017)

    first_line = 'year,quarter,city,airline,predicted_traffic'.swapcase()
    print(first_line, file=f)

    for year in years:
        for quarter in quarters:
            for city in sorted(all_cities):
                passengers_key = city+'_'+str(year)+'_'+quarter
                if passengers_key not in passengers_citywise_quarterly:
                    continue

                for airline in sorted(all_airlines):
                    air_key = airline+'_'+str(year)+'_'+quarter
                    if air_key not in airline_percent:
                        continue

                    traffic = math.floor((airline_percent[air_key] * passengers_citywise_quarterly[passengers_key])/100)
                    # print(traffic)
                    print(year, quarter, city, airline, traffic, sep=',', file=f)

    f.close()                

    
def main():
    passengers_citywise_quarterly = city_pair_wise()
    airline_percent = airline_wise()
    generate_csv(passengers_citywise_quarterly, airline_percent)
    print('Predicted traffic generated in predicted_traffic.csv file')


if __name__ == '__main__':
    main()
    

        

    
