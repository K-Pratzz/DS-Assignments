from network_engine import SocialEngine

def main():
    sne = SocialEngine()
    
    # Setup Data (Faculty Checklist)
    users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    for u in users:
        sne.add_user(u, ["TopicA", "TopicB"])

    sne.add_friendship("Alice", "Bob")
    sne.add_friendship("Bob", "Charlie")
    sne.add_friendship("Charlie", "David")
    
    print("SNE CLI ACTIVE")
    print("Shortest path Alice to David:", sne.get_shortest_path("Alice", "David"))
    print("Users within 2 degrees of Alice:", sne.explore_depth("Alice", 2))

if __name__ == "__main__":
    main()