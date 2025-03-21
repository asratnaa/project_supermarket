#!/usr/bin/env python
# coding: utf-8

# In[63]:


from tabulate import tabulate

class Transaction:
    """
    Kelas untuk menangani transaksi belanja dengan fitur:
    - Menambahkan item ke keranjang
    - Memperbarui nama, jumlah, dan harga item
    - Menghapus item atau mereset keranjang
    - Mengecek validitas pesanan
    - Menghitung total harga dengan diskon otomatis
    - Menampilkan isi keranjang dalam bentuk tabel
    """



    def __init__(self,transaction_id):
        """Inisialisasi transaksi dengan ID unik dan daftar item kosong."""
        self.transaction_id = transaction_id
        self.items = []
        self.counter = 1

    def add_item(self,item_name,quantity,price,category):
         """Menambahkan item ke dalam keranjang dengan ID unik."""
         if not isinstance(item_name,str) or not isinstance (quantity,int) or not isinstance(price,(int,float)):
            return "Error: Invalid data type."
         if quantity <= 0 or price<= 0:
            return "Error: Quantity and price must be greater than 0."
         cart_item = {"id":self.counter,"item_name": item_name, "quantity" : quantity , "price" : price , "category": category}
         self.items.append(cart_item)
         self.counter += 1
         return cart_item
        
    def update_item_name(self,old_name,new_name):
        """Memperbarui nama item yang sudah ada di keranjang."""
        for name in self.items:
            if name["item_name"] == old_name: 
                name["item_name"] = new_name 
                return f'Item name: {old_name} has been changed to {new_name}'
        return "Item name not found."   

    def update_item_qty(self,old_name,new_qty):
        """Memperbarui qty item berdasarkan nama produk."""
        for qty in self.items:
            if qty["item_name"] == old_name: 
                qty["quantity"] = new_qty
                return f'Quantity of {old_name} has been updated to {new_qty}'
        return "Item quantity not found."

    def update_item_price(self,old_name,new_price):
        """Memperbarui harga item berdasarkan nama produk."""
        for price in self.items:
            if price["item_name"] == old_name:  
                price["price"] = new_price 
                return f'Price of {old_name} has been updated to {new_price}'
        return "Item price not found."
        
        

    def delete_item(self,remove_item):
        """Menghapus item dari keranjang berdasarkan nama produk."""
        for remove in self.items:
            if remove["item_name"] == remove_item:
                self.items.remove(remove)
                return f'{remove_item} removed from the shopping cart.'
        return "Item not found in the cart."   

    def reset_transaction(self):
        """Menghapus semua item di keranjang dan mereset ID produk."""
        self.items.clear()
        self.counter = 1
        return "All items have been removed from the cart."
    
    def check_order(self):
        """Memeriksa apakah semua data dalam pesanan valid."""
        for item in self.items:
            if not isinstance(item["item_name"], str) or not isinstance(item["quantity"], int) or not isinstance(item["price"], (int,float)):
                return "There is an error in the input data."
        return "Order data is valid."


    def total_price(self):
        """Menghitung total harga dengan diskon jika memenuhi syarat."""
        total = sum(x["price"] * x["quantity"] for x in self.items)
        final_price = total

        if total > 500_000:
            final_price -= total * 0.1 
        elif total > 300_000:
            final_price -= total *0.08

        elif total > 200_000:
            final_price -= total *0.05

              

        return final_price
    
    def show_cart(self):
        """Menampilkan isi keranjang dalam bentuk tabel termasuk total harga."""
        if not self.items:
            return "Shopping cart is empty."
        
        table_cart = [] 
        for i,item in enumerate  (self.items, start = 1) :
            total_per_item = item["quantity"] * item["price"]
            table_cart.append([i,item["id"], item["item_name"], item["quantity"], item["price"],total_per_item])

        headers = ["No","ProductID", "Item Name", "Quantity", "Price per Item", "Total price"]
        cart_table = tabulate(table_cart,headers= headers , tablefmt= "grid")   

        total_harga_akhir = self.total_price()  # Total harga setelah diskon
        return f"{cart_table}\n\nTotal Overall Price (after discount): Rp {total_harga_akhir}"
    



# In[64]:


# Creating a transaction ID
trnsct_123 = Transaction("123raara")

# Display the initial items
print(f"Initial items: {trnsct_123.items}")

# Adding items to the cart
item1 = trnsct_123.add_item(item_name="computer", 
                            quantity=2, price=12_000_000, 
                            category="electronics")
item2 = trnsct_123.add_item(item_name="airfryer", 
                            quantity=1, price=420_000, 
                            category="electronics")

item3 = trnsct_123.add_item(item_name="dragon fruit", 
                            quantity=3, price=50_000, 
                            category="fruit")

# Update item name         
wrong_name = trnsct_123.update_item_name(old_name="computer", new_name="hp")
print(wrong_name)     

# Update item quantity
quantity = trnsct_123.update_item_qty(old_name="computer", new_qty=5)
print(quantity)     

# Update item price
price = trnsct_123.update_item_price(old_name="dragon fruit", new_price=45_000)
print(price) 

# Cancel item in cart
cancel = trnsct_123.delete_item("airfryer")
print(cancel)

# Remove all items in cart
reset = trnsct_123.reset_transaction()
print(reset)

item4 = trnsct_123.add_item(item_name="vaseline", 
                            quantity=1, price=100_000, 
                            category="beauty")
item5 = trnsct_123.add_item(item_name="blackmores", 
                            quantity=5, price=200_000, 
                            category="vitamin")

# Check order
check = trnsct_123.check_order()
print(check)

# Check total price
total = trnsct_123.total_price()
print(total)

# Check cart contents
print(trnsct_123.show_cart())

