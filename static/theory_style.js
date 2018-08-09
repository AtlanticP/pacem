
$('#theory_span_1').hover(function(){
  var html = $('#theory_span_1').text();
  console.log(html);
});

$('span').each(function(i, v){
  console.log(i, $(this).text());
});