// $('input').focus(function(){
//     $(this).parents('.form-group').addClass('focused');
//   });
  
//   $('input').blur(function(){
//     var inputValue = $(this).val();
//     if ( inputValue == "" ) {
//       $(this).removeClass('filled');
//       $(this).parents('.form-group').removeClass('focused');  
//     } else {
//       $(this).addClass('filled');
//     }
//   })

const inputGroup = document.querySelectorAll('.input');
const inputs = document.querySelectorAll('input');

inputs.forEach((input) => {
    input.addEventListener('click', e => {
        if (e.target.classList.contains("filled")) {
            e.target.classList.remove("filled");
            inputGroup.classList.add("focused");
        } else {
            e.target.classList.add("filled");
            inputGroup.classList.remove("focused");
        }
    })
})