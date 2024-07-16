document.addEventListener('DOMContentLoaded', function() {
    // Function to initially show only the first 10 rows
    function limitTableRows() {
        const table = document.querySelector('#table-container table');
        if (!table) return;

        const rows = table.querySelectorAll('tbody tr');
        rows.forEach((row, index) => {
            if (index >= 10) {
                row.style.display = 'none';
            }
        });

        // Add event listener to load more rows when scrolled to the bottom
        const container = document.querySelector('#table-container');
        container.addEventListener('scroll', () => {
            if (container.scrollTop + container.clientHeight >= container.scrollHeight) {
                rows.forEach((row, index) => {
                    if (index >= 10 && row.style.display === 'none') {
                        row.style.display = '';
                    }
                });
            }
        });
    }

    // Call the function on page load
    limitTableRows();

    // Function to open plot window after search
    document.getElementById('search-form').onsubmit = function(event) {
        event.preventDefault();
        var form = event.target;

        fetch(form.action, {
            method: form.method,
            body: new FormData(form),
        }).then(response => {
            if (response.ok) {
                return response.text();
            }
            throw new Error('Network response was not ok.');
        }).then(html => {
            document.body.innerHTML = html;
            limitTableRows();
            window.open('/plot', '_blank', 'width=800,height=600');
        }).catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    };
});
