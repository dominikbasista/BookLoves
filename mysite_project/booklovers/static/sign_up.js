function addEventListeners() {
    if(window.addEventListener()) {
        document.getElementById('next_button_1').addEventListener('click',myFun1,false)

    } else if(window.attachEvent()){
        document.getElementById('next_button_1').attachEvent('click',myFun1,false)

    }
     function myFun1(){alert(this.id+" pozwla cos tam cos tam");
    }
}
window.onload = addEventListeners();