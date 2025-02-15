import musicalbeeps as mb

player = mb.Player(volume=0.1, mute_output=False)

#Rhythm Dictionary
rd = {
    "Redonda": 2.0,
    "Blanca" : 1.0,
    "Negra" : 0.5,
    "Corchea" : 0.25,
    "RedondaPuntillo": 3.0,
    "BlancaPuntillo": 1.5,
    "NegraPuntillo": 0.75,
    "CorcheaPuntillo": 0.375,
}

musicData = [
    ["E", "Corchea"],
    ["E", "Corchea"],
    ["E", "Negra"],
    ["E", "Corchea"],
    ["A", "Corchea"],
    ["A", "Corchea"],
    ["A", "Corchea"],
    ["A", "Corchea"],
    ["G", "Corchea"],
    ["G", "Corchea"],
    ["G", "Corchea"],
    ["G", "Corchea"],
    ["C", "Corchea"],
    ["C", "Corchea"],
    ["C", "Corchea"],
    ["C", "Corchea"],
    ["D", "Corchea"],
    ["D", "Corchea"],
    ["D", "Corchea"],
    ["D", "Corchea"],
    ["D", "Corchea"],
    ["D", "Corchea"],
    ["E", "Corchea"],
    ["E", "Corchea"],
    ["E", "Corchea"],
    ["E", "Corchea"],
    ["G", "Corchea"],
    ["F", "Negra"],
    ["F", "Corchea"],
    ["C", "Corchea"],
    ["D", "Negra"],
    ["D", "Corchea"],
    ["A", "Corchea"],
    ["G", "Negra"],
    ["F", "Negra"],
    ["E", "Negra"],
    ["E", "Corchea"],
    ["E", "Corchea"],
    ["G", "Negra"],
    ["F", "Corchea"],
    ["F", "Corchea"],
    ["D", "Negra"],
    ["D", "Corchea"],
    ["F", "Corchea"],
    ["E", "Corchea"],
    ["F", "Negra"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Negra"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Corchea"],
    ["A", "Blanca"],
    ["D", "Negra"],
    ["D", "Corchea"],
    ["G", "Corchea"],
    ["F", "Negra"],
    ["F", "Negra"],
    ["E", "Negra"],
    ["E", "Corchea"],
    ["E", "Corchea"],
    ["G", "Negra"],
    ["F", "Corchea"],
    ["F", "Corchea"],
    ["D", "Negra"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Corchea"],
    ["F", "Negra"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Negra"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["E", "Corchea"],
    ["F", "Corchea"],
    ["F", "Negra"]
        ]

# Test
for i in range(len(musicData)):
    player.play_note(musicData[i][0],rd[musicData[i][1]])
