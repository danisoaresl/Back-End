
const form1 = document.getElementById('form1');
const form2 = document.getElementById('form2');


form1.addEventListener('submit', handleSubmit);
form2.addEventListener('submit', handleSubmit);


function handleSubmit(event) {
    event.preventDefault(); 

    const formData = new FormData(event.target); 
    const url = event.target.getAttribute('action'); 

    
    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao enviar dados do formulário.');
        }
        return response.text();
    })
    .then(data => {
        console.log(data); 
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}
