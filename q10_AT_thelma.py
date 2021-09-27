import pandas as pd 
import requests
from collections import Counter

class Question_10():

    def __init__(self):

        self.url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"
        #self.medal_list = self.build_table() 
        self.medal_list_filter = []
        self.data_list = []
        self.list_of_infos = []

    def build_table(self):
        csv = requests.get(self.url).text
        lines = csv.splitlines() 
        column_names = lines[0].split(",") 

        for l in range(1, len(lines)):
            column = lines[l].split(",")
            label = column[0]
            obj = {}

            for index, name in enumerate(column_names):
                obj[name] = column[index]
            self.data_list.append(obj)
        return self

    def filter_sport_by_medal(self):
        for medal in self.data_list:
            if int(medal["Year"]) >= 2001:
                if medal["NOC"] == "SWE" or medal["NOC"] == "NOR" or medal["NOC"] == "DEN":
                    if(medal["Sport"].lower() == "curling" or medal["Sport"].lower() == "skating" or medal["Sport"].lower() == "skiing" or medal["Sport"].lower() == "ice hockey"):
                        if medal["Medal"] == "Gold":
                            self.medal_list_filter.append(medal)
        return self

    def get_report(self):
        for medal in self.data_list:
            info = "Year: %s, City: %s, Sport: %s, Discipline: %s, NOC: %s, Event: %s, Event gender: %s, Medal: %s" % (medal["Year"], medal["City"],  medal["Sport"], medal["Discipline"], medal["NOC"], medal["Event"], medal["Event gender"], medal["Medal"])
            self.list_of_infos.append(info)
        return self
    
    def print_output(self):
        print("Report for total medals for each country:") 
        print(self.list_of_infos) 
        print("_____ end of report ____")
        country = Counter(map(lambda medal: medal["NOC"], self.medal_list_filter)).most_common(1) 
        print(f"\nThe biggest gold medalist was {country[0][0]} with {country[0][1]} medals.")
        

def main():
    Question_10().build_table().filter_sport_by_medal().get_report().print_output()

main()