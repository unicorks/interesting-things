function stuff(vars) {
            console.log(vars)
            return vars
        }
window.addEventListener('load', function(){
        let editButtons = document.querySelectorAll(".edit")
        // put values in addnote modal on click (for you section)
        editButtons.forEach(function(elem) {
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
    })