# Please use below command to run the code: 
python main.py 


**💳 Payment Processing System**

A modern, Object-Oriented Payment Processing System built with Python. This project demonstrates clean code principles, modular architecture, and the use of high-performance Python tooling.

**🚀 Features**
Modern Environment Management: Built using uv for lightning-fast dependency resolution and project isolation.

OOPS Architecture: Implements Object-Oriented Programming for scalable and maintainable transaction handling.

Structural Pattern Matching: Uses Python’s match keyword for elegant routing of different payment methods (UPI, Card, Refunds).

Professional Formatting: Advanced use of f-strings to generate clean, aligned transaction histories.

Time-Stamped Logging: Integrated time module for real-world transaction simulation.

**🛠️ Technical Stack**
Language: Python 3.10+

**Package Manager:**

**Key Modules:** time, re, dataclasses

**📥 Installation & Setup**
Ensure you have uv installed. If not, you can install it via:

1. Clone the repository
2. Sync the environment
3. Run the application
📖 Key Concepts Covered
1. Structural Pattern Matching
We use the match statement to handle various transaction types efficiently:

2. Modular Structure
The project is split into packages and modules to keep the logic separated:

**core:** Contains the base OOPS logic.

**utils:** Contains formatting and helper functions.

**Sample Output:**

Use 1 --> Add, 2 --> refund, 3 --> check balance, 4 --> check history, 5 --> quit

------------------------------------------------------------------------
| TXN ID                 | TYPE       | METHOD   |   AMOUNT |  BALANCE |
------------------------------------------------------------------------
| 1770565635.6909955     | CREDIT     | UPI      | +   1000 |     1000 |
| 1770565645.0274868     | CREDIT     | CARD     | +   2000 |     3000 |
| 1770565654.1928244     | REFUND     | N/A      | ↺    600 |     2400 |
| 1770565667.330947      | CREDIT     | CARD     | +   1237 |     5637 |
| 1770565676.8719413     | CREDIT     | UPI      | +   2000 |     8637 |
| 1770565688.4877427     | REFUND     | N/A      | ↺   2300 |     6337 |
------------------------------------------------------------------------