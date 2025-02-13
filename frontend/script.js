document.getElementById('productForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const product_name = document.getElementById('product_name').value;
    const amount = document.getElementById('amount').value;

    const data = {
        product_name: product_name,
        amount: parseInt(amount)
    };

    console.log('Dados enviados:', data)

    fetch('http://localhost:5001/api/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.mensagem) {
            alert(data.mensagem);
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Erro ao enviar dados', error);
    });
});