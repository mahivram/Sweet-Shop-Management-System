const API = "http://127.0.0.1:5000";

function fetchSweets() {
    fetch(`${API}/sweets`)
        .then(res => res.json())
        .then(data => renderSweets(data));
}

function renderSweets(sweets) {
    const tbody = document.getElementById('sweetsTableBody');
    tbody.innerHTML = '';
    sweets.forEach(sweet => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${sweet.id}</td>
            <td>${sweet.name}</td>
            <td>${sweet.category}</td>
            <td>${sweet.price}</td>
            <td>${sweet.quantity}</td>
            <td>
                <button onclick="purchaseSweet(${sweet.id})">Purchase</button>
                <button onclick="restockSweet(${sweet.id})">Restock</button>
                <button onclick="deleteSweet(${sweet.id})">Delete</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

document.getElementById('addSweetForm').onsubmit = function(e) {
    e.preventDefault();
    const sweet = {
        id: document.getElementById('id').value,
        name: document.getElementById('name').value,
        category: document.getElementById('category').value,
        price: document.getElementById('price').value,
        quantity: document.getElementById('quantity').value
    };
    fetch(`${API}/sweets`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(sweet)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('addSweetMsg').innerText = data.message || data.error;
        fetchSweets();
    });
};

function deleteSweet(id) {
    fetch(`${API}/sweets/${id}`, {method: 'DELETE'})
        .then(res => res.json())
        .then(() => fetchSweets());
}

function purchaseSweet(id) {
    const qty = prompt("Enter quantity to purchase:");
    if (qty) {
        fetch(`${API}/sweets/${id}/purchase`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({quantity: qty})
        })
        .then(res => res.json())
        .then(data => {
            alert(data.message || data.error);
            fetchSweets();
        });
    }
}

function restockSweet(id) {
    const qty = prompt("Enter quantity to restock:");
    if (qty) {
        fetch(`${API}/sweets/${id}/restock`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({quantity: qty})
        })
        .then(res => res.json())
        .then(data => {
            alert(data.message || data.error);
            fetchSweets();
        });
    }
}

function searchSweets() {
    const name = document.getElementById('searchName').value;
    const category = document.getElementById('searchCategory').value;
    const price_min = document.getElementById('searchPriceMin').value;
    const price_max = document.getElementById('searchPriceMax').value;
    let url = `${API}/sweets/search?`;
    if (name) url += `name=${encodeURIComponent(name)}&`;
    if (category) url += `category=${encodeURIComponent(category)}&`;
    if (price_min) url += `price_min=${price_min}&`;
    if (price_max) url += `price_max=${price_max}&`;
    fetch(url)
        .then(res => res.json())
        .then(data => renderSweets(data));
}

function sortSweets() {
    const by = document.getElementById('sortBy').value;
    fetch(`${API}/sweets/sort?by=${by}`)
        .then(res => res.json())
        .then(data => renderSweets(data));
}

window.onload = fetchSweets;
