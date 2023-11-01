$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const languageCode = $('INPUT#language_code').val();

    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    }).fail(function() {
      $('DIV#hello').text('Error: Unable to fetch translation');
    });
  });
});
