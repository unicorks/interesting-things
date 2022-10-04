window.addEventListener('load', function(){
    document.querySelector('.edit').addEventListener('click', () => {
            let notediv = document.querySelector('.edit').parentNode;
            let data = {
                'title': notediv.querySelector('h2').textContent,
                'content': notediv.querySelector('pre').textContent,
            }
            const oldNote = JSON.stringify(data)

            // open note edit modal
            document.querySelector('#editTitle').setAttribute('value', notediv.querySelector('h2').textContent)
            document.querySelector('#editBody').innerText = $(notediv.querySelector('pre')).html().replace(new RegExp('\r?\n','g'), '&#10;')

            // send info to flask app
            $.ajax({
                url:"/editnote",
                type:"POST",
                contentType: "application/json",
                data: JSON.stringify(oldNote)});

        })
    })