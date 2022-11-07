import json;

## format the JSON file correctly for data manipulation to be handled properly
"""
Sources Used:
- https://www.geeksforgeeks.org/python-append-to-a-file/
- https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
- https://www.geeksforgeeks.org/read-json-file-using-python/
- https://stackoverflow.com/questions/62115001/how-to-convert-json-string-into-integer-in-python
"""

# for customers
f = open('./data/customer.json')
data = json.load(f)

for i in data:
    i["customer_id"] = int(i['customer_id'])
    i["store_id"] = int(i['store_id'])
    i["active"] = int(i['active'])
    with open("./data/customer_payment.json", "a") as outfile:
        json.dump(i, outfile)
        outfile.write(", ")

f.close()


# for staff
f = open('./data/staff.json')
data = json.load(f)

for i in data:
    i["staff_id"] = int(i['staff_id'])
    i["active"] = int(i['active'])
    i["store_id"] = int(i['store_id'])
    with open("./data/staff_payment.json", "a") as outfile:
        json.dump(i, outfile)
        outfile.write(", ")

f.close()


# for staff
f = open('./data/rental.json')
data = json.load(f)

for i in data:
    i["rental_id"] = int(i['rental_id'])
    i["inventory_id"] = int(i['inventory_id'])
    i["customer_id"] = int(i['customer_id'])
    i["staff_id"] = int(i['staff_id'])
    with open("./data/rental_payment.json", "a") as outfile:
        json.dump(i, outfile)
        outfile.write(", ")

f.close()


# for staff
f = open('./data/payment.json')
data = json.load(f)

for i in data:
    i["payment_id"] = int(i['payment_id'])
    i["customer_id"] = int(i['customer_id'])
    i["staff_id"] = int(i['staff_id'])
    i["rental_id"] = int(i['rental_id'])
    i["amount"] = float(i['amount'])
    with open("./data/payment_updated.json", "a") as outfile:
        json.dump(i, outfile)
        outfile.write(", ")

f.close()