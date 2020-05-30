$(document).ready(function() {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {

            state: {
                validators: {
                    notEmpty: {
                        message: 'Це поле не може бути пустим'
                    }
                }
            },
            zip: {
                validators: {
                    notEmpty: {
                        message: 'Будь-ласка введіть сумму витрати'
                    },
                    regexp: {
                        regexp: /^[0-9.]+$/,
                        message: 'Це поле може приймати тільки цілі дробові числа'
                    },
                    stringLength: {
                        max: 16,
                        message: 'Сума завелика, введіть іншу'
                    },
                }
            },
            limit: {
                validators: {

                   regexp: {
                        regexp: /^[0-9.]+$/,
                        message: 'Це поле може приймати тільки цілі дробові числа'
                    },
                    stringLength: {
                        max: 16,
                        message: 'Сума завелика, введіть іншу'
                    },
                }
            }

            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});