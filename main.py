
from web_info.WebData import ScrapeWebData

class Mainer():
    def stam(self):
        return


if __name__ == '__main__':
    try:
        handler = ScrapeWebData()
        handler.get_url_data("https://www.whoscored.com/Teams/63/Show/Spain-{0}".format("Atletico-Madrid"))
        handler.extract_players_data()
        players_insert = handler.parse_players_scraped_data()

        DB_handler =
    except Exception as e:
        print("Error is: {}".format(e))