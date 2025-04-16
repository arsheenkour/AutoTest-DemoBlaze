# 🧾 Traceability Matrix

This document maps the relationship between website features, test scenarios, manual test cases, and the corresponding automated scripts.

| **Feature**            | **Scenario**                              | **Manual Test Case ID** | **Automated Script**                   |
|------------------------|--------------------------------------------|--------------------------|----------------------------------------|
| Login Functionality     | Valid user login with correct credentials | TC_Login_01              | `test_1login.py`                        |
| Cart Functionality      | Add a single product to cart              | TC_Cart_01               | `test_2Add_to_cart.py`                  |
| Cart Functionality      | Add multiple products to cart             | TC_Cart_02               | `test_3Add_multiple_to_cart.py`         |
| Cart Functionality      | Delete a product from cart                | TC_Cart_03               | `test_4delete_product_from_cart.py`             |

---

 Each script logs Pass/Fail result and takes screenshots.  
 All test cases are included in the generated HTML report via `pytest-html`.

