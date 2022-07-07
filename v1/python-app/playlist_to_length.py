import re

list_of_example_playlists = ["https://www.youtube.com/playlist?list=PLEK0ehXF1XBtaFRg6P1sC1Q-iGTvg3Ksj", "https://www.youtube.com/playlist?list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl", "https://www.youtube.com/playlist?list=PLyfE3pnEkrBMiCPLNDhft9hmeXK1wtkGF", "https://www.youtube.com/playlist?list=PLo3pNg0eiPc8rRO3XqFnl1Je2GTu7am-F", "https://www.youtube.com/playlist?list=PLY37FwYZkYU4BQL6YxUv9fhfbsdlRsnze", "https://www.youtube.com/playlist?list=PLnQX-jgAF5pTkwtUuVpqS5tuWmJ-6ZM-Z", "https://www.youtube.com/playlist?list=PLnQX-jgAF5pTkwtUuVpqS5tuWmJ-6ZM-Z", "https://www.youtube.com/playlist?list=PLZDug8AltzwDl5YrN4cBv3j97TD4rH3Gq", "https://www.youtube.com/playlist?list=PLpfv1AIjenVMmT7iRx6Nwu6uG6A9gSD0j", "https://www.youtube.com/playlist?list=PLxjfhCENE_F31wm-dRIndUuwaHcQVjc9w"]
list_of_example_times = ["PT3M21S", "PT2M57S", "PT5M43S", "PT2M9S", "PT3M13S", "PT4M31S", "PT4M24S", "PT3M56S", "PT4M40S", "PT2M37S", "PT4M22S", "PT4M33S", "PT3M21S", "PT4M30S", "PT4M44S", "PT4M42S", "PT4M47S", "PT5M23S", "PT3M6S", "PT4M16S", "PT18M7S", "PT22M58S", "PT16M15S", "PT18M48S", "PT17M11S", "PT9M26S", "PT24M26S", "PT27M29S", "PT6M2S", "PT57M3S", "PT9M26S", "PT24M26S", "PT27M29S", "PT6M2S", "PT57M3S", "PT6M56S", "PT28M10S", "PT32M18S", "PT27M", "PT29M20S", "PT7M14S", "PT7M", "PT4M10S", "PT3M45S", "PT3M18S", "PT7D7S", "PT2D4H1S", "PT2D4H", "PT2D43M1S"]


txt = "https://www.youtube.com/playlist?list=PLxjfhCENE_F1GBWSK3W6UDX7LxX0sh1uH"

def sum_un_lists(*args):
    c = [0, 0, 0, 0]
    for list in args:
        for n, i in enumerate(list[::-1]):
            c[n] = c[n]+i
    if c[0]>=60:
        c[1]+=c[0]//60
        c[0]+=(c[0]%60 -c[0])
    if c[1]>=60:
        c[2]+=c[1]//60
        c[1]+=(c[1]%60 -c[1])
    if c[2]>=24:
        c[3]+=c[2]//24
        c[2]+=(c[2]%24 -c[2])
    return c[::-1]

def url_to_id(x):
    # youtube domains only
    return str(x)[-34:] if (re.match(r"^playlist", str(x)[24:]) and re.match(r"^list=", str(x)[33:]) and re.match(r"^https://www.youtube.com", str(x)) and (len(x)==72)) else "invalid url, not a youtube url or not a youtube playlist"

from googleapiclient.discovery import build, HttpError

# yt api set up
api_key = "AIzaSyBxcoSpqCCANK-PQqO7cQVS6E9deEENA4w"
youtube = build('youtube', 'v3', developerKey=api_key) 

def nothing_to_zero(x):
    zeros_set = ["S", "M", "H", "D"]
    for n, i in enumerate(zeros_set):
        if re.search(i, x) == None:
            x = (x+"0S") if (n == 0) else x
            x = ((("PT0M"+x[2:]) if (re.search("D", x) == None) else re.split("D",x)[0]+"D0M"+re.split("D",x)[1]) if (re.search("H", x) == None) else re.split("H",x)[0]+"H0M"+re.split("H",x)[1]) if (n == 1) else x
            x = (("PT0H"+x[2:]) if (re.search("D", x) == None) else re.split("D",x)[0]+"D0H"+re.split("D",x)[1]) if (n == 2) else x
            x = ("PT0D"+x[2:])if n==3 else x
    return x

def time_parser(x):
    if x[1] != "T": x = "PT"+re.sub("T", '', x[1:])
    out, n = [[]], 0
    for i in re.findall("[d -d]", nothing_to_zero(x)[2:][::-1][1:]):
        try: out[n].append(int(i))
        except ValueError: 
            out.append([])
            n += 1
    return [int(''.join(str(j) for j in i[::-1])) for i in out][::-1]

def until_4(x):
    if len(x) < 4:
        x.append(0)
        return until_4(x)
    return x

def playlist_to_length(x):
    try:
        next_page_token, final = None, []
        while True:
            pl_request = youtube.playlistItems().list(part='contentDetails', playlistId=url_to_id(x), maxResults=50, pageToken=next_page_token).execute()
            #print(len(pl_request.execute()['items']))
            id_list = [item['contentDetails']['videoId'] for item in pl_request['items']]
            requests_vids = youtube.videos().list(part="contentDetails", id=','.join(id_list)).execute()['items']
            out = [[] for i in requests_vids]
            tot = [0, 0, 0, 0]
            for n, i in enumerate(requests_vids):
                #length 
                out[n].append(time_parser(i['contentDetails']['duration']))
            for i in out:
                tot = sum_un_lists(tot, (list(i[0])))
            for i in tot:
                if i == 0: 
                    tot.pop(0)
                else:
                    break
            tot = until_4(tot[::-1])
            final.append(tot)
            next_page_token = pl_request.get('nextPageToken')
            if not (next_page_token): break
        new_final = []
        for i in list(final):
            this_ = []
            for j in list(i):
                this_.append(int(j))
            new_final.append(this_)
        p1, p2, p3, p4 = 0, 0, 0, 0
        for i in new_final:
            p1 += i[0]
            p2 += i[1]
            p3 += i[2]
            p4 += i[3]
        if p1>=60:
            p2+=p1//60
            p1+=(p1%60 -p1)
        if p2>=60:
            p3+=p2//60
            p2+=(p2%60 -p2)
        if p3>=24:
            p4+=p3//24
            p3+=(p3%24 -p3)
        return (p1+p2*60+p3*(60*60)+p4*(60*60*24)), [p1, p2, p3, p4]
    except HttpError:
        return "playlist not found//http error"
