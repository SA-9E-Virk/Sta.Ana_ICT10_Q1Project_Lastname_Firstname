from pyscript import document
import random


def SKU_generator(event=None):

    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    quantity = document.getElementById("quantity").value

    output = document.getElementById("sku_output")

    if product_name == "":
        output.innerHTML = """
        <p class="text-danger text-center mb-0">
            Please enter a product name.
        </p>
        """
        return

    if quantity == "":
        output.innerHTML = """
        <p class="text-danger text-center mb-0">
            Please enter the stock quantity.
        </p>
        """
        return

    category_code = {
        "Perishables": "PER",
        "Beverages": "BEV",
        "Disposables": "DIS",
        "Packaging": "PAC"
    }

    code = category_code[category]
    product_code = product_name[:3].upper()
    number = random.randint(100, 999)

    sku = f"{code}-{product_code}-{number}"

    output.innerHTML = f"""
    <div class="result-box">

        <div class="text-muted text-center">
            Generated SKU
        </div>

        <div class="sku-code">
            {sku}
        </div>

        <hr>

        <div>
            <strong>Product:</strong> {product_name}
        </div>

        <div>
            <strong>Category:</strong> {category}
        </div>

        <div>
            <strong>Stock Quantity:</strong> {quantity}
        </div>

    </div>
    """
