document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const roomImages = document.getElementById('room-images').files;
    const themeSelect = document.getElementById('theme-select').value;

    if (roomImages.length === 0 || !themeSelect) {
        alert('Please upload images and select a theme.');
        return;
    }

    // Prepare form data
    const formData = new FormData();
    for (let i = 0; i < roomImages.length; i++) {
        formData.append('room-images', roomImages[i]);
    }
    formData.append('theme', themeSelect);

    // Send data to the backend
    fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayRecommendations(data.recommendations);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function displayRecommendations(recommendations) {
    const recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = '';

    recommendations.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';

        const img = document.createElement('img');
        img.src = product.image_url;
        productCard.appendChild(img);

        const title = document.createElement('h3');
        title.textContent = product.name;
        productCard.appendChild(title);

        const link = document.createElement('a');
        link.href = product.product_url;
        link.textContent = 'View Product';
        link.target = '_blank';
        productCard.appendChild(link);

        recommendationsDiv.appendChild(productCard);
    });
}
