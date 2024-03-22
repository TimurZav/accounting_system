$(document).ready(function() {
    $('.select').change(function() {
        var $this = $(this);
        var dataType = $this.data('type');
        var relatedId = $this.val();
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
                        $(targetId).append('<option value="' + item.value + '">' + item.text + '</option>');
                    });
                }
            });
        } else {
            // Очищаем элемент с нужным id
            $(targetId).html('<option value="">Выберите одно из меню</option>');
        }
    });
});
