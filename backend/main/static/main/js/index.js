// JavaScript
$(document).ready(function() {

    $('#business').change(function() {
        var businessId = $(this).val();
        if (businessId && businessId != 'Выберите одно из меню') {
            $.ajax({
                url: '/get_form_payments/',
                type: 'GET',
                data: {'business_id': businessId},
                success: function(data) {
                    $('#formPayment').html('<option value="">Выберите одно из меню</option>');
                    data.forEach(function(item) {
                        $('#formPayment').append('<option value="' + item.value + '">' + item.text + '</option>');
                    });
                }
            });
        } else {
            $('#formPayment').html('<option value="">Выберите одно из меню</option>');
            $('#legalEntity').html('<option value="">Выберите одно из меню</option>');
            $('#rc').html('<option value="">Выберите одно из меню</option>');
        }
    });


    $('#formPayment').change(function() {
        var formPaymentId = $(this).val();
        if (formPaymentId) {
            $.ajax({
                url: '/get_legal_entities/',
                type: 'GET',
                data: {'form_payment_id': formPaymentId},
                success: function(data) {
                    $('#legalEntity').html('<option value="">Выберите одно из меню</option>');
                    data.forEach(function(item) {
                        $('#legalEntity').append('<option value="' + item.value + '">' + item.text + '</option>');
                    });
                }
            });
        } else {
            $('#legalEntity').html('<option value="">Выберите одно из меню</option>');
            $('#rc').html('<option value="">Выберите одно из меню</option>');
        }
    });


    $('#legalEntity').change(function() {
        var legalEntityId = $(this).val();
        if (legalEntityId) {
            $.ajax({
                url: '/get_rcs/',
                type: 'GET',
                data: {'legal_entities_id': legalEntityId},
                success: function(data) {
                    $('#rc').html('<option value="">Выберите одно из меню</option>');
                    data.forEach(function(item) {
                        $('#rc').append('<option value="' + item.value + '">' + item.text + '</option>');
                    });
                }
            });
        } else {
            $('#rc').html('<option value="">Выберите одно из меню</option>');
        }
    });

});
