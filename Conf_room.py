def check_room(req_details, room_details):
    if (req_details['ppl'] <= room_details['max_ppl']):
        for s,e in zip(room_details['start'], room_details['end']):
            if (req_details['start'] >= s) \
                and (req_details['end'] <= e):
                return room_details["room"], abs(req_details['room']-room_details['room'])
        
if __name__=="__main__":
    with open("rooms.txt") as fd:
        rooms = fd.read().split()
        rooms = list(map(lambda x:x.split(","), rooms))
        rooms_details = list(map(lambda x: {"room":float(x[0]), "max_ppl":int(x[1]), "start":x[2::2], "end":x[3::2]},rooms))

    req = input()
    req_details = req.split(",")
    req_details = {"ppl":int(req_details[0]), "room":int(req_details[1]), "start":req_details[2], "end":req_details[3]}

    selected = None
    diff = None
    for room in rooms_details:
        if diff == None:
            diff = abs(req_details['room']-room['room'])

        if diff > abs(req_details['room']-room['room']):
            result = check_room(req_details, room)
            if result!= None:
                selected = result[0]
                diff = result[1]

    print("Room Number: ",selected)