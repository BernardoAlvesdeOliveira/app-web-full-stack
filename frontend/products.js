const productsTable = document.getElementById('productsTable');
const productsState = document.getElementById('productsState');
const refreshButton = document.getElementById('refreshButton');

function showState(message, type = 'info') {
    productsState.textContent = message;
    productsState.className = `message ${type}`;
}

function renderProducts(products) {
    productsTable.innerHTML = '';

    if (!products.length) {
        showState('No products have been registered yet.', 'info');
        return;
    }

    productsState.className = 'hidden';
    products.forEach((product) => {
        const row = document.createElement('tr');
        const nameCell = document.createElement('td');
        nameCell.dataset.label = 'Product';
        nameCell.textContent = product.product_name;

        const amountCell = document.createElement('td');
        amountCell.dataset.label = 'Quantity';
        const quantity = document.createElement('span');
        quantity.className = 'quantity';
        quantity.textContent = product.amount;
        amountCell.appendChild(quantity);

        const dateCell = document.createElement('td');
        dateCell.dataset.label = 'Registered on';
        dateCell.textContent = new Date(product.data_cadastro).toLocaleString();

        row.append(nameCell, amountCell, dateCell);
        productsTable.appendChild(row);
    });
}

async function loadProducts() {
    showState('Loading products...', 'info');
    refreshButton.disabled = true;

    try {
        const response = await fetch('http://localhost:5001/api/products');
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.erro || 'Could not load products.');
        }
        renderProducts(data);
    } catch (error) {
        showState(error.message, 'error');
    } finally {
        refreshButton.disabled = false;
    }
}

refreshButton.addEventListener('click', loadProducts);
loadProducts();
