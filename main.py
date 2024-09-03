#ข้อมูลอัตราแลกเปลี่ยนสกุลเงินของ 10 ประเทศ
rates = {
    "USD":1.0,
    "THB":34.24,
    "EUR":0.90,
    "JPY":146.18,
    "GBP":0.76,
    "CAD":1.35,
    "SGD":1.30,
    "CNY":7.12,
    "EGP":48.50,
    "TRY":33.98
}

def convert_currency(amount,base_currency,target_currency):
    if base_currency not in rates or target_currency not in rates:
        return ("สกุลเงินไม่ถูกต้อง")
    
    base_usd = amount/rates[base_currency]
    target_amount = base_usd * rates[target_currency]
    return target_amount

def results_rates(amount,base_currency):
    print(f"แลกเปลี่ยนสกุลเงิน {amount}{base_currency}")
    for currency in rates:
        if currency != base_currency:
            results = convert_currency(amount,base_currency,currency)
            print(f"{base_currency} เป็น {currency} : {results:.2f}")

amount = float(input("จำนวนเงิน :"))
base_currency = input("สกุลเงินที่ต้องการแปลง :").upper()

results_rates(amount,base_currency)
