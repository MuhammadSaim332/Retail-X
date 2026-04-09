# The Stock Engine - Color Enhanced Version with Professional Header
import os
import sys
from google import genai
from google.genai import types
from google.genai import errors
import colorama
from colorama import Fore, Back, Style
import json
import time
from datetime import datetime

# Initialize Colorama
colorama.init(autoreset=True)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_retail_x_banner():
    """Prints a professional Retail-X banner at the top of screen"""
    clear_screen()
    print("\n" + f"{Fore.CYAN}{'═'*70}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}")
    print("        ██████╗ ███████╗████████╗ █████╗ ██╗██╗     ██╗  ██╗")
    print("        ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║     ╚██╗██╔╝")
    print("        ██████╔╝█████╗     ██║   ███████║██║██║      ╚███╔╝ ")
    print("        ██╔══██╗██╔══╝     ██║   ██╔══██║██║██║      ██╔██╗ ")
    print("        ██║  ██║███████╗   ██║   ██║  ██║██║███████╗██╔╝ ██╗")
    print("        ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝")
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("                   AI Integrated Retail Engine")
    print(f"{Fore.WHITE}")
    print("─"*70)
    print(f"{Fore.YELLOW}          University of Engineering & Technology Lahore")
    print(f"{Fore.CYAN}{'═'*70}{Style.RESET_ALL}")

def talk_to_style():
    client = genai.Client(api_key="AIzaSyCJQ7Rip__VCSj9BdrC4SsRV-_Xd4lQrvc")
    STYLEBOT_PROMPT = """You are StyleBot, an AI fashion and inventory assistant for The Stock Engine.

Your purpose is to help users with clothing selection, fashion advice, and store inventory management.
You will take into account user context (occasion, preferences, budget, style).
You must tailor responses based on user needs. You will also answer user queries about the store system.

✅ What You ARE Allowed to Do
1. Fashion & Styling Guidance
Help users choose appropriate clothing
Suggest occasion-based outfits, such as:
- Casual/Everyday
- Business/Formal
- Party/Special Events
- Seasonal wear
Identify suitable clothing combinations
Ask clarifying questions if needed like occasion, budget, preferred style
Tell users to consider comfort and appropriateness for the occasion
If user just asks for help, provide a menu of assistance options

2. Store Navigation Assistance
Guide users to use inventory features
Explain how to search, filter, and view products
Help users understand stock status indicators
Suggest using system features for specific queries

3. Clothing & Fabric Education
Explain different clothing materials
Provide care instructions
Compare garment types and styles
Suggest sizing and fit guidelines
Recommend quality over quantity

4. Inventory System Guidance
Explain how to use The Stock Engine features:
- Add/Update/Delete items (admin only)
- Search and filter products
- View sales reports
- Check low stock alerts
Always reference actual system menu options

❌ What You MUST NOT Do
Do NOT provide:
- Exact inventory numbers (unless in context)
- Medical advice about clothing
- Financial investment advice
- Legal or compliance advice
Do NOT:
- Guarantee specific item availability
- Share unverified fashion "facts"
- Promote competitors or other stores
- Make definitive statements about trends

🚫 Handling Complex or Inappropriate Requests
If user asks for:
- Medical advice related to clothing
- Financial investment recommendations
- Competitor comparisons
- Inappropriate content
Respond ONLY with:

"I am StyleBot, your fashion and store assistant. I can only help with clothing advice, fashion tips, and store navigation. For other inquiries, please consult appropriate professionals."

🧾 Response Style
Short, to-the-point answers
Terminal-friendly formatting
Use emojis sparingly (1-2 per response)
Clear section breaks when needed

== FORMATTING ==
- Use bullet points for lists
- Clear spacing between sections
- Reference actual menu options
- Use size/color/style specifics when helpful

🆔 Identity
Always respond as StyleBot from The Stock Engine
Always prioritize helpfulness, appropriateness, and system accuracy
Reference actual inventory categories and features when possible

## CURRENT INVENTORY CONTEXT:
{categories_list}
{inventory_context}

## CONVERSATION HISTORY:
{conversation_history}

## RESPONSE GUIDELINES:
1. If asking about specific products, suggest using Search/Filter features
2. If asking about stock levels, refer to View Products with status indicators
3. For fashion advice, consider the occasion and user context
4. Always be helpful but redirect to system features for specific data
5. Keep responses concise (2-4 sentences for most queries)

Now respond to the user's query appropriately:"""

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=STYLEBOT_PROMPT
        )
    )

    while True:
        print_retail_x_banner()
        print(f"\n{Fore.CYAN}{'✦'*70}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}        🤖 STYLEBOT AI ASSISTANT")
        print(f"{Fore.CYAN}{'✦'*70}")
        print(f"{Fore.GREEN}Hello! I'm StyleBot, your AI fashion assistant.")
        print(f"{Fore.CYAN}Ask me about styling, inventory, or fashion advice!")
        print(f"{Fore.YELLOW}Type 'exit', 'back', or 'quit' to return to main menu.")
        print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}\n")
        
        user_input = input(f"{Fore.GREEN}> ")
        if user_input.lower() in ["exit", "quit", "back", "bye"]:
            print(f"\n{Fore.YELLOW}GoodBye! Returning to main menu...")
            time.sleep(1.5)
            break

        try:
            response = chat.send_message(user_input)
            print_retail_x_banner()
            print(f"\n{Fore.CYAN}{'✦'*70}")
            print(f"{Fore.MAGENTA}{Style.BRIGHT}        🤖 STYLEBOT RESPONSE")
            print(f"{Fore.CYAN}{'✦'*70}")
            print(f"{Fore.WHITE}{response.text}")
            print(f"\n{Fore.CYAN}{'─'*70}")
            input(f"{Fore.YELLOW}Press Enter to continue...")
        except errors.ClientError as e:
            print(f"\n{Fore.RED}[Error] System busy or quota reached. Details: {e}\n")
            time.sleep(2)

# Configuration
ADMIN_PASSWORD = "admin123" 

def authenticate_admin():
    """Returns True if password is correct, False otherwise"""
    attempts = 3
    print_retail_x_banner()
    print(f"\n{Fore.BLUE}🔐 --- Admin Authentication ---")
    while attempts > 0:
        password = input(f"{Fore.YELLOW}🔑 Enter Admin Password ({attempts} attempts left): ")
        print(f"{Fore.CYAN}⏳ Verifying credentials...")
        time.sleep(1)
        if password == ADMIN_PASSWORD:
            print(f"{Fore.GREEN}✅ Access Granted!")
            time.sleep(1)
            return True
        else:
            attempts -= 1
            print(f"{Fore.RED}❌ Incorrect Password!")
    
    print(f"{Fore.RED}🚫 Access Denied. Returning to main menu...")
    time.sleep(2)
    return False

def menu():
    print_retail_x_banner()
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}👔 --- Clothing Inventory Management ---")
    print(f"{Fore.CYAN}1. {Fore.GREEN}➕ Add Item")
    print(f"{Fore.CYAN}2. {Fore.BLUE}📋 View Items")
    print(f"{Fore.CYAN}3. {Fore.YELLOW}🔍 Search Item")
    print(f"{Fore.CYAN}4. {Fore.MAGENTA}📂 Filter by Category")
    print(f"{Fore.CYAN}5. {Fore.CYAN}🔄 Update Item")
    print(f"{Fore.CYAN}6. {Fore.RED}🗑️ Delete Item")
    print(f"{Fore.CYAN}7. {Fore.YELLOW}⚠️ Low Stock Alert")
    print(f"{Fore.CYAN}8. {Fore.GREEN}📈 View Sales Report")
    print(f"{Fore.CYAN}9. {Fore.GREEN}🤖StyleBot")
    print(f"{Fore.CYAN}10. {Fore.WHITE}🚪 Back to Main Menu")

def load_inventory():
    """Load inventory from file"""
    try:
        with open("inventory.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory():
    """Save inventory to file"""
    with open("inventory.json", "w") as f:
        json.dump(inventory, f)

def add():
    print_retail_x_banner()
    print(f"\n{Fore.GREEN}{'➕'*35}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}        ADD NEW PRODUCT")
    print(f"{Fore.GREEN}{'➕'*35}{Style.RESET_ALL}")
    
    id = int(input(f"{Fore.YELLOW}🆔 Enter Product ID: "))
    # Check if ID already exists
    for item in inventory:
        if item["id"] == id:
            print(f"{Fore.RED}❌ Product ID already exists!")
            time.sleep(1.5)
            return
            
    name = str(input(f"{Fore.YELLOW}👕 Enter Product Name: ").upper())
    category = str(input(f"{Fore.YELLOW}📂 Enter Product Category: ").upper())
    size = input(f"{Fore.YELLOW}📏 Enter Product Size: ")
    color = str(input(f"{Fore.YELLOW}🎨 Enter Product Color: ").capitalize())
    quantity = int(input(f"{Fore.YELLOW}🔢 Enter Product Quantity: "))
    price = float(input(f"{Fore.YELLOW}💰 Enter Product Price: "))
    
    info = {
        "id": id,
        "name": name,
        "category": category,
        "size": size,
        "color": color,
        "quantity": quantity,
        "price": price,
    }
    print(f"{Fore.CYAN}⏳ Adding product to system...")
    time.sleep(1)
    inventory.append(info)
    save_inventory()
    print(f"{Fore.GREEN}✅ Product added successfully!")
    time.sleep(1.5)

def view():
    print_retail_x_banner()
    print(f"{Fore.CYAN}⏳ Loading inventory records...")
    time.sleep(0.8)
    if not inventory:
        print(f"{Fore.YELLOW}📭 Inventory is empty")
    else:
        print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
        print(f"{Fore.WHITE}-" * 70)
        for item in inventory:
            qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
            print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def search():
    print_retail_x_banner()
    print(f"\n{Fore.YELLOW}{'🔍'*35}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}        SEARCH PRODUCTS")
    print(f"{Fore.YELLOW}{'🔍'*35}{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}1. {Fore.YELLOW}🆔 Search by ID")
    print(f"{Fore.CYAN}2. {Fore.YELLOW}👕 Search by Name")
    choiceSearch = int(input(f"{Fore.GREEN}Select a Choice: "))
    found = False
    
    if choiceSearch == 1:
        idSearch = int(input(f"{Fore.YELLOW}Enter Product ID: "))
        print(f"{Fore.CYAN}⏳ Searching database...")
        time.sleep(0.7)
        for item in inventory:
            if idSearch == item["id"]:
                found = True
                print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
                print(f"{Fore.WHITE}-" * 70)
                qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
                print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
                
    elif choiceSearch == 2:
        nameSearch = input(f"{Fore.YELLOW}Enter Product Name: ").upper()
        print(f"{Fore.CYAN}⏳ Searching database...")
        time.sleep(0.7)
        for item in inventory:
            if nameSearch in item["name"]:
                found = True
                print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
                print(f"{Fore.WHITE}-" * 70)
                qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
                print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
    
    if not found:
        print(f"{Fore.RED}❌ Product Not Found")
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def update():
    print_retail_x_banner()
    print(f"\n{Fore.CYAN}{'🔄'*35}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}        UPDATE PRODUCT")
    print(f"{Fore.CYAN}{'🔄'*35}{Style.RESET_ALL}")
    
    idSearch = int(input(f"{Fore.YELLOW}🆔 Enter Product ID: "))
    found = False
    
    for item in inventory:
        if idSearch == item["id"]:
            found = True
            print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
            print(f"{Fore.WHITE}-" * 70)
            qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
            print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
            
            print(f"\n{Fore.CYAN}Select a field to update:")
            print(f"{Fore.CYAN}1. {Fore.YELLOW}🆔 ID")
            print(f"{Fore.CYAN}2. {Fore.YELLOW}👕 Name")
            print(f"{Fore.CYAN}3. {Fore.YELLOW}📂 Category")
            print(f"{Fore.CYAN}4. {Fore.YELLOW}📏 Size")
            print(f"{Fore.CYAN}5. {Fore.YELLOW}🎨 Color")
            print(f"{Fore.CYAN}6. {Fore.YELLOW}🔢 Quantity")
            print(f"{Fore.CYAN}7. {Fore.YELLOW}💰 Price")
            choice = int(input(f"{Fore.GREEN}Select a choice: "))
            
            if choice == 1:
                new_id = int(input(f"{Fore.YELLOW}Enter new ID: "))
                for existing_item in inventory:
                    if existing_item["id"] == new_id and existing_item != item:
                        print(f"{Fore.RED}❌ Product ID already exists!")
                        time.sleep(1.5)
                        return
                item["id"] = new_id
            elif choice == 2:
                item["name"] = input(f"{Fore.YELLOW}Enter new Name: ").upper()
            elif choice == 3:
                item["category"] = input(f"{Fore.YELLOW}Enter new Category: ").upper()
            elif choice == 4:
                item["size"] = input(f"{Fore.YELLOW}Enter new Size: ")
            elif choice == 5:
                item["color"] = input(f"{Fore.YELLOW}Enter new Color: ").capitalize()
            elif choice == 6:
                item["quantity"] = int(input(f"{Fore.YELLOW}Enter new Quantity: "))
            elif choice == 7:
                item["price"] = float(input(f"{Fore.YELLOW}Enter new Price: "))
            else:
                print(f"{Fore.RED}❌ Invalid choice.")
                time.sleep(1.5)
                return
            
            print(f"{Fore.CYAN}⏳ Updating records...")
            time.sleep(1)
            save_inventory()
            print(f"{Fore.GREEN}✅ Product updated successfully!")
            time.sleep(1.5)
            break

    if not found:
        print(f"{Fore.RED}❌ Product not found.")
        time.sleep(1.5)

def delete():
    print_retail_x_banner()
    print(f"\n{Fore.RED}{'🗑️'*35}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}        DELETE PRODUCT")
    print(f"{Fore.RED}{'🗑️'*35}{Style.RESET_ALL}")
    
    idSearch = int(input(f"{Fore.YELLOW}🗑️ Enter Product ID to Delete: "))
    found = False
    
    for item in inventory:
        if idSearch == item["id"]:
            found = True
            print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
            print(f"{Fore.WHITE}-" * 70)
            qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
            print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')

            confirm = input(f"\n{Fore.YELLOW}⚠️ Are you sure you want to delete this product? (Y/N): ").upper()
            if confirm == "Y":
                print(f"{Fore.CYAN}⏳ Removing product...")
                time.sleep(1)
                inventory.remove(item)
                save_inventory()
                print(f"{Fore.GREEN}✅ Product deleted successfully!")
            else:
                print(f"{Fore.RED}❌ Deletion cancelled.")
            time.sleep(1.5)
            break

    if not found:
        print(f"{Fore.RED}❌ Product not found.")
        time.sleep(1.5)

def low_stock():
    print_retail_x_banner()
    print(f"{Fore.CYAN}⏳ Analyzing stock levels...")
    time.sleep(1)
    print(f"\n{Fore.YELLOW}📉 --- Low Stock Items (Quantity < 20) ---")
    found = False
    if not inventory:
        print(f"{Fore.YELLOW}📭 Inventory is empty.")
        return

    header = f'{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(8)}{"Category".ljust(12)}{"Size".ljust(8)}{"Color".ljust(8)}{"Qty".ljust(7)}{"Price".ljust(5)}'
    
    for item in inventory:
        if item["quantity"] < 20:
            if not found:
                print(header)
                print(f"{Fore.WHITE}-" * 55)
                found = True
            
            qty_color = Fore.RED if item["quantity"] < 10 else Fore.YELLOW
            print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(8)}{item["category"].ljust(12)}{item["size"].ljust(8)}{item["color"].ljust(8)}{qty_color}{str(item["quantity"]).ljust(7)}{Fore.GREEN}{str(item["price"]).ljust(5)}')
    
    if not found:
        print(f"{Fore.GREEN}✅ All items are well-stocked (No items below 20).")
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def filter_by_category():
    print_retail_x_banner()
    if not inventory:
        print(f"{Fore.YELLOW}📭 Inventory is empty")
        time.sleep(1.5)
        return

    categories = set(item["category"] for item in inventory)
    print(f"\n{Fore.MAGENTA}📂 Available Categories: {Fore.CYAN}{', '.join(categories)}")
    
    cat_search = input(f"{Fore.YELLOW}🔍 Enter Category to filter: ").upper()
    print(f"{Fore.CYAN}⏳ Filtering for {cat_search}...")
    time.sleep(0.8)
    found = False
    
    header = f'{Fore.CYAN}\n{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}'
    
    for item in inventory:
        if cat_search in item["category"]:
            if not found:
                print(header)
                print(f"{Fore.WHITE}-" * 70)
                found = True
            qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
            print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
    
    if not found:
        print(f"{Fore.RED}❌ No items found in category: {cat_search}")
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def load_sales():
    try:
        with open("sales_history.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_sales(sales_list):
    with open("sales_history.json", "w") as f:
        json.dump(sales_list, f, indent=4)

def view_sales_report():
    print_retail_x_banner()
    print(f"{Fore.CYAN}⏳ Generating sales report...")
    time.sleep(1.2)
    history = load_sales()
    if not history:
        print(f"{Fore.YELLOW}📜 No sales recorded yet.")
        time.sleep(1.5)
        return

    print(f"\n{Fore.GREEN}📈 --- Sales History Report ---")
    header = f'{Fore.CYAN}{"Date & Time".ljust(20)}{"Item".ljust(15)}{"Qty".ljust(6)}{"Total Price".ljust(10)}'
    print(header)
    print(f"{Fore.WHITE}-" * 55)
    
    grand_total = 0
    for sale in history:
        print(f'{Fore.WHITE}{sale["date"].ljust(20)}{sale["name"].ljust(15)}{str(sale["quantity"]).ljust(6)}{Fore.GREEN}${str(sale["total_price"]).ljust(10)}')
        grand_total += sale["total_price"]
    
    print(f"{Fore.WHITE}-" * 55)
    print(f'{Fore.GREEN}{Style.BRIGHT}💰 TOTAL REVENUE: ${grand_total:.2f}')
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def userMenu():
    print_retail_x_banner()
    print(f"\n{Fore.BLUE}{Style.BRIGHT}👤 --- User Menu ---")
    print(f"{Fore.CYAN}1. {Fore.BLUE}📋 View Products")
    print(f"{Fore.CYAN}2. {Fore.YELLOW}🔍 Search Product")
    print(f"{Fore.CYAN}3. {Fore.MAGENTA}📂 Filter by Category")
    print(f"{Fore.CYAN}4. {Fore.GREEN}💳 Buy Product")
    print(f"{Fore.CYAN}5. {Fore.CYAN}🤖 StyleBot")
    print(f"{Fore.CYAN}6. {Fore.WHITE}🚪 Logout")

def userSearch():
    print_retail_x_banner()
    print(f"\n{Fore.YELLOW}{'🔍'*35}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}        SEARCH PRODUCTS")
    print(f"{Fore.YELLOW}{'🔍'*35}{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}1. {Fore.YELLOW}🆔 Search by ID")
    print(f"{Fore.CYAN}2. {Fore.YELLOW}👕 Search by Name")
    choiceSearch = int(input(f"{Fore.GREEN}Select a Choice: "))
    found = False
    
    if choiceSearch == 1:
        idSearch = int(input(f"{Fore.YELLOW}Enter Product ID: "))
        print(f"{Fore.CYAN}⏳ Searching...")
        time.sleep(0.5)
        for item in inventory:
            if idSearch == item["id"]:
                found = True
                print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
                print(f"{Fore.WHITE}-" * 70)
                qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
                print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
                
    elif choiceSearch == 2:
        nameSearch = input(f"{Fore.YELLOW}Enter Product Name: ").upper()
        print(f"{Fore.CYAN}⏳ Searching...")
        time.sleep(0.5)
        for item in inventory:
            if nameSearch in item["name"]:
                found = True
                print(f'\n{Fore.CYAN}{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
                print(f"{Fore.WHITE}-" * 70)
                qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
                print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
    
    if not found:
        print(f"{Fore.RED}❌ Product Not Found")
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def userView():
    print_retail_x_banner()
    print(f"{Fore.CYAN}⏳ Loading store...")
    time.sleep(0.8)
    if not inventory:
        print(f"{Fore.YELLOW}📭 Inventory is empty")
    else:
        print(f'{Fore.CYAN}\n{"ID".ljust(5)}{"Name".ljust(15)}{"Category".ljust(15)}{"Size".ljust(8)}{"Color".ljust(10)}{"Qty".ljust(6)}{"Price".ljust(8)}')
        print(f"{Fore.WHITE}-" * 70)
        for item in inventory:
            qty_color = Fore.RED if item["quantity"] < 20 else Fore.GREEN if item["quantity"] < 50 else Fore.YELLOW
            print(f'{Fore.WHITE}{str(item["id"]).ljust(5)}{item["name"].ljust(15)}{item["category"].ljust(15)}{item["size"].ljust(8)}{item["color"].ljust(10)}{qty_color}{str(item["quantity"]).ljust(6)}{Fore.GREEN}${str(item["price"]).ljust(7)}')
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    input(f"{Fore.YELLOW}Press Enter to continue...")

def userBuy():
    print_retail_x_banner()
    if not inventory:
        print(f"{Fore.YELLOW}📭 No products available")
        time.sleep(1.5)
        return
        
    userView()
    try:
        product_id = int(input(f"\n{Fore.YELLOW}🆔 Enter Product ID to purchase: "))
        quantity = int(input(f"{Fore.YELLOW}🔢 Enter quantity: "))
        
        for item in inventory:
            if item["id"] == product_id:
                if item["quantity"] >= quantity:
                    total_cost = item["price"] * quantity
                    confirm = input(f"{Fore.YELLOW}❓ Confirm purchase of {quantity} {item['name']} for ${total_cost:.2f}? (Y/N): ").upper()
                    
                    if confirm == "Y":
                        print(f"{Fore.CYAN}⏳ Processing payment...")
                        time.sleep(2)
                        item["quantity"] -= quantity
                        save_inventory()
                        
                        sale_entry = {
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "product_id": item["id"],
                            "name": item["name"],
                            "quantity": quantity,
                            "price_per_unit": item["price"],
                            "total_price": total_cost
                        }
                        
                        history = load_sales()
                        history.append(sale_entry)
                        save_sales(history)
                        
                        print(f"{Fore.GREEN}✅ Purchase successful! Thank you for shopping 🛍️")
                    else:
                        print(f"{Fore.RED}❌ Purchase cancelled.")
                    time.sleep(2)
                    return
                else:
                    print(f"{Fore.RED}❌ Insufficient quantity!")
                    time.sleep(1.5)
                return
        print(f"{Fore.RED}❌ Product not found!")
        time.sleep(1.5)
    except ValueError:
        print(f"{Fore.RED}❌ Invalid input!")
        time.sleep(1.5)

# Load inventory at startup
inventory = load_inventory()

# Main program
while True:
    print_retail_x_banner()
    
    print(f"\n{Fore.CYAN}{'═'*70}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}         MAIN MENU")
    print(f"{Fore.CYAN}{'═'*70}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}1. {Fore.BLUE}🛡️  Admin Access")
    print(f"{Fore.CYAN}2. {Fore.GREEN}👤 User Access")
    print(f"{Fore.CYAN}3. {Fore.RED}🚪 Exit System")
    
    try:
        accesType = int(input(f"\n{Fore.YELLOW}📋 Select an option: "))
        
        if accesType == 1:
            if authenticate_admin():
                while True:
                    menu()
                    try:
                        choice = int(input(f"{Fore.GREEN}Select a Choice: "))
                        if choice == 1: add()
                        elif choice == 2: view()
                        elif choice == 3: search()
                        elif choice == 4: filter_by_category()
                        elif choice == 5: update()
                        elif choice == 6: delete()
                        elif choice == 7: low_stock()
                        elif choice == 8: view_sales_report()
                        elif choice == 9: talk_to_style()
                        elif choice == 10: break
                        else: 
                            print(f"{Fore.RED}❌ Invalid Input! Try Again...")
                            time.sleep(1.5)
                    except ValueError:
                        print(f"{Fore.RED}❌ Please enter a valid number!")
                        time.sleep(1.5)

        elif accesType == 2:
            while True:
                userMenu()
                try:
                    userChoice = int(input(f"{Fore.GREEN}Select a choice: "))
                    if userChoice == 1: userView()
                    elif userChoice == 2: userSearch()
                    elif userChoice == 3: filter_by_category()
                    elif userChoice == 4: userBuy()
                    elif userChoice ==5: talk_to_style()
                    elif userChoice == 6: 
                        print(f"{Fore.YELLOW}👋 Thanks for visiting...")
                        time.sleep(1.5)
                        break
                    else: 
                        print(f"{Fore.RED}❌ Invalid Input! Try Again...")
                        time.sleep(1.5)
                except ValueError:
                    print(f"{Fore.RED}❌ Please enter a valid number!")
                    time.sleep(1.5)
                    
        elif accesType == 3:
            print_retail_x_banner()
            print(f"\n{Fore.YELLOW}{'👋'*35}")
            print(f"{Fore.MAGENTA}{Style.BRIGHT}        THANK YOU FOR USING RETAIL-X")
            print(f"{Fore.YELLOW}{'👋'*35}")
            print(f"\n{Fore.CYAN}Shutting down system...{Style.RESET_ALL}")
            time.sleep(2)
            clear_screen()
            break
        else:
            print(f"{Fore.RED}❌ Invalid choice! Please try again.")
            time.sleep(1.5)
    except ValueError:
        print(f"{Fore.RED}❌ Please enter a valid number!")
        time.sleep(1.5)