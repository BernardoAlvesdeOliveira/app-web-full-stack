document.getElementById('productForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const product_name = document.getElementById('product_name').value;
    const amount = document.getElementById('amount').value;

    const data = {
        product_name: product_name,
        amount: parseInt(amount, 10)
    };

    fetch('http://localhost:5001/api/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const message = document.getElementById('responseMessage');
        message.textContent = data.mensagem || data.erro || data.error;
        message.className = data.mensagem ? 'message success' : 'message error';
        if (data.mensagem) {
            document.getElementById('productForm').reset();
        }
    })
    .catch(error => {
        console.error('Erro ao enviar dados', error);
    });
});