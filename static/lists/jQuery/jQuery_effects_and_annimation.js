    $('#btnFadeOut').click(function () {
  // $('#box').fadeOut('slow'); // parametrs 'fast', 'slow' or integer (ms)
    $('#box').fadeOut(1500, function () {
      $('#btnFadeOut').text("It's faded!")
    });
});

$('#btnFadeIn').click(function () {
  $('#box').fadeIn(1500, function () {
      $('#btnFadeIn').text("It's appeared!")
  });
});

$('#btnFadeTog').click(function () {
  $('#box').fadeToggle(1500);
});


$('#btnSlideDown').click(function () {
  $('#box').slideDown(1500);
});

$('#btnSlideUp').click(function () {
  $('#box').slideUp(1500);
});

$('#btnSlideTog').click(function () {
  $('#box').slideToggle(3000);
});

$('#btnStop').click(function () {
  $('#box').stop();
});


// CSS: #div {position: relative;}

$('#btnMoveRight').click(function () {
  $('#box').animate({
    left: 500,
    height: '300px',
    width: '300px',
    opacity: '0.5',
  });
});

$('#btnMoveLeft').click(function () {
  $('#box').animate({
    left: 0,
    height: '50px',
    width: '50px',
    opacity: 1,
  });
});

$('#btnMoveAround').click(function () {
  var box = $('#box');
  
  box.animate({
    left: 300,
    opacity: 0.6,
  });
  
  box.animate({
    left: 300,
    top: 300,
    opacity: 0.25
  });
  
  box.animate({
    left: 0,
    top: 300,
    opacity: 0.6,
  });

  box.animate({
    left: 0,
    top: 0,
    opacity: 1,
  });

});