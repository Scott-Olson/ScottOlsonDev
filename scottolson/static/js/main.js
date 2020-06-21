// $(window).scroll(function(){
//   var $nav = $(".fixed-top");
//   $('nav').toggleClass('scrolled', $(this).scrollTop() > $nav.height());
// });

var clipboard = new ClipboardJS('.btnClip');

clipboard.on('success', function(e) {
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);

    e.clearSelection();
});

clipboard.on('error', function(e) {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})