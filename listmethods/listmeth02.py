#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

food= ["ramen","rice","kimchi","pasta","pizza"]
print(food)
print(food.count("ramen"))
print(f"ramen has counted {food.count('ramen')} in this lsit")
print(food.sort())
print(f"pasta is located at {food.index('pasta')} in this lsit")


