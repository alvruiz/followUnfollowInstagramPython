# followUnfollowInstagramPython
A program to check who is not following you from your following users. 
The version used for the development of this project is Python 3.9.2
## How to use it?
- Go to this  [page](https://www.instagram.com/download/request), fill with your email and check the JSON box.
  
![image](https://github.com/alvruiz/followUnfollowInstagramPython/assets/97341669/ea14859e-1b07-4ed3-8e6d-96ebf71318ce)  
- Wait the email with your data (it could take up to 48h)  
- Download de compressed file and go into the follower_and_following folder. Copy the "following.json" and "followers_1.json" files to the root folder of this repository. The result is this:
   
![image](https://github.com/alvruiz/followUnfollowInstagramPython/assets/97341669/18eb771f-d32e-40a8-9fcf-54fd180af3a3)
- Execute the program. How? Go to the root folder and open a terminal (maybe you will need root permissions to execute this) and write:

  ```python .\followUnfollow.py .\following.json .\followers_1.json```

  The format of the input is: python .\followUnfollow.py file_with_users_following file_with_followers
- Then you will see in the output all the persons that aren't following you

  
