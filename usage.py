
from mt.amino.auth import AminoAuth
from mt.amino.scraper import AminoScraper
from mt.amino.interact import AminoInteract

# Login
auth = AminoAuth()
auth.login("example@example.com", "password")

# Scrape data
scraper = AminoScraper(auth.token)
community_info = scraper.get_community_info("12345")
print(community_info)

# Interact with a post
interact = AminoInteract(auth.token)
interact.like_post("post12345", "12345")

# Logout
auth.logout()
    