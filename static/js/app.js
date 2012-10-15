$(function() {
    $('#on').click(function() {
        $.post($('#controls').data('vctrl'), {action: 'on'}, function() {
            setTimeout(function() {
                var img = $('<img>');
                img.attr('src', $('#cam').data('imgsrc'))
                $('#cam').append(img);
            }, 1000);

            $('#controls').removeClass('off').addClass('on');
        });
    });

    $('#off').click(function() {
        $.post($('#controls').data('vctrl'), {action: 'off'});
        $('#cam img').attr('src', '#').remove();

        $('#controls').removeClass('on').addClass('off');
    });
});