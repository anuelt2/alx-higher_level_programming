/* global $ */
$(document).ready(function () {
  function fetchLangHello () {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(fetchLangHello);
  $('INPUT#language_code').keypress(function (event) {
    if (event.key === 'Enter') {
      fetchLangHello();
    }
  });
});
