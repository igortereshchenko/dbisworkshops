
console.log('debug');
// array html element

const deleteBtns = document.querySelectorAll('delete-btn');
deleteBtns.forEach(btn => {
  btn.addEventListener('click', (event) => {
    alert('DELETE!');
});
});
