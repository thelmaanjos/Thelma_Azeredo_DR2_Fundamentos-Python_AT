import pandas as pd
import requests
from collections import Counter

class Question_11():
    
    def __init__(self):
        self.url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv" 
        self.video_games_sales = []
        self.best_10_years_seller = [] 
        self.action_games = [] 
        self.shooter_games = [] 
        self.platform_games = [] 
        self.games = []

    def build_table(self):    
        csv = requests.get(self.url).text
        lines = csv.splitlines()
        column_names = lines[0].split(",")

        for line in range(1, len(lines)):
            columns = lines[line].split(",")

            obj = {}
            for index, name in enumerate(column_names):
                obj[name] = columns[index]
            self.video_games_sales.append(obj)
        return self

    def get_three_best_publishers(self):
        for game in self.video_games_sales:
            if game["Genre"] == "Action" or game["Genre"] == "Shooter" or game["Genre"] == "Platform":
                self.games.append(game)
        
        print("\nThe three brands that published the most games of the three genres combined:\n")
        best_seller = Counter(map(lambda game: game["Publisher"], self.games)).most_common(3)
        print(f"1: {best_seller[0][0]} with {best_seller[0][1]} publications")
        print(f"2: {best_seller[1][0]} with {best_seller[1][1]} publications")
        print(f"3: {best_seller[2][0]} with {best_seller[2][1]} publications")
        return self
 
    def get_three_best_sellers(self):
        df = pd.DataFrame(self.games)
        df = df.groupby(["Publisher", "Global_Sales"],as_index=False).count()
        df = df.groupby("Publisher").count()
        print("\nThree top-selling brands of the three genres combined: \n")
        print(df.sort_values(by="Global_Sales", ascending=False).head(3))
        return self
    
    def get_list_best_sellers_10_years(self):
        for game in self.games: 
            try:
                if int(game["Year_of_Release"]) >= 2011:
                    self.best_10_years_seller.append(game)
                    if game["Genre"] == "Action":
                        self.action_games.append(game)
                    elif game["Genre"] == "Shooter":
                        self.shooter_games.append(game)
                    else:
                        self.platform_games.append(game)
            except:
                pass
        return self
        
    def get_ten_years_best_sellers(self):
        best_publisher_platform = Counter(map(lambda game: game["Publisher"], self.platform_games)).most_common(1)[0]
        print(f"\nThe brand with the most platform games publications in the last 10 years is {best_publisher_platform[0]} with {best_publisher_platform[1]} publications")
        best_publisher_shooter = Counter(map(lambda game: game["Publisher"], self.shooter_games)).most_common(1)[0]
        print(f"The brand with the most shooter games publications in the last 10 years is {best_publisher_shooter[0]} with {best_publisher_shooter[1]} publicações")
        best_publisher_action = Counter(map(lambda game: game["Publisher"], self.action_games)).most_common(1)[0] 
        print(f"The brand with the most action games publications in the last 10 years is {best_publisher_action[0]} with {best_publisher_action[1]} publications") 
        return self

    def get_best_seller_action(self):
        df_action_sales = pd.DataFrame(self.action_games, columns=["JP_Sales", "Publisher", "Name", "Genre"]) 
        df_action_sales = df_action_sales["JP_Sales"].groupby(df_action_sales["Publisher"]).sum() 
        df_action_sales = df_action_sales.to_frame() 
        best_JP_seller = df_action_sales.sort_values("JP_Sales", ascending=False).head(1).to_dict()
        for key, value in best_JP_seller["JP_Sales"].items():
            print(f"\nAction games best sales since 2011: {key} with {value}") 
        return self
        
    def get_best_seller_platform(self):
        df_platform_sales = pd.DataFrame(self.platform_games, columns=["JP_Sales", "Publisher", "Name", "Genre"])
        df_platform_sales = df_platform_sales["JP_Sales"].groupby(df_platform_sales["Publisher"]).sum()
        df_platform_sales = df_platform_sales.to_frame() 
        best_JP_seller = df_platform_sales.sort_values("JP_Sales", ascending=False).head(1).to_dict()
        for key, value in best_JP_seller["JP_Sales"].items():
            print(f"Platform games best sales since 2011: {key} with {value}")
        return self
    
    def get_best_seller_shooter(self):
        df_shooter_sales = pd.DataFrame(self.shooter_games, columns=["JP_Sales", "Publisher", "Name", "Genre"])
        df_shooter_sales = df_shooter_sales["JP_Sales"].groupby(df_shooter_sales["Publisher"]).sum()
        df_shooter_sales = df_shooter_sales.to_frame() 
        best_JP_seller = df_shooter_sales.sort_values("JP_Sales", ascending=False).head(1).to_dict()
        for key, value in best_JP_seller["JP_Sales"].items():
            print(f"Shooter games best sales since 2011: {key} with {value}")
        return self
        

def main():
    Question_11().build_table().get_three_best_publishers().get_three_best_sellers().get_list_best_sellers_10_years().get_ten_years_best_sellers().get_best_seller_action().get_best_seller_platform().get_best_seller_shooter()

main()