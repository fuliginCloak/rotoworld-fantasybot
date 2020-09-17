import json
import requests

UUID_dict = {

    'Cardinals' : '58a589f2-bb57-4002-b693-a7d4b0cc8454',
    'Falcons' : '9cd298fc-afb0-43cf-9b48-37c897ab7be2',
    'Ravens' : '10d0310b-d3a7-4944-979f-d32979267245',
    'Bills' : '21fe462d-7814-4a40-a5a7-85c199f176d8', 
    'Panthers' : '61bccd8c-d448-4287-ab5a-3a36504e47dd',
    'Bears' : '49e47174-8e87-48a4-9dc8-0757887f96f6',
    'Bengals' : 'e666d58b-a08e-4a95-804b-0e4c91026e88',
    'Browns' : 'a537e4e6-61ad-40a9-a2ae-b576263754f8',
    'Cowboys' : '3262f813-42c8-497d-9199-a24af7400111',
    'Broncos' : '2154898a-6830-49d8-a97e-fa3bb1a20698',
    'Lions' : '0f13a8cc-e316-4e98-a087-957e27aeca4e',
    'Packers' : '45f94267-2bcd-4658-ac5f-600eb9f93638',
    'Texans' : '46729892-9b7c-446f-8ff9-446693fc3341',
    'Colts' : '5cd71064-4206-4582-ab9e-669a8b21a7c7',
    'Jaguars' : 'a4e8194a-68ff-4be4-bba4-93a22ea0c546',
    'Chiefs' : '9487063c-5464-4f25-bfa3-0f987352ce19',
    'Raids' : 'c7478dfc-20ac-4bfc-9ade-f692bf80ca14',
    'Rams' : '1df34ace-5719-4a0a-9439-a85f6dca82ac',
    'Dolphins' : '1df34ace-5719-4a0a-9439-a85f6dca82ac',
    'Vikings' : '4a4837fe-861f-4da5-946b-47bc6fdc0256',
    'Patriots' : '7a476557-40f2-4860-94da-1594f608052e',
    'Saints' : '92d23f94-2cbc-4a13-8af5-aace480c4290', 
    'Giants' : '70e261bc-5424-4a05-b368-d6848a051fbf',
    'Jets' : '297d912f-ec4b-4a85-b9ee-7605cd4d54c6',
    'Eagles' : 'c1b015ed-6cc1-4b3e-83ad-8f26d593f23a',
    'Steelers' : 'fe7219ec-ca0b-40e3-a5f7-4377fb34abd3', 
    '49ers' : '18fcbd9d-5fe8-4393-a71a-49e1db2e7cec',
    'Seahawks' : 'b1d24b2c-7442-4917-bf69-d415a990ff95',
    'Buccaneers' : '83b9ba4e-72ca-4693-87cc-d217afa04942'

    }   

def nfl_database(base_url = 'https://www.rotoworld.com/api/team/depth_chart/'):



    UUID = list(UUID_dict.values())
    team_url = [base_url + i for i in UUID]

    response_all = [requests.get(i) for i in team_url]
    nfl_player_data =  [i.json() for i in response_all]

    return nfl_player_data



