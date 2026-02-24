# Shipping Cost Calculator

## Input package weight and shipping rate

weight = float(input("enter the package weight in kilograms"))
rate = float(input("enter theshipping rate per kilogram"))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"shipping cost: {shipping_cost} USD")
