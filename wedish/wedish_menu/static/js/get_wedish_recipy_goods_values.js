$(document).on('change', 'select[id^=id_menuitem_set]', function () {
    let _this = $(this);
    let selectedVal = $(this).val();
    menu_line_id = _this.attr('id').replace('-item', '-')
    $.ajax({
        url: '/wedish_menu/api/' + selectedVal,
        type: "POST", 
        success: function(data){
           console.log(data);
           $(_this).closest('tr').find('#' + menu_line_id + 'name').val(data.name);
           $(_this).closest('tr').find('#' + menu_line_id + 'price').val(data.recommended_retail_price);
        }
      });
});
