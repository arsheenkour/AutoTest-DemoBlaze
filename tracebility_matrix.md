# 🧾 Traceability Matrix

This document maps the relationship between website features, test scenarios, manual test cases, and the corresponding automated scripts.

| **Feature**            | **Scenario**                                      | **Manual Test Case ID** | **Automated Script**                   |
|------------------------|--------------------------------------------------|--------------------------|----------------------------------------|
| **Login Functionality** | Valid user login with correct credentials        | TC_Login_01              | `test_1login.py`                      |
| **Login Functionality** | Valid user login with incorrect credentials      | TC_Login_02              | `test_5login_invalid.py`              |
| **Cart Functionality**  | Add a single product to the cart                 | TC_Cart_01               | `test_2Add_to_cart.py`               |
| **Cart Functionality**  | Add multiple products to the cart                | TC_Cart_02               | `test_3Add_multiple_to_cart.py`      |
| **Cart Functionality**  | Delete a product from the cart                   | TC_Cart_03               | `test_4delete_product_from_cart.py`  |

---

### Additional Information:
- Each script logs **Pass/Fail** results and takes **screenshots** where necessary.
- All test cases are included in the generated HTML report via `pytest-html`.


