let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', 'rgb(220, 200, 164)');
}
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', 'rgb(220, 200, 164)');
    } else {
        $(this).css('color', 'rgb(218, 145, 12)');
    }
});