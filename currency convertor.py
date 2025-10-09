from currency_converter import CurrencyConverter

c = CurrencyConverter()

print("Hello")
print("This is the currency convertor")
print("")
input()

print("Please enter the currency you would want to convert money from:")
print("")

list=[
"US Dollar (USD)",
"Euro (EUR)",
"Japanese Yen (JPY)",
"British Pound Sterling (GBP)",
"Swiss Franc (CHF)",
"Canadian Dollar (CAD)",
"Australian Dollar (AUD)",
"Chinese Yuan Renminbi (CNY)",
"Indian Rupee (INR)",
"Singapore Dollar (SGD)"
]
for i, t in enumerate(list, start=1):
    print(f"{i}. {t}")
    


currencies = [
    "US Dollar (USD)",
    "Euro (EUR)",
    "Japanese Yen (JPY)",
    "British Pound Sterling (GBP)",
    "Swiss Franc (CHF)",
    "Canadian Dollar (CAD)",
    "Australian Dollar (AUD)",
    "Chinese Yuan Renminbi (CNY)",
    "Indian Rupee (INR)",
    "Singapore Dollar (SGD)"
]

curr_code = [
    "USD",
    "EUR",
    "JPY",
    "GBP",
    "CHF",
    "CAD",
    "AUD",
    "CNY",
    "INR",
    "SGD"
]


choice_from= int(input("Enter your currency(1-10): "))


choice_to=int(input("Enter Currency you want to convert into(1-10): "))

print("")
print("")

print("Enter the amount you want to convert from: ")
print( f"{currencies[choice_from - 1]}", "---TO--->", f"{currencies[choice_to - 1]}")
amt=int(input())


choice_from= f"{curr_code[choice_from - 1]}"
choice_to=f"{curr_code[choice_to - 1]}"
x=c.convert(amt,choice_from, choice_to)
print(x)
x=round(x, 3)
print(x)


