import sherlock

results = sherlock('liuflee')


for result in results:
    print("Red social:", result[0])
    print("Usuario:", result[1])
    print("URL:", result[2])
    print()
