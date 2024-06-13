import requests
import os
from colorama import Fore, Style, init

os.system("pip install requests")
os.system("clear")

init(autoreset=True)

print(Fore.RED + """
producer  〔coded by enesxsec〕
instagram 〔xsecit〕
github    〔https://github.com/ghost0x02〕""")

print(Fore.MAGENTA + """
          .,
.      _,'f----.._
|\ ,-'"/  |     ,'
|,_  ,--.      /
/,-. ,'`.     (_
f  o|  o|__     "`-.
,-._.,--'_ `.   _.,-`
`"' ___.,'` j,-'
  `-.__.,--'     Gen3 1.0v """)


def check_username(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "YouTube": f"https://www.youtube.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
    }

    for platform, url in platforms.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] {platform}: {Style.RESET_ALL}{url}")
        else:
            print(f"{Fore.RED}[-] {platform}: {Style.RESET_ALL}Kullanıcı bulunamadı")

if __name__ == "__main__":
    print(Fore.GREEN + "Kullanıcı adını girin ")
    username = input(Fore.RED + "root@Gen3:~ ")
    check_username(username)
    print(Style.RESET_ALL)
