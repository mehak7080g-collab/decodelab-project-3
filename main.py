recommendations = {
    "technology": ["Python Programming Course", "AI Fundamentals", "Web Development Course"],
    "gaming": ["Minecraft Survival Guide", "Game Development with Python", "PC Gaming Accessories"],
    "music": ["Music Production Basics", "Audio Editing Course", "Music Theory for Beginners"],
    "sports": ["Fitness Training Guide", "Sports Analytics Introduction", "Home Workout Program"],
    "books": ["Python Programming Book", "Artificial Intelligence Book", "Software Engineering Book"],
    "business": ["Entrepreneurship Fundamentals", "Digital Marketing Course", "Business Strategy Guide"]
}

print("=" * 60)
print("PROJECT 3: AI RECOMMENDATION LOGIC")
print("=" * 60)
print("Available interests:", ", ".join(recommendations.keys()))

while True:
    user_input = input("\nEnter your interests (comma-separated) or 'exit': ")

    if user_input.lower().strip() == "exit":
        print("Recommendation system closed. Goodbye!")
        break

    interests = [x.strip().lower() for x in user_input.split(",") if x.strip()]
    matched = []

    for interest in interests:
        if interest in recommendations:
            matched.extend(recommendations[interest])

    matched = list(dict.fromkeys(matched))

    if matched:
        print("\nRecommended for you:")
        for i, item in enumerate(matched, 1):
            print(f"{i}. {item}")
    else:
        print("\nNo exact preference match found.")
        print("Try:", ", ".join(recommendations.keys()))
