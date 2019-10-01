
from web_info.WebData import WebData



if __name__ == '__main__':
    try:
        handler = WebData()
        handler.get_url_data("https://www.whoscored.com/Teams/63/Show/Spain-{0}".format("Atletico-Madrid"))
        handler.extract_player_data()
        handler.table_to_players()
    except Exception as e:
        print("Error is: {}".format(e))