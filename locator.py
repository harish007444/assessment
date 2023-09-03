from geopy.distance import geodesic

# Sample bank branch data (replace with your dataset)
bank_branches = [
    {
        "name": "Branch A",
        "brand": "Bank A",
        "location": (40.7128, -74.0060),  # Latitude and longitude
        "facilities": ["ATM", "Mortgage"],
    },
    {
        "name": "Branch B",
        "brand": "Bank B",
        "location": (40.7282, -73.7949),
        "facilities": ["ATM", "Loans"],
    },
    # Add more branches here...
]

def find_nearby_branches(user_location, radius_km=5.0):
    nearby_branches = []

    for branch in bank_branches:
        branch_location = branch["location"]
        distance = geodesic(user_location, branch_location).kilometers

        if distance <= radius_km:
            nearby_branches.append({
                "name": branch["name"],
                "brand": branch["brand"],
                "facilities": branch["facilities"],
                "distance_km": distance,
            })

    return nearby_branches

# Example user location coordinates (New York City)
user_location = (40.730610, -73.935242)
print("User Location:", user_location)

# Find nearby branches
nearby_branches = find_nearby_branches(user_location, radius_km=5.0)

for branch in nearby_branches:
    print(f"Name: {branch['name']}")
    print(f"Brand: {branch['brand']}")
    print(f"Facilities: {', '.join(branch['facilities'])}")
    print(f"Distance (km): {branch['distance_km']:.2f}\n")
