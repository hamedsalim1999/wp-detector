import csv
from wp_detector import url_check
def parse_csv(name):
    name = name.replace('.csv', '')
    my_dic=[]
    with open(f"{name}.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            my_dic.append(url_check(row[0]))
    with open(f"{name}-out.csv", "w+") as csvfile:
        fieldnames = list(my_dic[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in my_dic:
           
            writer.writerow(url_check(row['url']))
