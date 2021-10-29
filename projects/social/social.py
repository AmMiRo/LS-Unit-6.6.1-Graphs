import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # get total friendships
        total_frendships = num_users * avg_friendships

        # create the appropriate number of users
        for user in range(1, num_users + 1):
            self.add_user(str(user))

        # initialize list for friendships
        friendships = []

        # for each user add friendship to friendships for each user not already friends with user
        for user in range(1, num_users + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)
        
        # shuffle friendships list
        self.fisher_yates_shuffle(friendships)
        
        # random friendships will be half of friendships list
        random_friendships = friendships[:total_frendships // 2]

        # add friendship for each friendship in friendships list
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # initialize visited dict which will be returned
        visited = {}  

        # initialize q
        q = [[user_id]]

        # while paths in q
        while len(q) > 0:
            # initialize current path/friend/neighbors
            cur_path = q.pop(0)
            cur_friend = cur_path[-1]
            neighbors = self.friendships[cur_friend]
            # if cur_friend is not in visited put it in visited
            if cur_friend not in visited:
                visited[cur_friend] = cur_path
                # if any neighbors for each neighbor add path with appended neighbor to q
                if len(neighbors) > 0:
                    for neighbor in neighbors:
                        q.append(cur_path + [neighbor])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
