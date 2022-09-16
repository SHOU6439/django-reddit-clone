let messageBox = document.getElementById("message_box_33")
let deleteButtonForm = document.getElementById("delete_message_from_33")

if(messageBox){
    messageBox.addEventListener('click', function(){
        deleteButtonForm.classList.toggle('dm-detail-row__delete-message-form--displayed')
    })
}

