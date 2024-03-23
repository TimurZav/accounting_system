$(document).ready(function() {
    // Обработчик события для селектов
    $('.select').change(function() {
        var $this = $(this);
        var dataType = $this.data('type');
        var relatedId = $this.find('option:selected').text();
        var targetId = '#' + dataType; // Генерируем селектор для элемента с нужным id

        if (relatedId && relatedId !== 'Выберите одно из меню') {
            $.ajax({
                url: '/get_related_data/',
                type: 'GET',
                data: {'data_type': dataType, 'related_id': relatedId},
                success: function(data) {
                    // Очищаем элемент с нужным id и добавляем новые опции
                    $(targetId).html('<option value="">Выберите одно из меню</option>');
                    data.forEach(function(item) {
                        $(targetId).append('<option label="' + item.text + '" value="' + item.text + '">' + item.value + '</option>');
                    });
                }
            });
        } else {
            // Очищаем элемент с нужным id
            $(targetId).html('<option value="">Выберите одно из меню</option>');
        }
    });


    // Обработчик события для кнопки "Записаться"
    $('#submitFormBtn').click(function() {
        // Находим форму, которую нужно отправить
        var form = $('form');
        // Отправляем данные формы в Django
        processForm(form);
    });

    // Функция для получения значения cookie по имени
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Функция для преобразования данных формы в объект
    function objectifyForm(formArray) {
      var returnArray = {};
      console.log(formArray);
      for (var i = 0; i < formArray.length; i++){
        returnArray[formArray[i]['name']] = formArray[i]['value'];
      }
      return returnArray;
    }

    // Функция для отправки данных формы в Django
    function processForm(self) {
        var form = $(self);
        var url = form.attr('action');
        var data = objectifyForm(form.serializeArray());
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            cache: false,
            success: function(data) {
                // Обработка успешного ответа
            },
            error: function(jqXHR, exception) {
                // Обработка ошибок
            }
        });
    }
});

