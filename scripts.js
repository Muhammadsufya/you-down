async function download() {
    const url = document.getElementById('url').value;
    const format = document.getElementById('format').value;
    const resolution = document.getElementById('resolution').value;

    const response = await fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url, format, resolution }),
    });

    if (response.ok) {
        const blob = await response.blob();
        const downloadUrl = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = url.split('v=')[1] + '.' + (format === 'video' ? 'mp4' : 'mp3');
        document.body.appendChild(a);
        a.click();
        a.remove();
    }
}

function detectUrl() {
    const urlInput = document.getElementById('url');
    if (urlInput.value.includes('youtube.com/watch?v=')) {
        urlInput.style.borderColor = 'green';
    } else {
        urlInput.style.borderColor = 'red';
    }
}
