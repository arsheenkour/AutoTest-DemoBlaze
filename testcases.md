##  Identify Two Critical Features of the Website

**Selected Website:** [https://www.demoblaze.com](https://www.demoblaze.com)

---

### Feature 1: User Login Functionality

#### (a) Test Scenarios
1. User logs in with valid credentials
2. User attempts to log in with invalid credentials
3. Login modal closes when 'Close' is clicked

#### (b) High-Level Manual Test Cases

| Test Case ID | Description                    | Steps                                                                                   | Expected Result                            |
|--------------|--------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------|
| TC_Login_01  | Login with valid credentials   | 1. Click **Login**<br>2. Enter valid username & password<br>3. Click **Login** button   | User is logged in and sees **Welcome [user]** |
| TC_Login_02  | Login with invalid credentials | 1. Click **Login**<br>2. Enter invalid credentials<br>3. Click **Login** button         | Error appears or login is rejected          |


---

### Feature 2: Add to Cart Functionality

#### (a) Test Scenarios
1. Add a single product to the cart
2. Add multiple products and verify they appear in the cart
3. Delete a product from the cart

#### (b) High-Level Manual Test Cases

| Test Case ID | Description                  | Steps                                                                                 | Expected Result                        |
|--------------|------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------|
| TC_Cart_01   | Add product to cart          | 1. Click on a product<br>2. Click **Add to cart**<br>3. Confirm alert                 | Product is added to cart, alert shown   |
| TC_Cart_02   | Add multiple products        | Repeat steps in TC_Cart_01 for 2-3 items<br>Go to **Cart**                            | All added products are visible in cart  |
| TC_Cart_03   | Delete product from cart     | 1. Go to **Cart**<br>2. Click **Delete** next to a product                            | Selected product is removed from cart   |

---
