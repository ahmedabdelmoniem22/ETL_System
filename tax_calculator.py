
print("⚙️ Tax Module is Initialized!")

def apply_tax(amount):
    return amount - (amount * 0.14)

if __name__ == "__main__":

# إنت هنا بتعمل تست للدالة بتاعتك عشان تتأكد إنها شغالة
    print(f"Test Result: {apply_tax(1000)}")

