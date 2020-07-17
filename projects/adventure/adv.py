from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import collections

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)





# Fill this out with directions to walk
traversal_path = []

# initialize stack
stack = []

# initialize visited dict
def makehash():
    return collections.defaultdict(makehash)
visited = makehash()
visited_set = set()

# initialize room_count
room_count = 0

# initialize directional list
directions = ["n", "e", "s", "w"]

# function to return next counter-clockwise direction
def next_counter(d):
    if d is None:
        return "n"
    current_index = directions.index(d)
    if current_index == 3:
        return directions[0]
    else:
        return directions[current_index + 1]

# function to return oposite direction
def opposite_direction(d):
    current_index = directions.index(d)
    if current_index < 1.5:
        return directions[current_index + 2]
    else:
        return directions[current_index - 2]

# function to find if room in visited has "?"
def has_q(room_id):
    count = 0
    for key in visited[room_id]:
        if visited[room_id][key] == "?":
            count += 1
    if count == 0:
        return False
    elif count > 0:
        return True

# # initialize complete
# complete = False

# # function returns true if traversal is complete
# def is_complete(room_id):
#     if has_q(room_id) == False and len(stack) == 0:
#         return True
#     elif room_count == 500:
#         return True
#     else:
#         return False

# initialize prior room
prior_room = None

# initialize current room with (room.id, direction from prior room)
current_room = (player.current_room.id, None)

# while loop if not complete (coplete only if stack is empty and current room in visited has no "?" for any value)
# get exits, check if room in visited, log room in visited, determine move, move, update prior and current
# while not complete:
#     # ge all possible exits
#     exits = player.current_room.get_exits()
#     # update visited and stack
#     if current_room[0] in visited:
#         # update visited
#         visited[prior_room[0]][prior_room[1]] = current_room[0]
#         visited[current_room[0]][current_room[1]] = prior_room[0]
#         # handle stack
#         prior_index = visited[current_room[0]]["index"]
#         stack = stack[:prior_index]
#         # check if complete
#         if is_complete(current_room[0]) is True:
#             complete = True
#             break
#     if current_room[0] not in visited:
#         # increase count
#         room_count += 1
#         # update visited
#         visited[current_room[0]]["index"] = len(stack)
#         for ex in exits:
#             if ex != current_room[1]:
#                 visited[current_room[0]][ex] = "?"
#             if ex == current_room[1]:
#                 visited[current_room[0]][ex] = prior_room[0]
#         if prior_room != None:
#             visited[prior_room[0]][prior_room[1]] = current_room[0]
#     # determine next direction
#     attempted_move = next_counter(current_room[1])
#     next_move = None
#     if has_q(current_room[0]) == False:
#         # if len(stack) == 0:
#         #     next_move = current_room[1]
#         # else:
#         next_move = stack.pop(-1)
#     elif has_q(current_room[0]) == True:
#         for ex in exits:
#             if visited[current_room[0]][ex] != "?":
#                 exits.remove(ex)
#         while next_move is None:
#             if attempted_move in exits:
#                 next_move = attempted_move
#             else: attempted_move = next_counter(attempted_move)
#     # move
#     player.travel(next_move)
#     # update prior/current rooms, stack, and traversal_path
#     reverse_move = opposite_direction(next_move)
#     prior_room = (current_room[0], next_move)
#     current_room = (player.current_room.id, reverse_move)
#     traversal_path.append(next_move)
#     stack.append(reverse_move)

# get initial directions for starting room
# pick unexplored direction and traverse clockwise until reached starting room
# repeat

starting_room = player.current_room.id

starting_exits = player.current_room.get_exits()

for initial_direction in starting_exits:
    print(traversal_path)
    complete = False
    while not complete:
        # ge all possible exits
        exits = player.current_room.get_exits()
        # update visited and stack
        if current_room[0] in visited:
            # update visited
            visited[prior_room[0]][prior_room[1]] = current_room[0]
            visited[current_room[0]][current_room[1]] = prior_room[0]
            # handle stack
            prior_index = visited[current_room[0]]["index"]
            stack = stack[:prior_index]
        if current_room[0] not in visited:
            if current_room[0] not in visited_set:
                visited_set.add(current_room[0])
            # update visited
            visited[current_room[0]]["index"] = len(stack)
            for ex in exits:
                if ex != current_room[1]:
                    visited[current_room[0]][ex] = "?"
                if ex == current_room[1]:
                    visited[current_room[0]][ex] = prior_room[0]
            if prior_room != None:
                visited[prior_room[0]][prior_room[1]] = current_room[0]
        # determine next direction
        attempted_move = next_counter(current_room[1])
        next_move = None
        if current_room[0] == starting_room:
            next_move = initial_direction
        elif has_q(current_room[0]) == False:
            next_move = stack.pop(-1)
        elif has_q(current_room[0]) == True:
            for ex in exits:
                if visited[current_room[0]][ex] != "?":
                    exits.remove(ex)
            while next_move is None:
                if attempted_move in exits:
                    next_move = attempted_move
                else: attempted_move = next_counter(attempted_move)
        # move
        player.travel(next_move)
        # update prior/current rooms, stack, and traversal_path
        if player.current_room.id != starting_room:
            reverse_move = opposite_direction(next_move)
            prior_room = (current_room[0], next_move)
            current_room = (player.current_room.id, reverse_move)
            traversal_path.append(next_move)
            stack.append(reverse_move)
        elif player.current_room.id == starting_room:
            traversal_path.append(next_move)
            stack = []
            visited = makehash()
            prior_room = None
            current_room = (player.current_room.id, None)
            complete = True

print(len(traversal_path))

not_visited = []
for i in range(1, 501):
    if i not in visited_set:
        not_visited.append(i)
print(not_visited)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
