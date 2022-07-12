class Player:

    firstTeam = []

    def __init__(self, name, age, position, team, player):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
#1
        self.players = players()


players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

#2 
player_kevin = players(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
player_jason = players(jason["name"], jason["age"], jason["position"], jason["team"])
player_kyrie = players(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])

#3
player_kevin.firstTeam.append()
player_jason.firstTeam.append()
player_kyrie.firstTeam.append()

#4
@classmethod
    def get_team(cls, team_list)
