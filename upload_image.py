import os
import django
from django.core.files import File

# 1. Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cm_backend.settings') # Change to your project name
django.setup()

from menu.models import Menu # Change to your app name

# 2. Path to your downloaded images
IMAGE_DIR = 'C:\Users\dell\OneDrive\Desktop\image' 

# 3. Your Menu Data
menu_data = [
    { "name": "Espresso", "category": "coffee", "price": "80.00", "filename": "espresso.jpg" },
    { "name": "Cappuccino", "category": "coffee", "price": "120.00", "filename": "cappuccino.jpg" },
    { "name": "Latte", "category": "coffee", "price": "130.00", "filename": "latte.jpg" },
    { "name": "Mocha", "category": "coffee", "price": "140.00", "filename": "mocha.jpg" },
    
    { "name": "Veg Sandwich", "category": "snacks", "price": "150.00", "filename": "veg_sandwich.jpg" },
    { "name": "Grilled Sandwich", "category": "snacks", "price": "170.00", "filename": "grilled_sandwich.jpg" },
    { "name": "Cheese Toast", "category": "snacks", "price": "130.00", "filename": "cheese_toast.jpg" },
    { "name": "French Fries", "category": "snacks", "price": "120.00", "filename": "french_fries.jpg" },
    
    { "name": "Chocolate Cake", "category": "dessert", "price": "200.00", "filename": "chocolate_cake.jpg" },
    { "name": "Brownie", "category": "dessert", "price": "180.00", "filename": "brownie.jpg" },
    { "name": "Ice Cream", "category": "dessert", "price": "120.00", "filename": "ice_cream.jpg" },
    { "name": "Pancake", "category": "dessert", "price": "170.00", "filename": "pancake.jpg" },
    
    { "name": "Veg Burger", "category": "meal", "price": "180.00", "filename": "veg_burger.jpg" },
    { "name": "Cheese Burger", "category": "meal", "price": "200.00", "filename": "cheese_burger.jpg" },
    { "name": "Veg Pizza", "category": "meal", "price": "250.00", "filename": "veg_pizza.jpg" },
    { "name": "Pasta", "category": "meal", "price": "220.00", "filename": "pasta.jpg" },
    { "name": "Veg Wrap", "category": "meal", "price": "190.00", "filename": "veg_wrap.jpg" }
]

def upload_local_images():
    for item in menu_data:
        file_path = os.path.join(IMAGE_DIR, item['filename'])
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                # Create the Django object
                menu_item = Menu(
                    name=item['name'],
                    category=item['category'],
                    price=item['price'],
                    is_available=True
                )
                # Save the file into the ImageField
                menu_item.image.save(item['filename'], File(f), save=True)
                print(f"✅ Created and uploaded: {item['name']}")
        else:
            print(f"❌ File not found: {file_path}")

if __name__ == "__main__":
    upload_local_images()