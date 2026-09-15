from pyscript import document, display

def place_order(e):
    document.getElementById("output1").innerHTML = "" # clears previous result
    prod1 = document.getElementById("item1") #get item 1 id
    prod2 = document.getElementById("item2") #get item 2 id
    prod3 = document.getElementById("item3") #get item 3 id
    prod4 = document.getElementById("item4") #get item 4 id
    prod5 = document.getElementById("item5") #get item 5 id

    drinktotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked

    size = document.querySelector("input[name='size']:checked")
    sprice = float(size.value)

    grandtotal = drinktotal + sprice

    pastries = document.getElementById("pastries")
    pastries_price = float(pastries.value)

    tax = (grandtotal + pastries_price) * 0.12 # VAT OF 12%
    tax_price = (grandtotal + pastries_price) + tax # order total + tax

    final_order = tax_price
    display(f'You have a total of {final_order}', target="output1")