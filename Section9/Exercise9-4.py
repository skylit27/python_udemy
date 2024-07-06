def taxCalculator(payment,noTax):

    result = payment + (payment * (noTax/100))
    print(f"Pago con impuesto : {result}")

pay = float(input("Proporcione el pago sin impuesto: "))
taxAmmount= float(input("Proporcione el monto del impuesto: "))

taxCalculator(pay,taxAmmount)