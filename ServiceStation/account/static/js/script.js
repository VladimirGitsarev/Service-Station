formCarBtn = document.querySelector('#new-car');
formCar = document.querySelector('#car-form');
formCarHeader = document.querySelector('#new-car-header');
inputFocus = document.querySelector('input[type=text]');
formCarBtn.addEventListener('click', formCarBtnClick)

function formCarBtnClick(){
    formCar.style.display = 'block';
    formCarBtn.style.display = 'none';
    formCarHeader.style.display = 'block';
    inputFocus.focus();
}

$('a#delete-car').click(function(e){    
    thisId = $(this).data('id')
    e.preventDefault();    
    $.post('delete_car/',      
        {id: $(this).data('id')},     
        function(data){     
            if (data['status'] == 'ok'){
                $('div#car-'+thisId).remove()
            }   
        });  
    }); 
