def save_data(clean_data):
    print("Saving data to database...")
    # Implementation for saving data to database would go here
    with open("sales_data.txt", "a") as file:
        for row in clean_data:
            file.write(
                f"Order : {row['order_id']} | Customer : {row['customer']} | Amount : {row['amount']} $\n"
            )
            print(
                f"Order : {row['order_id']}, Customer : {row['customer']}, Amount : {row['amount']} $"
            )
