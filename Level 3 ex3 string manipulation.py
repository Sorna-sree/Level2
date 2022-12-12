#Ask the user what he likes for breakfast ,lunch and dinner.
# Print  'user like <input> for breakfast", "user likes <input> for lunch" , etc.

food=input("what he likes for breakfast,lunch and dinner:  ")
food=food.split(",")
print(f"user likes {food[0]} for breakfast, user likes {food[1]} for lunch , user likes {food[2]} for dinner")
