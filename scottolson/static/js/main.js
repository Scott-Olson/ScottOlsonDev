// $(window).scroll(function(){
//   var $nav = $(".fixed-top");
//   $('nav').toggleClass('scrolled', $(this).scrollTop() > $nav.height());
// });

function emailCopyFunction() {
  var copyText = document.getElementById("emailLink");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}