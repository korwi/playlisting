from playlist_to_length import playlist_to_length
from time_parser import time_parser


def display_text(playlist_link):
    length = list(playlist_to_length(str(playlist_link)))
    display = [
        "Length of playlist: "+time_parser(length[1]), 
        "At other speeds:",
        "0.25x: "+str(time_parser(length[0]/0.25)), 
        "0.5x: "+str(time_parser(length[0]/0.5)), 
        "0.75x: "+str(time_parser(length[0]/0.75)), 
        "1.25x: "+str(time_parser(length[0]/1.25)), 
        "1.5x: "+str(time_parser(length[0]/1.5)), 
        "1.75x: "+str(time_parser(length[0]/1.75)), 
        "2x: "+str(time_parser(length[0]/2))
    ]
    return display    

print(display_text("https://www.youtube.com/playlist?list=PLKeR9CeyAc9bEhQkuYBZLLQBwiFYyHV0n"))    