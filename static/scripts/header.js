//Changing the background colour when scrollTop
$(document).ready(function() {
  var scroll_pos = 0;
  $(document).scroll(function() {
    scroll_pos = $(this).scrollTop();
    if (scroll_pos > 10) {
      $("header").css('background-color', '#FBFBFB');
    } else {
      $("header").css('background-color', 'inherit');
    }
  });
});