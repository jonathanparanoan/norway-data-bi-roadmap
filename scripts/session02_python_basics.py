# Session 02 - Refresh Python basics
# Goal : practice variables, lists, dictionaries, loops, and functions.

sample_prices = [
    {"zone": "NO1", "date": "2026-03-20", "price_nok_kwh": 1.12},
    {"zone": "NO1", "date": "2026-03-21", "price_nok_kwh": 0.98},
    {"zone": "NO2", "date": "2026-03-20", "price_nok_kwh": 1.34},
    {"zone": "NO2", "date": "2026-03-21", "price_nok_kwh": 1.28},
    {"zone": "NO5", "date": "2026-03-20", "price_nok_kwh": 0.77},
    {"zone": "NO3", "date": "2026-03-21", "price_nok_kwh": 1.03},
]

def summarize_prices(records):
    total_price = 0
    highest_price = records [0]["price_nok_kwh"]
    lowest_price = records [0]["price_nok_kwh"]
    highest_zone = records [0]["zone"]
    lowest_zone = records [0]["zone"]

    for record in records:
        price = record["price_nok_kwh"]
        zone = record["zone"]

        total_price = total_price + price
        print (total_price)
        
        if price > highest_price:
            highest_price = price
            highest_zone = zone

        if price < lowest_price:
            lowest_price = price
            lowest_zone = zone

    average_price = total_price / len(records)  

    summary = {
        "number_of_records": len(records),
        "average_price": round(average_price, 2),
        "highest_price": highest_price,
        "highest_zone": highest_zone,
        "lowest_price": lowest_price,
        "lowest_zone": lowest_zone,
        "total_price": total_price
    }

    return summary

result = summarize_prices (sample_prices)

print("=== Session 02 Python Summary ===")
print(f"Number of records: {result['number_of_records']}")
print(f"Average price: {result['average_price']:.2f} NOK/kWh")
print(f"Highest price: {result['highest_price']:.2f} NOK/kWh in zone {result['highest_zone']}")
print(f"Lowest price: {result['lowest_price']:.2f} NOK/kWh in zone {result['lowest_zone']}")
print(f"Total price: {result['total_price']:.2f} NOK")
print("Script finished successfully!")

