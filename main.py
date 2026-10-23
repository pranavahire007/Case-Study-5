

import heapq


class GPSNavigation:
    def __init__(self):
      
        self.graph = {}
        self.add_location("Pune")
        self.add_location("Mumbai")
        self.add_location("Nashik")
        self.add_location("Satara")
        self.add_location("Kolhapur")
        self.add_location("Ahmednagar")

        self.add_road("Pune", "Mumbai", 150)
        self.add_road("Pune", "Nashik", 210)
        self.add_road("Pune", "Satara", 110)
        self.add_road("Satara", "Kolhapur", 180)
        self.add_road("Pune", "Ahmednagar", 120)
        self.add_road("Ahmednagar", "Nashik", 150)
        self.add_road("Mumbai", "Nashik", 170)
        self.add_road("Mumbai", "Satara", 190)

    # Add a new location
    def add_location(self, location):
        location = location.strip()

        if not location:
            print("Location name cannot be empty.")
            return False

        if location in self.graph:
            print("Location already exists.")
            return False

        self.graph[location] = {}
        print(f"Location '{location}' added successfully.")
        return True

    # Add a bidirectional road
    def add_road(self, source, destination, distance):
        if source not in self.graph:
            print(f"Location '{source}' does not exist.")
            return False

        if destination not in self.graph:
            print(f"Location '{destination}' does not exist.")
            return False

        if source == destination:
            print("A road cannot connect a location to itself.")
            return False

        if distance <= 0:
            print("Distance must be greater than zero.")
            return False

        self.graph[source][destination] = distance
        self.graph[destination][source] = distance

        print(
            f"Road added: {source} <-> {destination} "
            f"({distance} km)"
        )
        return True

    # Display all locations and roads
    def display_map(self):
        print("\n========== GPS MAP ==========")

        if not self.graph:
            print("No locations available.")
            return

        for location in sorted(self.graph):
            print(f"\n{location}:")

            if self.graph[location]:
                for neighbour, distance in sorted(
                    self.graph[location].items()
                ):
                    print(f"  -> {neighbour} ({distance} km)")
            else:
                print("  No connected roads.")

        print("\n============================")

    # Dijkstra's shortest path algorithm
    def shortest_route(self, source, destination):
        if source not in self.graph:
            print("Starting location does not exist.")
            return

        if destination not in self.graph:
            print("Destination location does not exist.")
            return

        if source == destination:
            print(f"\nYou are already at {source}.")
            print("Total distance: 0 km")
            print(f"Route: {source}")
            return

        # Initialize distances and previous locations
        distances = {location: float("inf")
                     for location in self.graph}
        previous = {location: None for location in self.graph}

        distances[source] = 0

        # Priority queue stores (distance, location)
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_location = (
                heapq.heappop(priority_queue)
            )

            # Skip outdated queue entries
            if current_distance > distances[current_location]:
                continue

            # Destination reached with minimum distance
            if current_location == destination:
                break

            # Explore neighbouring locations
            for neighbour, road_distance in (
                self.graph[current_location].items()
            ):
                new_distance = current_distance + road_distance

                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    previous[neighbour] = current_location

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbour)
                    )

        # Check whether destination is reachable
        if distances[destination] == float("inf"):
            print(
                f"\nNo route available from {source} "
                f"to {destination}."
            )
            return

        # Reconstruct the shortest route
        route = []
        current = destination

        while current is not None:
            route.append(current)
            current = previous[current]

        route.reverse()

        # Display results
        print("\n====== SHORTEST ROUTE ======")
        print("Starting Location :", source)
        print("Destination       :", destination)
        print("Route             :", " -> ".join(route))
        print("Total Distance    :", distances[destination], "km")
        print("============================")


def main():
    gps = GPSNavigation()

    while True:
        print("\n===== GPS NAVIGATION SYSTEM =====")
        print("1. Add Location")
        print("2. Add Road")
        print("3. Display Map")
        print("4. Find Shortest Route")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            location = input("Enter location name: ").strip()
            gps.add_location(location)

        elif choice == "2":
            source = input("Enter starting location: ").strip()
            destination = input("Enter destination location: ").strip()

            try:
                distance = float(
                    input("Enter road distance in kilometres: ")
                )

                if not distance.is_integer():
                    print("Please enter a whole-number distance.")
                    continue

                gps.add_road(source, destination, int(distance))

            except ValueError:
                print("Invalid distance! Please enter a number.")

        elif choice == "3":
            gps.display_map()

        elif choice == "4":
            source = input("Enter starting location: ").strip()
            destination = input("Enter destination location: ").strip()

            gps.shortest_route(source, destination)

        elif choice == "5":
            print("Thank you for using GPS Navigation System!")
            break

        else:
            print("Invalid choice! Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
