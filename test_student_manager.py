from student_manager import get_data, view_details

print("Testing get_data...")
header, rows = get_data()
print("Header found:", header)
print("Row count:", len(rows))
if rows:
    print("First row ID:", rows[0].get('ID'))

print("\nTesting view_details display...")
view_details()
