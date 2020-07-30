import instaloader
mod = instaloader.Instaloader()
a= input("Enter Username: ")
mod.download_profile(a,profile_pic_only = True)