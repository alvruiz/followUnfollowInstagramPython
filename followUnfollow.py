# This is a sample Python script.
import sys
import json

from Model.Follower import InstaInfo


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if((len(sys.argv)!=3  and len(sys.argv)!=2) or (len(sys.argv)==2 and sys.argv[1]!="-h")):
        exit("########################################"
             "\nInsert arguments correctly: \n\t ./followUnfollow following.json, followers.json\n"
             "########################################");
    if(sys.argv[1] == "-h"):
        exit("########################################"
             "\nRun code with the following format:\n\t ./followUnfollow following.json, followers.json\n"
             "########################################");
    try:
        following = open(sys.argv[1])
        followers = open(sys.argv[2])
    except Exception as e:
        exit(str(e));
    following_json = json.load(following);
    followers_json = json.load(followers);
    followers_user_array = [];
    following_user_array = [];

    for follower_user in followers_json:
      followers_user_array.append(InstaInfo(**follower_user).string_lista_data.value);

    for title_attr in following_json:
      following_attr = title_attr;

    for following_user in following_json[following_attr]:
      following_user_array.append(InstaInfo(**following_user).string_lista_data.value);
    print("\n#######################################");
    print("Tienes %s seguidores y sigues a %s" % ((len(followers_user_array)),len(following_user_array)));
    print("#######################################\n");
    print("No te siguen los siguiente usuarios:\n");
    result = [];
    for follow in following_user_array:
      if (follow not in followers_user_array):
        result.append(follow);

    for user in result:
      print("User: %s" % (user))

    print("\nTotal que sigues y no te siguen: %d" % (len(result)))
