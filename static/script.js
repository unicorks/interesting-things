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
    })