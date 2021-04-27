import instaloader

ig=instaloader.Instaloader()
profile=input("Enter Instagram Username:")
ig.download_profile(profile,profile_pic_only=True)
