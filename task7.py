# Print all friends name, contact and address for user Ram.
# Find out which user have less friends
# Find out which user have most friend in common.


user=[
        {
            "name":"Ram",
            "contact":"98342345",
            "address":"Ktm",
            "friends":[
                        
                            {"names":"Shyam", "contact":"98852331", "address":"Ktm"},
                            {"names":"Krishna", "contact":"98463454", "address":"Pkhr"},
                            {"names":"Hari", "contact":"983302589", "address":"Bkt"},

                        
            ]
        },
        {
            "name":"Shyam",
            "contact":"98334134",
            "address":"Ktm",
            "friends":[
                    
                            {"names":"Ram", "contact":"98852331", "address":"Ktm"},
                            {"names":"Krishna", "contact":"98463454", "address":"Pkhr"},
            ]

                        
        },
        {
            "name":"Hari",
             "contact":"98379854",
            "address":"Ktm",
            "friends":[
                        
                            {"names":"Ram", "contact":"98852331", "address":"Ktm"},

                        
            ]

        }

]




ram_len=len(user[0].get("friends"))
shyam_len=len(user[1].get("friends"))
hari_len=len(user[2].get("friends"))

ram_details=user[0].get("friends")
shyam_details=user[1].get("friends")
hari_detals=user[2].get("friends")


# res=list(set(ram_details).intersection(list(shyam_details.values())))

# print("Common value of ram and shyam", res)

if ram_len < shyam_len and ram_len < hari_len:
    print("User Ram has lowest friend")
elif shyam_len < ram_len and shyam_len < hari_len:
    print("User Shyam has lowest friend")
else:
    print("User Hari has lowest friend")

print(f"Name , contact and address of Ram's friend is {ram_details}")

