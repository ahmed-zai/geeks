import math

class Pagination:
    """
    A pagination system that breaks large lists into manageable pages.
    Provides navigation with method chaining and handles edge cases.
    """

    def __init__(self, items=None, page_size=10):
        self.items = items or []
        if page_size <= 0:
            raise ValueError("Page size must be greater than 0")
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        page_idx = page_num - 1
        if not (0 <= page_idx < self.total_pages):
            raise ValueError(f"Page number must be between 1 and {self.total_pages}")
        self.current_idx = page_idx

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return '\n'.join(str(item) for item in self.get_visible_items())

    def get_page_info(self):
        return {
            'current_page': self.current_idx + 1,
            'total_pages': self.total_pages,
            'page_size': self.page_size,
            'total_items': len(self.items),
            'items_on_page': len(self.get_visible_items())
        }

def test_pagination():
    print("=== Pagination System Test ===\n")

    items = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(items, 4)

    print("Initial visible items:", p.get_visible_items(), "\n")
    print("__str__ output:\n", str(p), "\n")

    print("Next page:", p.next_page().get_visible_items(), "\n")
    print("Last page:", p.last_page().get_visible_items(), "\n")

    print("Method chaining:", p.first_page().next_page().next_page().get_visible_items(), "\n")

    try:
        p.go_to_page(3)
        print("Page 3:", p.get_visible_items())
    except ValueError as e:
        print("Error:", e)

    print()
    try:
        p.go_to_page(0)
    except ValueError as e:
        print("Expected error (page 0):", e)

    try:
        p.go_to_page(10)
    except ValueError as e:
        print("Expected error (page 10):", e)

    print()
    print("Empty list test:", Pagination().get_visible_items())
    print("Single item:", Pagination(['item'], 5).get_visible_items())
    print("Large page size:", Pagination(list(range(5)), 10).get_visible_items(), "\n")

    print("Page info:")
    for k, v in p.get_page_info().items():
        print(f"  {k}: {v}")

def interactive_demo():
    print("\n=== Interactive Pagination Demo ===")
    data = [f"Item {i+1}" for i in range(25)]
    p = Pagination(data, 5)

    print(f"Pagination with {len(data)} items, page size: 5")
    print("Commands: next, prev, first, last, goto <n>, info, quit")

    while True:
        print(f"\n--- Page {p.current_idx + 1} of {p.total_pages} ---")
        print(p, "\n", "-"*30)
        cmd = input("Enter command: ").strip().lower()

        try:
            if cmd == 'next':
                p.next_page()
            elif cmd == 'prev':
                p.previous_page()
            elif cmd == 'first':
                p.first_page()
            elif cmd == 'last':
                p.last_page()
            elif cmd.startswith('goto'):
                _, page = cmd.split()
                p.go_to_page(int(page))
            elif cmd == 'info':
                for k, v in p.get_page_info().items():
                    print(f"{k}: {v}")
            elif cmd == 'quit':
                break
            else:
                print("Unknown command.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Running Required Test Cases:")
    print("="*40)

    letters = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(letters, 4)

    print("p.get_visible_items():", p.get_visible_items())
    print("\nAfter p.next_page():", p.next_page().get_visible_items())
    print("\nAfter p.last_page():", p.last_page().get_visible_items())

    try:
        p.go_to_page(7)
        print("\nAfter go_to_page(7):", p.current_idx + 1)
    except ValueError as e:
        print("Error:", e)

    try:
        p.go_to_page(0)
    except ValueError as e:
        print("Caught expected error:", e)

    print("\n" + "="*50)
    test_pagination()

    if input("\nTry the interactive demo? (y/n): ").lower().startswith('y'):
        interactive_demo()
