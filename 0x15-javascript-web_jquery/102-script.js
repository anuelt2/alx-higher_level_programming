/* global $ */
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
