# Gross Pay                     Tax Rate
# ----------------------------------------------------------
# Over 40,000                   30%
# >= 30,000 but below 40,000    25%
# >=20,000 but below 30,000     15%
# >=10,000 but below 20,000     10%
# Below 10,000                  no tax.

# Assuming that the net pay is (gross pay – tax amount)

def cacl_tax_n_net():
    try:
        gross_pay = float(input("Enter your gross pay:"))
        
        if gross_pay > 40_000:
            tax = 0.30 * gross_pay
        elif gross_pay >= 30_000 and gross_pay < 40_000:
            tax = 0.25 * gross_pay
        elif gross_pay >= 20_000 and gross_pay < 30_000:
            tax = 0.10 * gross_pay
        elif gross_pay >= 10_000 and gross_pay < 20_000:
            tax = 0.10 * gross_pay
        else :
            tax = 0
            
        net_pay = gross_pay - tax
        
        print(f"Tax: {tax} and Net: {net_pay}")
    except ValueError:
        print("Enter a valid gross pay.")


if __name__ == "__main__":
    cacl_tax_n_net()
