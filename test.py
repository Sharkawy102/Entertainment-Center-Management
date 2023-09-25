import db_inventory as items
# items.itemsData()
items.updateData("Coca cola", new_quantity=50, new_price=10)
print(items.view_items("Drinks"))
