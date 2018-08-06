// https://www.youtube.com/watch?v=q4FWSdX55ls
// Three ways of interaction CSS and JS.

$('p.para1').css('color', 'blue');  
$('p.para2').css({color: 'red', background: 'green'});
$('p.para3').addClass('myClass');
// $('p.para3').removeClass('myClass')

$('#btn1').click(function () {
  $('p.para3').toggleClass('myClass');
});

// $('#myDiv').html('<h5>Hello, World!</h5>');

var value;
value = $('#myDiv').text();   
console.log(value);           // Hello, World!

// $('ul').append('<li>Append a list.</li>')   // inside 'ul'
// $('ul').prepend('<li>Prepend a list.</li>')

// $('ul').before('<h4>Before!');              //outside 'ul'
// $('ul').after('<h4>After!');

$('.para2').appendTo('.para1');
$('.para2').prependTo('.para1');

// $('ul').empty();  // remove the content of 'ul'
// $('ul').detach();    // remove 'ul' itself 

$('a').attr('target', '_blank');
// <a href="http://www.yandex.ru" target="_blank">Yandex.ru</a>

$('a').removeAttr('target')
// <a href="http://www.yandex.ru">Yandex.ru in a new blank</a>

// $('p').wrap('<h1>');
// <h1><p class="para1"...</h1>, <h1><p class="para2"...</h1>, ...

$('p').wrapAll('<h1>'); 
// <h1><p ...></p>, <p ...></p>,...,</h1>

// $('body').append('Houuuuu!');
// $('div').append('Houuuuu!')     // <h5>Hello, World!</h5>\n"Houuuuu"
// $('div').html('Houuuuu!')    // ?????????????

// html - rewrite the whole tag
// append - only append the content of the tag

$('#newItem').keyup(function (e) {
  var code = e.which;
  if (code == 13) {  // hit Enter
    e.preventDefault();
    $('ul#list').append('<li>' + e.target.value + '</li>');
  };
});


var myArr = ['Brad', 'Kelley', 'Nate', 'Jose']

$.each(myArr, function (index, name) {       // iteration through array
  $('#users').append('<li>' + name + '</li>');
});

var newArr = $('ul#list li').toArray();
// console.log(newArr);  // (3) [li, li, li]

 // myArr = $('li').toArray();  // returns all of the elements in the jQuery set:

 $.each(newArr, function (index, tag) {       // iteration through array
  console.log(tag.innerHTML)  // List One.\n List Two.\n List Three.\n
});