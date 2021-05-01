//TypeWrite Animation script
var i = 0;
var txt = 'Now! Never Accept those Gigantic Terms & Conditions Blindly! & Quick Article Summarisation!'; /* The text */
var speed = 20; /* The speed/duration of the effect in milliseconds */

//function to give typing animation
function typeWriter() {
  if (i < txt.length) {
    document.getElementById("typedTxt").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
//function to wait for typeWriter function to end
function disBtn(){
  $('.buttons').addClass("ocupEffect");
  $('.pCon1').addClass("ocupEffect");
  $('.aCon1').addClass("ocupEffect");
  $('form').addClass("ocupEffect");
}

//Icon Animation
$('.aCon1').hover( () =>{
    $(".workI").addClass("iconA");
}, () => {
    $(".workI").removeClass("iconA");
});
$('.buttons').hover( () =>{
    $(".tryI").addClass("iconA1");
}, () => {
    $(".tryI").removeClass("iconA1");
});
