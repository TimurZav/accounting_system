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
        event.preventDefault(); // Остановить стандартное действие кнопки
        // Находим форму, которую нужно отправить
        var form = $('form');

        // Проверяем, заполнены ли обязательные поля
        var isValid = true;
        form.find('input[required], select[required]').each(function() {
            var input = $(this);
            var errorMessage = 'Пожалуйста, заполните это поле.';

            // Для input
            if (input.is('input')) {
                if (input.val() === '') {
                    isValid = false;
                    input.addClass('is-invalid'); // Добавляем класс для визуального указания на незаполненное поле
                    if (!input.next().hasClass('invalid-feedback')) {
                        input.after('<div class="invalid-feedback">' + errorMessage + '</div>'); // Добавляем сообщение об ошибке, если его еще нет
                    }
                } else {
                    input.removeClass('is-invalid'); // Удаляем класс, если поле заполнено
                    input.next('.invalid-feedback').remove(); // Удаляем сообщение об ошибке, если поле заполнено
                }
            }
            // Для select
            else if (input.is('select')) {
                if (!input.val()) {
                    isValid = false;
                    input.addClass('is-invalid'); // Добавляем класс для визуального указания на незаполненное поле
                    if (!input.next().hasClass('invalid-feedback')) {
                        input.after('<div class="invalid-feedback">' + errorMessage + '</div>'); // Добавляем сообщение об ошибке, если его еще нет
                    }
                } else {
                    input.removeClass('is-invalid'); // Удаляем класс, если поле заполнено
                    input.next('.invalid-feedback').remove(); // Удаляем сообщение об ошибке, если поле заполнено
                }
            }
        });

        // Если все обязательные поля заполнены, отправляем данные формы
        if (isValid) {
            processForm(form);
        }
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
        // Проверяем, заполнена ли форма
        if (!form[0].checkValidity()) {
            // Если форма не заполнена, ничего не делаем
            return;
        }
        var url = form.attr('action');
        var data = objectifyForm(form.serializeArray());
        data.csrfmiddlewaretoken = getCookie('csrftoken');
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            cache: false,
            success: function(response) {
                // Показываем успешное уведомление
                Swal.fire({
                    position: "top-end",
                    icon: "success",
                    title: "Данные успешно отправились в базу!",
                    toast: true,
                    showConfirmButton: false,
                    timer: 1500,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.onmouseenter = Swal.stopTimer;
                        toast.onmouseleave = Swal.resumeTimer;
                    }
                });
            },
            error: function(xhr, errmsg, err) {
                // Показываем уведомление об ошибке
                console.log(xhr.status + ": " + xhr.responseText);
                Swal.fire({
                    position: "top-end",
                    icon: "error",
                    title: "Данные не попали в базу!",
                    toast: true,
                    showConfirmButton: false,
                    timer: 1500,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.onmouseenter = Swal.stopTimer;
                        toast.onmouseleave = Swal.resumeTimer;
                    }
                });
            }
        });
    }
});

