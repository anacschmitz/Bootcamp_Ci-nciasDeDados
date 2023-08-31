# Dictionary to store the customers
customers = {}

# Function to add a customer to the "customers" dictionary
def add_customer(cpf, name, age, city):
    customers[cpf] = {
        "name": name,
        "age": age,
        "city": city
    }


cpf = int(input("Customer's CPF:"))
add_customer(cpf, input(), int(input()), input())

print("Customer Registered!")
print("Document: ", cpf)
print("Name: ", customers[cpf]["name"])
print("Age: ", customers[cpf]["age"])
print("City: ", customers[cpf]["city"])


# TODO: Print other data from "customers" dictionary.