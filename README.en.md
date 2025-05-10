
🧾 **Inventory Management System**  

---

### 📌 **Project Description**
This inventory management system allows performing basic operations to manage products within an inventory. Users can add products, check their existence, update prices, remove products, and see the total inventory value. The system validates input data to ensure correctness, and informative messages are displayed using color in the terminal.

---

### 🎯 **Features**
- **Add products**: Allows the user to add a product to the inventory by providing the name, price, and quantity.
- **Search products**: Allows the user to search for products by name and retrieve their price and quantity.
- **Update prices**: Allows the user to modify the price of an existing product.
- **Remove products**: Allows the user to remove products from the inventory.
- **Total inventory value**: Calculates and shows the total inventory value based on the price and quantity of products.
- **Show inventory**: Displays all products currently stored in the inventory.

---

### 🧠 **Implemented Logic**
The system is composed of several functions and classes:
1. **InventoryService**: Main class responsible for managing operations on the inventory, such as adding, removing, updating prices, and calculating the total value.
2. **Utils**: Helper functions for validating input data, including product name, price, and quantity.
3. **Main**: Function managing the user interface, displaying a menu, and executing user-selected actions.

---

### ✅ **Validations Applied**
- **Product name**: Validates that the product name is not empty and does not contain numeric characters.
- **Price**: Validates that the price is a positive number greater than 0.
- **Quantity**: Validates that the quantity is a positive integer between 1 and 100,000,000.
- **Menu options**: Validates that the selected menu option is one of the valid choices (1-7).

---

### 📁 **Project Structure**
```
/inventoryService.py          # Contains the inventory management logic
/utils.py                     # Functions for validating user input
/main.py                      # User interface and main logic
```

---

### 🧩 **File Descriptions**
- **inventoryService.py**: Contains the `InventoryService` class that manages inventory operations such as adding products, retrieving products, updating prices, removing products, and calculating the total inventory value.
- **utils.py**: Contains functions to validate that user inputs are correct (name, price, and quantity).
- **main.py**: Contains the logic interacting with the user via a menu. It allows executing inventory operations by selecting options.

---

### 💡 **Technical Justification**
The system has been implemented using a clear and simple structure, divided into classes and functions for greater modularity. Terminal colors are used to enhance the user experience while interacting with the system. Validations are implemented to prevent common mistakes and ensure correct data entry.

---

### 🚀 **Future Improvements**
- **Data persistence**: Currently, data is lost when the program is closed. It would be useful to integrate a database or file storage to preserve the inventory between runs.
- **Graphical user interface (GUI)**: A graphical interface could be implemented for a more intuitive user experience.
- **User and role management**: User roles with different permissions could be added, such as administrator and standard user roles.

---

### 💻 **Execution Instructions**
1. Clone or download the repository.
2. Make sure you have Python 3.x installed on your system.
3. Run the `main.py` file from the terminal:
   ```bash
   python main.py
   ```
4. Follow the menu instructions to interact with the inventory system.
