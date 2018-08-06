$('document').ready(function () {
  
  $('#but_hide').click(function () {
    $('#para1').hide();    // hide the element
  });

  $('#but_show').on('click', function () {
    $('#para1').show();    // show the element
  });

  $('#but_tog').dblclick(function () {  // double click
    $('#para1').toggle();  // toggle the element
  });

  $('#but_hover').hover(function () {  // hover = mouseenter + mouseleaves
    $('#but_hover').css('color', 'blue');  
    // $('#para1').toggle(); 
  });

// $(...).hover(...)  --> $(...).on('mouseenter' and 'mouseleave')

  $('#button5').on('mouseenter', function () {
    $('#button5').css({color: 'red', background: 'green'});
  });
  $('#button5').on('mouseleave', function () {
    $('#button5').css({color: 'black', background: 'yellow'});
  });

  $('#button6').on('mousemove', function () {
    $('#para1').toggle();    
  });

  $('#button7').on('mousedown', function () {
    $('#para1').toggle();
  });
  $('#button7').on('mouseup', function () {
    $('#para1').toggle();
  });

  $('#button8').click(function(e){
    console.log(e); 
    // jQuery.Event {originalEvent: MouseEvent, type: "click", 
    // isDefaultPrevented: ƒ, target: button#button8.btnClass, currentTarget: button#button8, …}
    
    console.log(e.currentTarget); // <button id="button8" class="btnClass">pass parametr e</button>
    console.log(e.currentTarget.id);  // button8
    console.log(e.currentTarget.innerHTML);  // pass parametr e
    console.log(e.currentTarget.className);  // btnClass
  });

  $('#button9').on('mousemove', function(e) {
    console.log('Coords: Y:' + e.clientY + ' Coords: X:' + e.clientX);
  });

  // $(document).on('mousemove', function (e) {
  //   console.log('Coords: Y:' + e.clientY + ' Coords: X:' + e.clientX);
  // });

  $(document).on('mousemove', function (e) {
    $('#coords').html('Coords: Y:' + e.clientY + ' Coords: X:' + e.clientX);
  });

});
