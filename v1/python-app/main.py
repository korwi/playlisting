from playlist_to_length import playlist_to_length
from playlist_to_length import sum_un_lists
from time_parser import time_parser
"""
for i in ["https://www.youtube.com/playlist?list=PLEK0ehXF1XBtaFRg6P1sC1Q-iGTvg3Ksj", "https://www.youtube.com/playlist?list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl", "https://www.youtube.com/playlist?list=PLyfE3pnEkrBMiCPLNDhft9hmeXK1wtkGF", "https://www.youtube.com/playlist?list=PLo3pNg0eiPc8rRO3XqFnl1Je2GTu7am-F", "https://www.youtube.com/playlist?list=PLY37FwYZkYU4BQL6YxUv9fhfbsdlRsnze", "https://www.youtube.com/playlist?list=PLnQX-jgAF5pTkwtUuVpqS5tuWmJ-6ZM-Z", "https://www.youtube.com/playlist?list=PLnQX-jgAF5pTkwtUuVpqS5tuWmJ-6ZM-Z", "https://www.youtube.com/playlist?list=PLZDug8AltzwDl5YrN4cBv3j97TD4rH3Gq", "https://www.youtube.com/playlist?list=PLpfv1AIjenVMmT7iRx6Nwu6uG6A9gSD0j", "https://www.youtube.com/playlist?list=PLxjfhCENE_F31wm-dRIndUuwaHcQVjc9w"]:
    print(playlist_to_length(i))
"""
print(sum_un_lists([0, 0, 0, 0], [0, 0, 0, 0]))
print(sum_un_lists([1, 2, 0, 3], [1, 0, 2, 3]))
print(sum_un_lists([70, 30, 0, 0], [0, 3240, 30, 0], [0, 0, 2345, 54]))
print(sum_un_lists([3, 61, 75, 23]))
"""
IDEAS RIGHT NOW:
give average video duration
give playlist length when sped up
give number of videos
give the top 5 channels from the playlist videos
give the person who made the playlist and info about them
give the total combined view count
total combined like count
total combined number of comments
"""
