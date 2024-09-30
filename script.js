document.getElementById('generate-btn').addEventListener('click', function() {
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = '';

    const language = document.getElementById('language').value;
    const textInput = document.getElementById('text-input').value.trim();

    if (!textInput) {
      errorMessage.textContent = 'Please enter some text to generate the word cloud.';
      return;
    }

    const data = {
      text: textInput,
      language: language
    };

    fetch('http://127.0.0.1:5000/word_cloud', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
      const wordCloudContainer = document.getElementById('word-cloud');
      wordCloudContainer.innerHTML = `<img src="data:image/png;base64,${result.cloud}" alt="Word Cloud">`;
    })
    .catch(error => {
      errorMessage.textContent = 'Error generating word cloud. Please try again.';
    });
});