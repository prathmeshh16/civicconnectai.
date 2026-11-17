document.addEventListener('DOMContentLoaded', () => {
  const tabs = [...document.querySelectorAll('.tab')];
  const kindInput = document.getElementById('kind-input');
  const textPanel = document.getElementById('text-panel');
  const filePanel = document.getElementById('file-panel');
  const fileInput = document.getElementById('file-input');
  const content = document.getElementById('content');
  const labels = { image: ['Upload an image', 'PNG, JPG, WEBP or GIF · up to 25 MB', '.png,.jpg,.jpeg,.webp,.gif'], video: ['Upload a video', 'MP4, WEBM, MOV or M4V · up to 25 MB', '.mp4,.webm,.mov,.m4v'], audio: ['Upload an audio file', 'MP3, WAV, OGG, M4A or WEBM · up to 25 MB', '.mp3,.wav,.ogg,.m4a,.webm'] };
  tabs.forEach(tab => tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.toggle('active', t === tab));
    const kind = tab.dataset.kind; kindInput.value = kind;
    textPanel.classList.toggle('hidden', kind !== 'text'); filePanel.classList.toggle('hidden', kind === 'text');
    if (kind !== 'text') { document.getElementById('file-title').textContent = labels[kind][0]; document.getElementById('file-hint').textContent = labels[kind][1]; fileInput.accept = labels[kind][2]; fileInput.value = ''; document.getElementById('file-name').textContent = ''; }
  }));
  if (content) content.addEventListener('input', () => { document.getElementById('char-count').textContent = `${content.value.length.toLocaleString()} / 5,000`; });
  if (fileInput) {
    const dropZone = document.querySelector('.drop-zone');
    const showFile = file => { document.getElementById('file-name').textContent = file?.name || ''; };
    fileInput.addEventListener('change', () => showFile(fileInput.files[0]));
    if (dropZone) {
      ['dragenter', 'dragover'].forEach(type => dropZone.addEventListener(type, event => { event.preventDefault(); dropZone.classList.add('drag-over'); }));
      ['dragleave', 'drop'].forEach(type => dropZone.addEventListener(type, event => { event.preventDefault(); dropZone.classList.remove('drag-over'); }));
      dropZone.addEventListener('drop', event => {
        const file = event.dataTransfer.files[0];
        if (!file) return;
        const kind = kindInput.value;
        if (!labels[kind] || !labels[kind][2].split(',').some(ext => file.name.toLowerCase().endsWith(ext))) {
          fileInput.value = '';
          showFile(null);
          return;
        }
        fileInput.files = event.dataTransfer.files;
        showFile(file);
      });
    }
  }
});
