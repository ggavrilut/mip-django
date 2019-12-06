$(document).ready(function() {
    $('body').on('submit', '#newsletter-form', function(e) {
        e.preventDefault();
        console.log('submit');
        var form = $(this);
        var url = form.attr('data-ajax-url');
        $.ajax({
            method: "POST",
            url: url,
            data: {
                email: form.find('#id_email').val()
            },
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    var csrftoken = getCookie('csrftoken');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function(data, textStatus, jqXHR) {
                console.log('ajax success', data, textStatus, jqXHR)
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log('ajax error', errorThrown, textStatus, jqXHR)
            },
            complete: function(jqXHR, textStatus ) {
                console.log('ajax complete', textStatus, jqXHR)
            }
        })
        return false;
    });
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}