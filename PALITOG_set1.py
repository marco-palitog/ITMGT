def savings(gross_pay, tax_rate, expenses):
    after_tax = gross_pay - gross_pay*tax_rate
    after_tax = after_tax//1
    after_tax_expenses = after_tax - expenses
    return(int(after_tax_expenses))

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    remaining_material = total_material - total_consumed
    return(str(remaining_material) + material_units)

def interest(principal, rate, periods):
    quantity = rate * periods
    simple_interest = principal * quantity
    final = (principal + simple_interest)//1
    return(int(final))