function stuff(vars) {
            console.log(vars)
            return vars
        }
function stuff2(vars) {
            console.log(vars)
            return vars
        }
window.addEventListener('load', function(){
    // clear an old value (for add/edit note)
    document.getElementById('savenote').value = "";

        let addButtons = document.querySelectorAll(".add")
        // put values in addnote modal on click (for you section)
        addButtons.forEach(function(elem) {
            elem.addEventListener('click', function() {
                let value = elem.value;
                for(let i = 0; i < arr.length; i += 1) {
                    if (arr[i]["type"] === value) {
                        document.querySelector('.title').value = arr[i]["type"];
                        document.querySelector('textarea').value = arr[i]["content"];
                    }
                }
            })
        })

        // edit note func
        let editButtons = document.querySelectorAll(".edit")
        // put values in addnote modal on click (notes section)
        editButtons.forEach(function(eleme) {
            eleme.addEventListener('click', function() {
                let value = eleme.value;
                for(let i = 0; i < ee.length; i += 1) {
                    if (parseInt(ee[i]["note_id"]) === parseInt(value)) {
                        document.querySelector('.title').value = ee[i]["title"];
                        document.querySelector('textarea').value = ee[i]["note"];
                        document.getElementById('savenote').value = value;
                    }
                }
            })
        })

        // search note
        let input = document.querySelector('.search');
            input.addEventListener('keyup', function() {
                $.get('/search?q=' + input.value, function(notes) {
                  let html = '';
                  for (let i = 0; i < notes.length; i++)
                  {
                      let title = notes[i].title
                      let note = notes[i].note
                      let id = notes[i].id

                      html += `<div class="note generic-div">
                                    <button data-bs-toggle="modal" data-bs-target="#addNoteModal" value="${id}" class="edit">🖉</button>
                                    <form action="/deletenote" method="post">
                                    <!-- delete button -->
                                    <button type="submit" name="delete" value="${id}" class="delete">🗑</button>
                                    </form>
                                    <h2>${title}</h2>
                                    <pre>${note}</pre>
                                    </div>`

                  }

                  document.querySelector('flex-container2').innerHTML = html;
                });
            });

    })