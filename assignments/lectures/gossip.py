#  AND
#  OR
#  NOT

rider_name = "Sam"
has_ticket = False
vip_pass = False
height = 49
openly_bleeding = False
screaming_uncontrollably = True

if not screaming_uncontrollably:
    print("Yay!")

if height > 48 and (has_ticket or vip_pass) and (openly_bleeding or screaming_uncontrollably):
    print(rider_name + " can ride.")
else:
    print("Sorry buddy")
