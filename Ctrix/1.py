def priceCheck(products, productPrices, productSold, soldPrice):
    store = {}
    for i in range(len(products)):
        store[products[i]] = productPrices[i]

    errors = 0
    for i in range(len(productSold)):
        if store[productSold[i]] != soldPrice[i]:
            errors += 1

    return errors
