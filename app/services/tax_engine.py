def calculate_tax_with_relief(taxable_income: float, is_salaried: bool):
    # 1. Standard Slab Calculation
    if is_salaried:
        tax = 0
        if taxable_income <= 400000: tax = 0
        elif taxable_income <= 800000: tax = (taxable_income - 400000) * 0.05
        elif taxable_income <= 1200000: tax = 20000 + (taxable_income - 800000) * 0.10
        else: tax = 60000 + (taxable_income - 1200000) * 0.15

        # 2. Section 87A Rebate (Full rebate up to 12L)
        if taxable_income <= 1200000:
            return 0

        # 3. Marginal Relief Calculation 
        excess_income = taxable_income - 1200000
        if tax > excess_income:
            tax = excess_income # Tax is capped at the extra income earned

        return tax * 1.04 # Final tax with 4% Cess
    else:
        return("NOT A SALARIED EMPLOY")