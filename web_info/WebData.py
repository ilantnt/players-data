
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from web_info.Player import Player





class Configuration(object):

    def __init__(self):
        with open('config.json') as json_file:
            self.data = json.load(json_file)
            print(self.data)

class WebData:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        #options.add_argument('--disable-gpu')

        conf = Configuration()
        print(conf.data)
        self.driver = webdriver.Chrome(conf.data['Driver_Path'], chrome_options=options)
        self.players = []

    def get_url_data(self, url):
        self.driver.get(url)

    def extract_player_data(self):
        """
            fetches the table of players stats and reformat the table

        """
        result_fetched = None
        while result_fetched is None:
            table_players_stats = (self.driver.find_element_by_id('player-table-statistics-body'))
            table_players_stats = table_players_stats.text

            self.players = table_players_stats.splitlines()

            if self.players != []:
                result_fetched = "got info"
            print("1.{}".format(self.players))
        # delete the unnecessary row number
        del self.players[:len(self.players):3]
        print(self.players)

    def table_to_players(self):
        """
            after table format, break each row to separate player
        :return:
        """
        print(self.players)
        for i in range(len(self.players)):

            if i % 2:
                #palyers data
                data = self.players[i].split(' ')

                #dictionary contain all player necessary data

                player_data = {}
                player_data['name'] = name
                player_data['goals'] = data[-9]
                player_data['assists'] = data[-8]
                player_data['minutes_played'] = data[-10]
                player_data['rating'] = data[-1]
                player_data['apps'] = data[-11]

                plater_sample = Player(player_data)
                print("Scraped...")



                print('\n')
            else:
                name = self.players[i]
                #print("The player name is: {}".format(self.players[i]))


