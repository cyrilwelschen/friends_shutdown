#!/usr/bin/python3

import os.path

BASE_PATH = "/home/cyril/Desktop/Friends/F"


def current_path():
    cache = open("friends_cache.txt", "r")
    season = cache.readline(1)
    cache.close()
    return BASE_PATH + season


def current_episode():
    cache = open("friends_cache.txt", "r+")
    episode = cache.readlines()
    cache.seek(0)
    cache.write(episode[0] + str(int(episode[1])+1))
    cache.truncate()
    cache.close()
    episode = int(episode[1])
    print(episode)
    return episode


def main():
    PATH = current_path()
    if os.path.lexists(PATH):
        array_of_episodes = sorted(os.listdir(PATH))
        last = array_of_episodes[current_episode() % len(array_of_episodes)]
        found = False
        for i, name in enumerate(array_of_episodes):
            if name == last:
                os.system("cd " + PATH + "; vlc " +
                          array_of_episodes[(i+1) % len(array_of_episodes)] +
                          " " + array_of_episodes[(i+2) %
                                                  len(array_of_episodes)])
                # os.system("shutdown -P +34")
                found = True
        if not found:
            print("Couldn't find next episode")
    else:
        print("Proposed path doesn't exist!")

if __name__ == "__main__":
    main()
