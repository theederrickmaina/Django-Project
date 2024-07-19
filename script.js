document.getElementById('obituaryForm').addEventListener('submit', function(event) {
    var name = document.getElementById('name').value;
    var date_of_birth = document.getElementById('date_of_birth').value;
    var date_of_death = document.getElementById('date_of_death').value;
    var content = document.getElementById('content').value;
    var author = document.getElementById('author').value;

    if (!name || !date_of_birth || !date_of_death || !content || !author) {
        alert('All fields are required!');
        event.preventDefault();
    }
});
