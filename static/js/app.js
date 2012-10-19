$(function() {
    $('#on').click(function() {
        $.post($('#controls').data('vctrl'), {action: 'on'}, function() {
            setTimeout(function() {
                var img = $('<img>');
                img.attr('src', $('#cam').data('imgsrc'))
                $('#cam').append(img);
            }, 1000);

            $('body').removeClass('off').addClass('on');
        });
    });

    $('#off').click(function() {
        $.post($('#controls').data('vctrl'), {action: 'off'});
        $('#cam img').attr('src', '#').remove();

        $('body').removeClass('on').addClass('off');
    });


    // BrowserID goodness
    $('#login').click(function(ev) {
        ev.preventDefault();
        navigator.id.request();
    });

    $('#logout').click(function(ev) {
        ev.preventDefault();
        navigator.id.logout();
    });

    navigator.id.watch({
        loggedInUser: currentUser,
        onlogin: function(assertion) {
            $.ajax({
                type: 'POST',
                url: '/authenticate',
                data: { assertion: assertion },
                success: function(res, status, xhr) {
                    window.location.reload();
                },
                error: function(res, status, xhr) {
                    console.log('Login failure:' + res.status + ': ' + res.statusText);

                    // Remove any old notices
                    $('.notice.sign-in-error').remove();

                    var message = $('<div></div>');
                    message.addClass('notice error dismissable sign-in-error');
                    message.html('We were unable to sign you in. Please try again.');

                    message.on('click', function() {
                      $(this).fadeOut(600, function() {
                        $(this).remove();
                      });
                    });

                    message.hide();
                    $('#main-notices').prepend(message);

                    message.fadeOut(0, function() {
                      message.fadeIn(400);
                    });
                }
            });
        },
        onlogout: function() {
            $.ajax({
                type: 'POST',
                url: '/logout',
                success: function(res, status, xhr) {
                    window.location.reload();
                },
                error: function(res, status, xhr) {
                    console.log('Logout failure: ' + res.status + ': ' + res.statusText);
                }
            });
        }
    });
});