def clean_sales_data (row_sales) :
    for row in row_sales :
        amount = row ["amount"].replace ("$", "").strip ()
        if amount == "Free" :
            row ["amount"] = 0
        else :
            row ["amount"] = int (amount)
    return row_sales