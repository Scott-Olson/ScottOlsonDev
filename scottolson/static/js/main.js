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

function copiedToClipboard() {
  var copyText = document.getElementById("copyLinkButton");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
  
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Copied: " + copyText.value;
}

function outFunc() {
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Copy to clipboard";
}