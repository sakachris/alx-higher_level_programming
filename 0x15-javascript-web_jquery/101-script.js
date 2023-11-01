$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  $('DIV#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  $('DIV#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
