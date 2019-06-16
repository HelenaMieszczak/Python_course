import webbrowser
import urllib
import re


def open_site(site):
    part = r"https://\http://\www\.pl\.com"
    check = re.search(part, site)
    if check:
        webbrowser.open(site)
    else:
        raise urllib.URLError("Wrong site address")


# if r"$(.pl|com).site":
#     webbrowser.open(site)
#     if r"^(https://|http://|www).site":


def main():
    user_site = input("Enter site address: ")
    open_site(user_site)


main()
