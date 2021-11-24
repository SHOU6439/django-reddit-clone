const accountDropDownButton = document.getElementById('account-drop-down-button');
const dropDownMenuContainer = document.getElementById('drop-down-id')

if(accountDropDownButton){
    accountDropDownButton.addEventListener('click', function(){
        dropDownMenuContainer.classList.toggle('user-menu-is-open')
    });
}